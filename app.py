from flask import Flask, Response


app = Flask(__name__)

@app.route('/')
def home_page():
    return Response('<html><title>To-Do lists</title></html>')