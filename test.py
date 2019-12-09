import os
import json
import utils

projects_info = utils.readJson(os.path.join('content', 'projects.json'))
final = []
final.append(projects_info['java'][0])
final.append(projects_info['java'][1])
final.append(projects_info['python'][0])

print(final)
