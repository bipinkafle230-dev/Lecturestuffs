#lists
mylist=["apple", "banana", "cherry"]
print(mylist)

#mylist.add["playing"]  #'list' object has no attribute 'add'
#mylist.add(1,"kopila") #'list' object has no attribute 'add'
#features
'''
ordered
changeable
allows duplication
'''

#examples of list
#lists length
print(len(mylist))

#accessing in lists
print(mylist[1])

#change items value
mylist[2]="naspati"
print(mylist)

#indexwise
mylist[0:2]="mango", "blackberry"
print(mylist)

#inserting new items here
mylist.insert(3,"Kimbuu")
print(mylist)

#append 
mylist.append(3,"kandamul")
print(mylist)

#extend adding two list using extend function
okeyXa=["23","778"]
mylist2=mylist.extend(okeyXa)
print(mylist2)

#removing
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

#pop function
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#clear() function
mylist.clear()
print(mylist)

#loop through list
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
  
  
