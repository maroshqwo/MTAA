import sys
sys.path.append("PySipFullProxy")
import PySipFullProxy.sipfullproxytcp as proxy

HOST, PORT = "0.0.0.0", 5060

if __name__ == '__main__':
    proxy.recordroute = "Record-Route: <sip:%s:%d;transport=tcp;lr>" % (HOST, PORT)
    proxy.topvia = "Via: SIP/2.0/TCP %s:%d" % (HOST, PORT)
    proxy.registrar = {}
    proxy.running = True
    proxy.HOST, proxy.PORT = HOST, PORT
    proxy.startServer()
    while True:
        pass

