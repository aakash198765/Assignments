#-----------------Assignment 2 ----------------------------------

#Required altitude in feet
requied_altitude=1000

#Flight Altitude
altitude=int(input("Please Enter your Altitude so we can help : "))

if altitude>5000:
    print("Turn Around")
elif altitude < 5000 and altitude>requied_altitude:
    print("Bring down to 1000ft")
else:
    print("Safe to land")

