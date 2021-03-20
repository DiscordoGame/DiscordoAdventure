from common.dbhandle import DatabaseHandler

class Player:
    def __init__(self, discord_id):
        self.discord_id = discord_id

    def seen_tutorial(self):
        db = DatabaseHandler()

        cmd = "SELECT seen_tutorial from players where discord_id = %s"
        if db.get_query(cmd):
            res = c.fetchone()[0]
            return res
        else:
            return False
        
    def save_to_db(self, login_date):
        cmd = f"INSERT INTO players VALUES({self.discord_id}, {login_date}, {login_date}, 0) ON DUPLICATE KEY UPDATE last_msg_date = {login_date}"
        db = DatabaseHandler()
        db.set_query(cmd)

