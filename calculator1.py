#calculator 
num1=int(input("Enter an num1 : "))
op=input("Enter an operator : ")
num2=int(input("Enter an num2 : "))
if op=="+":
    print("Addation is ", num1+num2)
elif op=="-":
    print("Subraction is " ,num1-num2)
elif op=="*":
    print("Multlipcation is ",num1*num2)
else:
    print("Division is ",num1/num2)