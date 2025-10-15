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