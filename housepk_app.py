from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    print("API endpoint accessed")
    return jsonify({
        "message": "House PK API v2.0",
        "version": "2.0",
        "endpoints": ["/login", "/dashboard", "/properties", "/health"],
        "status": "operational"
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username', 'Guest')
    print(f"User {username} attempting login")
    return jsonify({
        "message": f"User {username} logged in successfully",
        "status": "success"
    })
@app.route('/dashboard')
def dashboard():
    print("Dashboard accessed by user")
    return jsonify({
        "message": "Welcome to Dashboard",
        "data": {
            "total_properties": 150,
            "new_listings": 12
        }
    })