from twilio.rest import Client
from queue import Queue
import requests
from requests.auth import HTTPBasicAuth

# This script retrieves the last transcription list=1  that was done on my account
# with the account SID and token below

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC57bc749eab01cd497d2093b28b33dd23'
auth_token = '317463371bcb7b141bc963714b2ab1e3'



def do_work(recording):
    print(recording)
    data = requests.get(recording, auth=HTTPBasicAuth(account_sid, auth_token),
                        stream=True)
    # Create a .wav file and stream the recording to improve performance.
    with open(recording.sid + '.wav', 'wb') as fd:
        for chunk in data.iter_content(1):
            fd.write(chunk)
    #client.recordings.delete(recording.sid)
    # Make sure the whole print completes or threads
    # can mix up output in one line.
    #with lock:
        print(threading.current_thread().name,
              "has downloaded to the local folder and "
              "has been deleted off Twilio", recording.sid)

def message():
    """ Creates a client object and retrieves the latest transcription"""
    #create a Client object
    client = Client(account_sid, auth_token)

    #return the most recent transcription ID from Twilios REST API
    transcription = client.transcriptions.list(limit=1)



    #get the sid of the voicemail and store it for our retrieval call
    sid = transcription[0].sid

    # return the most recent recording
    recording = client.recordings.get(sid=sid)
    print(recording)

    #fetch the transcription and assign it
    t = client.transcriptions(sid).fetch()


    #print the last message
    print(t.transcription_text)

    # create a text message and send ourselves the text
    '''
    m = client.messages \
        .create(
        body=str(t.transcription_text),
        from_='+14054448415',
        to='+18644238288'
    )
    print(t.transcription_text)
    print(m.sid)
    '''

    return str(sid)



if __name__ == '__main__':
    message()