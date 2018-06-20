from flask import render_template, Blueprint, redirect, url_for, flash
from flask_login import LoginManager, login_user, UserMixin, logout_user, login_required
from ccms.form.SystemForms import LoginForm
from ccms.model.Teacher import Teacher
from ccms import db, app, login_manger


@app.route('/index')
@app.route('/')
def index():
    form = LoginForm()
    return render_template('login.html', form=form)


@app.route('/login', methods=['POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Teacher.query.filter_by(no=form.username.data).first()
        if user is not None and user.password == form.password.data:
            login_user(user)
            flash('登陆成功')
            return render_template('index.html', name=user.name)
        else:
            flash('用户名或密码错误')
            return render_template('login.html', form=form)
    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('你已退出登录')
    return redirect(url_for('ccms.index'))