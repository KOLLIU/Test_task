from sqlalchemy import Table, MetaData, Column, Text, create_engine

pg_user = ""
host = ""
db_name = ""
password = ""

engine = create_engine(f"postgresql+psycopg2://{pg_user}:{password}@{host}/{db_name}")

conn = engine.connect()

metadata = MetaData()

urls = Table("urls", metadata,
             Column('short', Text(), primary_key=True),
             Column('full', Text()))

metadata.create_all(engine)
