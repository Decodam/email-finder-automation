import json
from utils import generate_email_combinations
from tqdm import tqdm  # Importing tqdm for progress bar
from email_sender import send_email  # Importing the send_email function

def generate_emails_for_company(company_name, file_path):
    # Initialize a counter for total emails
    total_emails = 0

    # Load the JSON data
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return

    # Check if the company exists in the data
    if data.get("company").lower() == company_name.lower():
        print(f"Generating email combinations for {company_name}...\n")
        
        # Prepare the list of names to generate emails for
        names = data["hiring"]
        emails_to_generate = []

        # Generate emails for each name and domain
        for name in names:
            emails = generate_email_combinations(name, data["domain"])
            emails_to_generate.extend((name, email) for email in emails)

        # Create a progress bar for the email sending process
        for name, email in tqdm(emails_to_generate, desc="Sending Emails", unit="email"):
            print(f"Sending email to: {name} - {email}")  # Actual sending email

            # Call the send_email function to send the email
            send_email(name, email, company_name)

            total_emails += 1  # Increment the email counter

        print("\n" + "-" * 40)  # Dash separator after emails

        # Print the total number of emails generated
        print(f"Total number of emails generated: {total_emails}")
    else:
        print(f"No data found for company: {company_name}")

# Example of how the function can be called
company_name = input("Enter the company name: ").strip()
file_path = 'json/zomato.json'  # Corrected file path
generate_emails_for_company(company_name, file_path)
