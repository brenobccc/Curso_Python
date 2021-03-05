'''
if condição:
	bloco de instruções

else:
	bloco de instruções

	___________

if condição:
	bloco de instruções
elif condição:
	bloco-de-instruções
else:
	bloco de instrução

'''
selic = 14.25
if selic > 14:
	print("teste")
elif selic<0:
	print("ha")


a = 10
b = 5
c = 7


	
if a>c>b:
	print(a, "é o maior")

	
#out: 10 é o maior

#COMANDO pass
#define bloos de códigos vazios, já que o python n usa chaves
if a>c>b:
	pass


#COMANDO None = representa o valor NULL.
nome = None
	type(nome)