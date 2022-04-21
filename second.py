from Producer import messageSender

while True:
    data=input("Enter Message \n")
    if data=='stop':
        break
    messageSender(data.encode('utf-8'))
    