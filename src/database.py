import peewee
from datetime import datetime

db = peewee.SqliteDatabase('database.db')

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
    virtualresource = peewee.ForeignKeyField(VirtualRes)

class Capabilities(BaseModel):
    name = peewee.CharField(unique=True)
    description = peewee.CharField(default=None)
    association = peewee.CharField(default=None)

class ResourceCapability(BaseModel):
    capability = peewee.ForeignKeyField(Capabilities)
    virtualresource = peewee.ForeignKeyField(VirtualRes)

class SensorData(BaseModel):
    sensor = peewee.ForeignKeyField(RealSensors)
    data = peewee.TextField(default=None)
    timestamp = peewee.DateTimeField(default=datetime.now())

if __name__ == "__main__":
    try:
        db.create_tables([
            VirtualRes,
            Capabilities,
            RealSensors,
            ResourceCapability,
            SensorData
        ])
        print("Tabelas Criadas")    
    except:
        print("Erro na criação das tabelas")