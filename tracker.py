#! /usr/bin/env python3

import csv
import datetime

keep_running = True

def print_completed():
    try:
        with open('tracker.csv', mode='r') as f:
            reader = csv.DictReader(f)
            for line in reader:
                print(line['Report Name'], line['Date Completed'])
    except IOError:
        print('No completed reports could be found. Record some reports and try again')

def complete_report():
    report_name = input("Please enter the name of the report you completed: ")
    print(report_name)
    date = datetime.datetime.now()

    try:
        with open('tracker.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            
            writer.writerow([report_name, date])
            
        print("Added %s to tracker with completion date %s" % (report_name, date))
        
    except IOError:
        print("There was an IO error. Completion not recorded. Try again.")

def get_status():
    answer = input("Enter 'New Report' to add a new report, 'stop' to stop: ")
    if answer == 'New Report':
        complete_report()
        get_status()
    elif answer == 'stop':
        exit()
    elif answer == 'Completed Today':
        print_completed()
        get_status()
    else:
        print('That is not a valid answer')
        get_status()

if __name__=='__main__':
    get_status()
