def sum(n):
    return (n)

num1=int(input("enter num1:"))
num2=int(input("enter num2:"))
n=num1+num2
print(n)


# If-elif-else
age = 18
if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
else:
    print("Adult")

# For loop
for i in range(5):  # 0 to 4
    print(i)

# While loop
count = 0
while count < 5:
    print(count)
    count += 1
    
#playing game here
#random user and cpu game
num1=int(input("enter number between 1-100:"))
for x in range(1,100):
     print(x)
     
#check
if(num1>x):
    print("you won")
elif(num1==x):
    print("equal")  
elif(num1<x):
     print("you lost")
else:
    print("type here...........")


