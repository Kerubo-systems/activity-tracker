# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 16:15:57 2026

@author: godfr
"""

"""
Activity Tracker CLI App
------------------------
This is a command-line app (basically no icons) for planning and productivity purposes.

It lets a user:
    1. Add tasks
    2. Track study sessions
    3. Set goals
    4. View progress
    5. Save/load data from a file
"""

# Motivation: I love coding and being organized.
# Doing this primarily for fun and practice after a coding break.

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
            if len(tasks) <= 0:               #thinking of updating this later to alert the user that neg integers are invalid
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
                
                if 0 <= index < len(tasks):      #controls parameters for indexing and slicing
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
