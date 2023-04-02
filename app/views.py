"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""

from app import app
from flask import render_template, request, redirect, url_for, flash, send_from_directory
from .forms import PropertiesForm
from app.models import UserProperties
from app import db
from werkzeug.utils import secure_filename
import os
import psycopg2

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")


@app.route('/properties/create' , methods = ['GET', 'POST'])
def properties():
    form=PropertiesForm()
    if request.method == 'POST':

        if form.validate_on_submit():
            title = form.title.data
            type = form.type.data
            location = form.location.data
            Description = form.Description.data
            price = form.price.data
            photo = form.photo.data
            no_of_bedrooms = form.no_of_bedrooms.data
            no_of_bathrooms = form.no_of_bathrooms.data
            filename = secure_filename(photo.filename)

            property = UserProperties(title=title,filename=filename,location=location,type=type,Description=Description,price=price,no_of_bedrooms=no_of_bedrooms,no_of_bathrooms=no_of_bathrooms)
            db.session.add(property)
            db.session.commit()
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))

            return redirect(url_for('property'))
            #print('Success')
    return render_template("properties.html", form=form)

@app.route('/properties')
def property():
    property_data = connect_db()
    cursor = property_data.cursor()
    cursor.execute('select * from user_properties')
    collect = cursor.fetchall()
    return render_template('display.html', collect=collect)

@app.route('/properties/<propertyid>' , methods = ['GET', 'POST'])
def propertiesid(propertyid):
    propid = connect_db()
    cursor = propid.cursor()
    cursor.execute(f'select * from property where id = {propertyid}')
    pid = cursor.fetchall()
    return render_template('properties.html', pid=pid)

@app.route('/uploads/<filename>')
def get_image(filename):
    return send_from_directory(os.path.join(os.getcwd(),app.config['UPLOAD_FOLDER']), filename)



###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404

def connect_db(): 
    return psycopg2.connect(host="localhost", database="project1", user="project1", password="asher1129")