selic = 14.25

def exibir():
	print('selic em {0:.2f} %'.format(selic))

def atualizar(taxa):
	global selic#usa a variavel global
	selic = taxa 

exibir()
atualizar(13)
exibir()
