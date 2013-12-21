from rpyc.utils.server import ThreadedServer
from gumballservice import GumballServiceSh


server_sh = ThreadedServer(GumballServiceSh, port=9998, auto_register=False)
server_sh.start()
