from flask_login import LoginManager, login_user, UserMixin, logout_user, login_required
from ccms import db, login_manger


class Teacher(UserMixin, db.Model):
    __tablename__ = 't_teacher'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    no = db.Column(db.String(20), unique=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(20))
    birthday = db.Column(db.Date)
    id_number = db.Column(db.String(20))

    def __init__(self, no, name, password, birthday, id_number):
        self.no = no
        self.name = name
        self.password = password
        self.birthday = birthday
        self.id_number = id_number

    def get_id(self):
        return self.no

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False



