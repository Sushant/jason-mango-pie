from pymongo import Connection

def init():
  connection = Connection()
  db = connection['stern']
  populate_staff(db)

def populate_staff(db):
  staff = db.staff
  staff.remove()
  print 'Populating staff members data...'
  members = [{'name': 'John Doe',
              'title': 'Professor',
              'email': 'john@cs.abc.edu',
              'office_hours': ['Monday 2-3pm,','Tuesday 3.30-5.30pm'],
              'link': 'http://www.example.com'},
             {'name': 'John Appleseed',
              'title': 'Teaching Assistant',
              'email': 'jappleseed@abc.edu',
              'office_hours': ['Monday 2-3pm,','Wednesday 2-3pm']},
             {'name': 'Lindsay Lau',
              'title': 'Administrative Assistant',
              'email': 'llau@cs.abc.edu',
              'office_hours': ['Monday-Friday 9am-5pm,']}]
  staff.insert(members)


if __name__ == '__main__':
  init()

