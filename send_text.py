from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACc721ce326e028e19b072b56a58c9568c"
auth_token  = "b8f670f44531f6f1197ccd83d8e898c9"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="We Are The Champions!!!",
    to="+13108040264",    # Replace with your phone number
    from_="+14243227120") # Replace with your Twilio number
print message.sid
