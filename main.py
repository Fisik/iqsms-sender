from gate import Gate

sender = Gate(api_login = 'YOURLOGIN', api_password = 'YOURPASSWORD');

phonesArray = ['79991234567', '79991234576']

# getting account credits
print(sender.credits()) 

#getting sender names and removing from response some shit
senders = str(sender.senders()).replace("b'", "").split("\\n") 

#send sms
for phone in phonesArray:
    print(sender.send(phone = phone, text ='some text here', sender=senders[0])) 

#you may get status by request id in such way
#print(sender.status(12345))