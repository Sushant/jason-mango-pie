#!python2.6

import cherrypy
import json

from pymongo import Connection


class Root:
  # Get a connection object for local MongoDB instance
  connection = Connection()
  db = connection['stern']

  @cherrypy.expose
  def index(self):
    raise cherrypy.HTTPRedirect('/staff')

  
  @cherrypy.expose
  def staff(self):
    staff = self.db.staff
    member_list = []
    # Get all records from staff db
    for member in staff.find():
      # Remove the ObjectID field from the record
      del member['_id']
      member_list.append(member)

    # Convert python dict to json
    return json.dumps(member_list)

if __name__ == '__main__':

  # Config for our CherryPy webserver
  config = {
    'global': {
      'server.socket_host': "0.0.0.0",
            'server.socket_port': 8080,
            'server.thread_pool': 10,
            'engine.autoreload_on':False,
        }
  }

  cherrypy.config.update(config['global'])
  cherrypy.tree.mount(Root(), config=config)

  try:
    # Start the CherryPy Webserver on specified port
    cherrypy.engine.start()
    print 'Successfully started the Control Panel'
    cherrypy.engine.block()
  except socket.error, fault:
    print 'Unable to start Control Panel: ', fault
