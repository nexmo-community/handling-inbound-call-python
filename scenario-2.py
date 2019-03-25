from flask import Flask, request, jsonify

NEXMO_NUMBER = "44700900002"
YOUR_SECOND_NUMBER = "447700900001"

app = Flask(__name__)

ncco = [
    {
        "action": "talk",
        "text": "Hello, one moment please, your call is being forwarded to our agent."
    },
    {
        "action": "connect",
        "from": NEXMO_NUMBER,
        "endpoint": [{
           "type": 'phone',
           "number": YOUR_SECOND_NUMBER
         }]
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
