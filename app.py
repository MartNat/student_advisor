from flask import Flask, render_template, request

app = Flask(__name__)

class KnowledgeBase:
    def __init__(self):
        self.courses = {
            'Computer Science': {
                'side_hustle': 'Freelance coding projects',
                'supplementary_courses': ['Web Development', 'Data Science'],
                'clubs': ['Coding Club', 'Tech Innovators']
            },
            'Business Administration': {
                'side_hustle': 'Online business or consulting',
                'supplementary_courses': ['Marketing', 'Entrepreneurship'],
                'clubs': ['Business Club', 'Entrepreneurship Society']
            },
            'Business Computing': {
                'side_hustle': 'Online business or consulting, Freelance coding projects',
                'supplementary_courses': ['Data Science', 'Entrepreneurship', 'Web Development'],
                'clubs': ['Business Club', 'Entrepreneurship Society']
            },
            # Add more courses and information as needed
        }

    def get_recommendations(self, user_input):
        if 'computer science' in user_input.lower():
            return self.courses.get('Computer Science', {})
        elif 'business administration' in user_input.lower():
            return self.courses.get('Business Administration', {})
        elif 'business computing' in user_input.lower():
            return self.courses.get('Business Computing', {})
        # Add more conditions for other courses as needed
        else:
            return "Course not found in the knowledge base."

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get', methods=['POST'])
def get_bot_response():
    user_input = request.form['input']

    knowledge_base = KnowledgeBase()
    bot_response = knowledge_base.get_recommendations(user_input)

    if isinstance(bot_response, dict):
        response_text = (f"Recommendations for {user_input} students:\n"
                         f"Side Hustle: {bot_response.get('side_hustle', 'Not available')}\n"
                         f"Supplementary Courses: {', '.join(bot_response.get('supplementary_courses', []))}\n"
                         f"Clubs to Join: {', '.join(bot_response.get('clubs', []))}")
    else:
        response_text = bot_response

    return response_text

if __name__ == '__main__':
    app.run(debug=True)
