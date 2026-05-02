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


from datetime import date
from data import load_data, save_data
from analytics import calculate_summary, weekly_summary
from dashboard import show_dashboard
from export import export_report, export_csv

tasks = []
sessions = []


def performance_summary():
    subject_totals, total_time, total_today, date_totals = calculate_summary(sessions)
    
    if not subject_totals:
        print("No study data yet.")
        return
    
    else:
        best_subject = max(subject_totals, key = subject_totals.get)
        best_day = max(date_totals, key=date_totals.get)
    
        print("PERFORMANCE SUMMARY")
        print("-" * len("PERFORMANCE SUMMARY"))
        print(f"Total time: {total_time} min.")
        print(f"Today's time: {total_today} min.")
        print(f"Best day: {best_day} ({date_totals[best_day]} min)")
        print(f"Best subject: {best_subject} ({subject_totals[best_subject]} min)")
        

def show_weekly_summary():
    subject_totals, daily_totals = weekly_summary()

    print("\nWEEKLY SUMMARY")
    print("-" * 20)

    if not subject_totals:
        print("No study data this week.")
        return

    total_time = sum(daily_totals.values())
    print(f"Total time: {total_time} min")

    # Best subject
    best_subject = max(subject_totals, key=subject_totals.get)
    print(f"Top subject: {best_subject} ({subject_totals[best_subject]} min)")

    # Best day
    best_day = max(daily_totals, key=daily_totals.get)
    print(f"Best day: {best_day} ({daily_totals[best_day]} min)")

    print("\nDaily Breakdown:")
    for day, time in sorted(daily_totals.items()):
        print(f"{day}: {time} min")

import matplotlib.pyplot as plt

def plot_weekly_trend():
    _, daily_totals = weekly_summary()

    if not daily_totals:
        print("No data to plot.")
        return

    # sort dates
    sorted_days = sorted(daily_totals.keys())
    times = [daily_totals[day] for day in sorted_days]

    plt.figure()
    plt.plot(sorted_days, times, marker="o")

    plt.title("Weekly Study Trend")
    plt.xlabel("Date")
    plt.ylabel("Minutes")

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
def plot_subject_breakdown():
    subject_totals, _ = weekly_summary()

    if not subject_totals:
        print("No data to plot.")
        return

    subjects = list(subject_totals.keys())
    times = list(subject_totals.values())

    plt.figure()
    plt.bar(subjects, times)

    plt.title("Weekly Study by Subject")
    plt.xlabel("Subject")
    plt.ylabel("Minutes")

    plt.tight_layout()
    plt.show()
    



