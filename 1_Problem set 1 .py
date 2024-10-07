a=float(input("enter first number:"))
b=float(input("enter second number:"))
c=float(input("enter third number:"))
d=float(input("enter fourth number:"))
if(a>b and a>c and a>d):
    print("a is greatest number:")

elif(b>a and b>c and b>d):
    print("b is greatest number:")
elif(c>b and c>a and c>d):
    print("c is greatest number:")
elif(d>c and d>b and d>a):
    print("d is greatest number")