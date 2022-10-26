distance=int(input("Enter distance in meter: "))
time=int(input("Enter time in second: "))

distance=distance/1000
time=time/3600
velocity=distance/time
print(velocity,"km/h")
if(velocity>90):
    print("Too fast. Only a few changes should suffice")
elif(60<=velocity<=90):
    print("Velocity is okay. The car is ready!")
else:
    print("Too slow. Need more changes.")