def show_menu():
    while True:
       
        print("\n---Study Tracker---")
        print("1. Task Management")
        print("2. Study Session Management")
        print("3. Performance Summary")
        print("4. Weekly Summary")
        print("5. Show Graphs")
        print("6. Dashboard")
        print("7. Exports (Txt Report/CSV)")
        print("8. Exit")
        
        choice = int(input("Choose an option. "))
        print("\n")
        
        #TASK MANAGEMENT=========================================================================================
        if choice == 1:
            print("lOADING TASK MANAGEMENT MENU...")
            print("--------------------")
            
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Mark Task Complete")
            print("4. Delete Task")
            
            
            task_action = int(input("What would you want to do? "))
            
            #ADD TASK-----------------------------------------------------------------------------------------------------
            if task_action == 1:
                print("Adding Task...")
                print("--------------\n")
                title = input("What is the title to your task? ")

                task = {
                    "title": title,
                    "completed": False
                    }

                tasks.append(task)
                save_data(sessions, tasks)
                

            #VIEW TASKS----------------------------------------------------------------------------------------
            elif task_action == 2:
                print("Viewing Tasks...")
                if len(tasks) <= 0:               
                    print("No tasks available.")
            
                else:
                    for n,task in enumerate(tasks):
                        status = "✅" if task["completed"] else "❌"
                        print(f"{n+1}. {task['title']} [{status}]")
            


            #MARK TASKS COMPLETE------------------------------------------------------------------------------------------------------
            elif task_action == 3:
                print("Marking task status...")
            
                if len(tasks) == 0:
                    print("No tasks available.")
                
                else:
                    for n,task in enumerate(tasks):
                        status = "✅" if task["completed"] else "❌"
                        print(f"{n+1}. {task['title']} [{status}]")
                    
                    
                    TaskNo = int(input("What task would you want to mark complete? "))
                    index = TaskNo - 1
                
                    if 0 <= index < len(tasks):      #controls parameters for indexing and slicing
                        tasks[index]["completed"] = True
                        t = tasks[index]
                        print(f"Marking task {TaskNo} ({t['title']} {'✅' if t['completed'] else '❌'}) complete!")
                
                    else:
                        print("Invalid task number.")
                save_data(sessions,tasks)
                
            
                
            #DELETE TASKS------------------------------------------------------------------------------------------------
            elif task_action == 4:
                print("Task Deletion...")
                for n,task in enumerate(tasks):
                    status = "✅" if task["completed"] else "❌"
                    print(f"{n+1}. {task['title']} [{status}]")
                
                task_no = int(input("What task (by number) do you wanna delete? "))
                task_no -= 1
                
                if not (0 <= task_no < len(tasks)):
                   print("Invalid choice")
                else:
                    t = tasks[task_no]
                    print(f"Deleting: {t['title']} ({'✅' if t['completed'] else '❌'})")
                    tasks.pop(task_no)
                   
                save_data(sessions, tasks)
                    
                
            else:
                print("Invalid choice.")
                
                
        #STUDY SESSION MANAGEMENT================================================================================           
        elif choice == 2:
            print("LOADING STUDY SESSION MANAGEMENT MENU")
            print("-------------------------------------")
            
            print("1. Log Study Session")
            print("2. View Study Sessions")
            print("3. Delete Study Session")
            
            session_action = int(input("What would you like to do? "))
            
            #LOGGING STUDY SESSIONS----------------------------------------------------------------------------------
            if session_action == 1:
                print("Logging study session...")
                subject = input("Enter subject name: ")
                duration = int(input("Enter duration (minutes): "))
                day = date.today().isoformat()
            
            
                if duration <= 0:
                    print("Come on! Even a minute🥺: ")
                    continue
            
                session = {
                    "subject": subject,
                    "duration": duration,
                    "date": day
                    }
            
           
                sessions.append(session)
                save_data(sessions, tasks)
            
        # STUDY SUMMARY------------------------------------------------------------------------------------------------
            elif session_action == 2:
                print("Viewing Study Summary...")
            
                if len(sessions) <= 0:
                    print("No sessions available.")
                
                else:
                    #SUBJECT TOTALS
                    subject_totals, total_time, total_today, date_totals = calculate_summary(sessions)
                
                    
                for subject, time in sorted(subject_totals.items(), key = lambda x:x[1], reverse = True):
                    print(f"{subject}: {time} minutes")

                    
                    
                #TOTAL TIME
                print(f"Your total study time (all-time) was: {total_time} minutes")
                
                print("\n All Study Sessions:")
                for n,session in enumerate(sessions):
                    sub = session["subject"]
                    time = session["duration"]
                    day = session.get("date", "No date")
                    
                    print(f"{n+1}. {sub}: {time} minutes ({day})")
                    
                    
                #Today's time
                today_date = date.today().isoformat()
                        
                print(f"Total study time today was: {total_today} minutes.")
                
                print("\nToday's sessions were:")
                for session in sessions:
                    if session.get("date") == today_date:
                        sub = session["subject"]
                        time = session["duration"]
                        day = session.get("date", "No date")
                        
                        print(f"{sub}: {time} minutes.")
                        
            #DELETING TASKS---------------------------------------------------------------------------------------------------------    
            elif session_action == 3:
                print("Study Session Deletion...")
            
                for n, session in enumerate(sessions):
                    sub = session['subject']
                    time = session['duration']
                    day = session.get('date', 'No date')
                
                
                    print(f"{n+1}. {sub}: {time} min ({day})")
            
                session_no = int(input("What study session by number would you want to delete? "))
                session_no -= 1
            
                if not (0 <= session_no < len(sessions)):
                    print("Invalid choice")
                else:
                    s = sessions[session_no]
                    print(f"Deleting: {s['subject']} - {s['duration']} min ({s.get('date', 'No date')})")
                    sessions.pop(session_no)
               
                save_data(sessions, tasks)
            
            else:
                print("Invalid choice")
                
                
        #PERFORMANCE SUMMARY========================================================================================================    
        elif choice == 3:
            performance_summary()
            
            
        #WEEKLY SUMMARY===============================================================================================    
        elif choice == 4:
            show_weekly_summary()
            
        
        #SHOWING GRAPHS=====================================================================================================================
        elif choice == 5:
            print("Showing graphs...")
            print("1. Weekly graphs.")
            print("2. Subject breakdown")
            graph = int(input("Which graph would you want to see? "))
            
            if graph == 1:
                plot_weekly_trend()
                
            elif graph == 2:
                plot_subject_breakdown()
                
            else:
                print("Invalid choice")
                
                
        
        #DASHBOARD===================================================================================================================
        elif choice == 6:
            show_dashboard(sessions)
                
       
        #EXPORT FILES================================================================================================================
        elif choice == 7:
            print("Listing export files...")
            print("1. Txt Report")
            print("2. CSV")
            export_file = int(input("Choose a file (number): "))
            
            if export_file == 1:
                export_report(sessions)
            
            elif export_file == 2:
                export_csv(sessions)
           
            else:
                print("Invalid choice.")
            
        
        #EXIT============================================================================================================================
        elif choice == 8:
            save_data(sessions, tasks)
            print("Exiting...")
            print("Exited successfully.")
            break
        
        else:
            print("Invalid choice. Try again.")


sessions, tasks = load_data()
save_data(sessions, tasks)
show_menu()

