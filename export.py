# -*- coding: utf-8 -*-
"""
Created on Sat May  2 19:01:06 2026

@author: godfr
"""


from analytics import calculate_summary
import csv

def export_report(sessions, filename = "report.txt"):
    subject_totals, total_time, total_today, date_totals = calculate_summary(sessions)
    
    
    with open(filename, "w") as f:
        #write header
        f.write("STUDY REPORT\n")
        f.write("-" * 20 + "\n\n")
        
        #write totals
        f.write("OVERVIEW\n")
        f.write(f"Total study time: {total_time} min\n")
        f.write(f"Today's study time: {total_today} min\n\n")
        
        #best insights
        if subject_totals:
            best_subject = max(subject_totals, key = subject_totals.get)
            
        if date_totals:
            best_day = max(date_totals, key=date_totals.get)
            
            f.write(f"Best day: {best_day} ({date_totals[best_day]} min)\n\n")
            f.write(f"Best subject: {best_subject} ({subject_totals[best_subject]} min)\n\n\n")
            
        
        #loop subjects
        f.write("SUBJECT BREAKDOWN:\n")
        f.write("-----------------\n")
        for subject, time in sorted(subject_totals.items(), key = lambda x:x[1], reverse = True):
            f.write(f"- {subject}: {time} min\n")
            
        f.write("\n")
            
        f.write("DAILY BREAKDOWN\n")
        f.write("---------------\n")
        for day, time in sorted(date_totals.items()):
            f.write(f"{day}: {time} min\n")
            
        print(f"Report exectuted successfully - {filename}")
            
def export_csv(sessions, filename = 'sessions.csv'):
    with open(filename, 'w', newline = "") as f:
        writer = csv.writer(f)
        
        #HEADER
        writer.writerow(["Subject", "Duration (min)", "Date"])
        
        #DATA
        for session in sessions:
            subject = session.get("subject", "Unknown")
            duration = session.get("duration", 0)
            date = session.get("date", "No date")
            
            writer.writerow([subject, duration, date])
            
    print(f"CSV exported successfully - {filename}")
            
    
        
    
            
