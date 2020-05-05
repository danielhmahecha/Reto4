"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """


import config as cf
from ADT import list as lt
from ADT import graph as g
from ADT import map as map
from ADT import list as lt
from DataStructures import listiterator as it
from datetime import datetime
from DataStructures import dijkstra as dk

"""
Se define la estructura de un catálogo de libros.
El catálogo tendrá tres listas, una para libros, otra para autores 
y otra para géneros
"""

# Construccion de modelos

def newCatalog():
    """
    Inicializa el catálogo y retorna el catalogo inicializado.
    """
    rgraph = g.newGraph(111353,compareByKey)
    catalog = {'reviewGraph':rgraph}    
    return catalog


def addReviewNode (catalog, row):
    """
    Adiciona un nodo para almacenar un libro o usuario 
    """
    if not g.containsVertex(catalog['reviewGraph'], row['SOURCE']):
        g.insertVertex (catalog['reviewGraph'], row['SOURCE'])
    if not g.containsVertex(catalog['reviewGraph'], row['DEST']):
        g.insertVertex (catalog['reviewGraph'], row['DEST'])

def addReviewEdge (catalog, row):
    """
    Adiciona un enlace para almacenar una revisión
    """
    if row['AIR_TIME'] != "":
        g.addEdge (catalog['reviewGraph'], row['SOURCE'], row['DEST'], float(row['AIR_TIME']))


def addLibraryNode (catalog, row):
    """
    Adiciona un nodo para almacenar una biblioteca
    """
    if not g.containsVertex(catalog['librariesGraph'], row['ID_src']):
        g.insertVertex (catalog['librariesGraph'], row['ID_src'])
    if not g.containsVertex(catalog['librariesGraph'], row['ID_dst']):
        g.insertVertex (catalog['librariesGraph'], row['ID_dst'])

def addLibraryEdge  (catalog, row):
    """
    Adiciona un enlace entre bibliotecas
    """
    g.addEdge (catalog['librariesGraph'], row['ID_src'], row['ID_dst'], float(row['dist']))


def countNodesEdges (catalog):
    """
    Retorna la cantidad de nodos y enlaces del grafo de bibliotecas
    """
    nodes = g.numVertex(catalog['reviewGraph'])
    edges = g.numEdges(catalog['reviewGraph'])

    return nodes,edges

def getShortestPath (catalog, source, dst):
    """
    Retorna el camino de menor costo entre vertice origen y destino, si existe 
    """
    graph = catalog['reviewGraph']
    print("vertices: ",source,", ",dst)
    if g.containsVertex(graph, source) and g.containsVertex(graph, dst):
        dijks = dk.newDijkstra(graph,source)
        if dk.hasPathTo(dijks, dst):
            path = dk.pathTo(dijks,dst)
        else:
            path = 'No hay camino'
    else:
        path = 'No existen los vértices'

    return path
    # ejecutar Dijkstra desde source
    # obtener el camino hasta dst
    # retornar el camino
    
   # return None
    
# Funciones de comparacion

def compareByKey (key, element):
    return  (key == element['key'] )  

