import rpyc
from rpyc.utils.server import ThreadedServer

class MeuServico(rpyc.Service):
	lista = []

	def exposed_append (self, dado):
		self.lista.append(dado)
		return self.lista

	def exposed_valor (self):
		return self.lista


t = ThreadedServer(MeuServico, port=8752)
t.start()
