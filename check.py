#  Asks the user to enter an integer 

num=int(input("enter the number:"))

#  checks different conditions: 

if num>0 and num%2==0:
    print("The number is a positive even number.")

# a.	If the number is positive and even → "The number is a positive even number." 

elif num>0 and num%2!=0:
    print("The number is a positive odd number.")
# b.	If the number is positive and odd → "The number is a positive odd number." 

elif num<0 and num%2==0:
    print("The number is a negative even number.")
# c.	If the number is negative and even → "The number is a negative even number." 

elif num<0 and num%2!=0:
    print("The number is a negative odd number.")
# d.	If the number is negative and odd → "The number is a negative odd number." 

else:
    print("The number is zero.")
# e.	If the number is zero → "The number is zero." 

# this is end of program 