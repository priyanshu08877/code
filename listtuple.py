#num=2
#a=1
#print("the multiplication table of :",num)
# while a<=10:
#    ans=num*a
#    print(num,'x',a,'=',ans)
 #   a+=1
 
 
#break statement ka use tab kiya jata hai jub hume ek certain condition k baad loop se exit karna ho..for example:-
#colors = ["red","yellow","green","black"]
#for x in colors:
#    print(x)
#   if x == "green":
#       break

#continue satement ka use current iteration ko skip karke next\ one k saath continue karne k liye kiya jata hai..for example:- 
#colors = ["red","green","yellow","black"]
#for x in colors :
#    if x == "green":
#        continue
#   print(x)

#range function ka use ek group of satements ko specified number of times tak execute karne k liye kiya jata hai..for example:-
#for x in range(5):
#    print(x)
#to print in specified range   
#print(list(range(2,8))) 

#end clause is used at the end of for loop..else part tab execute karta hai jab loop naaturally terminate karta hai matlab foor loop k execute karne k baad else part execute karta hai..for example:-
#colors = ['yellow','black','green','purple']
#for x in colors:
#    print(x)
#else:
#   print("done!!")

# python program that accepts a word from user and reverses it :-
#string = input()
#reverse_string =""
#for i in string:
#    reverse_string = i+ reverse_string
#print(reverse_string)

#python program to find factorial of number:-
#num=5
#factorial=1
#for i in range(1,num+1):
#    factorial=factorial*i
#print("the factorial of",num,"is",factorial)

#python program to print first 10 natural number:-
#n=11
#for i in range(1,n):
#    print(i)

#python program to print all the even numbers within the given range:-
#num=10
#for i in range(num):
#    if i%2==0:
#       print(i)

# python program to sum of numbers:-
# n=10
# sum=0
# i=1
# while i <= n:
#     sum= sum + i
#     i=i+1
# print("the sum is", sum)

# python program to print pattern:-
# n=int(input("enter number of rows:"))
# for i in range(n):
#     for j in range(i,-1,-1):
#         print(j+1,end=" ")
#     print()



 
# list=['java','python',1997,2000];
# print("value avliable in index 2:") 
# print(list[2])
# list[2]=2001;
# print("new value available in index 2")  
# print(list[2])

# list=['java','python',1991,2000]
# list.insert(2,'django')
# print(list)

#enumerate function ka use karke hum kisi ka index number bta sakte hai..
# letters=['a','b','c','d']
# print(list(enumerate(letters)))

# fruits=["apple","orange","mango"]
# i=0
# while i<len(fruits):
#     print(fruits[i])
#     i=i+1

# list1=[[1,2],[],[3,4]]
# for i in list1:
#     if i==[]:
#         print(i,"is empty")
#     else:
#         print(i,"has data!")

# tuple1=()
# print("initial empty tuple:")
# print(tuple1)

# creating a tuple with the use of string 
# tuple1=('hello','python')
# print("\n tuplewithe the use of string:")
# print("tuple 1")

# list1=[1,3,5,7,9,"hello","python"]
# print("\n tuple using list:")
# print(tuple(list1))

# tuple1=tuple('python')
# tuple1=tuple("python")
# print(tuple1)

# tuple1=tuple("python")
# print("\n first element of tuple")
# print(tuple1[0])

#creating a tuple with nested tuples:-

Tuple1=(1,2,3)
Tuple2=('Django','Python')
Tuple3=(Tuple1,Tuple2)
print("\nTuple with nested tuples: ")
print(Tuple3)

#tuple unpacking
# tuple1=("python","for","freshers")
#the line unpacked value of tuple1
# a,b,c=tuple1
# print("\n value after unpacking")
# print(a)
# print(b)
# print(c)

#concatenation of tuples
# tuple1=(0,1,2,3)
# tuple2=('python','for','freshers')
# tuple3=tuple1+tuple2
#printin first tuple
# print(tuple1)
# print("\n tuple 2:")
# print(tuple2)
#print final tuple
# print("\n tuple after concatenation:")
# print(tuple3)

# tuple1=tuple('pythonforfreshers')
# print("removal of first element:")
# print(tuple1[1:])
# print("\n tuple after sequence of element is reversed:")
# print(tuple1[::-1])
# print("\n printinf elements between range 4-9:")
# print(tuple1[4:9])

# name=["priyanshu","sonu","naveen","gaurav"]
# roll_no=[1,3,4,5]
# course=["bca","mca","bba","mba"]
# mapped_result=zip(name,roll_no,course)
# print(list(mapped_result))

# name=["sonu","pelu","bholu","golu"]
# roll_no=[1,2,3,4]
# course=["bca","mca","bba","mba"]
# mapped_result=zip(name,roll_no,course)
# list1=list(mapped_result)
# print(list1)
# n,r,c=zip(* list1)
# print(n)
# print(r)
# print(c)




