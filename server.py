from flask import *
import time
app = Flask(__name__)
data={"help":"You'll have to tell me what you need help with","sing":"You'll have to give me some sound files for that!","starblast":"That's a great game!","hey":"what","whats up":"I'll be telling intresting things soon","i'm bored":"I'll be able to tell you stuff later in the future!!","stba":"I've heard it lags.","you":"What about me","bye":"Goodbye, user"
,"cryptography":"I've heard it's illegal to use it some places. By the way there are lots of cool encryption algorthims!","time travel":"It's JUST NOT POSSIBLE","yell":"I'M YELLING AT YOU BY USING CAPS BUT PROBALY IT DOESN'T WORK","bob":"??????"

      }
rep={"show time":"time"}
def logic(t):
    if t=="hi":
        return "hi, back to you"
    if t=="restart":
        return """Restart capbility has not been added yet {print("Send act message")}"""
    intent=t.split(" ")
    if intent[0]=="yt":
        return "Playing from youtube {features.playchromecast("+intent[1]+")}"
    if t in ["time","what time is it","what's the time","tell me the time"]:
        return "It's "+str(time.asctime())+" on the server right now"
    if t in rep.keys():
        t=rep[t]
    if t in data.keys():
        return data[t]
    return "Please rephrase"
    
@app.route("/",methods=["GET","POST"])
def run():
    if request.method=="GET":
        return '''

<h1>ACS ai demo</h1>
<from method=POST>
<input type="text" name="text"></input>
</form>





'''
    else:
        try:
            return logic(request.form["text"].lower())
        except:
            return "Improper format"
app.run(host="0.0.0.0",port=80)
