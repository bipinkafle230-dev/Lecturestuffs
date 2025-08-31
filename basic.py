# We need to import the 'time' module for the delay
import time

def countdown_timer(seconds):
    while seconds:
        # Calculate minutes and seconds
        mins, secs = divmod(seconds, 60)
        # Format the time as MM:SS
        timer = '{:02d}:{:02d}'.format(mins, secs)
        # Print the timer, overwriting the previous line
        print(timer, end='\r')
        # Wait for one second
        time.sleep(1)
        # Decrement the total seconds
        seconds -= 1
    
    print("Time's up!") 

# Get input from user (e.g., type 120 for 2 minutes)
total_seconds = int(input("Enter the time in seconds: "))
countdown_timer(total_seconds)