#CONFIG
SERVER="http://voicepy.localtunnel.me/"
GTTS_ENABLED=True
#END CONFIG
from tkinter import *
from tkinter.ttk import *

tk=Tk()
root=tk
window=tk
try:
    import features
except Exception as e:
    print(e)
    messagebox.askokcancel("Feautres disabled","The features have been disabled, please copy/download the features.py to enable features. ")
def process(text):
    from urllib import request, parse
    data = parse.urlencode({"text":text}).encode()
    req =  request.Request(SERVER, data=data) # this will make the method "POST"
    resp = request.urlopen(req)
    resp=resp.read().decode()
    if resp.find("{")>-1:
        try:
            exec(resp[resp.find("{")+1:resp.find("}")])
        except Exception as e:
            print("FAIL RUN "+str(e))
        a=resp.find("{")
        b=resp.find("}")
        resp=list(resp)
        for x in range(a,b):
            resp[x]=" "
        resp="".join(resp)
    return resp
import os
installed=False
def modinstall(mod):
    reply=messagebox.askokcancel("Module install","Would you like to install the module?")
    if reply=="yes":
        try:
            
            os.system("pip install --user "+r)
            return True
        except:
            messagebox.askokcancel("ERROR","Cannot install module "+mod+", please install it manually")
            return False
    return False
def ch(mod,do):
    
    try:
        __import__(mod)
        do()
    except:
        if modinstall(mod):
            do()       
i=0
class app(Frame):
    def doit(self,a=0):
        global i
        result=process(self.e.get())
        self.t.insert(END,"\n"+result)
        if GTTS_ENABLED:
                i=i+1
                try:
                    os.remove("tts.mp3")
                except:
                    pass
                from gtts import gTTS
                tts = gTTS(result)
                tts.save("tts"+str(i)+".mp3")
                import playsound as ps
                ps.playsound("tts"+str(i)+".mp3",0)
        
    def __init__(self,master):
        Frame.__init__(self,master)
        self.t=Text(self)
        self.t.pack(fill=BOTH,expand=YES)
        self.e=Entry(self)
        self.e.pack(fill=BOTH,expand=YES)
        self.pack(fill=BOTH,expand=YES)
        self.t.insert(END,"\nWelcome to assistant beta")
        self.send=Button(self,text="Send",command=self.doit)
        self.send.pack()

import os, re

def purge( pattern):
    for f in os.listdir(dir):
        if re.search(pattern, f):
            os.remove(f)
def cleanup():
    purge("tts*.mp3")
                         
if __name__=="__main__":
    tk.title("Assistant")
    host=app(tk)
    



