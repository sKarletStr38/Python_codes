hrs=int(input('Enter hours in 24 format: '))
if(0<=hrs<=23):
    if(4<=hrs<=6):
        print("Breakfast")
    elif(12<=hrs<=13):
        print("Lunch")
    elif(16<=hrs<=17):
        print("Snacks")
    elif(19<=hrs<=20):
        print("Dinner")
    else:
        print("Patience is a virtue")
else:
    print("Wrong time")