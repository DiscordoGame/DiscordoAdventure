from common.config import Config
import MySQLdb

class DatabaseHandler:
    __handle = None
    __last_cursor = None
    
    def __init__(self):
        host = Config.get_by_key('db_host')
        user = Config.get_by_key('db_user')
        passwd = Config.get_by_key('db_pass')
        
        if DatabaseHandler.__handle == None:
            try:
                DatabaseHandler.__handle = MySQLdb.connect(host = host, user = user, passwd = passwd)
            except Exception as e:
                print('Error connecting to database: ' + str(e))

            test_db_name = Config.get_by_key('test_db_name')
            try:
                DatabaseHandler.__handle.query('USE ' + test_db_name + ";")
            except Exception as e:
                print('Error setting the database we are going to use: ' + str(e))

    @property
    def handle(self):
        return DatabaseHandler.__handle

    def set_last_cursor(self, c):
        DatabaseHandler.__last_cursor = c

    @property
    def last_cursor(self):
        return DatabaseHandler.__last_cursor

    def get_query(self,cmd):
        c = self.handle.cursor(MySQLdb.cursors.DictCursor);
        self.set_last_cursor(c)
        return c.execute(cmd)
    
    def set_query(self,cmd):
        c = self.handle.cursor();
        c.execute(cmd)
        self.handle.commit();

        self.set_last_cursor(c)
