from .entities.User import User

@classmethod
class ModelUser():
    def login(self, db, user):
        try:
            cursor=db.connection.cursor()
            sql="SELECT id, mail, passwd FROM user WHERE mail = '{}'".format(user.mail)
            cursor.execute(sql)
            row = cursor.fetchnone()
            if row != None:
                user = User(row[0], row[1], row[2])
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)