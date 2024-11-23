# Q.1) Build a bot which provides all the information related to you in college
# Ans:-

from flask import Flask, request, jsonify
app = Flask(__name__)
# Replace these with your own information
your_name = "Your Name"
your_program = "Your Program"
your_year = "Your Year"
your_interests = ["Interest 1", "Interest 2", "Interest 3"]

@app.route('/college_bot', methods=['POST'])
def college_bot():
    data = request.get_json()
    if 'action' in data:
        action = data['action']
    if action == 'get_info':
        response = {
            'name': your_name,
            'program': your_program,
            'year': your_year,
            'interests': your_interests
        }
        return jsonify(response)
    else:
        return jsonify({'error': 'Invalid action'})
        return jsonify({'error': 'Action not provided'})

if __name__ == '__main__':
    app.run(debug=True)