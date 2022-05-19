list3=[]
n=int(input("Enter an length : "))
print("\n Enter an Elements : ")
for i in range(0,n):
    list3.append(input("Enter an "+str(i)+" element "))
print("\n Printing an elements : ")
for i in list3:
    print(i,end=" " )
