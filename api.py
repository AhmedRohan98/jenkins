from flask import Flask, request, jsonify

app = Flask(__name__)

# Home route
@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the Basic Python API!"})

# Example GET route
@app.route('/api/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'World')  # Get 'name' parameter from query string
    return jsonify({"greeting": f"Hello, {name}!"})

# Example POST route
@app.route('/api/echo', methods=['POST'])
def echo():
    data = request.json  # Parse JSON body of the request
    if not data:
        return jsonify({"error": "No JSON data provided"}), 400
    return jsonify({"received_data": data})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
