from sqlalchemy import create_engine, MetaData
from decouple import config

conn_str = config("CONNSTR")

engine = create_engine(conn_str)

meta = MetaData()

conn = engine.connect()