from common.dbhandle import DatabaseHandler

class Player:
    def __init__(self, discord_id):
        self.discord_id = discord_id

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

        cmd = "INSERT INTO players VALUES(%s, %s, %s, 0) ON DUPLICATE KEY UPDATE last_msg_date = %s"
        c = db.handle.cursor();
        c.execute(cmd, (self.discord_id, login_date, login_date, login_date,))
        db.handle.commit();

