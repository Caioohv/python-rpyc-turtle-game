import rpyc

lista = []

class MeuServico(rpyc.Service):
    def exposed_contador_linha(self, objeto_arquivo):
        n_linhas = len(objeto_arquivo.readlines())
        return n_linhas
    def exposed_test(self, valor):
        lista.append(valor)
        return lista
    

from rpyc.utils.server import ThreadedServer
t = ThreadedServer(MeuServico, port=18861)
t.start()