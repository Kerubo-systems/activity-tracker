# -*- coding: utf-8 -*-
"""
Created on Fri May  1 21:41:28 2026

@author: godfr
"""

import json
import os

def save_data(sessions, tasks):
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
            
        return sessions, tasks