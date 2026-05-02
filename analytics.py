# -*- coding: utf-8 -*-
"""
Created on Sat May  2 18:28:10 2026

@author: godfr
"""

from datetime import date, datetime, timedelta


def calculate_summary(sessions):
    subject_totals = {}
      
    for session in sessions:
       sub = session["subject"]
       time = session["duration"]
       
       if sub not in subject_totals:
           subject_totals[sub] = time
       else:
            subject_totals[sub] += time
        
    #TOTAL TIME
    total_time = 0
    
    for session in sessions:
        total_time += session["duration"]
        
        
    #Today's time
    total_today = 0
    today_date = date.today().isoformat()
    
    for session in sessions:
        
        if session.get("date") == today_date:
            total_today += session["duration"]
            
    #DATE TOTALS
    date_totals = {}
    
    for session in sessions:
        session_date = session.get("date")
        duration = session['duration']
        
        if not session_date:
            continue
        
        elif session_date not in date_totals:
            date_totals[session_date] = duration
        else:
            date_totals[session_date] += duration
    
    return subject_totals, total_time, total_today, date_totals

def get_weekly_sessions(sessions):
    today = datetime.today().date()
    week_ago = today - timedelta(days=6)
    
    weekly_sessions = []
    
    for session in sessions:
        session_date = session.get('date')
        
        if not session_date:
            continue
        
        try:
            session_date = datetime.fromisoformat(session_date).date()
        except ValueError:
            try:
                session_date = datetime.strptime(session_date, "%m/%d/%y").date()
            except ValueError:
                continue

    
        if week_ago <= session_date <= today:
            weekly_sessions.append(session)
            
    return weekly_sessions
        

def weekly_summary(sessions):
    weekly_sessions = get_weekly_sessions(sessions)

    subject_totals = {}
    daily_totals = {}

    for session in weekly_sessions:
        sub = session["subject"]
        time = session["duration"]
        day = session["date"]

        # subject totals
        subject_totals[sub] = subject_totals.get(sub, 0) + time

        # daily totals
        daily_totals[day] = daily_totals.get(day, 0) + time

    return subject_totals, daily_totals

