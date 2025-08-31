import calendar
# import time
# # import time
# # import time

# # # import time for real time timing

# # #define for count down

# # def count(seconds):

# #     #seconds for parameters

# #  while seconds:
# #     mins,secs=divmod(seconds,60)
# #     timer='{:02d}:{:02d}'.format(mins, secs)
# #     print(timer,end='\r')
# #     time.sleep(1)
# #     seconds-=1
# #     print("Time's up !!")

# #     total_seconds=int(input("Enter it:"))
# #     count(total_seconds)



# def count(seconds):
#     while seconds:
#         mins, secs = divmod(seconds, 60)
#         timer = '{:02d}:{:02d}'.format(mins, secs)
#         print(timer, end='\r')
#         time.sleep(1)
#         seconds -= 1
#     print("Time's up !!")

# # Ask user for countdown time
# total_seconds = int(input("Enter time in seconds: "))
# count(total_seconds)





# Show calendar for August 2025
year = 2025
month = 8

print(calendar.month(year, month))


