# Parte 1
lista1 = ['gato','','perro','ratones','']
lista1.pop(1)
lista1.pop(3)
print(lista1)
# Parte 2
lista1 = [1,2, [200, 400, [1000, 6000], 800], 30, 40]
lista1[2][2].insert(1,5000)
print(lista1)
# Parte 3
str = 'Despues de la tempestad''viene la calma'
print(str[0]+str[19]+str[36])
# Parte 4
temperatura_centigrados = 20
a = 20
b = 9/5
c = 32
Tf = b*a + c
print (Tf)
# Parte 5
dict1 = {'Diez' : 10, 'Veinte' : 20, 'Treinta' : 30}
dict2 = {'Treinta' : 30, 'Cuarenta' : 40, 'Cicuenta' : 50}
print(dict1.pop('Treinta'))
# Parte 6
dict1= {'Diez': 10, 'Veinte': 20}
dict1.update(dict2)
print(dict1)
# Parte 7
diccionarioEstudiante = {'clase': {'estudiante': {'nombre': 'Mike', 'marcas': {'fisica': 70, 'historia' : 80}}}}
print(diccionarioEstudiante['clase']['estudiante']['marcas']['historia'])
# Parte 8
dict={'nombre': 'Platon', 'Pais': 'Antigua Grecia', 'fecha_de_nacimiento': -427, 'maestro': 'Socrates', 'alumno': 'Aristoteles'}
dict['fecha_de_nacimiento'] = 428
print (dict)

