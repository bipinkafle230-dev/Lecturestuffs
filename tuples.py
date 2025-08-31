#Tuple are used to store multiple items in a single variable.
#Tuples are ordered , unchangeable and allow for duplication.
my_tuple=("apple","mango","banana")
print(my_tuple)

#some other functionings
print(len(my_tuple))

#one element tuple
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#The tuple() Constructor
thistuple=tuple(("apple","banana"))
print(thistuple)

#accessing data in tuple
thisFr=("chatgpt","Deepseek","claude","cursor")
print(thisFr)

#index from 0 to 2 
print(thisFr[0:2])

#negative indexing
print(thisFr[0:-3])

#access in tuples elements
#check if "apple" is present in the tuple:
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
  
#tuples and list
x=("1,3,4,5,9")
y=list(x)
y[1]="joke"
x=tuple(y)
print(y)

# Adding items
#Convert the tuple into a list, add "orange", and convert it back into a tuple:
print("Adding")
year_with=("kabin","neer","kher")
print(year_with)
y=list(year_with)
print(y)
y.append("apple")
print(tuple(y))


# Add using 
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)


# Remove
print("Removing")
this_kinda=("ink","paper","pencil","copy")
y=list(this_kinda)
print(this_kinda)
y.remove("copy")
this_kinda=tuple(y)
print(y)


#Unpacking a tuple:
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

#astrik using
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)