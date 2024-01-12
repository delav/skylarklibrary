from deco import keyword


class MySQLClient(object):

    def __init__(self):
        self.host = '127.0.0.1'

    @keyword
    def update_sql(self, sql_str):
        result = self.host + ':8080'
        return result

    @keyword
    def query_sql(self, sql_str):
        result = self.host + ':8080'
        return {"a": 1}
