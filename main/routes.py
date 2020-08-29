from flask import Blueprint, render_template, request, url_for

import os
import utils

r_blog = Blueprint('r_blog', __name__, template_folder='templates',
                   static_folder='static', url_prefix='/blog')


@r_blog.route('/')
def blog():
    articles_json = utils.readJson(os.path.join('content', 'articles.json'))
    return render_template('views/blog/blog.html', articles=articles_json, dir_title='Blog')


@r_blog.route('/<string:article>')
def blog_saas(article):
    art_dict = utils.get_article_by_id(article)
    article_path = os.path.join('views', 'blog', 'article')
    try:
        return render_template(os.path.join(article_path, 'base.html'),
                               blog=utils.get_article_by_id(article), dir_title=art_dict['title'])
    except Exception as e:
        return render_template('views/build.html')
