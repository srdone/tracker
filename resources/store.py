import sqlite3

class ReportDatabase(object):
	"""docstring for ReportDatabase"""
	def __init__(self, arg):
		super(ReportDatabase, self).__init__()
		self.arg = arg
		
	def create_initial_db(self):
		db = sqlite3.connect('data/mydata')

		cursor = db.cursor()
		cursor.execute('''
			CREATE TABLE reports(
				id INTEGER PRIMARY KEY AUTO_INCREMENT,
				report_title VARCHAR(30),
				create_date DATE,
				next_due_date DATE,
				recurring BOOLEAN,
				FOREIGN KEY(owner) REFERENCES analysts(id)
				)
			''')

		cursor.execute('''
			CREATE TABLE completion_dates(
				id INTEGER PRIMARY KEY AUTO_INCREMENT,
				FOREIGN KEY(report_id) REFERENCES reports(id),
				complete_date DATE
				)
			''')

		cursor.execute('''
			CREATE TABLE notes(
				id INTEGER PRIMARY KEY AUTO_INCREMENT,
				FOREIGN KEY(report_id) REFERENCES reports(id),
				note TEXT
				)
			''')

		cursor.execute('''
			CREATE TABLE analysts(
				id INTEGER PRIMARY KEY AUTO_INCREMENT,
				first_name VARCHAR(30),
				last_name VARCHAR(30)
				FOREIGN KEY(repo)
				)
			''')

		cursor.execute('''
			CREATE TABLE reports_owners(
				FOREIGN KEY(owner_id) REFERENCES analysts(id)
				FOREIGN KEY(report_id) REFERENCES reports(id)
				)
			''')

	def add_analyst(self, first_name, last_name):
		pass

	def add_report(self, report_title, create_date, next_due_date, recurring, owner=None):
		pass

	def complete_report():
		pass

	def add_notes():
		pass

	def add_owner():
		pass

	def edit_owner():
		pass

	def edit_report():
		pass

	def edit_analyst():
		pass
