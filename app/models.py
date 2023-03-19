from . import db
from werkzeug.security import generate_password_hash


class UserProperties(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'user_properties'

    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(80))
    title = db.Column(db.String(80))
    location = db.Column(db.String(80))
    type = db.Column(db.String(80))
    description = db.Column(db.String(80))
    price = db.Column(db.String(128))
    no_of_bedrooms = db.Column(db.String(80))
    no_of_bathrooms = db.Column(db.String(80))

    def __init__(self, title, filename, location, type, description, price, no_of_bedrooms, no_of_bathrooms):
        self.title = title
        self.filename = filename
        self.location = location
        self.type = type 
        self.description = description
        self.price = price
        self.no_of_bedrooms = no_of_bedrooms
        self.no_of_bathrooms = no_of_bathrooms

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)