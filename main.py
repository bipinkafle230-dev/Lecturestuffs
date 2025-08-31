#list in python
details=[
   'bipin',
   'sameer',
   'aadi',
   'kaluwa',
   'sandesh'
]
print(details)
print(type(details))
hack=len(details )
print(hack)

#list append 
details.append("ram")
print(details)

#list insertion
details.insert(2,"foxman")
print(details)

#list removing
details.remove("aadi")
print(details)

#list remove from pop()
details.pop(1)
print(details)


# play input and output
name=input("\nEnter the name:\n")
print("Hello", name ,"Welcome!")

name=input("Enter the name:")
print(f"Hello,{name} Welcome!")