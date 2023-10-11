from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    mode = request.cookies.get('mode', 'light')
    return render_template('main_page.html', mode=mode)

@app.route('/set_mode', methods=['POST'])
def set_mode():
    mode = request.form.get('mode', 'light')
    resp = make_response("Mode set!")
    resp.set_cookie('mode', mode, max_age=30*24*60*60)  
    return resp

@app.route('/student_api')
def student_api():
    mode = request.cookies.get('mode', 'light')
    return render_template('student_api.html', mode=mode)

@app.route('/py2a_dsa')
def py2a_dsa():
    mode = request.cookies.get('mode', 'light')
    return render_template('py2a_dsa.html', mode=mode)


if __name__ == '__main__':  
    app.run(debug=True)
