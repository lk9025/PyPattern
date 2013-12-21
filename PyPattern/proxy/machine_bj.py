from rpyc.utils.server import ThreadedServer
from gumballservice import GumballServiceBj


server_bj = ThreadedServer(GumballServiceBj, port=9999, auto_register=False)
server_bj.start()
