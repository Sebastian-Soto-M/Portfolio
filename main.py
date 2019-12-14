import os
import utils
import jinja2
from operator import itemgetter
from flask import Flask, render_template, send_file

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


@app.route('/')
def index():
    techs_json = utils.readJson(os.path.join('content', 'technologies.json'))
    projects_info = utils.readJson(os.path.join('content', 'projects.json'))
    projects_json = []
    projects_json.append(projects_info['java'][0])
    projects_json.append(projects_info['java'][1])
    projects_json.append(projects_info['python'][0])
    return render_template('views/index/index.html',
                           technologies=techs_json,
                           projects=projects_json)


@app.route('/download/resume')
def download_resume():
    return send_file(os.path.join('content', 'SebastianSoto_cv.pdf'))


@app.route('/projects')
def projects():
    projects_json = utils.get_full_project_info()
    return render_template('views/projects/projects.html',
                           projects=projects_json)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('views/404.html', dir_title='Not Found'), 404


if __name__ == '__main__':
    app.run(debug=True, port=5000)
