from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('./index.html', title='Home', page='Home')

@app.route('/contact')
def contact():
    return render_template('./index.html', title='Contact', page='Contact')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    
    