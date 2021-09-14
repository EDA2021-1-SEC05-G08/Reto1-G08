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

def newCatalog():
    catalog = {
        'Artists': None,
        'ArtWorks': None
    }

    catalog['Artist'] = lt.newList('SINGLE_LINKED')
    catalog['ArtWorks'] = lt.newList('SINGLE_LINKED')
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
               

# Funciones para agregar informacion al catalogo

def addArtists(catalog, Artists):
    # Se adiciona el libro a la lista de libros
    lt.addLast(catalog['Artists'], Artists)
    # Se obtienen los autores del libro
    Artist = Artists['Display Name'].split(",")
    # Cada autor, se crea en la lista de libros del catalogo, y se
    # crea un libro en la lista de dicho autor (apuntador al libro)
    for author in Artist:
        addArtist(catalog, author.strip(), Artists)

def addArtist(catalog, DisplayName, Artists):

    Artist = catalog['Display Name']
    postArtist = lt.isPresent(Artist, DisplayName)
    if postArtist > 0:
        Artista = lt.getElement(Artist, postArtist)
    else:
        Artista = newArtist(DisplayName)
        lt.addLast(Artist, Artista)
    lt.addLast(Artista['Artist'], catalog)

def AddArtWorks(catalog, Artwork):
    Work = newArtWork(Artwork['ObjectID'],Artwork['Title'],Artwork['ConstituentID'],Artwork['Date'],Artwork['Medium'],Artwork['Dimensions'],Artwork['CreditLine'],Artwork['AccesionNumber'],Artwork['Classification'],Artwork['Department'],Artwork['DateAcquired'],Artwork['Catalogued'],Artwork['URL'],Artwork['Circumference (cm)'],Artwork['Depth (cm)'],Artwork['Diameter (cm)'],Artwork['Height (cm)'],Artwork['Length (cm)'],Artwork['Weight (kg)'],Artwork['Width (cm)'],Artwork['Seat Height (cm)'],Artwork['Duration (sec.)'])
    lt.addLast(catalog['ArtWorks'], Work)
# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento