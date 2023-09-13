from flask import Flask, jsonify, render_template, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    mode = request.cookies.get('mode', 'light')
    return render_template('home.html', mode=mode)

@app.route('/about')
def about():
    mode = request.cookies.get('mode', 'light')
    return render_template('about.html', mode=mode)

@app.route('/skills')
def skills():
    mode = request.cookies.get('mode', 'light')
    return render_template('skills.html', mode=mode)

@app.route('/work')
def work():
    mode = request.cookies.get('mode', 'light')
    return render_template('work.html', mode=mode)

@app.route('/contact')
def contact():
    mode = request.cookies.get('mode', 'light')
    return render_template('contact.html', mode=mode)

@app.route('/set_mode', methods=['POST'])
def set_mode():
    mode = request.form.get('mode')
    res = make_response("Mode set")
    res.set_cookie('mode', mode, max_age=60*60*24*365*2)  # Set cookie for 2 years
    return res

if __name__ == '__main__':
    app.run(debug=True)
