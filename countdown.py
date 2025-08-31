# Countdown Timer
def countdown_timer():
    count_from = int(input("Enter a number to start the countdown from: "))
    
    # The current value of our counter
    current = count_from
    
    print("Countdown starting now!")
    
    # Loop as long as current is greater than or equal to 0
    while current >= 0:
        print(current)
        # This is the same as current = current - 1
    
    print("Blast off! 🚀")

# Start the timer
countdown_timer()