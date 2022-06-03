import math
from datetime import datetime
from http import HTTPStatus
from fastapi import responses
import numpy as np
import pandas as pd
from fastapi import FastAPI, Depends
from sqlalchemy.orm.session import Session

from fastapi import Request
from fastapi.responses import RedirectResponse
from dashboard_analytics.commons import schemas 
# from dashboard_analytics.base.api_service import FastService

from dashboard_analytics.svc.software_mgmt_services import (
    UserService    
)
from dashboard_analytics.base import database_models 
from dashboard_analytics.settings.constants import Constants
from sqlalchemy import and_
from sqlalchemy import cast, Date
from dashboard_analytics.db.db_connection_util import DbConnectionUtil
#from dashboard_analytics.base.clickhouse_models import Alarm

get_db = DbConnectionUtil.get_db_session_scope

class UserDetailsService():
    def __init__(self):
        self.app = FastAPI()
        self._routes()
        self.constants = Constants()
        # self.session: Session = DbConnectionUtil().get_db_session_scope()

    def _routes(self):
        @self.app.post('/', response_model=schemas.ShowUser)
        def create_user(request: schemas.User,db: Session = Depends(get_db)):
            new_user = database_models.User(name=request.name,email=request.email,password=request.password)
            db.add(new_user)
            db.commit()
            db.refresh(new_user)
            return new_user
        
        @self.app.post("/user/user_info/", tags=["user_info"])
        async def get_user_info(request: schemas.User):
            tool_meta_service = UserService()
            find_one_options = database_models.User.name == request.name
            tool_data = tool_meta_service.get_tool_by_toolname(find_one_options)

            if tool_data is None:
                response = {
                    "Status": HTTPStatus.OK,
                    "data": {}
                    }
            else:
                response = {
                    "Status": HTTPStatus.OK,
                    "data": tool_data.getvals()
                    }

            return response


client = UserDetailsService()
app = client.app
