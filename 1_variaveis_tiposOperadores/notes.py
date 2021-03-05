#print

print("Hello World")

x = int("3")
#instancia-se um objeto do tipo int.

'''
	Tipos de dados
	Numeros: int, float, complex
	Booleanos: bool(true, false)
	String: str
	Listas e Tuplas: list, tuple
'''
name = 'Learn Python'
type(x)#retorna o tipo ou classe de um objeto
print(name,x)

'''
Faça um algoritmo que leia 2 valores inteiros e armazene-os nas variáveis A e B. Efetue a soma de A e B atribuindo o seu resultado na variável C. Imprima C.


'''

a = input()
b = input()#ou b = int(input())
# print(a,b)
#print(a+b)
print(int(a)+int(b))




'''
Leia dois valores inteiros. Efetue as quatro operações matemáticas : 
Adição, Subtração, Multiplicação e Divisão.  
'''
a = input()
b = input()
print('\nA=',(a+b),'\nS=',(a-b),'\nM=',(a*b),'\nD=',(a/b))



#STRINGS em PY

 a = """a"""
 a = "a"
 a= 'a'
 a = '''a'''

''' CONCATENAÇÃO
>>> s = s1+s2
>>> s
'ifcearacati'
>>> s = s1+' '+s2
>>> s
'ifce aracati'
>>> t = len(s)
>>> t
12
'''
print('fulano' in 'fulano de tal')#true

#slice notation
s = 'python'
s[:]
s[1:5]
#string[inicio:fim]


#conversao = int(),str(),float(),bool()