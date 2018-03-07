from app import db
from app.models import Ing
import os

'''
Creates a table in the database provided as the 'SQLALCHEMY_DATABASE_URI'
configuration parameter in __init__.py with the schema defined by models.Ing()
'''

#def create_db():
db.create_all()
    # print('2 creating')
    # ing1 = Ing(i_ingredients='tortillas, cheese')
    # ing2 = Ing(i_ingredients='curry paste, basil')
    # db.session.add(ing1)
    # db.session.add(ing2)
    # db.session.commit()
print('db created')

# if __name__ == "__main__":
#     create_db()