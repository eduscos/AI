# Q1. Write a python program to generate Calendar for the given month and year?. [
# 10 Marks]
# Ans:-

import calendar

def generate_calendar(year, month):
    cal = calendar.monthcalendar(year, month)
    month_name = calendar.month_name[month]
    
    print(f"Calendar for {month_name} {year}:")
    
    # Print weekday names
    print("Mo Tu We Th Fr Sa Su")

    # Print each week
    for week in cal:
        week_str = ' '.join(str(day) if day != 0 else ' ' for day in week)
        print(week_str)

# Input: Year and Month
year = int(input("Enter the year: "))
month = int(input("Enter the month (1-12): "))

generate_calendar(year, month)