import csv
import datetime
from resources.cli_menu import *
from resources.decorators import rename

@rename('Exit')
def end_program():
	'Exit the program'
	exit()

@rename('Print all completed reports')
def print_all_completed():
	'Prints all reports that were completed to the command line'
	try:
		with open('tracker.csv', mode='r') as f:
			reader = csv.DictReader(f)
			for line in reader:
				print(line['Report Name'], line['Date Completed'])
	except IOError:
		print('No completed reports could be found. Record some reports and try again')

@rename('Print reports completed today')
def print_completed_today():
	'Prints all reports that were completed today'
	print('Completed today under construction')

@rename('Complete Report')
def complete_report():
	'Requests the name of the report the user completed and appends it to the list of completed reports'
	#Every entry is date and time stamped.
	report_name = input("Please enter the name of the report you completed: ")
	print(report_name)
	date = datetime.datetime.now()

	try:
		with open('tracker.csv', 'a', newline='') as f:
			writer = csv.writer(f)
			
			writer.writerow([report_name, date])
		
		#Provide record written message to user.
		print("Added %s to tracker with completion date %s" % (report_name, date))
		
	except IOError:
		print("There was an IO error. Completion not recorded. Try again.")