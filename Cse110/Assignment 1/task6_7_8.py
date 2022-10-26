n=int(input("Enter number:"))

if(n%2==0 or n%5==0):
    print(n)
else:
    print("Not multiple of 2 or 5")

#----Task7----
num=int(input("Enter number:"))

if(num%2==0 and num%5==0):
    print("Multiple of 2 and 5")
elif(num%2==0):
    print(num)
elif(num%5==0):
    print(num)
else:
    print("Not multiple")

#----Task8----
numb=int(input("Enter number:"))

if(numb%2==0 and numb%5==0):
    print(numb)
else:
    print("Not multiple of 2 and 5 both")