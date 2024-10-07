




p1 ="Make a lot of money"
p2 ="buy now"
p3 ="subscribe this"
p4 ="click this"
message =input("enter a comment:")
if( (p1 in message) or (p2 in message) or (p3 in message)or (p4 in message)):
    print("this message is a spam")
else:
    print("This message is not a scam")