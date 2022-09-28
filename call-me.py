# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse

# This script calls me using twilio studio -  flow ID has to be copied to make this work
# 6-7-2020

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid =
auth_token =
client = Client(account_sid, auth_token)

to ="+18644238288"
from_="+14054448415"
flow_id ='FW8449c63ef54275407d8c976ddd8bb276'

client.studio.v1.flows(flow_id).executions.create(to=to, from_=from_)