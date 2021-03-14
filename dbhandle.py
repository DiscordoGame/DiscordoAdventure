from MySQLdb import _mysql

class DatabaseHandle:
    handle = None
    
    def __init__(self):
        # TODO(mateusz): create a config class that will store this info
        host = 'localhost'
        user = 'root'
        passwd = open('dbpass.txt').read().strip()
        
        if DatabaseHandle.handle == None:
            try:
                DatabaseHandle.handle = _mysql.connect(host = host, user = user, passwd = passwd)
            except:
                print('Error connecting to database')
