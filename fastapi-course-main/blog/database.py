from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHAMY_DATABASE_URL = 'sqlite:///./blog.db'
# user="postgres"
# password="admin"
# host="localhost"
# port="5432"
# database="suri"
user="postgres"
password="admin123"
host="suridbinstance2.cccqk0oueyhz.ap-south-1.rds.amazonaws.com"
port="5432"
database="suriawsdb"
SQLALCHAMY_DATABASE_URL = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"

engine = create_engine(SQLALCHAMY_DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False,)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()