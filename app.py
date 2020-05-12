from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from main import msgs
#print(msgs)
app = Flask(__name__)


def reply():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)

    # Start our TwiML response
    resp = MessagingResponse()

    # Determine the right reply for this message

    if body == 'Check' or body == 'check':
        resp.message(msgs)
    elif body == 'Bye':
        resp.message("Goodbye")
    elif body == 'Hi':
        resp.message('Hello Pavan')

    return str(resp)


@app.route("/")
def hello():
    return "Hello World"


@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    return reply()


if __name__ == "__main__":
    app.run(debug=True)
