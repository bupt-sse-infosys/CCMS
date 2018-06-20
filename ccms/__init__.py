from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
from flask_wtf import FlaskForm
from flask_login import LoginManager, login_user, UserMixin, logout_user, login_required
from flask_bootstrap import Bootstrap
import pymysql
import sys


defaultEncoding = 'utf-8'
if sys.getdefaultencoding() != defaultEncoding:
    sys.setdefaultencoding(defaultEncoding)

app = Flask(__name__)

# 加载配置文件
app.config.from_object('ccms.setting')

# 创建数据库对象
db = SQLAlchemy(app)

bootstrap = Bootstrap(app)
moment = Moment(app)

login_manger = LoginManager()
login_manger.session_protection = 'strong'
login_manger.login_view = 'ccms.login'
login_manger.init_app(app)


@login_manger.user_loader
def load_user(user_id):
    from ccms.model import Teacher
    return db.session.query(Teacher).filter_by(id == 1).first()


