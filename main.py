from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    mode = request.cookies.get('mode', 'light')
    experiences = [
        {
            "title": "Nexclap - Software Developer",
            "date": "Jan 2024 - Present",
            "location": "Remote - San Ramon, CA",
            "details": [
                "Spearheading the expansion of our platform to incorporate AI-driven features for enhanced user engagement.",
                "Developing a scalable backend infrastructure using Node.js and MongoDB to support real-time data processing and analytics.",
                "Implementing a custom chatbot service using the OpenAI GPT-3 model to provide instant support and enhance customer service.",
                "Leading the migration to a microservices architecture to improve modularity and deployment efficiency."
            ],
            "logo": "static/img/nexclap_logo.jpg"
        },
        {
            "title": "Siliconvalley4u - Coding Instructor",
            "date": "Jan 2023 - Present",
            "location": "Remote - San Ramon, CA",
            "details": [
                "Developing comprehensive course material to mentor over 200 middle and high school students in data structures, algorithms, Python, Java, web development, and more.",
                "Self-taught introductory Generative AI & NLP principles to teach a semester-long class, achieving a 95% student satisfaction rating.",
                "Conducting virtual class meetings with coordinated parent scheduling, boosting parent engagement by 30% through timely reminders and weekly progress reports."
            ],
            "logo": "static/img/siliconvalley4u_logo.png"
        },
        {
            "title": "Yatsys – Software Developer",
            "date": "June 2023 – July 2023",
            "location": "Remote - United States",
            "details": [
                "Contributed to an agile team developing a prototype using Flask and Google Cloud technologies focused on facial and emotion recognition, part of a larger initiative to enable real-time alert dispatch for parents of children with disabilities.",
                "Assisted in developing custom deep learning models for personalized emotional cue recognition using TensorFlow.js and a Firebase-backend UI for user uploaded facial data, successfully meeting phase one requirements within a two-month timeline.",
                "Authored technical documentation outlining the architecture, providing development recommendations, and ensuring a successful hand-off for future work."
            ],
            "logo": "static/img/YatsysLogo.jpg"
        },
        {
            "title": "DHL Supply Chain – Business Data Analyst Intern",
            "date": "June 2021 – July 2021",
            "location": "Fort Worth, TX",
            "details": [
                "Constructed a feasibility analysis model to examine warehouse inefficiencies, advancing the implementation of an RPA solution that reduced labor costs by 20%.",
                "Utilized Power BI and Excel for visualization of labor planning and warehouse management data to aid in decision-making and enhanced data reliability."
            ],
            "logo": "static/img/DHL_logo.png"
        },
        {
            "title": "Zen Distributions – Product Consultant",
            "date": "May 2020 – June 2020",
            "location": "Dallas, TX",
            "details": [
                "Established an effective distribution channel for medical masks for 14 critical access hospitals and pop-up clinics during a global supply chain crisis, ensuring a reliable supply of PPE when most needed.",
                "Contributed to a 15% increase in sales by implementing a CRM system to improve order processing speeds and customer follow-up."
            ],
            "logo": "static/img/zendistributionslogo.jpg"
        },
        {
            "title": "Kaizen Guest Properties – Co-Founder & Property Manager",
            "date": "Feb 2019 – Sept 2019",
            "location": "Austin, TX",
            "details": [
                "Co-founded a property management startup focused on providing fully furnished corporate housing and short-term leases.",
                "Directed logistics for the entire property portfolio including four apartment units, one house, and a duplex, generating $75,000 in revenue over 4 months."
            ],
            "logo": "static/img/stayhikaru_logo.jpg"
        }
    ]
    return render_template('main_page.html', mode=mode, experiences=experiences)

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
            'image': 'static/img/Screenshot 2023-12-20 160859.png'
        },
        {
            'title': 'Cat Facts API',
            'description': 'Mini Project implementing the Cat Facts API',
            'link': 'https://gamma.app/docs/Mini-Project-Random-Cat-Fact-Generator-8het0l1i3fvmy3q',
            'image': 'static/img/Screenshot 2023-12-20 165037.png'
        },
        {
            'title': 'Google Maps API Project',
            'description': 'Student Project using the Google Maps API',
            'link': 'https://gamma.app/docs/Google-Maps-API-Project-38pmes92j8ba820',
            'image': 'static/img/Screenshot 2023-12-20 160503.png'
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
            'image': 'static/img/Screenshot 2023-11-03 205218.png'
        },
        {
            'title': 'NLP: Introduction to Natural Language Processing',
            'description': 'Understanding the basics of Natural Language Processing.',
            'link': 'https://gamma.app/docs/0r46z0in5jnpv1f',
            'image': 'static/img/Screenshot 2023-11-03 205339.png'
        },
        {
            'title': 'NLP Chatbot',
            'description': 'A simple chatbot applying the basics of natural language processing ',
            'link': 'https://colab.research.google.com/drive/1zdkPmYsYBVoQN_KWxM3v5AKO8jAuoLTY?usp=sharing',
            'image': 'static/img/Screenshot 2023-11-03 213059.png'
        },
        {
            'title': 'TensorFlow Chatbot',
            'description': 'Chatbot using a neural network/TensorFlow ',
            'link': 'https://gamma.app/public/TensorFlow-Chatbot-vc4hp8yz8pwmsdh',
            'image': 'static/img/Screenshot 2023-11-03 212134.png'
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

