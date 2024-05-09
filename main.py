from flask import Flask, render_template, request, make_response
import os

app = Flask(__name__)

@app.route('/')
def index():
    mode = request.cookies.get('mode', 'light')
    
    skills = [
        {"name": "Python", "type": "icon", "icon": "fab fa-python", "description": "Python"},
        {"name": "JavaScript", "type": "icon", "icon": "fab fa-js", "description": "JavaScript"},
        {"name": "Java", "type": "icon", "icon": "fab fa-java", "description": "Java"},
        {"name": "HTML", "type": "icon", "icon": "fab fa-html5", "description": "HTML"},
        {"name": "CSS", "type": "icon", "icon": "fab fa-css3-alt", "description": "CSS"},
        {"name": "React", "type": "icon", "icon": "fab fa-react", "description": "React"},
        {"name": "Flask", "type": "icon", "icon": "fas fa-flask", "description": "Flask"},
        {"name": "Google Cloud Platform", "type": "icon", "icon": "fas fa-cloud", "description": "Google Cloud Platform"},
        {
            "name": "Firebase",
            "type": "svg",
            "svg_content": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="#4F46E5" width="3em" height="3em"><path d="M93.19,329.38,140.64,25.31c1.64-10.37,15.55-12.82,20.46-3.55l51,95.45ZM432,400,385.26,123.21a11,11,0,0,0-18.54-6L80,400l159.36,91.91a33.18,33.18,0,0,0,31.91,0ZM302.36,158.93,265.82,89.39a10.86,10.86,0,0,0-19.36,0L85.83,375.74Z"/></svg>""",
            "description": "Firebase"
        },
        {"name": "NoSQL", "type": "icon", "icon": "fas fa-database", "description": "NoSQL"},
        {"name": "SQL", "type": "icon", "icon": "fas fa-database", "description": "SQL"},
        {
            "name": "PostgreSQL",
            "type": "svg",
            "svg_content": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 50 50" width="50px" height="50px"><path d="M 34.902344 2 C 32.863281 2 31.097656 2.550781 29.875 3.09375 C 28.675781 2.691406 26.6875 2.003906 24.300781 2.5 C 22.910156 2.742188 21.632813 3.316406 20.460938 4.195313 C 18.53125 3.265625 16.515625 2.695313 14.402344 2.601563 C 13.101563 2.5 7.800781 3.101563 5.898438 5.898438 C 5.199219 7 4.5 8.398438 4.199219 10.097656 C 3.898438 11.597656 3.898438 13.300781 4.398438 16.800781 C 4.699219 19.199219 5.101563 20.800781 6 24.097656 C 6.101563 24.398438 6.601563 26 8.101563 30.402344 C 8.398438 31.199219 9 32.699219 10.199219 34.097656 C 11 35.097656 11.800781 35.699219 12.800781 35.699219 C 14.101563 35.699219 15 34.800781 15.800781 33.800781 C 15.859375 33.734375 15.921875 33.660156 15.980469 33.59375 C 15.90625 33.710938 15.839844 33.839844 15.800781 34 C 15.601563 35 16.800781 35.800781 17.800781 36.199219 C 18.601563 36.597656 19.5 36.699219 20.199219 36.699219 C 21.097656 36.699219 21.800781 36.5 22.199219 36.402344 C 22.542969 36.285156 23.285156 35.964844 24.078125 35.4375 C 24.113281 37.992188 24.136719 41.007813 24.199219 41.699219 C 24.5 44.300781 25.199219 46.097656 26.5 47.097656 C 27.5 47.898438 29.300781 48 29.402344 48 C 31.199219 48 34 46.800781 35.199219 44.902344 C 35.800781 44 36 43.199219 36.199219 42.097656 C 36.398438 41.5 36.597656 38 36.699219 37.300781 C 36.835938 36.195313 36.941406 35.105469 37.046875 34.046875 C 37.707031 34.21875 38.519531 34.402344 39.402344 34.402344 C 41 34.402344 43.101563 33.300781 43.5 33.097656 C 44.300781 32.5 45.898438 31.101563 45.199219 29.902344 C 44.800781 29.199219 44.199219 29.199219 42.699219 29.402344 C 42.699219 29.402344 40.300781 29.699219 40.097656 29.597656 C 39.953125 29.542969 39.730469 29.402344 39.480469 29.21875 C 40 28.414063 40.460938 27.617188 41 26.902344 C 42.199219 24.601563 42.902344 22.800781 43.402344 21.402344 C 44.300781 18.902344 44.800781 16.898438 45.097656 15.5 C 45.800781 12.5 46 11.101563 45.597656 9.5 C 44.800781 6.699219 41.898438 4.300781 40.699219 3.601563 C 39.898438 3.199219 37.902344 2 34.902344 2 Z M 34.902344 4 C 37.402344 4 39.101563 5 40 5.398438 C 41.101563 6 43.601563 8 43.800781 9.898438 C 43.902344 11 44 12.101563 43.300781 15 C 42.902344 16.398438 42.5 18.199219 41.597656 20.699219 C 41.097656 22.097656 40.5 23.800781 39.300781 25.902344 C 39.269531 25.953125 39.234375 26.007813 39.203125 26.0625 C 39.320313 25.640625 39.402344 25.300781 39.402344 25.300781 C 39.601563 24.300781 39.601563 23.5 39.5 22.300781 C 39.398438 21.699219 39.300781 20.199219 39.300781 19.597656 C 39.300781 19.300781 39.597656 16.199219 39.699219 15.097656 C 39.800781 13.300781 38.699219 11.097656 38.402344 10.699219 C 36.902344 8.398438 36.101563 7.101563 34.5 5.800781 C 34.101563 5.460938 33.417969 4.894531 32.488281 4.324219 C 33.222656 4.144531 34.035156 4 34.902344 4 Z M 26.066406 4.410156 C 27.371094 4.441406 28.476563 4.800781 29.300781 5.101563 C 31.402344 5.800781 32.699219 6.898438 33.300781 7.398438 C 34.601563 8.5 35.300781 9.601563 36.800781 11.902344 C 36.910156 12.121094 37.195313 12.585938 37.421875 13.234375 C 35.375 13.046875 34.015625 13.765625 33.199219 14.5 C 32 15.5 32.097656 17 32.199219 18.097656 C 32.199219 18.898438 32.402344 19.902344 33.902344 23.300781 C 34.5 24.800781 35.097656 26.398438 35.699219 27.5 C 36.011719 28.121094 36.394531 28.691406 36.804688 29.199219 C 36.566406 29.320313 36.324219 29.476563 36.097656 29.699219 C 35.5 30.398438 35.398438 31.101563 35.199219 32.402344 C 35 33.402344 34.800781 35.5 34.699219 37.199219 C 34.699219 37.898438 34.402344 41.300781 34.300781 41.800781 C 34 42.800781 33.898438 43.300781 33.5 43.902344 C 32.800781 45 30.601563 45.902344 29.300781 45.800781 C 28.902344 45.800781 28.300781 45.800781 27.800781 45.402344 C 26.699219 44.601563 26.300781 42.800781 26.199219 41.402344 C 26.097656 40.402344 26.199219 33.199219 26 31.597656 C 25.898438 31.199219 25.800781 30.199219 25 29.5 C 24.664063 29.21875 23.96875 29.074219 23.3125 28.976563 C 23.320313 28.640625 23.339844 28.304688 23.402344 28 C 23.5 27.398438 23.699219 27.097656 23.902344 26.597656 C 24 26.300781 24.199219 25.902344 24.402344 25.402344 C 25.300781 22.601563 25.097656 18.898438 24.597656 16.597656 C 24.5 16.398438 24.097656 14.800781 22.699219 13.902344 C 21.199219 13 19.597656 13.5 18.699219 13.800781 C 18.328125 13.902344 17.960938 14.0625 17.59375 14.25 C 17.65625 13.832031 17.710938 13.410156 17.800781 13 C 18.199219 11 18.601563 9.300781 19.902344 7.601563 C 21.300781 5.898438 22.898438 4.800781 24.699219 4.5 C 25.175781 4.425781 25.632813 4.398438 26.066406 4.410156 Z M 13.71875 4.585938 C 13.953125 4.582031 14.152344 4.585938 14.300781 4.601563 C 15.863281 4.683594 17.359375 5.050781 18.84375 5.675781 C 18.660156 5.878906 18.476563 6.082031 18.300781 6.300781 C 16.601563 8.300781 16.199219 10.398438 15.800781 12.5 C 15.300781 15 15.199219 17.597656 15.597656 20.199219 L 15.402344 22.097656 C 15.300781 23.097656 15.097656 25 16.199219 27 C 16.585938 27.664063 17.011719 28.226563 17.480469 28.707031 C 16.464844 30.050781 15.386719 31.320313 14.300781 32.5 C 13.699219 33.199219 13.199219 33.699219 12.800781 33.699219 C 12.699219 33.699219 12.300781 33.5 11.699219 32.800781 C 10.597656 31.601563 10.199219 30.300781 10 29.800781 C 8.800781 26.199219 8.101563 23.898438 8 23.597656 C 7.199219 20.398438 6.800781 18.800781 6.398438 16.5 C 5.898438 13.300781 5.898438 11.699219 6.199219 10.402344 C 6.5 9 7 7.898438 7.5 7.101563 C 8.726563 5.175781 12.09375 4.628906 13.71875 4.585938 Z M 36.664063 15.125 C 36.984375 15.125 37.332031 15.164063 37.699219 15.242188 C 37.6875 16.175781 37.300781 19.105469 37.300781 19.5 C 37.300781 20.300781 37.5 21.898438 37.5 22.5 C 37.601563 23.601563 37.601563 24.199219 37.5 25 C 37.5 25 37.351563 25.714844 37.199219 26.222656 C 36.734375 25.171875 36.21875 23.917969 35.597656 22.5 C 34.097656 19.101563 34 18.402344 34 17.902344 C 34 17.199219 34 16.300781 34.597656 15.902344 C 35.160156 15.402344 35.84375 15.132813 36.664063 15.125 Z M 21.140625 15.417969 C 21.339844 15.441406 21.523438 15.5 21.699219 15.597656 C 22.5 16 22.699219 17 22.699219 17 C 23.199219 19.199219 23.398438 22.5 22.597656 24.699219 C 22.5 25.097656 22.300781 25.398438 22.199219 25.699219 C 22 26.199219 21.800781 26.699219 21.597656 27.597656 C 21.546875 27.96875 21.523438 28.335938 21.511719 28.703125 C 20.820313 28.558594 20.167969 28.3125 19.699219 28 C 18.898438 27.601563 18.300781 26.898438 17.902344 26.097656 C 17.199219 24.597656 17.300781 23.199219 17.402344 22.402344 L 17.597656 20.097656 C 17.457031 18.972656 17.390625 17.84375 17.40625 16.722656 C 17.867188 16.328125 18.46875 15.925781 19.300781 15.699219 C 19.902344 15.550781 20.558594 15.34375 21.140625 15.417969 Z M 35.886719 16.089844 C 35.625 16.101563 35.347656 16.148438 35.199219 16.199219 C 34.800781 16.300781 34.699219 16.300781 34.597656 16.5 C 34.5 16.699219 34.800781 17 34.902344 17.199219 C 35 17.199219 35.300781 17.5 35.699219 17.402344 C 36 17.300781 36.199219 17.101563 36.300781 17 C 36.402344 16.898438 36.800781 16.398438 36.5 16.199219 C 36.398438 16.097656 36.148438 16.074219 35.886719 16.089844 Z M 20.914063 16.816406 C 20.804688 16.824219 20.699219 16.851563 20.597656 16.902344 C 20.5 16.902344 20.300781 17 20.199219 17.199219 C 20.097656 17.398438 20.199219 17.597656 20.300781 17.699219 C 20.5 18 20.800781 18.300781 21.300781 18.300781 C 21.402344 18.300781 21.800781 18.300781 22.097656 18 C 22.097656 18 22.402344 17.699219 22.402344 17.402344 C 22.300781 17.199219 22.101563 17.101563 21.800781 17 C 21.574219 16.925781 21.238281 16.792969 20.914063 16.816406 Z M 19.074219 29.902344 C 19.6875 30.230469 20.425781 30.496094 21.234375 30.679688 C 21.019531 31.109375 20.710938 31.464844 20.402344 31.699219 C 19.699219 32.199219 18.800781 32.5 17.902344 32.699219 C 17.699219 32.699219 17.601563 32.800781 17.402344 32.800781 C 16.917969 32.9375 16.449219 33.089844 16.128906 33.421875 C 17.109375 32.332031 18.09375 31.128906 19.074219 29.902344 Z M 38.355469 30.703125 C 38.792969 31.03125 39.222656 31.273438 39.597656 31.402344 C 40.199219 31.601563 40.699219 31.601563 42.5 31.402344 C 42.199219 31.699219 41.300781 32.199219 40 32.402344 C 39.164063 32.484375 38.125 32.285156 37.28125 32.042969 C 37.359375 31.476563 37.449219 31.152344 37.597656 31 C 37.652344 30.949219 37.984375 30.847656 38.355469 30.703125 Z M 23.296875 31.003906 C 23.503906 31.039063 23.667969 31.066406 23.699219 31.097656 C 23.898438 31.300781 24 31.800781 24 32 C 24.011719 32.171875 24.019531 32.605469 24.027344 32.90625 C 23.203125 33.871094 21.878906 34.40625 21.597656 34.5 C 21.199219 34.699219 20 34.898438 18.800781 34.5 C 19.800781 34.199219 20.800781 33.902344 21.597656 33.300781 C 22.296875 32.800781 22.898438 32.003906 23.296875 31.003906 Z"/></svg>""",
            "description": "PostgreSQL"
        },
        {"name": "Docker", "type": "icon", "icon": "fab fa-docker", "description": "Docker"},
        {"name": "PyTest", "type": "icon", "icon": "fas fa-vial", "description": "PyTest"},
        {"name": "Git", "type": "icon", "icon": "fab fa-git", "description": "Git"},
    ]

    experiences = [
        {
            "title": "Nexclap - Software Developer",
            "date": "Jan 2024 - Present",
            "location": "Remote - San Ramon, CA",
            "details": [
                "Spearheading the expansion of an eLearning platform into an AI-enhanced social network designed to connect students with recruiters, utilizing Google Cloud for scalability, data management, and storage",
                "Implementing a custom chatbot service using the OpenAI REST API & Python SDK with Flask for career and education advising",
                "Developing an in-house video conference feature and recruiter hub to facilitate direct interaction between students and recruiters",
                "Modernized development by migrating to a local PostgreSQL environment, using Docker for containerization, and integrating GitHub Actions for automatic deployment and CI/CD, saving hundreds of development hours and streamlining patch management"
            ],
            "logo": "static/img/nexclap_logo.jpg"
        },
        {
            "title": "Siliconvalley4u - Coding Instructor",
            "date": "Jan 2023 - Present",
            "location": "Remote - San Ramon, CA",
            "details": [
                "Developing comprehensive course materials to mentor over 200 middle and high school students in data structures, algorithms, Python, Java, web development, and more",
                "Self-taught introductory Generative AI & NLP principles to teach a semester long class, achieving a 95% student satisfaction rating",
                "Conducting virtual class meetings with coordinated parent scheduling, boosting parent engagement by 30% through timely reminders and weekly progress reports"
            ],
            "logo": "static/img/siliconvalley4u_logo.png"
        },
        {
            "title": "Yatsys - Software Developer",
            "date": "June 2023 - July 2023",
            "location": "Remote - United States",
            "details": [
                "Contributed to an agile team developing a prototype using Flask and Google Cloud technologies focused on facial and emotion recognition, part of a larger initiative to enable real-time alert dispatch for parents of children with disabilities",
                "Assisted in developing custom deep learning models for personalized emotional cue recognition using TensorFlow.js and a Firebase-backend UI for user uploaded facial data, successfully meeting phase one requirements within a two-month timeline",
                "Authored technical documentation outlining the architecture, providing development recommendations, and ensuring a successful hand-off for future work"
            ],
            "logo": "static/img/YatsysLogo.jpg"
        },
        {
            "title": "DHL Supply Chain - Business Data Analyst Intern",
            "date": "June 2021 - July 2021",
            "location": "Fort Worth, TX",
            "details": [
                "Constructed a feasibility analysis model to examine warehouse inefficiencies, advancing the implementation of an RPA solution that reduced labor costs by 20%.",
                "Utilized Power BI and Excel for visualization of labor planning and warehouse management data to aid in decision-making and enhanced data reliability."
            ],
            "logo": "static/img/DHL_logo.png"
        },
        {
            "title": "Zen Distributions - Product Consultant",
            "date": "May 2020 - June 2020",
            "location": "Dallas, TX",
            "details": [
                "Established an effective distribution channel for medical masks for 14 critical access hospitals and pop-up clinics during a global supply chain crisis, ensuring a reliable supply of PPE when most needed.",
                "Contributed to a 15% increase in sales by implementing a CRM system to improve order processing speeds and customer follow-up."
            ],
            "logo": "static/img/zendistributionslogo.jpg"
        },
        {
            "title": "Kaizen Guest Properties - Co-Founder & Property Manager",
            "date": "Feb 2019 - Sept 2019",
            "location": "Austin, TX",
            "details": [
                "Co-founded a property management startup focused on providing fully furnished corporate housing and short-term leases.",
                "Directed logistics for the entire property portfolio including four apartment units, one house, and a duplex, generating $75,000 in revenue over 4 months."
            ],
            "logo": "static/img/stayhikaru_logo.jpg"
        }
    ]
    return render_template('main_page.html', mode=mode, skills=skills, experiences=experiences)

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
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

