import sqlite


class schema:
    def __init__(self):
        self.conn = sqlite3.connect('todo.db')
        self.create_user_table()
        self.create_to_do_table()

    def create_to_do_table(self):

        query = """
        CREATE TABLE IF NOT EXISTS "Todo" (
            id INTEGER PRIMARY KEY,
            title TEXT,
            description TEXT,
            _is_done boolean,
            _is_deleted boolean,
            createdon DATE DEFAULT CURRENT_DATE,
            duedate DATE,
            userid INTEGER FOREIGNKEY REFERENCES User(_id)
        );
        """

        self.conn.execute(query)

    def create_user_table(self):
        pass
