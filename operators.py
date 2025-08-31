#operators
#arithmetic operators
a=int(input("enter the number:"))
b=int(input("enter the number:"))
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)
print(a//b)
print(b**a)


#assignment operator
a+=b
print(a)
a*=b
print(a)
a%=b
print(a)

#logical operation 
num1=int(input("enter num1:"))
num2=int(input("enter num2:"))

if(num1>num2):
    print("num1 is greater than num2.")
elif(num2>num1):
    print("num2 is greater than num1.")    
elif(num1==num2):
    print("num1 is equals to num2.")   
else:
    print("Not equal:") 
    

#bitwise operation

num=(num1&num2)
print(f"num is here {num}")

nuil=(num1|num2)
print(f"num is here {nuil}")

nim=(num1 ^num2)
print(f"num is here{nim}")

kiop=(num1>>num2)
print(f"num is here{kiop}")

lop=(num1<<num2)
print(f"num is here {lop}")


#other operation

A = 7-1**3
print(A)

