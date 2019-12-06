import os
import utils
import jinja2
import pandas as pd
from operator import itemgetter
from flask import Flask, render_template

app = Flask(__name__)

template_dir = os.path.join('.', 'templates')
loader = jinja2.FileSystemLoader(template_dir)
environment = jinja2.Environment(loader=loader)


@app.context_processor
def inject_dict_for_all_templates():
    return dict(nav_bar=utils.readJson(os.path.join('content',
                                                    'nav.json')))


@app.context_processor
def inject_color_palette():
    return dict(colors=utils.readJson(os.path.join('content',
                                                   'colors.json')))


@app.context_processor
def inject_personal_info():
    return dict(info=utils.readJson(os.path.join('content',
                                                 'info.json')))


@app.route('/')
def index():
    techs_json = utils.readJson(os.path.join('content', 'technologies.json'))
    projects_json = utils.readJson(os.path.join('content', 'projects.json'))[:3]
    return render_template('views/index/index.html', technologies=techs_json, projects=projects_json)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('views/404.html', dir_title='Not Found'), 404


if __name__ == '__main__':
    app.run(debug=True, port=5000)
