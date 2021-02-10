#----------------------List and list's built-in function----------------------------------Task 1-------------------------
fruits=['apple','mango','guava','banana','grapes']
print(fruits)

#copy lsit - fruits
fruit1=fruits
print(fruit1)

#sort list - fruits
fruit1=fruits
fruit1.sort()
print(fruit1)

#reverse list - fruits
fruit1=fruits
fruit1.reverse()
print(fruit1)

#length of list - fruits
print(len(fruits))

#type of list - fruits
print(type(list))


#-----------------------Dictionary and it's built-in function------------------------Task 2----------------------------------------
cars={
    "Name" : "Mustang",
    "Model": "23AD",
    "Color": "Black",
    "Year": 2010
}

#print dictionay item - indexing
print("Color of car : ", cars["Color"])

#length of dictionay
print(len(cars))

#type of dictionary
print(type(cars))

#copy built-in function
car=cars.copy()
print(car)

#del built-in function
del car["Color"]
print(car)

#update built-in function
car.update({"Speed": "20kmh"})
print(car)