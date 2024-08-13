import os
from utilities.logerror import Logerror
from utilities.teams_message import TeamsMessage
from datetime import datetime


FILE_PATH = ""

logfile = Logerror().open_file(FILE_PATH)

start_pattern = "from"
mid_pattern = datetime.today().strftime("%a %b %d")
last_pattern = datetime.today().strftime("%Y")


logfile_filtered = Logerror.filter_content(
    logfile, start_pattern, mid_pattern, last_pattern
)


process_with_erros = Logerror.identify_errors(logfile_filtered)


teams_message = TeamsMessage(
    webhook=os.environ.get("TEAMS_WEBHOOK"),
    host=os.environ.get("HOSTNAME"),
    msg=process_with_erros,
)

teams_message.send_message()
