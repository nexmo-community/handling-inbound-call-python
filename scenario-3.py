from flask import Flask, request, jsonify
from threading import Timer
import nexmo

UUID = ""
APPLICATION_ID = "YOUR_APP_ID"
PRIVATE_KEY = "private.key"
TIMEOUT = 40 # Agent becomes available after this period of time
NEXMO_NUMBER = "447009000002" # Your Nexmo number
YOUR_SECOND_NUMBER = "447009000001" # Your second phone (agent)

audio_url = "https://your_domain.com/your_music.mp3"
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

def transfer_call ():
    print ("Transferring call...")
    client = nexmo.Client(application_id = APPLICATION_ID, private_key=PRIVATE_KEY)
    dest = {"type": "ncco", "url": [ncco_url]}
    response = client.update_call(UUID, action="transfer", destination=dest)

def register_timer_callback():
    t = Timer(TIMEOUT, transfer_call)
    t.start()

register_timer_callback()
    
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

if __name__ == '__main__':
    app.run(host="localhost", port=9000)
