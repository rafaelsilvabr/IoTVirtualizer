import peewee
from datetime import datetime

db = peewee.SqliteDatabase('resources.db')

class BaseModel(peewee.Model):
    class Meta:
        database=db

class VirtualRes(BaseModel):
    uuid=peewee.TextField(unique=True)
    description = peewee.TextField(default=None)
    capabilities = peewee.TextField(default=None)
    timestamp=peewee.DateTimeField(default=datetime.now())

class RealSensors(BaseModel):
    uuid=peewee.TextField(unique=True)
    description = peewee.TextField(default=None)
    capabilities = peewee.TextField(default=None)
    VirtualResource = peewee.ForeignKeyField(VirtualRes)

class Capabilities(BaseModel):
    name = peewee.CharField(default=None)
    description = peewee.CharField(default=None)
    association = peewee.CharField(default=None)


db.create_tables([VirtualRes, Capabilities, RealSensors])