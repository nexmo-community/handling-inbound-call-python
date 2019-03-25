from flask import Flask, request, jsonify

app = Flask(__name__)

ncco = [
    {
        "action": "talk",
        "text": "Hello, our office hours are Monday to Friday nine until five thirty. Please call back then."
    }
]

@app.route("/webhooks/answer")
def answer_call():
    return jsonify(ncco)

@app.route("/webhooks/event", methods=['POST'])
def events():
    return ("200")

if __name__ == '__main__':
    app.run(host="localhost", port=9000)
