"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog_Artists():
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    catalog_Artist = {'ConstituentID': None,
               'DisplayName': None,
               'ArtistBio': None,
               'Nationality': None,
               "Gender": None,
               "BeginDate": None,
               "EndDate": None,
               "WikiQID": None,
               "ULAN": None}

    

    catalog_Artist['ConstituentID'] = lt.newList()
    catalog_Artist['DisplayName'] = lt.newList('SINGLE_LINKED')
    catalog_Artist['ArtistBio'] = lt.newList('SINGLE_LINKED')
    catalog_Artist['Nationality'] = lt.newList('SINGLE_LINKED')
    catalog_Artist['Gender'] = lt.newList('SINGLE_LINKED')
    catalog_Artist['BeginDate'] = lt.newList('SINGLE_LINKED')
    catalog_Artist['EndDate'] = lt.newList('SINGLE_LINKED')
    catalog_Artist['WikiQID'] = lt.newList('SINGLE_LINKED')
    catalog_Artist['ULAN'] = lt.newList('SINGLE_LINKED')

    return catalog_Artist

def newCatalog_Artworks():
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    catalog_Artworks = {'ObjectID': None,
               'Title': None,
               'ConstituentID': None,
               'Date': None,
               "Medium": None,
               "Dimensions": None,
               "CreditLine": None,
               "AccesionNumber": None,
               "Classification": None,
               "Department": None,
               "DateAcquired": None,
               "Catalogued": None,
               "URL": None,
               "Circumference": None, 
               "Depth": None,
               "Diameter": None,
               "Classification": None,
               "Height": None,
               "Length": None,
               "Weight": None,
               "Width": None,
               "SeatHeight": None,
               "Duration": None}

    

    catalog_Artworks["ObjectID"] = lt.newList('SINGLE_LINKED')
    catalog_Artworks["Title"] = lt.newList('SINGLE_LINKED')
    catalog_Artworks["ConstituentID"] = lt.newList('SINGLE_LINKED')
    catalog_Artworks["Date"] = lt.newList('SINGLE_LINKED')
    catalog_Artworks["Medium"] = lt.newList('SINGLE_LINKED')
    catalog_Artworks["Dimensions"] = lt.newList('SINGLE_LINKED')
    catalog_Artworks["CreditLine"] = lt.newList('SINGLE_LINKED')
    catalog_Artworks["AccesionNumber"] = lt.newList('SINGLE_LINKED')
    catalog_Artworks["Classification"] = lt.newList('SINGLE_LINKED')
    catalog_Artworks["Department"] = lt.newList('SINGLE_LINKED')
    catalog_Artworks["DataAcquiered"] = lt.newList('SINGLE_LINKED')
    catalog_Artworks["Catalogued"] = lt.newList('SINGLE_LINKED')
    catalog_Artworks["URL"] = lt.newList('SINGLE_LINKED')
    catalog_Artworks["Circumference"] = lt.newList('SINGLE_LINKED')
    catalog_Artworks["Depth"] = lt.newList('SINGLE_LINKED')
    catalog_Artworks["Diameter"] = lt.newList('SINGLE_LINKED')
    catalog_Artworks["Classification"] = lt.newList('SINGLE_LINKED')
    catalog_Artworks["Height"] = lt.newList('SINGLE_LINKED')
    catalog_Artworks["Length"] = lt.newList('SINGLE_LINKED')
    catalog_Artworks["Weight"] = lt.newList('SINGLE_LINKED')
    catalog_Artworks["Width"] = lt.newList('SINGLE_LINKED')
    catalog_Artworks["SeatHeight"] = lt.newList('SINGLE_LINKED')
    catalog_Artworks["Duration"] = lt.newList('SINGLE_LINKED')

    return catalog_Artworks

print(newCatalog_Artworks())


# Funciones para agregar informacion al catalogo

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento