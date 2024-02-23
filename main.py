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
    course_materials = [
        {
            'title': 'Introduction to APIs',
            'description': 'With a Simple Weather App',
            'link': 'https://gamma.app/docs/Introduction-to-APIs-with-a-Simple-Weather-App-l6ttjedomwep6qc',
            'image': '\static\Screenshot 2023-12-20 160859.png'
        },
        {
            'title': 'Cat Facts API',
            'description': 'Mini Project implementing the Cat Facts API',
            'link': 'https://gamma.app/docs/Mini-Project-Random-Cat-Fact-Generator-8het0l1i3fvmy3q',
            'image': 'static\Screenshot 2023-12-20 165037.png'
        },
        {
            'title': 'Google Maps API Project',
            'description': 'Student Project using the Google Maps API',
            'link': 'https://gamma.app/docs/Google-Maps-API-Project-38pmes92j8ba820',
            'image': 'static\Screenshot 2023-12-20 160503.png'
        }
    ]
    mode = request.cookies.get('mode', 'light')
    return render_template('student_api.html', mode=mode, course_materials=course_materials)

@app.route('/py2a_dsa')
def py2a_dsa():
    mode = request.cookies.get('mode', 'light')
    return render_template('py2a_dsa.html', mode=mode)

@app.route('/generative_ai')
def generative_ai():
    course_materials = [
        {
            'title': 'Generative Networks: GANs and VAEs',
            'description': 'An introduction to Neural Networks.',
            'link': 'https://gamma.app/docs/w5x6kc483k62dq2',
            'image': 'static\Screenshot 2023-11-03 205218.png'
        },
        {
            'title': 'NLP: Introduction to Natural Language Processing',
            'description': 'Understanding the basics of Natural Language Processing.',
            'link': 'https://gamma.app/docs/0r46z0in5jnpv1f',
            'image': 'static\Screenshot 2023-11-03 205339.png'
        },
        {
            'title': 'NLP Chatbot',
            'description': 'A simple chatbot applying the basics of natural language processing ',
            'link': 'https://colab.research.google.com/drive/1zdkPmYsYBVoQN_KWxM3v5AKO8jAuoLTY?usp=sharing',
            'image': 'static\Screenshot 2023-11-03 213059.png'
        },
        {
            'title': 'TensorFlow Chatbot',
            'description': 'Chatbot using a neural network/TensorFlow ',
            'link': 'https://gamma.app/public/TensorFlow-Chatbot-vc4hp8yz8pwmsdh',
            'image': 'static\Screenshot 2023-11-03 212134.png'
        }
       
    ]

    mode = request.cookies.get('mode', 'light')
    return render_template('generative_ai.html', mode=mode, course_materials=course_materials)


@app.route('/valentines')
def valentines():
    mode = request.cookies.get('mode', 'light')
    return render_template('valentines.html', mode=mode)


@app.route('/yatsys')
def yatsys():
    mode = request.cookies.get('mode', 'light')
    return render_template('yatsys.html', mode=mode)


@app.route('/nexclap')
def nexclap():
    mode = request.cookies.get('mode', 'light')
    return render_template('nexclap.html', mode=mode)


if __name__ == '__main__':
    app.run(debug=True)

