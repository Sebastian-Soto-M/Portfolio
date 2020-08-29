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
