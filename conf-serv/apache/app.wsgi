import sys
sys.path.insert(0, '/var/www/html/pyweb-sql')
activate_this = '/home/kire/flask/bin/activate_this.py'
with open(activate_this) as file_:
	exec(file_.read(), dict(__file__=activate_this))	

from portal import app as application

