import os
import json

def readJson(file_path):
    with open(file_path,'r', encoding='utf-8') as f:
       return json.load(f)