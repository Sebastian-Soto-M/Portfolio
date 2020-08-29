import os
import utils
import jinja2
import random
from operator import itemgetter
from flask import Flask, render_template, send_file

app = Flask(__name__)

template_dir = os.path.join('.', 'templates')
loader = jinja2.FileSystemLoader(template_dir)
environment = jinja2.Environment(loader=loader)

with app.app_context():
    from main.routes import r_blog
    app.register_blueprint(r_blog)


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
    projects_json = utils.get_full_project_info()
    rand_list = random.sample(projects_json, k=3)
    return render_template('views/index/index.html',
                           technologies=techs_json,
                           projects=rand_list,
                           index=True)


@app.route('/download/resume')
def download_resume():
    return send_file(os.path.join('content', 'SebastianSoto_cv.pdf'))


@app.route('/projects')
def projects():
    projects_json = utils.get_full_project_info()
    return render_template('views/projects/projects.html',
                           projects=projects_json, dir_title='Projects')


@app.route('/projects/<string:id>')
def project_definition(id):
    return render_template('views/build.html')


@app.route('/about')
def about():
    return render_template('views/about/about.html', dir_title='About')


@app.route('/education')
def education():
    return render_template('views/education/education.html', dir_title='Education')


@app.route('/contact')
def contact():
    return render_template('views/contact/contact.html', dir_title='Contact')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('views/404.html', dir_title='Not Found'), 404
