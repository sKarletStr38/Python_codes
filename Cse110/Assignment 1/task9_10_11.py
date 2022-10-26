sec=int(input('Enter value in seconds: '))
hours= int(sec/3600)
minutes=int((sec%3600)/60)
secs=int((sec%3600)%60)
print("Hours: ",hours," Minutes: ",minutes," Seconds: ",secs)


#----Task10----

hrs=int(input('Enter working hours: '))
if(0<hrs<=40):
    print(hrs*200)
elif(168>hrs>40):
    print(8000+(hrs-40)*300)
elif(hrs>168):
    print("Impossible to work more than 168 hours weekly")
else:
    print("Hours cannot be negative")

#-----Task11-----
s=int(input('Enter value of S: '))
ell=0
if(s>=100):
    ell=12000/(4+(s**2/14900))
else:
    ell=3000-125*s**2
print(ell)