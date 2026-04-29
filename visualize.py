# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 12:57:28 2026

@author: godfr
"""
import json
import matplotlib.pyplot as plt


with open("sessions.json", "r") as s:
    loaded_sessions = json.load(s)
# with open("tasks.json", "r") as t:
#     loaded_tasks = json.load(t)
        
subject_totals = {}

for session in loaded_sessions:
   sub = session["subject"]
   time = session["duration"]
  
   if sub not in subject_totals:
       subject_totals[sub] = time
   else:
        subject_totals[sub] += time
        
keys = list(subject_totals.keys())
values = list(subject_totals.values())


plt.bar(keys,values)
plt.xlabel("Subjects")
plt.ylabel("Time (min)")
plt.title("Study Time Per Subject")
plt.tight_layout()
plt.show()

dateNtime = {}

for session in loaded_sessions:
    time = session['duration']
    date = session.get('date')
    
    if not date:
        continue
    elif date not in dateNtime:
        dateNtime[date] = time
    else:
        dateNtime[date] += time
        
sorted_data = sorted(dateNtime.items())
        
dates = [item[0] for item in sorted_data]
times = [item[1] for item in sorted_data]

plt.plot(dates, times)
plt.xlabel("Dates")
plt.ylabel("Time (min)")
plt.title("Total Study Time Per Day")
plt.xticks()
plt.tight_layout()
plt.show()

subject_date_time = {}

for session in loaded_sessions:
    time = session['duration']
    date = session.get('date')
    sub = session['subject']
    
    
    if not date:
        continue
    
    else:
        if sub not in subject_date_time:
            subject_date_time[sub] = {}
        
        if date not in subject_date_time[sub]:
            subject_date_time[sub][date] = time
            
        else:
            subject_date_time[sub][date] += time

for subject in subject_date_time:
    
    data = subject_date_time[subject]
   
    sorted_data = sorted(data.items())
    
    dates = [item[0] for item in sorted_data]
    times = [item[1] for item in sorted_data]
    
    plt.plot(dates, times, marker = 'o', label = subject)
    plt.xlabel("Dates")
    plt.ylabel("Time (min)")
    plt.title("Study Time Per Subject")
    
plt.legend()
plt.show()




