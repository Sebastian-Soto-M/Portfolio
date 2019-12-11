import os
import json

def readJson(file_path):
    with open(file_path,'r', encoding='utf-8') as f:
       return json.load(f)

def get_full_project_info():
    projects = readJson(os.path.join('content', 'projects.json'))
    technologies = readJson(os.path.join('content', 'technologies.json'))

    print(technologies)