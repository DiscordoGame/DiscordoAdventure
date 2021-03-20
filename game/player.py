from common.dbhandle import DatabaseHandler

import MySQLdb

class Player:
    def __init__(self, discord_id):
        self.discord_id = discord_id

        db = DatabaseHandle()

        cmd = "SELECT * from players where discord_id = %s"
        c = db.handle.cursor(MySQLdb.cursors.DictCursor)
        if c.execute(cmd, (self.discord_id,)):
            assert c.rowcount == 1
            d = c.fetchone()
            assert d['discord_id'] == discord_id
            self.data = d
        else:
            cmd = "INSERT INTO players VALUES(%s, %s, %s, 0, 1, NULL, NULL, NULL, NULL)"
            c = db.handle.cursor(MySQLdb.cursors.DictCursor)
            db.handle.commit()

            # TODO(mateusz): @Copy-paste
            c.execute(cmd, (discord_id, ident_date, ident_date,))
            cmd = "SELETCT * from players where discord_id = %s"
            c = db.handle.cursor(MySQLdb.cursors.DictCursor)
            assert c.execute(cmd, (self.discord_id, ))

            assert c.rowcount == 1
            d = c.fetchone()
            assert d['discord_id'] == discord_id
            self.data = d

    @property
    def first_msg_date(self):
        return self.data['first_msg_date']
    
    @property
    def last_msg_date(self):
        return self.data['last_msg_date']
    
    @property        
    def current_region_id(self):
        return self.data['current_region_id']
    
    @property
    def health(self):
        return self.data['health']

    @property
    def mana(self):
        return self.data['mana']

    @property
    def gold(self):
        return self.data['gold']

    @property
    def exp(self):
        return self.data['exp']
    
    def seen_tutorial(self):
        db = DatabaseHandler()

        cmd = "SELECT seen_tutorial from players where discord_id = %s"
        c = db.handle.cursor();
        if c.execute(cmd, (self.discord_id,)):
            res = c.fetchone()[0]
            return res
        else:
            return False
        
    def save_to_db(self, login_date):
        db = DatabaseHandler()

        cmd = "UPDATE players SET last_msg_date = %s WHERE discord_id = %s"
        c = db.handle.cursor();
        c.execute(cmd, (self.last_msg_date, self.discord_id,))
        db.handle.commit();
