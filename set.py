#list is ordered, changeable and allow duplicate values..
#tuple is ordered, unchangeable and allow duplicate values..
#set is unorderd, unchangeable*, unindexed and doesn't allow duplicate values..
#sets are used to store multiple values in a single variable..

# thisset={'banana','mango','cheery'}
# print(thisset)

#sets are unorderd so you can't be sure in which order theitems will appear..
#once a set is created,you cant make any changes to it but you can ramove and add new items..
#the values True and 1 are considered same in set, and are treated as dplicate and return value any one of them..

# thisset={'ram','shyam','mohan','ram',1,True,2} 
# print(thisset)

#length of set:-

# thisset={'ram','shyam','mohan','krishn'}
# print(len(thisset))

#set items-data types:-
#string,int,boolean data types:-
# set1={'apple','mango','cherry','guava'}
# set2={1,3,5,7,9}
# set3={True,False,False}
# print(set1)
# print(set2)
# print(set3)

#a set with string,integer and boolean values:-
# thisset={'banana','ram',True,False,23,25}
# print(thisset)

#type of set:-

# myset={"ram","shyam","mohan","krishn"}
# print(type(myset))

#the set() constructor to make a set:-

# myset=set(("ram","shyam","krishn","mohan"))
# print(myset)

#access set items:-
# myset={"ram","mohan","shyam","krishn"}
# for x in myset:
#    print(x)
   #check if shyam is present in this set:-
# myset={"ram","mohan","shyam","krishn"}
# print("shyam" in myset)

#how to add set:-
# myset={"banana","orange","apple"}
# myset.add("grapes")
# print(myset)  

#to add items from another set to cuurent set use update() method:-
# myset={"orange","apple","mango","grapes"}
# thisset={"ram","shyam","mohan","krishn"}
# myset.update(thisset)
# print(myset)

#the object in update() method does not have to be set,it can be any iterable objects like tuples,lists,dictionaries,etc.for example:-
# myset={"ram","shyam","mohan","krishn"}
# mylist=["orange","apple","grapes","cheery"]
# myset.update(mylist)
# print(myset)

#to remove an item in set use remove() or discard() method:-
#myset={"ram","shyam","mohan","krishn"}
#myset.remove("mohan"){item to remove is not present,remove() will raise an error}
#or,
#myset.discard("mohan"){item to discard is not present,discard() will not raise an error}
#print(myset)

#using pop() method will remove random item from set because set is unordered..for example:-

# myset={"orange","apple","mango","grapes"}
# x= myset.pop()
# print(x)
# print(myset)

#to empty the set use clear() method:-
# myset={"ram","shyam","mohan","krishn"}
# myset.clear()
# print(myset)

#the del keyword will delete the set completely..for example:-
# myset={"shyam","ram","mohan","krishn"}
# del myset
# print(myset)

#you can loop through set items using a for loop:-
# myset={"ram","shyam","mohan","krishn"}
# for x in myset:
#    print(x)

#there are several ways to join two or more sets in python..
# union() method returns a new set containing all items from both the sets and update()
# method insert all the items from one set into another:-

# set1={"ram","shyam","mohan","krishn"}
# set2={1,2,3,4}
# set3=set1.union(set2)
# print(set3)






