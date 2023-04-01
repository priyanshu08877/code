# normal function 
# def double(x):
#     return x*2
# print(double(9))

# lambda function :-

# double =lambda x: x*2
# print(double(7))

# python code illistrate square of number
# showing difference between def() and lambda()
# defining the normal function using def 
# def square(x):
#     return x*x
# definding th elambda funcrion 
# lambda_square=lambda y: y*y
# using the normallu defined function 
# print(square(5))
# using the lambda fucntion 
# print(lambda_square(5))

# def multi(x,y):
#     return x*y
# print(multi(5,11))

# multi =lambda x,y: x*y
# print(multi(5,11))

# normal function and lambda function execute table 
# def func(a,b,c,d,e):
#     return ((a+b)/(c+d))*e
# print(func(1,2,3,4,5))

# func =lambda a,i: a*i
# for r in range (1,11):
#     print('5 x ', r , ' = ',func(5,r))
# exapmle of lambda function using if-else 
# a=int(input("Enter 1st number : "))
# b=int(input("Enter 2nd number : "))
# Max=lambda a,b: a if(a>b) else b
# print(Max(a,b))

# Example-2 : find wether the number is Even or Odd
# result=lambda x: print(x, "is even") if x % 2 ==0 else print (x,"is odd")
# result(32)
# result(31)
# Another way  of writing the same lambda function is by using 
# result=lambda x: f'{x} is even' if x % 2==0 else f'{x} is odd'
# print(result(3))

# output=lambda x,y : f"{x} is smaller than {y}"\
# if x < y else f"P{x} is greater than {y}" if x > y \
#     else f"{x} is equeal to {y}"
# print(output(20,50))
# print(output(20,20))
# print(output(20,10))

# result=lambda x: x*2 if x< 10 else x* 3 if x< 20 else x
# print ("result of 7", result(7) )
# print("result of 12 ", result(12))

# map function:-

# def doSquare(n):
#     return n*n
# numbers=[1,2,3,4]
# result =map(doSquare,numbers)
# print(result)

# def doSquare(n):
#     return n*n
# numbers=[1,2,3,4]
# result =map(doSquare,numbers)
# sursand=tuple(result)
# for item in sursand:
#     print(item,end=" ")

# map() function
# filter function()
# filter with lambda
# file hnadling

# def doSquare(n1,n2):
#     return n1 * n2
# numlist1=[1,2,3,4]
# numlist2=[10,20,30,40]
# result =map(doSquare,numlist1,numlist2)
# print(list(result))

# numbers=(1,2,3,4,5,6,7,8,9,10)
# def check_even(number):
#     if number % 2 == 0: return True
#     else: return False
# even_numbers_iterator= filter(check_even,numbers)
# even_numbers=list(even_numbers_iterator)
# print(even_numbers)

# ages=[45,10,15,7,24,32]
# adults=list(filter(lambda x:(x > 18),ages))
# print(adults)

