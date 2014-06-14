#! /usr/bin/env python3

import csv
import datetime

keep_running = True

def rename(newname):
	def decorator(f):
		f.__name__ = newname
		return f
	return decorator

@rename('Exit')
def end_program():
	exit()

@rename('Print Completed')
def print_completed():
	try:
		with open('tracker.csv', mode='r') as f:
			reader = csv.DictReader(f)
			for line in reader:
				print(line['Report Name'], line['Date Completed'])
	except IOError:
		print('No completed reports could be found. Record some reports and try again')

@rename('Complete Report')
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
		
menu_options = {'1': print_completed, '2': complete_report, 'exit': end_program}

def show_menu():
	print('Please select from the following options:')
	for key, value in sorted(menu_options.items()):
		print(key, ": ", value.__name__)
	response=input()
	
	if response in menu_options.keys():
		menu_options[response]()
		show_menu()
	else:
		print(response + ' is not a valid selection.')
		show_menu()

if __name__=='__main__':
	show_menu()
