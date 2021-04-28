import peewee
from datetime import datetime

db = peewee.SqliteDatabase('resources.db')

class BaseModel(peewee.Model):
    class Meta:
        database=db

class VirtualRes(BaseModel):
    uuid=peewee.TextField(unique=True)
    description = peewee.TextField(default=None)
    timestamp=peewee.DateTimeField(default=datetime.now)

class Capabilities(BaseModel):
    virtualResource = peewee.ForeignKeyField(VirtualRes, backref='Capabilities')
    capabilitie = peewee.CharField(default=None)


db.create_tables([VirtualRes, Capabilities])