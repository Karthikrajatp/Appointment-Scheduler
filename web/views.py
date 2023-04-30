from flask import Blueprint,render_template,request,redirect,url_for,flash
from flask_login import login_required,current_user
from werkzeug.security import generate_password_hash,check_password_hash

from .models import User,Appointments
from . import db 
from datetime import datetime

views = Blueprint('views', __name__)
@views.route('/all-terraformers')
@login_required
def home():
    data = User.query.all()
    return render_template("all-terra.html",data=data)

@views.route('/available-terraformers')
@login_required
def avail():
    avail_data = User.query.filter_by(availability=True).all()
    return render_template("avail-terra.html",data=avail_data)

@views.route('/book-appointment',methods=['POST','GET'])
@login_required
def book():
    if request.method == 'POST':
        host_email = current_user.email
        guest_email = request.form.get('guest_email')
        title = request.form.get('title')
        temp_time = request.form.get('time')
        agenda = request.form.get('agenda')
        form_time = datetime.fromisoformat(temp_time)

        new_appointment = Appointments(host_email=host_email,guest_email=guest_email,title=title,agenda=agenda,time=form_time)
        db.session.add(new_appointment)
        db.session.commit()
        return redirect(url_for('views.avail'))
    
    return render_template("appointment.html")

@views.route('/appointment-list')
@login_required
def list():
    user_email = current_user.email
    host_data = Appointments.query.filter_by(host_email=user_email).all()
    guest_data = Appointments.query.filter_by(guest_email=user_email).all()

    return render_template('appointment_list.html',host_data = host_data,guest_data=guest_data)


@views.route('/profilechange',methods=['POST'])
@login_required
def profilechange():
    current_password = request.form.get('currentpass')
    new_password = request.form.get('newpass')
    confirm_password = request.form.get('renewpass')

    if not check_password_hash(current_user.password,current_password):
        flash('Invalid current password')
           
    if new_password != confirm_password:
        flash('New password and confirmation do not match')
        
    current_user.password = generate_password_hash(new_password,method='sha256')
    db.session.commit()
    flash('Password updated successfully')
    return redirect('/profile')

@views.route('/namechange',methods=['POST'])
@login_required
def namechange():
        
    current_name = request.form.get('currentname')
    new_name = request.form.get('newname')

    if current_name == new_name:
        flash('Username unchanged')
    current_user.username = new_name
    db.session.commit()
    flash('Username updated successfully')
    return redirect('/profile')

@views.route('/availchange',methods=['POST'])
@login_required
def availchange():
    current_status = current_user.availability
    new_status = request.form.get('avail')

    if str(current_status) == new_status:
        flash('Availability unchanged')
        return redirect('/profile')

    if new_status=="False":
        current_user.availability = False
    else:
        current_user.availability = True    
    db.session.commit()
    flash('Availability updated successfully')
    return redirect('/profile')


@views.route('/profile',methods=['GET'])
@login_required
def profileview():
    return render_template("profile.html")

        
         
