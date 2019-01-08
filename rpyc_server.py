#!/usr/bin/env python3
import time
import rpyc
from rpyc.utils.server import ThreadedServer
from threading import Thread
                
class RPCService(rpyc.Service):

    def __init__(self,my_object):
        self.my_object = my_object
        
    def exposed_get_my_object(self):
        return self.my_object
        
class My_Object(object):

    def __init__(self):
        self.solution = 42

def execute():

    my_object = My_Object()

    server = ThreadedServer(RPCService(my_object),
                            port=12345,
                            protocol_config={"allow_all_attrs":True,
                                             "allow_pickle":True,
                                             "allow_setattr":True})
    t = Thread(target=server.start)
    t.daemon = True
    t.start()

    while True:
        print(f"Solution: {my_object.solution}")
        time.sleep(2)
        
if __name__ == "__main__":

    execute()
