import rpyc

proxy = rpyc.connect('localhost', 18861, config={'allow_public_attrs': True})
lista = proxy.root.exposed_test(1)
print('Lista atual: ', lista)
lista = proxy.root.exposed_test(2)
print('Lista atual: ', lista)
lista = proxy.root.exposed_test(3)
print('Lista atual: ', lista)
lista = proxy.root.exposed_test(4)
print('Lista atual: ', lista)
lista = proxy.root.exposed_test(5)
print('Lista atual: ', lista)
print('Numero de linhas no arquivo: ', n_linhas)