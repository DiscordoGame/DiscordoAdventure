from common.config import Config
import MySQLdb

class DatabaseHandler:
    __handle = None
    
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

    def get_record_count(self, table_name):
        # TODO(mateusz): Should set-up some rules how to guards
        # against unwanted SQL injection attacks
        # Anyway, this is stupid and is just here for debugging

        sql = "SELECT * FROM " + table_name.strip() + ";"
        cursor = self.handle.cursor();
        cursor.execute(sql)

        result = cursor.rowcount
        cursor.close()
        return result

    def get_query(self,cmd):
        db = DatabaseHandler()
        c = db.handle.cursor();
        return c.execute(cmd)
        
    
    def set_query(self,cmd):
        db = DatabaseHandler()
        c = db.handle.cursor();
        c.execute(cmd)
        db.handle.commit();
