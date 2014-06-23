import sqlite3

class ReportDatabase(object):
	"""docstring for ReportDatabase"""
	def __init__(self):
		db = sqlite3.connect('data/mydata')
		
	def create_initial_db(self):
		cursor = db.cursor()
		cursor.execute('''
			CREATE TABLE reports(
				id INTEGER PRIMARY KEY AUTO_INCREMENT,
				report_title VARCHAR(30),
				create_date DATE,
				next_due_date DATE
				recurring BOOLEAN
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
				)
			''')

		cursor.execute('''
			CREATE TABLE reports_owners(
				FOREIGN KEY(owner_id) REFERENCES analysts(id)
				FOREIGN KEY(report_id) REFERENCES reports(id)
				)
			''')

	def add_analyst(self, analyst):
		cursor = db.cursor()

		cursor.execute('''
			INSERT INTO analysts(first_name, last_name)
			VALUES (?,?)
			''', (analyst.first_name, analyst.last_name))

		db.commit()
		return True

	def add_report(self, report, analyst):
		cursor = db.cursor()

		cursor.execute('''
			INSERT INTO reports(report_title, create_date,
				next_due_date, recurring) VALUES(?,?,?,?)
			''', (report.report_title, report.create_date
				, report.next_due_date, report.recurring)

		cursor.execute('''
			INSERT INTO reports_owners(owner_id, report_id)
			VALUES(?,?)
			''', (analyst.id, report.id))

		db.commit()

	def complete_report(self, report, date):
		cursor = db.cursor()

		cursor.execute('''
			UPDATE completion_dates SET complete_date=? WHERE id=?
			''', (report.id, date))

		cursor.execute()

	def add_notes():
		pass

	def add_owner(self, report, analyst):
		cursor = db.cursor()

		cursor.execute('''
			INSERT INTO reports_owners(owner_id, report_id)
			VALUES(?,?)
			''', (analyst.id, report.id))

		db.commit()

	def delete_owner(self, report, analyst):
		'Delete a line of ownership'
		cursor = db.cursor()

		cursor.execute('''
			DELETE FROM reports_owners WHERE owner_id=? AND report_id=?
			''', (analyst.id, report.report_id))

		cursor.execute()

	def edit_report(self, report):
		pass

	def edit_analyst(self, analyst):
		pass

	def delete_analyst(self, analyst):
		#delete all ownership lines for reports belonging to this analyst
		#delete the analyst record
		pass

	def delete_report(self, report):
		#delete all ownership lines for this report
		#delete the report record
		pass

	def get_analysts(self):
		cursor = db.cursor

		return cursor.execute('''SELECT * FROM analysts''')

	def get_analyst(self, id):
		cursor = db.cursor

		cursor.execute('''SELECT * FROM analysts WHERE id=?''', id)
		analyst_row = cursor.fetchone()

		analyst = Analyst(id=analyst_row['id'], first_name=analyst_row['first_name']
			, last_name=analyst_row['last_name'])
		
		analyst.reports.append(get_analyst_reports(analyst))

		return analyst

	def get_analyst_reports(self, analyst):
		cursor = db.cursor

		report_list = cursor.execute('''SELECT r.*, max(cd.complete_date) AS max_complete_date
								FROM reports as r
								LEFT JOIN reports_owners AS ro
								ON reports.id=reports_owners.report_id 
								LEFT JOIN completion_dates AS cd
								ON reports.id=completion_dates.report_id
								WHERE analysts.id=?
								GROUP BY reports.*''', analyst.id)

		for line in report_list:
			reports.append(Report(report_id=line['id'], report_title=line['report_title']
				, create_date=line['create_date'], next_due_date=line['next_due_date']
				, recurring=line['recurring'], max_complete_date=line['max_complete_date']))
