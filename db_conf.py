import mysql.connector
from mysql.connector import errorcode
from tabulate import tabulate


class DBConfig:
    def __init__(self):
        try:
            self.cnx = mysql.connector.connect(
                user="thujuli",
                password="thujuli",
                host="localhost",
                database="python_mysql",
            )
            cursor = self.cnx.cursor()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

        try:
            cursor.execute(
                "CREATE TABLE IF NOT EXISTS todo_list("
                "id INT NOT NULL AUTO_INCREMENT,"
                "task VARCHAR(255) NOT NULL,"
                "finish TINYINT NOT NULL DEFAULT 0,"
                "PRIMARY KEY(id),"
                "UNIQUE task_unique (task));"
            )
        except mysql.connector.Error as err:
            print("Failed creating table: {}".format(err))

        cursor.close()

    def insert(self, task):
        try:
            cursor = self.cnx.cursor()
            cursor.execute("INSERT INTO todo_list(task) VALUES('{}')".format(task))
        except mysql.connector.Error as err:
            print(err)

        self.cnx.commit()
        cursor.close()

    def fetch_all(self):
        try:
            cursor = self.cnx.cursor()
            cursor.execute("SELECT * FROM todo_list")
        except mysql.connector.Error as err:
            print(err)

        # Manipulation field finish in cursor
        raw = list(cursor).copy()
        res = [list(raw[i]) for i in range(len(raw))]
        for i in range(len(res)):
            if res[i][2] == 0:
                res[i][2] = "on progress".capitalize()
            else:
                res[i][2] = "complete".capitalize()

        # Change output to Table
        try:
            table = [("ID", "TASK", "FINISH")]
            for data in res:
                table.append(data)
            print(tabulate(table, headers="firstrow", tablefmt="grid"))
        except Exception as err:
            print(err)

    def delete(self, id):
        try:
            cursor = self.cnx.cursor()
            cursor.execute("DELETE FROM todo_list WHERE id = {}".format(id))
        except mysql.connector.Error as err:
            print(err)

        self.cnx.commit()
        cursor.close()

    def update_finish(self, id):
        try:
            cursor = self.cnx.cursor()
            cursor.execute("UPDATE todo_list SET finish = 1 WHERE id = {}".format(id))
        except mysql.connector.Error as err:
            print(err)

        self.cnx.commit()
        cursor.close()


if __name__ == "__main__":
    test = DBConfig()
    # test.insert("testing")  # success
    # test.delete(4) # sucess
    # test.update_finish(7)  # success
    test.fetch_all()  # success
