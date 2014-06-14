import resources
from resources.controller import *
from resources.decorators import rename

def show_menu():
	'Prints the main menu for interacting with the application'
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

@rename('Print Completed Reports')
def show_completed_menu():
	'Displays the options for printing details of reports that have been completed.'
	print('Please select from the following options')
	for key, value in sorted(completed_menu_options.items()):
		print(key, ": ", value.__name__)
	
	response = input()
	if response in completed_menu_options.keys():
		completed_menu_options[response]()
		show_completed_menu()
	else:
		print(response + ' is not a valid selection.')
		show_completed_menu()

@rename('Return to main menu')
def return_to_main_menu():
	'Return to completed reports menu.'
	show_menu()
	
menu_options = {'1': show_completed_menu, '2': complete_report, 'exit': end_program}
completed_menu_options = {'1': print_all_completed, '2': print_completed_today
								, 'return': return_to_main_menu, 'exit': end_program}