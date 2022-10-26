marks=int(input('Enter the marks: '))
if(0<=marks<=100):
    if(marks<50):
        print("F")
    elif(50<=marks<=59):
        print("E")
    elif(60<=marks<=69):
        print("D")
    elif(70<=marks<=79):
        print("C")
    elif(80<=marks<=89):
        print("B")
    else:
        print("A")
else:
    print("Invalid Input")