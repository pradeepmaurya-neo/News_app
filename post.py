from forms import PostForm
from flask import request, redirect, render_template, Blueprint, flash, url_for
from models import Post
from db import session


post_bp = Blueprint('post', __name__)


@post_bp.route('/posts', methods=['GET', 'POST'])
def add_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, conetent=form.content.data)
        session.add(post)
        session.commit()
        flash("data added successfully!")
        return render_template('post.html', form=form)

    form.title.data = ""
    form.content.data = ""
    return render_template('post.html', form=form)

@post_bp.route('/<int:id>')
def posts(id):
    post = session.query(Post).filter(Post.id==id).first()
    return render_template('index.html', post=post)