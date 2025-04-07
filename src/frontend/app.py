from flask import Flask, render_template_string
import requests

app = Flask(__name__)


@app.route('/')
def home():
    try:
        # Make a request to the FastAPI backend
        response = requests.get("http://backend:8000/api/greeting")
        data = response.json()
        message = data.get('message', 'No message found')
    except Exception as e:
        message = f"Error: {str(e)}"

    # Render the HTML template with the message
    return render_template_string("""
    <h1>Welcome to Frontend!</h1>
    <p>Backend says: {{ message }}</p>
    """, message=message)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5000)
