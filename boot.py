import network

# Replace the following with your WIFI Credentials
SSID = 'PLUSNET-XFC3FN'
SSI_PASSWORD = '3FHJVYLUMVUHk7'

def do_connect():

    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('Connecting to network...')
        sta_if.active(True)
        sta_if.connect(SSID, SSI_PASSWORD)
        while not sta_if.isconnected():
            pass
    print('Connected! Network config:', sta_if.ifconfig())
    
print("Connecting to your wifi...")
do_connect()