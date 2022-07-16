import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailHandler:
    # event_type, email_contents, email_list,
    def __init__(self, email_string):
        self.email_string = email_string

    # Returns string error messages
    def send_mass_email(self):
        smtp_server = "smtp.gmail.com"
        port = 587
        sender_email = "Enter email"
        sender_pass = "Enter Pass"
        # name, date, time
        # "ACM Meeting,4/12/22,1:30 P.M.,[emails]"
        email_split = self.email_string.split(",")
        event_name = email_split[0]
        event_date = email_split[1]
        event_time = email_split[2]

        message = MIMEMultipart("alternative")
        message["Subject"] = "Event Sign-Up Confirmation"
        message["From"] = sender_email

        html = """
            <html>
              <body>
                <p><b> You have been signed up to attend an event. </b><br>
                <br>Event: {}</br>
                <br>Date: {}\n</br>
                <br>Time: {}\n</br>

                <br>Please let the event administrators know if you are not planning on attending.</br>
                </br>
               </p>
              </body>
            </html>
        """.format(event_name,event_date,event_time)

        part2 = MIMEText(html, "html")
        message.attach(part2)
        # Create a secure SSL context
        context = ssl.create_default_context()

        try:
            server = smtplib.SMTP(smtp_server, port)
            server.starttls(context=context)
            server.login(sender_email, sender_pass)
            for email in email_split[3:]:
                server.sendmail(sender_email, email, message.as_string())
        except Exception as e:
            return "Unable to make connection or send emails."
        finally:
            server.quit()
        # Test code to display the contents of the split input string
        #for e in email_split:
        #    print(e)

# Test code
temp = EmailHandler("ACM Club Meeting,4-15-22,1:30 P.M.,[enter receiver emails as comma separated list here]")
temp.send_mass_email()
