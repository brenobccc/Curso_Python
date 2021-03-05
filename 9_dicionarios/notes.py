d.keys()#strings
dict_keys(['bender','fry', 'zoidberg','amy'])

d.values()#inteiros
dict_values([5,23,45,21])

d.items()
dict_items([('bender',5),('fry',23)])

d = {}

d = dict()

d = {'john':23,'paulMcartney':45}
d['jude'] = 40#insere ou atualiza
del d['jude']#remove

d.clear()#limpa todos os items.

ida = d.pop('john')#remove o item retornando o valor

d.get('admin')