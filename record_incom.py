from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse
from twilio.rest import Client

app = Flask(__name__)

# this app uses ngrok http 5000 from command line to start up a small flask webserver
# you call into Twilio and then it trascribes the message and sends an SMS message
# 6-7-2020
#
@app.route("/record", methods=["POST"])
def record():
    """ Returns TwiML which prompts the caller to record a message"""
    # Define TwiML response object
    response = VoiceResponse()

    # Make sure this is the first call to our URL and record and transcribe
    if 'RecordingSid' not in request.form:
        # Use <Say> verb to provide an outgoing message
        response.say("Hello, please leave your message after the tone.")

        # Use <Record> verb to record incoming message and set the transcribe argument to true
        response.record(transcribe_callback="/message")
        # transcribe=True)

        # return status message
        print(str(response))
    else:
        # Hang up the call
        print("Hanging up...")
        response.hangup()
    return str(response)


@app.route("/message", methods=["POST"])
def message():
    """ Creates a client object and returns the transcription text to an SMS message"""
    # create a client object and pass it our secure authentication variables

    # Your Account Sid and Auth Token from twilio.com/console
    # DANGER! This is insecure. See http://twil.io/secure
    account_sid =
    auth_token =
    client = Client(account_sid, auth_token)

    # return the most recent transcription ID from Twilios REST API
    transcription = client.transcriptions.list(limit=1)

    # get the sid of the voicemail and store it for our retrieval call
    sid = transcription[0].sid


    # fetch the transcription and assign it
    t = client.transcriptions(sid).fetch()
    print(t.transcription_text)

    # create a text message and send ourselves the text
    m = client.messages \
        .create(
        body=str(t.transcription_text),
        from_='+14054448415',
        to='+18644238288'
    )
    print(t.transcription_text)
    print(m.sid)
    return str(sid)


if __name__ == "__main__":
    app.run()