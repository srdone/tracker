import csv
import datetime

keep_running = True

def print_completed():
    with open(r'F:\Python Scripts\tracker.csv', mode='r') as f:
        reader = csv.DictReader(f)
        for line in reader:
            print(line['Report Name'], line['Date Completed'])

def get_status():
    answer = input("Enter 'New Report' to add a new report, 'stop' to stop: ")
    if answer == 'New Report':
        return True
    elif answer == 'stop':
        return False
    elif answer == 'Completed Today':
        print_completed()
        get_status()
    else:
        print('That is not a valid answer')
        get_status()
        
keep_running = get_status()

while keep_running:
    report_name = input("Please enter the name of the report you completed: ")
    print(report_name)
    #date = input("Please enter today's date: ")
    date = datetime.datetime.now()

    f = open(r'F:\Python Scripts\tracker.csv', 'a', newline='')
    writer = csv.writer(f)

    writer.writerow([report_name, date])
    f.close()

    print("Added %s to tracker with completion date %s" % (report_name, date))

    keep_running = get_status()
        
