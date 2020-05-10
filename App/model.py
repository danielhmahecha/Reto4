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
from DataStructures import dfs as dfs 
from DataStructures import bfs as bfs 

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
    tgraph = g.newGraph(111353,compareByKey,True)
    catalog = {'non_directed_Graph':rgraph, 'directed_Graph':tgraph}    
    return catalog
    

def addReviewNode_non_directed (catalog, row):
    """
    Adiciona un nodo para almacenar un libro o usuario 
    """
    if not g.containsVertex(catalog['non_directed_Graph'], row['SOURCE']):
        g.insertVertex (catalog['non_directed_Graph'], row['SOURCE'])
    if not g.containsVertex(catalog['non_directed_Graph'], row['DEST']):
        g.insertVertex (catalog['non_directed_Graph'], row['DEST'])

def addReviewEdge_non_directed (catalog, row):
    """
    Adiciona un enlace para almacenar una revisión
    """
    if row['AIR_TIME'] != "":
        g.addEdge (catalog['non_directed_Graph'], row['SOURCE'], row['DEST'], float(row['AIR_TIME']))


def addReviewNode_directed (catalog, row):
    """
    Adiciona un nodo para almacenar un libro o usuario 
    """
    if not g.containsVertex(catalog['directed_Graph'], row['SOURCE']):
        g.insertVertex (catalog['directed_Graph'], row['SOURCE'])
    if not g.containsVertex(catalog['directed_Graph'], row['DEST']):
        g.insertVertex (catalog['directed_Graph'], row['DEST'])

def addReviewEdge_directed (catalog, row):
    """
    Adiciona un enlace para almacenar una revisión
    """
    if row['AIR_TIME'] != "":
        g.addEdge (catalog['directed_Graph'], row['SOURCE'], row['DEST'], float(row['AIR_TIME']))


def countNodesEdges_non_directed (catalog):
    """
    Retorna la cantidad de nodos y enlaces del grafo de bibliotecas
    """
    nodes = g.numVertex(catalog['non_directed_Graph'])
    edges = g.numEdges(catalog['non_directed_Graph'])

    return nodes,edges
def countNodesEdges_directed (catalog):
    """
    Retorna la cantidad de nodos y enlaces del grafo de bibliotecas
    """
    nodes = g.numVertex(catalog['directed_Graph'])
    edges = g.numEdges(catalog['directed_Graph'])

    return nodes,edges


def getPath (catalog, source, dest, strct):
    """
    Retorna el camino, si existe, entre vertice origen y destino
    """
    path = None
    if g.containsVertex(catalog['non_directed_Graph'],source) and g.containsVertex(catalog['non_directed_Graph'],dest):
        #print("vertices: ",source,", ", dest)
        if strct == 'dfs':
            search = dfs.newDFS(catalog['non_directed_Graph'],source)
            path = dfs.pathTo(search,dest)
        if strct == 'bfs':
            search = bfs.newBFS(catalog['non_directed_Graph'],source)
            path = bfs.pathTo(search, dest)
    # ejecutar dfs desde source
    # obtener el camino hasta dst
    # retornar el camino

    return path



def getShortestPath (catalog, source, dst):
    """
    Retorna el camino de menor costo entre vertice origen y destino, si existe 
    """
    graph = catalog['directed_Graph']
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

