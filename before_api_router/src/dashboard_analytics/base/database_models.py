from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime, \
     ForeignKey, Boolean, event
from sqlalchemy.orm import scoped_session, sessionmaker, backref, relation
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, MetaData, literal
# from clickhouse_sqlalchemy import Table, make_session, get_declarative_base, types, engines
from sqlalchemy.orm import relationship

from dashboard_analytics.db.db_connection_util import DbConnectionUtil
from dashboard_analytics.settings.constants import Constants
from dashboard_analytics.settings.env_vars import EnvironmentVars

constant = Constants()
env_vars = EnvironmentVars()
metadata = MetaData(bind=DbConnectionUtil().get_database_engine())
Base = declarative_base(metadata=metadata)


class User(Base):
    __tablename__ = 'users2'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    def getvals(self):
        temp_dict = {}
        temp_dict["id"] = self.id
        temp_dict["name"] = self.name
        temp_dict["email"] = self.email
        temp_dict["password"] = self.password
        
        return temp_dict

class Blog(Base):
    __tablename__ = 'blogs2'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
  


#ToolMetadata.__table__.create(engine)
#ChamberMetadata.__table__.create(engine)
#SensorMetadata.__table__.create(engine)
Base.metadata.create_all(bind=DbConnectionUtil().get_database_engine(), checkfirst=True)