import sqlite3
from classifer import vectorization
from classifer import mnb

class BotDB:

    def __init__(self, db_fale):
        self.conn = sqlite3.connect(db_fale)
        self.cursor = self.conn.cursor()


    def url(self, url):
        """Проверяем, есть ли url в базе"""
        result = self.cursor.execute("SELECT `url` FROM `URL` WHERE `url` = ?", (url,))
        return bool(len(result.fetchall()))

    def label(self, label):
        """Проверяем label в базе"""
        result=self.cursor.execute("SELECT `label` FROM `URL` WHERE `url` = ?", (label,))
        if result.fetchone()[0]==1:
            return True
        else:
            return False

    def add_url(self, text,label):
        """Добавляем url в базу"""
        self.cursor.execute("INSERT INTO URL (url,label) VALUES (?,?)", (text,label))
        return self.conn.commit()

    def classification(self,olol):
        """Используем классификатор"""
        testing_pr=[olol]
        pred = mnb.predict(vectorization.transform(testing_pr))
        if pred[0]==1:
            return True
        if pred[0] == 0:
            return False


    def close(self):
        """Закрываем соединение с БД"""
        self.conn.close()
        return self.conn.commit()

