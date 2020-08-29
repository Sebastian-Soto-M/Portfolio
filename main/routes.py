import os
import random

from flask import Blueprint, render_template, request, send_file, url_for

import utils

r_blog = Blueprint('r_blog', __name__, template_folder='templates',
                   static_folder='static', url_prefix='/blog')

r_index = Blueprint('r_index', __name__,
                    template_folder='templates', static_folder='static')

r_base = Blueprint('r_base', __name__, template_folder='templates',
                   static_folder='static')

r_projects = Blueprint('r_projects', __name__, template_folder='templates',
                       static_folder='static', url_prefix='/projects')


@r_blog.route('/')
def blog():
    articles_json = utils.readJson(os.path.join('content', 'articles.json'))
    return render_template('views/blog/blog.html', articles=articles_json, dir_title='Blog')


@r_blog.route('/<string:article>')
def blog_saas(article):
    art = utils.get_article_by_id(article)
    article_path = os.path.join('views', 'blog', 'article')
    try:
        if art != None:
            if os.stat(os.path.join('main', 'templates', 'views', 'blog', 'article', 'html', article + '.html')) == 0:
                raise FileNotFoundError
            return render_template(os.path.join(article_path, 'base.html'),
                                   blog=art, dir_title=art['title'])
        else:
            return render_template('views/404.html', dir_title='Not Found'), 404
    except FileNotFoundError as e:
        return render_template('views/build.html')


@r_index.route('/')
def index():
    techs_json = utils.readJson(os.path.join('content', 'technologies.json'))
    projects_json = utils.get_full_project_info()
    rand_list = random.sample(projects_json, k=3)
    return render_template('views/index/index.html',
                           technologies=techs_json,
                           projects=rand_list,
                           index=True)


@r_index.route('/download/resume')
def download_resume():
    return send_file(os.path.join('..', 'content', 'SebastianSoto_cv.pdf'))


@r_projects.route('/')
def projects():
    projects_json = utils.get_full_project_info()
    return render_template('views/projects/projects.html',
                           projects=projects_json, dir_title='Projects')


@r_projects.route('/<string:id>')
def project_definition(id):
    return render_template('views/build.html')


@r_base.route('/about')
def about():
    return render_template('views/about/about.html', dir_title='About')


@r_base.route('/education')
def education():
    return render_template('views/education/education.html', dir_title='Education')


@r_base.route('/contact')
def contact():
    return render_template('views/contact/contact.html', dir_title='Contact')
