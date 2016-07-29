import MySQLdb


class Query(object):
    def __init__(self):
        try:
            self.con = MySQLdb.connect("localhost", "User", "password", 'dbName')
            self.cur = self.con.cursor()
        except Exception as e:
            self.cur = None
            print(e)

    def _exit(self):
        if self.con:
            self.con.close()

    def query(self):
        pass