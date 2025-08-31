import calendar
# ''' What actually is python??

# it is Natural Programming Language
# simple to learn
# easy to understand

# Python is a popular programming language. 
# It was created by Guido van Rossum, and released in 1991.

# It is used for:

# web development (server-side),
# software development,
# mathematics,
# system scripting.

# '''

# print("hello world")

# # python variabes
# name="bipin"
# age=20
# email="kalue@gmail.com"
# Trial=True
# height=5.9

# print(name)
# print(age)
# print(email)
# print(Trial)
# print(height)

# # concatenation
# print("My name is " + name + " and my age is " + str(age) + ". My email is " + email)

# # datatypes knowing 

# print(type(name))
# print(type(age))  
# print(type(email))
# print(type(Trial))
# print(type(height))


# # type casting
# age = 20
# age = str(age)  # converting integer to string
# print("My age is " + age)  # now this will 

# height=2.90
# height=int(height)  # converting float to integer
# print("My height is " + str(height))  # now this will work

# trial="true"
# trial=str(trial)  # converting boolean to string
# print("Trial is " + trial)  # now this will work


# # input from user
# name = input("Enter your name: ")
# age= input("Enter your age: ") 
# email = input("Enter your email: ")
# print("My name is " + name + ", my age is " + age + ", and my email is " + email)

# # if we ask user for input if it is integer only than also interpreter think it is a string so for other than string we have to convert it
# age = int(input("Enter your age: "))  # converting string to integer
# height=float(input("Enter your height: "))  # converting string to float
# ("My age is " + str(age) + " and my height is " + str(height))
# # using f-string for better readability
# print(f"My name is {name}, my age is {age}, and my email is {email}. My height is {height}.")  

# #loop used here

# for x in range(10):
#     print(x)
    
#     # 10 numbers printed here !!!!
      


# # String operations
# first = "Hello"
# second = "World"
# combined = first + " " + second  # "Hello World" 
# repeated = first * 3            # "HelloHelloHello"

# print(combined)
# print(repeated)


# #quotations
# print("this is quotion:""")


# # argument here is function call garda pass garne value.

# print("bipin" , end="")
# print("here")


# #funtion
# def total(*num):
#     return sum(num)
# print(total(8, 23 ,43 ,22 )) 
  
  
# # multiple inputs in line 

# x, y, z = input("Enter three values: ").split()
# print("Total number of students: ", x)
# print("Number of boys is : ", y)
# print("Number of girls is : ", z)


# #string doing here 
# name, address, post =input("Enter the name , address and post of yours:").split()
# print(f"My name is {name}.")
# print(f"My permanent address is {address}.")
# print(f"My post in my company is {post}.")

# #data's are taken 
# data = f"{name}, {address}, {post}"

# # Writing 'name' to file1.txt
# with open("file1.txt", "w") as f1:
#     f1.write(data)

# # Reading from file1.txt
# with open("file1.txt", "r") as f1:
#     content = f1.read()

# # Writing the read content to file2.txt
# with open("file2.txt", "w") as f2:
#     f2.write(content)

# #checking if the file is copied or not
# if content == data:
#     print("File copied successfully!!") #copied
# else:
#     print("No file copied here") # no copy



#calendar  


year =2025
month =8

print(calendar.month(year, month))



