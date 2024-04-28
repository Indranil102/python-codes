
num1=int(input("enter num1"))
num2=int(input("enter num2"))
op=input("enter operator")

if (op=='+'):
    print(num1+num2)
elif(op=='-'):
    print(num1-num2)
elif(op=='*'):
    print(num1*num2)
elif(op=='/'):
    print(num1/num2)
else:
    print("invalid operator")