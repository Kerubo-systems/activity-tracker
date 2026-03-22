# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 16:15:57 2026

@author: godfr
"""

"""
This is a command-line app(basically no icons) for planning and productivity purposes
It lets a user:
    1. add tasks
    2. track study sessions
    3. set goals
    4. view progress
    5. save/load data from a file
"""

# I'm doing this because I love to code and be organized as well. 
# Primarily for fun and I haven't coded in a while too.
# So let's get started. (Day format: DD/MM/YYYY)

#Day 1(17/03/2026): ...I'm wondering whether this should be in a README file.
"""
I can't believe I haven't started coding. Still comments!!
Today's goal:
    - Program should let the user:
        1. Add a task
        2. View tasks
        3. Mark tasks as complete.
"""

# Menu Loop

tasks = []

def show_menu():
    while True:

        print("\n---Study Tracker---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Complete")
        print("4. Exit")
        

        choice = int(input("Choose an option. "))
        
            

        if choice == 1:
            print("Adding Task...")
            title = input("What is the title to your class? ")

            task = {
                "title": title,
                "completed": False
            }

            tasks.append(task)


        elif choice == 2:
            print("Viewing Tasks...")
            if len(tasks) <= 0:
                print("No tasks available.")
            
            else:
                for n,task in enumerate(tasks):
                    status = "✅" if task["completed"] else "❌"
                    print(f"{n+1}. {task['title']} [{status}]")
            

        elif choice == 3:
            print("Marking task status...")
            
            if len(tasks) == 0:
                print("No tasks available.")
                
            else:
                TaskNo = int(input("What task would you want to mark complete? "))
                index = TaskNo - 1
                
                if 0 <= index < len(tasks):
                     tasks[index]["completed"] = True
                     print(f"Marking task {TaskNo} complete!")
                
                else:
                    print("Invalid task number.")
            
        
        elif choice == 4:
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Try again.")
            

show_menu()