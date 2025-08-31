# Greeting Using Built-in string function 

greet= input("Enter the greeting:").lower()  #Case-insensitivity

 #always input in lower correcting for case-insenstivity

if greet.startswith("hello"):
    print("$0")

# Greeting starts with "hello" → output $0

elif greet.startswith("h"):
    print("$20")

# Greeting starts with "h" (but not "hello") → output $20`
else:
    print("$100")

# Otherwise → output $100

#end of program