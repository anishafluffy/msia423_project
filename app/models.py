from app import db


# Create a data model for the database to be setup for the app
class Ing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    i_ingredients = db.Column(db.String(200), unique=False, nullable=False)

    def __repr__(self):
        return '<Ing %r>' % self.id