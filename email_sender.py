import yagmail

def send_email(name, email, company):
    with open('credentials.txt', 'r') as file:
        lines = file.readlines()
        user = lines[0].split('=')[1].strip()
        password = lines[1].split('=')[1].strip()
    
    # Connect to Gmail SMTP server
    yag = yagmail.SMTP(user=user, password=password)
    
    # Capitalize name and company properly
    first_name = name.split()[0].title()  # Capitalize first name
    company = company.capitalize()  # Capitalize company name
    
    subject = "Let’s make this a win-win situation... I’ll owe you coffee forever!"
    
    content = f"""
    Hey <strong>{first_name}</strong> 👋,

    Firstly, thanks for even opening this email (because, let’s be real, most don't!). I came across your LinkedIn profile, and I have to say, I’m really impressed with the work you're doing at <strong>{company}</strong>.

    Now, a little about me — <strong>I’m Arghya Mondal</strong>, a two-time hackathon winner (no big deal, just the humble brag of the century 🏆). I’m an expert in <strong>MERN stack</strong> and <strong>Python</strong>, and I can pick up anything you throw my way. For example, I recently built <a href="https://lifeline-ai.netlify.app/">Lifeline</a>, an AI-based medical consultant platform.

    <strong>All I need is an internship opportunity, and I’ll give it my absolute best.</strong>

    I would love to work with someone as skilled as you at {company}. If you think I’d be a good fit, <strong>I’d be forever grateful for a referral</strong>. I'll attach links to my <a href="https://arghya-mondal-work.netlify.app">Portfolio Website</a> & <a href="https://drive.google.com/file/d/1UGx0b5IUwr2LSQUZecWSJcn0WDFO5sk9/view">Resume</a> for your review.

    Let’s make this a win-win situation... I’ll owe you coffee forever 😁

    Cheers,<br><strong>Arghya</strong>
    """
    
    # Send email
    yag.send(to=email, subject=subject, contents=content)
    print(f"Email sent successfully to {first_name} at {email}!")
