class Coffee:
    __table__ = "coffee"
    keys = ("timestamp", "price")

    def init_query(self):
        sql = f"""
                CREATE TABLE IF NOT EXISTS {self.__table__} (
                  ts TIMESTAMP,
                  price FLOAT
                ) timestamp(ts);
           """
        return sql

    def insert_query(self):
        sql = f"""
                INSERT INTO {self.__table__}
                    VALUES (%s, %s);
           """
        return sql

    def fetch_query(self):
        sql = f"SELECT * FROM {self.__table__};"

        return sql
