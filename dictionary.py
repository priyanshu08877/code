# dictionaries are used to store data into key:values pairs..
#a dictionary is a collection which is ordered,*changeable and don't allow duplicate values..
#dictionaries are written within curly brackets and have keys and values..

#create and print dictionaries:-

# car= {
# "brand":"ford",
# "model":"mustang",
# "year":1964    
#   }
# print(car)

#to print key value of brand or accessing the items of a dictionary {by referring to its key name,inside square brackets}:-

# car= {
# "brand":"ford",
# "model":"mustang",
# "year":1964    
#   }
#print(car["brand"])

#to determine how many items a dictionary has,use the len() function:-
# car= {
# "brand":"ford",
# "model":"mustang",
# "year":1964    
#   }
# print("length of dictinary",len(car))

#duplicate values will overwrite exiciting values..for example:-

# car= {
# "brand":"ford",
# "model":"ford",
# "year":1964,
# "year":2020  
# }
# print(car)

#the values in the dictionary items can be of any data type string,int,boolean and list data types..for example:-

# car= {
#     "brand":"ford",
#     "electric":"False",
#     "year":2020,
#     "colors":["red","white","blue"]
# }
# print(car)

#to print the data type of dictionary:-

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(type(thisdict))

#we can use dict() constructor to make a dictionary..for example:-

# thisdict = dict(name = "John", age = 36, country = "Norway")
# print(thisdict)

#get() method is also used to accessing the items of a dictionary:-

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = thisdict.get("model")
# print(x)

#the keys() method will return a list of all the keys in the dictionary:-

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x=thisdict.keys()
# print(x)

#The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list..

#Add a new item to the original dictionary, and see that the keys list gets updated as well..for example:-

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }
# x = car.keys()
# print(x) #before the change
# car["color"] = "white"
# print(x) #after the change

#The values() method will return a list of all the values in the dictionary..for example:-

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = thisdict.values()
# print(x)

#The list of the values is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the values list..

#Make a change in the original dictionary, and see that the values list gets updated as well..for example:-
# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }
# x = car.values()
# print(x) #before the change
# car["color"] = "red"
# print(x) #after the change

#The items() method will return each item in a dictionary, as tuples in a list..for example:-

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }
# x=car.items()
# print(x)

#The returned list is a view of the items of the dictionary, meaning that any changes done to the dictionary will be reflected in the items list..

#Make a change in the original dictionary, and see that the items list gets updated as well..for example:-

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }
# x = car.items()
# print(x) #before the change
# car["year"] = 2020
# print(x) #after the change

#Add a new item to the original dictionary, and see that the items list gets updated as well..for example:-

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }
# x = car.items()
# print(x) #before the change
# car["color"] = "red"
# print(x) #after the change

#To determine if a specified key is present in a dictionary use the in keyword..for example:-

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# if "model" in thisdict:
#   print("Yes, 'model' is one of the keys in the thisdict dictionary")

#You can change the value of a specific item by referring to its key name..for example:-

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["year"] = 2018
# print(thisdict)

#The update() method will update the dictionary with the items from the given argument..
#The argument must be a dictionary, or an iterable object with key:value pairs..for example:-

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.update({"year": 2020})
# print(thisdict)

#Adding an item to the dictionary is done by using a new index key and assigning a value to it..for example:-

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["color"] = "red"
# print(thisdict)

#There are several methods to remove items from a dictionary..

#The pop() method removes the item with the specified key name..for example:-

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.pop("model")
# print(thisdict)

#The popitem() method removes the last inserted item..for example:-

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.popitem()
# print(thisdict)

#The del keyword removes the item with the specified key name..for example:-

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# del thisdict["model"]
# print(thisdict)

#The del keyword can also delete the dictionary completely..for example:-

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# del thisdict
# print(thisdict) #this will cause an error because "thisdict" no longer exists.

#The clear() method empties the dictionary.for example:-

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.clear()
# print(thisdict)


# student_name= input("enter student's name: ")
# marks={"bill":90,"james":55,"andrew":77}
# for students in marks:
#     if students==student_name:{marks[students]}
#     break

#You can loop through a dictionary by using a for loop..

#When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well..

#Print all key names in the dictionary, one by one:

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for x in thisdict:
#   print(x)
  
#Print all values in the dictionary, one by one:

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for x in thisdict:
#   print(thisdict[x])
  
#You can also use the values() method to return values of a dictionary..for example:-
# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for x in thisdict.values():
#   print(x)

#You can use the keys() method to return the keys of a dictionary:

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for x in thisdict.keys():
#   print(x)

#Loop through both keys and values, by using the items() method:

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for x, y in thisdict.items():
#   print(x, y)

#You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2..

#There are ways to make a copy, one way is to use the built-in Dictionary method copy()..for example:-

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# mydict = thisdict.copy()
# print(mydict)

#Another way to make a copy is to use the built-in function dict().

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# mydict = dict(thisdict)
# print(mydict)


# student_name= input("enter student's name: ")
# marks={"bill":90,"james":55,"andrew":77}
# endcounter=0
# for students in marks:
#     if students== student_name: print(marks[students])
#     break
# else:
#     endcounter+=1
#     if endcounter== len(marks):
#      print("students name not found!")

#merge in dictionary
# dict1={'a':10,'b':20}
# dict2={'d':6,'c':4}
# dict3={**dict1,**dict2}
# print(dict3)
# print("length of dict3: ",len(dict3))

#list in dictionaries:-
# keys = {'ten','twenty','thirty'}
# values =[10,20,30]
# res_dict=dict(zip(keys,values))
# print(res_dict)

#A dictionary can contain dictionaries, this is called nested dictionaries..

#Create a dictionary that contain three dictionaries:-

# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }
# print(myfamily)

#Create three dictionaries, then create one dictionary that will contain the other three dictionaries:-

# child1 = {
#   "name" : "Emil",
#   "year" : 2004
# }
# child2 = {
#   "name" : "Tobias",
#   "year" : 2007
# }
# child3 = {
#   "name" : "Linus",
#   "year" : 2011
# }

# myfamily = {
#   "child1" : child1,
#   "child2" : child2,
#   "child3" : child3
# }
# print(myfamily)


# student={1: {'name': 'john', 'age': 18}, 2:{'name': 'deep', 'age': 20}}
# print(student[2],('name'))
# print(student[2],('age'))

# dictionary methods:-

# clear()- removes all items from the dictionary..
# copy()- returns a copy of dictionary..
# fromkeys()- returns a dictionary with specified keys and values..
# get()- returns a value with specified key..
# items()- returns a list containing a tuple for each key value pair..


