from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib

template = Template(Path("template.html").read_text())

message = MIMEMultipart()
message["from"] = "Paul McCartney"
message["to"] = "testuser@codewithme.com"
message["subject"] = "This is a test"

# body = template.substitute({"name": "John"}) # with dictionary
body = template.substitute(name="John")  # with keyword arguments
message.attach(MIMEText(body, "html"))

message.attach(MIMEImage(Path("me.png").read_bytes()))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("jebarcha@gmail.com", "Libertad1974$")
    smtp.send_message(message)
    print("Sent...")
