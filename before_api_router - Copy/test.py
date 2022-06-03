

from dashboard_analytics.db.db_connection_util import DbConnectionUtil
from dashboard_analytics.settings.constants import Constants
from dashboard_analytics.settings.env_vars import EnvironmentVars

constant = Constants()
env_vars = EnvironmentVars()
engine=DbConnectionUtil().get_database_engine()
df = pd.read_sql("SELECT * FROM \"" + POSTGRE_DETAILS['owps_log_table'] + "\"", engine)