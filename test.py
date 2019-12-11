import os
import json
import utils
techs_json = utils.readJson(os.path.join('content', 'technologies.json'))
print(json.dumps(techs_json,indent=4))
