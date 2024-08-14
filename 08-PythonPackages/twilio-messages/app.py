from twilio.rest import Client

account_sid = ""
auth_token = ""

client = Client(account_sid, auth_token)

call = client.messages.create(
    to="...",
    from_="",
    body="This is our first message"
)

# call.date_created
# call.date_sent
