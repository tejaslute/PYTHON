#calculator basic operations : 
number1=float(input("Enter an number1 : "))
number2=float(input("Enter an number2 : "))
print("1.Addition\n2.subraction\n3.Multiplicatoion\n4.Division\n5.Modulus")
input1=int(input("\nEnter an your choice : "))
def switch(input):
    if input1==1:
        print(number1+number2)
    elif input1==2:
        print(number1-number2)
    elif input1==3:
        print(number1*number2)
    elif input1==4:
        print(number1/number2)
    else:
        print(number1%number2)
switch(input1)
