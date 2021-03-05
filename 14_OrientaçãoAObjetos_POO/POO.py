#classes: determina um conjunto de objetos
#atributos e metodos
#atributos: variaveis etc, caracteristicas
#metodos: funcoes, funcionalidades, operacoes associadas a classe

#todo objeto é uma instancia de uma classe
#construtores sao metodos especiais que implementam as ações necessárias para inicializar um objeto
#__init__(self..)
class User:
	def __init__(self):

	def __init__(self, nome, sobrenome, email):
		self.nome = nome
		self.sobrenome = sobrenome
		self.email = email
	def nome_completo(self):
		return '{} {}'.format(self.nome, self.sobrenome)

u = User('du','edu','duedu@gmail.com')
print(u.nome)
print(u.nome_completo())
#out: du edu



#ENCAPSULAMENTO
#combina atributos e metodos em uma classe
#__dois_undescores: atributo privado
#_um_underscore: atributo protegido.


class x:
	def __init__(self):
		self.a = '123'
		self._b = '234'
		self.__c = '345'

'''
x = X()
x.a
x._b
x.__c -> error, correct: x._X__c
'''

#HERANÇA
#classes dentro de outras classes(Superclasses e Subclasses)

#herança simples
class Pessoa:
	def __init(self,nome,idade):
		self.nome = nome 
		self.idade = idade 

class Atleta(Pessoa):
	def __init__(self,nome,idade,peso,altura):
		self.peso = peso 
		self.altura = altura
		self.imc = peso/altura**2
		super().__init__(nome,idade)
		#super() é usado para referenciar a superclasse

#Herança multipla

class Homem:
	def __init__(self):
		print('Homem')
		self.nome = 'fulano'

class Lobo:
	def __init__(self):
		print('Lobo')
		self.cor = 'branco'

class Lobisomem(Lobo, Homem):
	def __init__(self):
		print('Lobisomem')
		Homem.__init__(self)
		super().__init__()

	def __repr__(self):
		return 'Lobisomem {}: {}'.format(self.nome, self.cor)


#POLIMORFISMO: sobreescrita ou sobrecarga de métodos.

class Animal:
	def emite_som(self):
		pass

class Arara(Animal):
	def emite_som(self):
		print('AAA')

class Cascavel(Animal):
	def emite_som(self):
		print('SSS')


'''
arara = Arara()
arara.emite_som
cascavel = Cascavel()
Cascavel.emite_som()


OVERRINDING
OVERLOADING
'''


class Usuario:
	qtde_usuarios = 0 # variavel de classe

	def __init__(self, first, last, email):
		self.nome = first
		self.sobrenome = last
		self.email = email

		Usuario.qtde_usuarios +=1

	def full_name(self):
		return '{} {}'.format(self.nome, self.sobrenome)

if __name__ == '__main__':
	u1 = Usuario('Jose', 'da Silva', 'jose@gmail.com')
	u2 = Usuario('João', 'da Silva', 'joao@gmail.com')
	u3 = Usuario('Tales', 'da Silva', 'tales@gmail.com')
	print(Usuario.qtde_usuarios)


#DECORATOR
'''
@classmethod = metodo da classe
'''


class Disciplina:
	qtde_max = 35#atritudes
	count = 0

	@classmethod#decorator
	def set_max_qtde(cls,qtde):
		'''Um metodo de classe'''
		cls.qtde_max = qtde

Disciplina.set_max_qtde(15)
'''
Disciplina.qtde_max
15
'''	

'''
@static method
'''


class Circulo:
	@staticmethod
	def Area(raio):
		return 3.14*raio**2

print(Circulo.Area(5))