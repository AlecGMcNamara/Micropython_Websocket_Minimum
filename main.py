from microdot_asyncio import Microdot, Response, send_file
from microdot_utemplate import render_template
from microdot_asyncio_websocket import with_websocket
import ujson

# Initialize MicroDot
app = Microdot()
Response.default_content_type = 'text/html'
myCounter=0

# root route
@app.route('/')
async def index(request):
    return render_template('index.html')

@app.route('/ws')
@with_websocket
async def wsMessage(request, ws):
    global myCounter
    jsonSend={
            "V1":"Video",
            "V2":False,
            "V3":myCounter,
            "V4":"",
            "V5":"",
            "V6":"",
            "V7":"",
            "V8":"",
            "V9":"",
            "V10":""
            }
    await ws.send(ujson.dumps(jsonSend))
    jsonReceive = ujson.loads(await ws.receive())
    myCounter = jsonReceive["V3"]  #save to variable
    myCounter +=1
   
# Static CSS/JSS
@app.route("/static/<path:path>")
def static(request, path):
    return send_file("static/" + path)

# shutdown
@app.get('/shutdown')
def shutdown(request):
    request.app.shutdown()
    return 'The server is shutting down...'

app.run()

while True:
        #
        # put main loop code here
        #
    pass 
    
