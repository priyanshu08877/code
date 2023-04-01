# x=24
# y="ing"
# mylist=[10,20,30,40,50]
# mystr="Coding"
# if(x not in mylist):
#     print("X is not present in mylist")
# else:
#     print("x is prsent in my list ")


# ternary operator
# nice_weather=True

# print("Go out for a walk ! " if nice_weather else "Watch movie at  home!")
# How to take input from user 
#input method stop program 
#input hone ke bad string type ka hi variable banta hai 
# print("Line1")
# print("Line2")
# # x=input("Enter your name: ")
# x=int(input("Enter any number : "))

# print("value of x: ", x+1)
# ek data-type me convert krne ko typecasting kahte hai 
# a=int(input("Enter 1st number "))
# b=int(input("Enter 2nd number "))
# s=a+b
# print("Sum is ", s)
# split function
#ye sentence me space dekhta hai aur uske bad ye space ke abd ka word ko divide kr deta hai 
#split sirf string pe work krta hai aur koi data type pe nahi krta hai 
#agr ham kisssi particular charcter se ya symbol se split krna chahte hai to ham split ke andar ka hum symbol de skte hai

# a, b=input("Enter two number ").split()

# s=int(a)+int(b)
# print("Sum is : ", s)
# age hame swap krna ho to ham is prakar se  kr sskte hai 
# a,b=10,23
# print(a,b)
# a,b=b,a
# print(a,b)

# Working with string 
# type to initailise string 
#string ke andar ka particular part me ham assign na kr skte hai 
#string ko ham iterative ke skte hai 
#print method hamesha end new line ke sath hota hai 
#str1="Hello"
#str1[2]="L"
# for v in str1:
#     print(v,end="")

# str1="HelloPython"
# print(str1[0:4:2])
#Docstrings means documentation string 

#function ko hamseha 
# def myFunc():
#     '''
#      function name: mufunc()
#      usage: myfunc(int(x), int(y))
#      fdsf fsds fdsf sd fs 
#     '''
#     print("djdjsd")

# help(myFunc)
# Docstring kko help me se access kr skte hai 
#print(myFunc._doc_)
#jo variable double undersocre laga hota hai aage aur piche  se hota hai usko tander varible bolte hai 

# print(type(myFunc))

# age muje kissi string ko delete krna hai to del keyword ka use kr skte hai 
# str1="jell"
# del str1
# print(str1)
str1="helllo"
#print(len(str1))
obj=enumerate(str1)
for  o in obj:
    print(o)
# enumerate  function enumerate object banata hai