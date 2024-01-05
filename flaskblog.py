from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author':'Debarshi',
        'title':'Blog post 1',
        'content':'First post content',
        'date_posted':'January 5, 2024'
    },
    {
        'author':'Kashica',
        'title':'Blog post 2',
        'content':'Second post content',
        'date_posted':'January 6, 2024'
    }
]

@app.route("/")
@app.route("/home")
def hello_world():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__=='__main__':
    app.run(debug=True)