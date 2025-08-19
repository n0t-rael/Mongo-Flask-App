from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from models.post import Post

blog_bp = Blueprint("blog", __name__)

@blog_bp.route("/dashboard")
@login_required
def dashboard():
    posts = Post.get_all_posts()
    return render_template("dashboard.html", posts=posts)

@blog_bp.route("/create", methods=["GET", "POST"])
@login_required
def create_post():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        Post.create_post(current_user.username, title, content)
        return redirect(url_for("blog.dashboard"))
    return render_template("post.html")
