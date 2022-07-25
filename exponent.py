
#power function using for loop
def raise_to_power(base,power):
    result=1
    for index in range(power):
        result=result*base
    return result

base=int(input("Enter an base : "))
power=int (input("Enter an power : "))
print("power is : ", raise_to_power(base,power))
