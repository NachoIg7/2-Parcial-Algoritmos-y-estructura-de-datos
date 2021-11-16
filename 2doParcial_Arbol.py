# El encargado de Jurassic World nos solicita que desarrollemos un algoritmo que nos permita
# resolver los siguientes requerimientos:
# 1. almacenar los datos de los distintos dinosaurios que hay en la isla, de cada uno se
# conoce su nombre, código de cinco dígitos y zona de ubicación (un dígito y un carácter
# por ejemplo 7A), existen varios dinosaurios con el mismo nombre pero sus códigos son
# distintos, los códigos no pueden ser repetidos (tenga cuidado);
# 2. se deben almacenar los datos en dos arboles uno ordenado por nombre y otro por
# código;
# 3. realizar un barrido en orden del árbol ordenado por nombre;
# 4. mostrar toda la información del dinosaurio 792;
# 5. mostrar toda la información de todos los T-Rex que hay en la isla;
# 6. modificar el nombre del dinosaurio en Sgimoloch en ambos arboles porque esta mal
# cargado, su nombre correcto es Stygimoloch;
# 7. mostrar la ubicación de todos los Raptores que hay en la isla;
# 8. contar cuantos Diplodocus hay en el parque;
# 9. debe cargar al menos 15 elementos.

from arbol_binario import Arbol

# datos = [
#     {'nombre':'T-Rex', 'codigo': 12345, 'zona ubicacion': '1A'},
#     {'nombre':'Velociraptor', 'codigo': 54321, 'zona ubicacion': '2A'},
#     {'nombre':'Raptor', 'codigo': 54312, 'zona ubicacion': '3A'},
#     {'nombre':'Arqueopterix', 'codigo': 54421, 'zona ubicacion': '4A'},
#     {'nombre':'Sgimoloch', 'codigo': 12397, 'zona ubicacion': '1D'},
#     {'nombre':'Arqueopterix', 'codigo': 14785, 'zona ubicacion': '4C'},
#     {'nombre':'Diplodocus', 'codigo': 14789, 'zona ubicacion': '1Z'},
#     {'nombre':'Amargasaurio', 'codigo': 14741, 'zona ubicacion': '6S'},
#     {'nombre':'Braquiosaurio', 'codigo': 14412, 'zona ubicacion': '5D'},
#     {'nombre':'Gallimimo', 'codigo': 12986, 'zona ubicacion': '5R'},
#     {'nombre':'Espinosaurio', 'codigo': 12777, 'zona ubicacion': '8T'},
#     {'nombre':'Mamenquisaurio', 'codigo': 77712, 'zona ubicacion': '2Q'},
#     {'nombre':'Coritosaurio', 'codigo': 98652, 'zona ubicacion': '7P'},
#     {'nombre':'Amargasaurio', 'codigo': 10004, 'zona ubicacion': '9I'},
#     {'nombre':'Triceratops', 'codigo': 11228, 'zona ubicacion': '4M'},
#     {'nombre':'Estiracosaurio', 'codigo': 78845, 'zona ubicacion': '7G'},
#     {'nombre':'Raptor', 'codigo': 99999, 'zona ubicacion': '6S'},
#     {'nombre':'Chiubacca', 'codigo': 792, 'zona ubicacion': '9D'},
#     {'nombre':'Raptor', 'codigo': 54399, 'zona ubicacion': '1A'},
#     {'nombre':'T-Rex', 'codigo': 55547, 'zona ubicacion': '5A'},
# ]

# arbol_nombre = Arbol()
# arbol_cod = Arbol()

# for dinosaurio in datos:
#     arbol_nombre = arbol_nombre.insertar_nodo(dinosaurio['nombre'], dinosaurio) 

# for dinosaurio in datos:
#     arbol_cod = arbol_cod.insertar_nodo(dinosaurio['codigo'], dinosaurio)

# # Punto 3 Barrido en orden por nombre
# arbol_nombre.inorden()

# # Punto 4 Info del dino 792
# print ('Informacion del dinosaurio cuyo codigo es 792')
# arbol_cod.mostrar_informacion_codigo(792)

#Punto 5- mostrar toda la información de todos los T-Rex que hay en la isla;
# print ('Informacion del T-Rex')
# arbol_nombre.mostrar_informacion_nombre('T-Rex')

# Punto 6- modificar el nombre del dinosaurio en Sgimoloch en ambos arboles porque esta mal
# cargado, su nombre correcto es Stygimoloch;
# buscado = input ('Ingrese las primeras letras del dinosaurio a modificar: ').capitalize() #Ponemos en maayusculas la primer letra
# arbol_nombre.busqueda_proximidad(buscado)
# print ()
# buscado = input('De la lista anterior, escriba el nombre completo del dinosaurio a modificar: ').capitalize()
# print()
# pos = arbol_nombre.busqueda(buscado)
# if (pos):
#     nuevo_nombre = input('Ingrese el nuevo nombre: ').capitalize()
#     nombre, dinosaurio = arbol_nombre.eliminar_nodo(buscado)
#     dinosaurio['nombre'] = nuevo_nombre
#     arbol = arbol_nombre.insertar_nodo(nuevo_nombre, dinosaurio)
#     print()
#     arbol_nombre.inorden()
#     print()
#     arbol_cod.inorden()
# print()

# #Punto 7- mostrar la ubicación de todos los Raptores que hay en la isla;
# print ('Ubiacion de todos los Raptores')
# arbol_nombre.mostrar_ubicacion_dinosaurio('Raptor')

# #Punto 8- contar cuantos Diplodocus hay en el parque;
# contador = arbol_nombre.contar_ocurrencias_dinosaurios('Diplodocus')
# print('El dinosaurio Diplodocus aparece en ',contador, ' oportunidad/es.')

