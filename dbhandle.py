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
            except Exception as e:
                print('Error connecting to database: ' + str(e))

            test_db_name = 'players'
            try:
                DatabaseHandle.handle.query('USE ' + test_db_name + ";")
            except Exception as e:
                print('Error setting the database we are going to use: ' + str(e))

    def get_record_count(self, table_name):
        # TODO(mateusz): Should set-up some rules how to guards
        # against unwanted SQL injection attacks
        # Anyway, this is stupid and is just here for debugging

        sql = "SELECT * FROM " + table_name.strip() + ";"
        DatabaseHandle.handle.query(sql)
        res = DatabaseHandle.handle.store_result();

        return res.num_rows()
