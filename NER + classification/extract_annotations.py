import sys
import json
from prodigy.components.db import connect

db = connect()
# This is a list of dictionaries that one can modify and export
data = db.get_dataset(sys.argv[1])

#remove unecessary variables
for s in data:
    s.pop("text", None)
    s.pop("meta", None)
    s.pop("tokens", None)
    s.pop("options", None)
    s.pop("_input_hash", None)
    s.pop("_task_hash", None)
    s.pop("_task_hash", None)
    s.pop("_session_id", None)
    s.pop("_view_id", None)
    s.pop("config", None)

with open(sys.argv[2], 'w') as outfile:
    json.dump(data, outfile)