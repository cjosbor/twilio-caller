# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse
import time
import csv
# 6-7-2020   Currently this script will call a number and
# listen ton transcripte it so the "message.py"  can retrieve the message
# I tried to copy the recording with no success
#

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



def message():
	""" Creates a client object and retrieves the latest transcription"""
	# create a Client object
	client = Client(account_sid, auth_token)

	# return the most recent transcription ID from Twilios REST API
	transcription = client.transcriptions.list(limit=1)

	# get the sid of the voicemail and store it for our retrieval call
	sid = transcription[0].sid

	# return the most recent recording
	recording = client.recordings.get(sid=sid)
	print(recording)

	# fetch the transcription and assign it
	t = client.transcriptions(sid).fetch()

	# print the last message
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
starting_time = time.time()
# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid =
auth_token =
client = Client(account_sid, auth_token)



'''
# Make sure this is the first call to our URL and record and transcribe

	response.say("Hello, please leave your message after the tone.")

	# Use <Record> verb to record incoming message and set the transcribe argument to true
	response.record(transcribe_callback="/message")
	# transcribe=True)

	# return status message
	print(str(response))
	# Hang up the call
	print("Hanging up...")
	response.hangup()
	'''
'''
try:
	response = VoiceResponse()
	#response.dial('+17049692771')
	response.say("Hello")
	response.record(transcribe=True,max_length='12')
	response.hangup()

	call = client.calls.create(
		# url='http://demo.twilio.com/docs/classic.mp3',
		to='+19316483600',
		from_='+14054448415',
		twiml=response,
		record=True,
		recording_channels='dual'
	)
except:
	pass

'''



blank_dict = {}
##########################################
print("opening file")
input_file = 'phone_number_input.csv'
sites_dict = {}
with open(input_file) as f:
	reader = csv.reader(f)
	next(reader) # skip header
	for row in reader:
		#get switch ip from file
		location_name = row[0].strip()
		switch_ip = row[2].strip()
		print("The location is {} and the phone # is '{}'".format(location_name,switch_ip))
		print("\n")
		try:
			response = VoiceResponse()
			# response.dial('+17049692771')
			response.say("Hello")
			response.record(transcribe=False, max_length='12')
			response.hangup()
			#print(response)

			call = client.calls.create(
					# url='http://demo.twilio.com/docs/classic.mp3',
					to='+1'+ str(switch_ip),
					from_='+14054448415',
					twiml=response,
					record=False,
					recording_channels='dual'
				)
			print(call.sid)
			new_dict1 = {location_name:call.sid}
			blank_dict.update(new_dict1)
			#print(blank_dict)
		except:
			pass
		#print("Sleeping for 20")
		#time.sleep(20)
		#print("transcribing message for {} this # {} \n".format(location_name,switch_ip))
		#message()
		#time.sleep(15)
		#print("done sleeping")
		#message()
###################################################

#time.sleep(30)  # Let the user actually see something!




stop_time = time.time()
print("\n")
print("Finished!!!!!! \n---- elapsed time=", stop_time - starting_time)





