#----Task3-----

num_1=int(input("Enter number:"))
num_2=int(input("Enter number:"))

if(num_1>num_2):
    print("First number is greater")
elif(num_1<num_2):
    print("Second number is greater")
else:
    print("The numbers are equal")


#-----Task4-----

num_1=int(input("Enter number:"))
num_2=int(input("Enter number:"))

if(num_1>num_2 or num_1==num_2):
    print(num_1-num_2)
else:
    print(num_2-num_1)


#-----Task5------

n=int(input("Enter number:"))
if(n%2==0):
    print("The number is even")
else:
    print("The number is odd")