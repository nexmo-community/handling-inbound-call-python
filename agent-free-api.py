from flask import Flask, request, jsonify
import nexmo

UUID = ""
APPLICATION_ID = "YOUR_APP_ID"
PRIVATE_KEY = "private.key"
NEXMO_NUMBER = "YOUR_NEXMO_NUMBER"
YOUR_SECOND_NUMBER = "YOUR_SECOND_NUMBER"

audio_url = "https://your_domain.com/music/your_music.mp3"
ncco_url = "https://1234abcd.ngrok.io/ncco"

ncco = [
    {
        "action": "talk",
        "text": "Hello, I'm sorry, but all our agents are helping customers right now. Please hold, and we will put you through as soon as possible."
    },
    {         
        "action": "stream",                           
        "streamUrl": [audio_url],
        "loop": 0
    }    
]

ncco2 = [
    {
        "action": "talk",
        "text": "Now connecting you. Thanks for waiting."
    },
    {
        "action": "connect",
        "from": NEXMO_NUMBER,
        "endpoint": [{"type": 'phone',"number": YOUR_SECOND_NUMBER}]
    }
]

app = Flask(__name__)

@app.route("/webhooks/answer")
def answer_call():
    global UUID
    UUID = request.args['uuid']
    print("UUID:====> %s" % UUID)
    return (jsonify(ncco))

@app.route("/webhooks/event", methods=['POST'])
def events():
    return ("200")

@app.route("/ncco")
def build_ncco():
    return jsonify(ncco2)

# In this version just navigate to localhost:9000/agentfree to simulate a free agent
@app.route("/agentfree")
def agent_free():
    print ("Transferring call...")
    client = nexmo.Client(application_id = APPLICATION_ID, private_key=PRIVATE_KEY)
    dest = {"type": "ncco", "url": [ncco_url]}
    response = client.update_call(UUID, action="transfer", destination=dest)    
    return ("Agent available")

if __name__ == '__main__':
    app.run(host="localhost", port=9000)
