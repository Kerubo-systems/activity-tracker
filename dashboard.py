# -*- coding: utf-8 -*-
"""
Created on Sat May  2 18:48:40 2026

@author: godfr
"""

import matplotlib.pyplot as plt
from analytics import weekly_summary

def show_dashboard(sessions):
    subject_totals, daily_totals = weekly_summary(sessions)

    if not subject_totals:
        print("No weekly data available.")
        return

    total_time = sum(daily_totals.values())
    best_subject = max(subject_totals, key=subject_totals.get)
    best_day = max(daily_totals, key=daily_totals.get)

    print("\n📊 WEEKLY DASHBOARD")
    print("-" * 25)
    print(f"Total time: {total_time} min")
    print(f"Top subject: {best_subject} ({subject_totals[best_subject]} min)")
    print(f"Best day: {best_day} ({daily_totals[best_day]} min)")

    # ---- GRAPH 1: TREND ----
    sorted_days = sorted(daily_totals.keys())
    times = [daily_totals[d] for d in sorted_days]

    plt.figure()
    plt.plot(sorted_days, times, marker="o")
    plt.title("Weekly Study Trend")
    plt.xlabel("Date")
    plt.ylabel("Minutes")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # ---- GRAPH 2: SUBJECTS ----
    subjects = list(subject_totals.keys())
    times = list(subject_totals.values())

    plt.figure()
    plt.bar(subjects, times)
    plt.title("Weekly Study by Subject")
    plt.xlabel("Subject")
    plt.ylabel("Minutes")
    plt.tight_layout()
    plt.show()