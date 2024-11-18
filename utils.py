def generate_email_combinations(full_name, domain):
    # Split the full name into first name and last name
    name_parts = full_name.split()
    
    # If the full name is not in a valid format, return an empty list
    if len(name_parts) < 2:
        print("Invalid full name format. Please provide a full name with at least first and last names.")
        return []

    first_name = name_parts[0].lower()
    last_name = name_parts[1].lower()
    
    # Expanded list of email formats
    email_formats = [
        # First Name only
        f"{first_name}@{domain}",                       #first@domail.com
        
        # Full first name, full last name
        f"{first_name}.{last_name}@{domain}",           # first.last@domain.com
        f"{first_name}.{last_name}@{domain}",           # firstlast@domain.com
        
        # Initials
        f"{first_name[0]}.{last_name}@{domain}",        # f.last@domain.com
        f"{first_name[0]}{last_name}@{domain}",         # flast@domain.com
        f"{first_name}.{last_name[0]}@{domain}",        # first.l@domain.com
        f"{first_name}{last_name[0]}@{domain}",        # firstl@domain.com
    ]
    
    # Remove duplicates by converting to a set and back to a list
    return list(set(email_formats))
