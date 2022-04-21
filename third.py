from Producer import keySender

key1="black"
key2="orange"
current = key1

while True:
    data=input("Enter Message \n")
    if data=='stop':
        break
    current = key2 if current==key1 else key1
    keySender(current,data+" ::"+ current)
    