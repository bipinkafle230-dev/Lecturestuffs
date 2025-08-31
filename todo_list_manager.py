# Simple To-Do List Manager (Command line):
todo_list=[]

# this is array for to-do list.

def show_menu():
    print("\n--- To-Do list Menu---")
    print("1.View list")
    print("2.Add task")
    print("3.Remove task")
    print("4.Quit")

# choose from here what to do.

def view_list():
    if not todo_list:
        print("Your to-do list is empty! Good job!")
    else:
        print("\nYour to-do list:")
        for i in range(len(todo_list)):
            print(f"{i+1}. {todo_list[i]}")
 
        # for index, task in enumerate(todo_list, start=1): #enumerate(todo_list, start=1) → gives both index (starting from 1) and the task.
        #     print(f"{index}.{task}")
# viewing to do list and what is inside of it.


def add_task():                                          #This function adds a new task.
    task = input("Enter the task to add:")
    todo_list.append(task)                               #todo_list.append(task) → adds it to the list.  
    print(f"Task '{task} added !")

# adding to do tasks here.


def remove_task():                                      #This function removes a task by number.
    view_list()                                         # View current tasks list

    try:
        task_num = int(input("Enter the number of the task to remove:"))

        if 1<= task_num <= len(todo_list):
           removed_task =todo_list.pop(task_num-1)       #todo_list.pop(task_num-1) removes the task at that position (minus 1 because lists start at index 0)
           print(f"Task ' {removed_task}' removed!")
        else:
            print("Invalid number!.")
    except ValueError:
        print("please enetr a valid number.")

# removing tasks as you complete it.


# Main program loop 

while True:                                              #This creates an infinite loop.
    show_menu()
    choice=input("Enter your choice(1-4):")              #Stores the answer as a string in choice.

    if choice =='1':                                     # view list 
        view_list()
    elif choice == '2':                                  # add list
        add_task()
    elif choice == '3':                                  # remove list
        remove_task()
    elif choice == '4':                                  #Exit it 
        print("Goodbye!")
        break
    else:
        print("Invalid choice . please try again.")     # end 

 #### this is what for satarting operation in to do list creation and deletion 


#### end of program 
