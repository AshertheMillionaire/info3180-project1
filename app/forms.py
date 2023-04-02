from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SelectField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed

class PropertiesForm(FlaskForm):
    title = StringField('title', validators=[InputRequired()])
    Description = TextAreaField('Description', validators=[InputRequired()])
    type = SelectField('Property type', choices=[('house', 'house'),('apartment', 'apartment')], validators=[InputRequired()])
    photo = FileField('photo', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
    location = StringField('location', validators=[InputRequired()])
    price = StringField('price', validators=[InputRequired()])
    no_of_bedrooms = StringField('no_of_bedrooms', validators=[InputRequired()])
    no_of_bathrooms = StringField('no_of_bathrooms', validators=[InputRequired()])

