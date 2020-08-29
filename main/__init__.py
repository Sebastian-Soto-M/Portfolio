import os
from operator import itemgetter

import jinja2
from flask import Flask, render_template

import utils

app = Flask(__name__)

template_dir = os.path.join('.', 'templates')
loader = jinja2.FileSystemLoader(template_dir)
environment = jinja2.Environment(loader=loader)


@app.context_processor
def inject_dict_for_all_templates():
    nav_info = utils.readJson(os.path.join('content', 'nav.json'))
    return dict(nav_bar=nav_info)


@app.context_processor
def inject_color_palette():
    return dict(colors=utils.readJson(os.path.join('content',
                                                   'colors.json')))


@app.context_processor
def inject_personal_info():
    return dict(info=utils.readJson(os.path.join('content',
                                                 'info.json')))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('views/404.html', dir_title='Not Found'), 404


with app.app_context():
    from main.routes import r_blog, r_index, r_projects, r_base
    app.register_blueprint(r_blog)
    app.register_blueprint(r_projects)
    app.register_blueprint(r_index)
    app.register_blueprint(r_base)
