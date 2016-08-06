"""Models and database functions for cars db."""

from flask_sqlalchemy import SQLAlchemy

# Here's where we create the idea of our database. We're getting this through
# the Flask-SQLAlchemy library. On db, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()


##############################################################################
# Part 1: Compose ORM

class Model(db.Model):
    """Car model."""

    __tablename__ = "models"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    brand_name = db.Column(
        db.String(20),
        db.ForeignKey('brands.name'))
    name = db.Column(db.String(25))
    year = db.Column(db.Integer)

    brands = db.relationship('Brand')

    def __repr__(self):
        """Show infor about Model."""

        return "<Model id={} brand_name={} name={} year={}>".format(self.id,
                self.brand_name, self.name, self.year)

class Brand(db.Model):
    """Car brand."""

    __tablename__ = "brands"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20))
    founded = db.Column(db.Integer)
    headquarters = db.Column(db.String(50))
    discontinued = db.Column(db.Integer, nullable=True)

    models = db.relationship('Model')

    def __repr__(self):
        """Show infor about Brand."""

        return "<Brand id={} name={} founded={} headquarters={} discontinued={}>".format(self.id,
                self.name, self.founded, self.headquarters, self.discontinued)



# End Part 1


##############################################################################
# Helper functions

def init_app():
    # So that we can use Flask-SQLAlchemy, we'll make a Flask app
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to DB."


def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///cars'
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    # So that we can use Flask-SQLAlchemy, we'll make a Flask app
    from flask import Flask

    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to DB."
