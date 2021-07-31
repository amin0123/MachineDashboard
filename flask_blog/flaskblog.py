from flask import Flask , render_template , url_for

app = Flask(__name__)

posts = [
    {
        'author' : 'corey shafer',
        'title' : 'blog post 1',
        'content' :  'first post content',
        'date_posted': 'july 29,2021'
    },
    {
        'author' : 'amin',
        'title' : 'blog post 2',
        'content' :  'second  post content',
        'date_posted': 'july 299,2021'
    }
]

@app.route("/")
@app.route("/home")
def hello():
    return render_template('hometest.html')

@app.route("/abouttest")
def about():
    return render_template('abouttest.html')   



if __name__ == '__main__':
    app.run(debug = True)

