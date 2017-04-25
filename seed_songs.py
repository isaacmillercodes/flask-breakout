from models import Songs
from app import db

rtj = Songs('A Christmas Fucking Miracle', 'Run the Jewels', 2013)
gambino = Songs('Freaks and Geeks', 'Childish Gambino', 2011)

db.session.add(rtj)
db.session.add(gambino)
db.session.commit()
