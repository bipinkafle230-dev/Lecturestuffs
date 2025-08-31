list=[]



def show_menu():
    print("\n--- Todo_list here:---\n")          ## this is my first step of to do list using basic python work 
    print("1.View list")                         ## this show menu for waht can you do as :
    print("2. Add tasks")                        ## view , add , remove , update  and exit todo list
    print("3.Remove tasks")
    print("4.Update list")
    print("5.Quit")
print(show_menu())                              ## this print the menu in console


#todo_list view 

def view_list():
    if not list:
        print("\n Your todo_list is empty. start making todo list.")
    else:
        print("\n Your todo_list is this:")
        for i in range (len(list)):
            print(f"{i+1}.{list[i]}")


#todo_list add
def add_task():
    task=input("Enter the task to to do list:")
    list.append(task)
    print(f"Task,{task} is added")



#todo_list remove

def remove():
    view_list()
 
    try:
        task_num = int(input("Enter the number of the task to remove:"))

        if 1<= task_num <= len(list):
           removed_task =list.pop(task_num-1)       
           print(f"Task ' {removed_task}' removed!")
        else:
            print("Invalid number!.")
    except ValueError:
        print("please enetr a valid number.")


        
# Main program loop 

while True:                                              #This creates an infinite loop.
    show_menu()
    choice=input("Enter your choice(1-4):")              #Stores the answer as a string in choice.

    if choice =='1':                                     # view list 
        view_list()
    elif choice == '2':                                  # add list
        add_task()
    elif choice == '3':                                  # remove list
        remove()
    elif choice == '4':                                  #Exit it 
        print("Goodbye!")
        break
    else:
        print("Invalid choice . please try again.")     # end 

 #### this is what for satarting operation in to do list creation and deletion 


 ### end of program

