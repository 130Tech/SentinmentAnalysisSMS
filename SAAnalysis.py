'''
A 130Tech® Product 1999 - 2019 All Rights Reserved
Read SMS and determine sentiment of text (positive of negative and respond accordingl)
this one works with Twilio so you'll need a Twilio number an SID and a Token
Note you'll also need to be running the latest version of NGrok (https://ngrok.com/download) for this to run on a local machine.
Using python 3.7 64bit to run this.
'''
from flask import Flask, Request
from twilio.twiml.messaging_response import MessagingResponse
from textblob import TextBlob
from textblob import Word
from twilio import twiml
from twilio.rest import Client
app = Flask(__name__)
@app.route("/", methods=['POST'])
def getSMSAndAnalyze():     
    resp = MessagingResponse()
    number = request.form['From']
    message_body = request.form['Body']    
    sAnalysis = TextBlob(message_body) #Lets use TextBlob for the SA
    #You can also get the subjectivity too by using
    sAnalysis.subjectivity()
    #Simple SA stuff with emoji's attached
    if sAnalysis.polarity > 0.5: #Positive
                
        resp.message("I'am glad you like it! \U0001F602")   
        
    else:
        dm.doEmail(message_body)
        resp.message("Sorry to hear that! How can we improve \U0001F621")
        
    # TODO: 001002 -  Add SQL Server integration and Goldmine or other CRM
    return str(resp)
    