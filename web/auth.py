from flask import Blueprint,render_template,flash,redirect,url_for,request
from .models import User
from .import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user,login_required,logout_user,current_user


auth = Blueprint('auth', __name__)
@auth.route('/',methods=['GET','POST'])
@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user is not None and check_password_hash(user.password,password):
            login_user(user,remember=True)
            flash('Logged in successfully')
            return redirect(url_for('views.home'))
        else:
            flash('Invalid email or password')
            return render_template('login.html')
    else:
        return render_template('login.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out')
    return redirect(url_for('auth.login'))

@auth.route('/sign-up',methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        fullname = request.form.get('fullname')
        designation = request.form.get('userdesignation')
        email = request.form.get('email')
        phonenumber = request.form.get('phonenumber')
        password1 = request.form.get('password')
        password2 = request.form.get('confirmpassword')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already registered')
        elif len(email)<5:
            flash('Email is too short')
        elif(len(fullname)<5):
            flash('Full Name is too short')
        elif len(phonenumber)<10:
            flash('Phone number is too short')
        elif len(password1)<7:
            flash('Password is too short')
        elif (password1!=password2):
            flash('Passwords do not match')
        else:
            new_user = User(username=fullname,userdesignation=designation,email=email,phonenumber=phonenumber,password=generate_password_hash(password1,method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user,remember=True)
            flash("Account Created!!",category="success")
            return redirect(url_for('auth.login'))
    return render_template('signup.html')

