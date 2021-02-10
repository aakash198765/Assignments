#-----------------Assignment 2 ----------------------------------

#Required altitude in feet
requied_altitude=1000

#Flight Altitude
altitude=int(input("Please Enter your Altitude so we can help : "))

if altitude < requied_altitude:
    print("land the plane")
elif altitude == requied_altitude:
    print("Safe to land")
elif altitude >requied_altitude and altitude < 5000:
    print("Bring down to 1000ft")
elif altitude > 5000:
    print("Turn Around")

