import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, sender_email, sender_password, recipient_email):
    try:
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = recipient_email
        message["Subject"] = subject

        message.attach(MIMEText(body, "plain"))

        smtp_server = "smtp.gmail.com"
        port = 587

        # Establish a secure session with gmail's outgoing SMTP server
        server = smtplib.SMTP(smtp_server, port, timeout=15)
        server.starttls()

        # Login to your gmail account
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, recipient_email, message.as_string())

        # Close the SMTP server connection
        server.quit()

        print(f"Email sent to {recipient_email}")
    except smtplib.SMTPException as e:
        print(f"Failed to send email to {recipient_email}. Error: {str(e)}")
    except Exception as e:
        print(f"An error occurred while sending the email: {str(e)}")

def main():
    sender_email = "sender@example.com"
    sender_password = "examplepassword"
    recipient_email = "recipient@example.com" #email to send to
    subject = "Hello!" #subject
    body = "Hi!" #message

    for i in range(4): #number of emails to send - max is 100, use responsibly
        send_email(subject, body, sender_email, sender_password, recipient_email)

if __name__ == "__main__":
    main()
