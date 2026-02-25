from flask import Flask, render_template, request, redirect, url_for

import storage

app = Flask(__name__)


@app.route("/")
def index():
    blog_posts = storage.get_blogposts()
    return render_template("index.html", posts=blog_posts)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        author = request.form.get("author")
        title = request.form.get("title")
        content = request.form.get("content")
        storage.add_blogpost(author, title, content)
        return redirect(url_for("index"))
    
    return render_template("add.html")


@app.route('/delete/<int:post_id>', methods=["GET"])
def delete(post_id):
    # Find the blog post with the given id and remove it from the list
    # Redirect back to the home page
    storage.delete_blogpost(post_id)
    return redirect(url_for("index"))


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    # Fetch the blog posts from the JSON file
    post = storage.fetch_post_by_id(post_id)
    if post is None:
        # Post not found
        return "Post not found", 404
    
    if request.method == 'POST':
        # Update the post in the JSON file
        author = request.form.get("author")
        title = request.form.get("title")
        content = request.form.get("content")
        storage.update_blogpost(post_id, author, title, content)
        # Redirect back to index
        return redirect(url_for("index"))

    # Else, it's a GET request
    # So display the update.html page
    return render_template('update.html', post=post)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
