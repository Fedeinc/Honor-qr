import smtplib
from email.mime.text import MIMEText
import os

def send_email(name, email, message):
    try:
        msg = MIMEText(f"Name: {name}\nEmail: {email}\nMessage: {message}")
        msg['Subject'] = 'Contact Form Submission'
        msg['From'] = email
        msg['To'] = 'honorqr2023@gmail.com'  # Your email address

        app_password = 'jozmghouoogdkjyu'  # Your generated app password

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            print("Attempting to login...")
            server.login('honorqr2023@gmail.com', app_password)  # Use the generated app password
            print("Login successful!")
            server.sendmail(email, 'honorqr2023@gmail.com', msg.as_string())
            print("Email sent successfully!")

    except smtplib.SMTPAuthenticationError as e:
        print("SMTPAuthenticationError occurred: ", e.smtp_code, e.smtp_error)
    except Exception as e:
        print("An error occurred: ", str(e))

# Example usage
send_email('John Doe', 'john.doe@example.com', 'Hello, this is a test message.')
