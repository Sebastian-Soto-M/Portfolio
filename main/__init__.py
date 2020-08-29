import os
import utils
import jinja2
from operator import itemgetter
from flask import Flask, render_template

app = Flask(__name__)

template_dir = os.path.join('.', 'templates')
loader = jinja2.FileSystemLoader(template_dir)
environment = jinja2.Environment(loader=loader)

with app.app_context():
    from main.routes import r_blog, r_index
    app.register_blueprint(r_blog)
    app.register_blueprint(r_index)


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
