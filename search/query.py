import MySQLdb


class Query(object):
    def __init__(self):
        try:
            self.con = MySQLdb.connect('localhost', 'ling', 'ling000', 'hlju');
        except Exception as e:
            self.con = None
            print(e)

    def _exit(self):
        if self.con:
            self.con.close()

    def _search_by_name(self):
        pass

    def _search_by_xh(self):
        pass

    def query(self, content):
        pass
