
# Cargar el esquema de red de la siguiente figura en un grafo e implementar los algoritmos
# necesarios para resolver las tareas, listadas a continuación:
# 1. cada nodo además del nombre del equipo deberá almacenar su tipo: pc, notebook, servidor, router, switch, impresora;
# 2. realizar un barrido en profundidad y amplitud partiendo desde la tres notebook: Red
# Hat, Debian, Arch;
# 3. encontrar el camino más corto para enviar a imprimir un documento desde la pc:
# Debian y Red Hat, hasta el servidor “MongoDB”;
# 4. encontrar el árbol de expansión mínima;
# 5. la impresora esta temporalmente fuera de linea por mantenimiento, quítela del grafo y
# realice un barrido en profundidad para corroborar que efectivamente fue borrada;
# 6. debe utilizar un grafo no dirigido.

from grafo import Grafo


componentes = Grafo (dirigido = False)

componentes.insertar_vertice("Arch", data ="Notebook")
componentes.insertar_vertice("Ubuntu", data ="PC")
componentes.insertar_vertice("Impresora", data ="Impresora")
componentes.insertar_vertice("Mint", data ="PC")
componentes.insertar_vertice("Switch1", data ="Switch")
componentes.insertar_vertice("Debian", data ="Notebook")
componentes.insertar_vertice("MongoDB", data ="Servidor")
componentes.insertar_vertice("Router1", data ="Router")
componentes.insertar_vertice("Router2", data ="Router")
componentes.insertar_vertice("Router3", data ="Router")
componentes.insertar_vertice("Red Hat", data ="Notebook")
componentes.insertar_vertice("Guarani", data ="Servidor")
componentes.insertar_vertice("Manjaro", data ="PC")
componentes.insertar_vertice("Switch2", data ="Switch")
componentes.insertar_vertice("Fedora", data ="PC")
componentes.insertar_vertice("Parrot", data ="PC")


componentes.insertar_arista(17, 'Switch 1', 'Debian')
componentes.insertar_arista(18, 'Switch 1', 'Ubuntu')
componentes.insertar_arista(22, 'Switch 1', 'Impresora')
componentes.insertar_arista(80, 'Switch 1', 'Mint')
componentes.insertar_arista(29, 'Switch 1', 'Router 1')
componentes.insertar_arista(37, 'Router 1', 'Router 2')
componentes.insertar_arista(43, 'Router 1', 'Router 3')
componentes.insertar_arista(50, 'Router 2', 'Router 3')
componentes.insertar_arista(25, 'Router 2', 'Red Hat')
componentes.insertar_arista(9, 'Router 2', 'Guarani')
componentes.insertar_arista(61, 'Switch 2', 'Router 3')
componentes.insertar_arista(40, 'Switch 2', 'Manjaro')
componentes.insertar_arista(12, 'Switch 2', 'Parrot')
componentes.insertar_arista(5, 'Switch 2', 'MongoDB')
componentes.insertar_arista(56, 'Switch 2', 'Arch')
componentes.insertar_arista(3, 'Switch 2', 'Fedora')


# Punt 2 -realizar un barrido en profundidad y amplitud partiendo desde la tres notebook: Red
# Hat, Debian, Arch;

# pos = componentes.buscar_vertice('Red Hat')
# print ('Barrido en profundidad desde Red Hat')
# componentes.barrido_profundidad(pos)
# componentes.marcar_no_visitado()
# print()
# print ('Barrido en Amplitud desde Red Hat')
# componentes.barrido_amplitud(pos)
# print ()

# pos = componentes.buscar_vertice('Debian')
# print ('Barrido en profundidad desde Debian')
# componentes.barrido_profundidad(pos)
# componentes.marcar_no_visitado()
# print()
# print ('Barrido en Amplitud desde Debian')
# componentes.barrido_amplitud(pos)
# print ()

# pos = componentes.buscar_vertice('Arch')
# print ('Barrido en profundidad desde Arch')
# componentes.barrido_profundidad(pos)
# componentes.marcar_no_visitado()
# print()
# print ('Barrido en Amplitud desde Arch')
# componentes.barrido_amplitud(pos)
# print ()

# Punto 3 encontrar el camino más corto para enviar a imprimir un documento desde la pc:
# Debian y Red Hat, hasta el servidor “MongoDB”;
# pc = 'Debian'
# servidor = 'MongoDB'
# ver_origen = componentes.buscar_vertice(pc)
# ver_destino = componentes.buscar_vertice(servidor)

# pila_camino = componentes.dijkstra (ver_origen, ver_destino)

# destino = servidor
# distancia = None
# print ('El camino mas corto para imprimir es: ')
# while(not componentes.pila_vacia()):
#     dato = componentes.desapilar()
#     if(dato[1][0] == destino):
#         if(costo is None):
#             costo = dato[0]
#         print(dato[1][0])
#         destino = dato[1][1]

# print('El costo para ir desde Debian hasta MongoDB es: ', distancia)

# print ()

# pc = 'Red Hat'
# servidor = 'MongoDB'
# ver_origen = componentes.buscar_vertice(pc)
# ver_destino = componentes.buscar_vertice(servidor)

# pila_camino = componentes.dijkstra (ver_origen, ver_destino)

# destino = servidor
# distancia = None
# print ('El camino mas corto para imprimir es: ')
# while(not componentes.pila_vacia()):
#     dato = componentes.desapilar()
#     if(dato[1][0] == destino):
#         if(costo is None):
#             costo = dato[0]
#         print(dato[1][0])
#         destino = dato[1][1]

# print('El costo para ir desde Red Hat hasta MongoDB es: ', distancia)

# print()

# Punto 4  encontrar el árbol de expansión mínima;
# print('Arbol de expansion minima')
# bosque = componentes.prim()
# peso = 0
# for elemento in bosque:
#     print (elemento[1][0], '-', elemento [1][1])
#     peso += elemento [0]
# print ('El costo toal es', peso)


# Punto 5 la impresora esta temporalmente fuera de linea por mantenimiento, quítela del grafo y
# realice un barrido en profundidad para corroborar que efectivamente fue borrada;
print('-------------------------')
eliminar = 'Impresora'
componentes.eliminar_vertice(eliminar)
componentes.barrido_profundidad(0)