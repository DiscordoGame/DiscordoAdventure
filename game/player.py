from common.dbhandler import DatabaseHandler

class Player:
    def __init__(self, discord_id, login_date):
        self.discord_id = discord_id

        db = DatabaseHandler()
        cmd = f"SELECT * from players where discord_id = {self.discord_id}"
        if db.get_query(cmd):
            c = db.last_cursor

            assert c.rowcount == 1
            d = c.fetchone()
            assert d['discord_id'] == discord_id
            self.data = d
        else:
            cmd = f"INSERT INTO players (discord_id, first_msg_date, last_msg_date, seen_tutorial, current_region_id) VALUES({self.discord_id}, {login_date}, {login_date}, 0, 1)"
            db.set_query(cmd)

            # TODO(mateusz): @Copy-paste
            cmd = f"SELECT * from players where discord_id = {self.discord_id}"
            db.get_query(cmd)
            c = db.last_cursor

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
    
    @property
    def seen_tutorial(self):
        return self.data['seen_tutorial']
        
    def save_to_db(self):
        db = DatabaseHandler()

        cmd = f"UPDATE players SET last_msg_date = '{self.last_msg_date}' WHERE discord_id = {self.discord_id}"
        db.set_query(cmd)
