from datetime import datetime

from sqlalchemy import and_, exc, func
from sqlalchemy.orm import load_only

from dashboard_analytics.base.db_service import ServiceBase
from dashboard_analytics.base.database_models import (
    User
    
)
from dashboard_analytics.exceptions.db import DbException


class UserService(ServiceBase):
    def __init__(self):
        super().__init__(User)

    def get_tools(self):
        return super().find_all()
    
    def get_count(self, findManyOptions=None):
        try:
            if findManyOptions is not None:
                results = self.session.query(User).filter(findManyOptions).count()
            else:
                results = self.session.query(User).count()
            return results
        except exc.SQLAlchemyError as e:
            raise DbException(e)
        except Exception as e:
            raise e
        finally:
            self.session.close()
    
    def get_distinct_count(self,fields, findManyOptions=None):
        try:
            if findManyOptions is not None:
                results = self.session.query(User).filter(findManyOptions).options(load_only(*fields)).distinct().count()
            else:
                results = self.session.query(User).options(load_only(*fields)).distinct().count()
            return results
        except exc.SQLAlchemyError as e:
            raise DbException(e)
        except Exception as e:
            raise e
        finally:
            self.session.close()
    
    def exist_tool(self, newTool):
        find_one_options = User.tool_name == newTool.tool_name
        result = self.get_tool_by_toolname(find_one_options)

        return result

    def get_tool_by_toolname(self, find_options):
        return super().find_one(find_options)

