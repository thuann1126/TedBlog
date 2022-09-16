from flask import Flask, render_template
import requests

app = Flask(__name__)

posts_data = requests.get('https://api.npoint.io/c790b4d5cab58020d391').json()
print(posts_data)

@app.route('/')
@app.route('/index.html')
def home_page():
    return render_template('index.html', data=posts_data)

@app.route('/about.html')
def about_page():
    return render_template('about.html')

@app.route('/contact.html')
def contact_page():
    return render_template('contact.html')


@app.route("/post.html/<int:index>")
def post_page(index):
    requested_post = None
    for post in posts_data:
        if post['id'] == index:
            requested_post = post
    return render_template('post.html', data=requested_post)

if __name__ == "__main__":
    app.run(debug=True)