from dbhandle import DatabaseHandle

class Player:
    def __init__(self, discord_id, ident_date):
        self.discord_id = discord_id
        self.login_date = ident_date

    def save_to_db(self):
        db = DatabaseHandle()

        cmd = """INSERT INTO players VALUES(%s, %s, %s, 0) ON DUPLICATE KEY UPDATE last_msg_date = %s"""        
        c = db.handle.cursor();
        c.execute(cmd, (self.discord_id, self.login_date, self.login_date, self.login_date,))
        db.handle.commit();

