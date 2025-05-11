import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(user_email, user_name, result):
    sender_email = "kushbajpai641@gmail.com"

    # Email Subject and Body
    subject = "Your Cognify Result Report"
    body = f"""
    Hi {user_name},

    Thank you for using Cognify. Here's your result:

    Cognitive Score: {result}

    Stay healthy and focused!

    Regards,
    Cognify Team
    """

    # Prepare the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = user_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Send the email using Gmail's SMTP server
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_password)  # Login to the server
            server.sendmail(sender_email, user_email, msg.as_string())  # Send the email
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

# Test the function
send_email("recipient_email@example.com", "John Doe", 85)
