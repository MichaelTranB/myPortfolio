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

@app.route('/generative_ai')
def generative_ai():
    course_materials = [
        {
            'title': 'Introduction to Neural Networks',
            'description': 'An introductory slide about Neural Networks.',
            'link': '/path/to/material1',
            'image': 'static\Screenshot 2023-10-10 224922.png'
        },
        {
            'title': 'Basics of NLP',
            'description': 'Understanding the basics of Natural Language Processing.',
            'link': '/path/to/material2',
            'image': 'static\Screenshot 2023-10-10 224922.png'
        },

        {
            'title': 'Basics of NLP',
            'description': 'Understanding the basics of Natural Language Processing.',
            'link': '/path/to/material2',
            'image': 'static\Screenshot 2023-10-10 224922.png'
        },
         {
            'title': 'Basics of NLP',
            'description': 'Understanding the basics of Natural Language Processing.',
            'link': '/path/to/material2',
            'image': 'static\Screenshot 2023-10-10 224922.png'
        }
       
    ]

    mode = request.cookies.get('mode', 'light')
    # Make sure to pass the course_materials to the template here
    return render_template('generative_ai.html', mode=mode, course_materials=course_materials)

if __name__ == '__main__':
    app.run(debug=True)

