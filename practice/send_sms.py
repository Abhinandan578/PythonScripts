from twilio.rest import Client
account_sid="ACcf655e4f5706a3dcda6a056a8905f7a8"
auth_token = "fdb52ae44dec12e927ccca6810fcf648"

client = Client(account_sid,auth_token)

message=client.messages.create(
	to="+917419111578",
	from_="+61488810558",
	body="Hey New assignment added")
print(message.sid)
