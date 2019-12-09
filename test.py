import os
import json
import utils

nav_info = utils.readJson(os.path.join('content', 'nav.json'))
projects_info = utils.readJson(os.path.join('content', 'projects.json'))

final = []
for item in projects_info:
    final.append({
        "header": item,
        "routes": projects_info[item]
    })

next(item for item in nav_info if item['id'] == 'projects')[
    'sub_links'] = final