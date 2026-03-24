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

import json
import os

tasks = []
sessions = []


def save_data():
    with open("sessions.json","w") as s:
        json.dump(sessions, s, indent=4)
    with open("tasks.json", "w") as t:
        json.dump(tasks, t, indent=4)
        
def load_data():
    if os.path.exists("sessions.json") and os.path.exists("tasks.json"):
        global sessions, tasks
        with open ("sessions.json", "r") as s:
            sessions = json.load(s)
        with open("tasks.json", "r") as t:
            tasks= json.load(t)

def show_menu():
    while True:
       
        print("\n---Study Tracker---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Complete")
        print("4. Log Study Session")
        print("5. View Study Summary")
        print("6. Exit")
        
        choice = int(input("Choose an option. "))
        
        if choice == 1:
            print("Adding Task...")
            title = input("What is the title to your task? ")

            task = {
                "title": title,
                "completed": False
            }

            tasks.append(task)
            save_data()

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
            save_data()
                    
        elif choice == 4:
            subject = input("Enter subject name: ")
            duration = int(input("Enter duration (minutes): "))
            
            if duration <= 0:
                print("Come on! Even a minute🥺: ")
                continue
            
            session = {
                "subject": subject,
                "duration": duration
                }
            
           
            sessions.append(session)
            save_data()
            
        # Study summary
        elif choice == 5:
            print("Viewing Study Summary...")
            
            if len(sessions) <= 0:
                print("No sessions available.")
                
            else:
                #SUBJECT TOTALS
                subject_totals = {}
                
                
                for session in sessions:
                   sub = session["subject"]
                   time = session["duration"]
                   
                   if sub not in subject_totals:
                       subject_totals[sub] = time
                   else:
                        subject_totals[sub] += time
                    
                for subject, time in sorted(subject_totals.items(), key = lambda x:x[1], reverse = True):
                    print(f"{subject}: {time} minutes")
                    
                    
                #TOTAL TIME
                total_time = 0
                
                for session in sessions:
                    total_time += session["duration"]
                
                print(f"Your total study time today was: {total_time} minutes")
            
        elif choice == 6:
            save_data()
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Try again.")
            


load_data()
show_menu()

