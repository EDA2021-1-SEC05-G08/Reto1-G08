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

    catalog['Artists'] = lt.newList('SINGLE_LINKED')
    catalog['ArtWorks'] = lt.newList('SINGLE_LINKED')
    """
    Inicializa el catálogo de obras de arte. Crea una lista vacia para guardar
    todas las obras, adicionalmente, crea una lista vacia para los artistas.
    Retorna el catalogo inicializado.
    """        
# Funciones para agregar informacion al catalogo

def addArtWork(catalog, ArtWork):
    # Se adiciona la obra a la lista de obras
    lt.addLast(catalog['ArtWorks'], ArtWork)
    # Se obtienen los autores de la obra
    artists = ArtWork['Artists'].split(",")
    # Cada artista, se crea en la lista de obras de arte del catalogo, y se
    # crea un libro en la lista de dicho artista
    for artist in artists:
        addArtWorkArtist(catalog, artist.strip(), ArtWork)

def addArtWorkArtist(catalog, artistname, ArtWork):
    """
    Adiciona un artista a lista de artistas, la cual guarda referencias
    a las obras de arte de dicho artista
    """
    artists = catalog['Artist']
    posartist = lt.isPresent(artists, artistname)
    if posartist > 0:
        artist = lt.getElement(artists, posartist)
    else:
        artist = newArtist(artistname)
        lt.addLast(artists, artist)
    lt.addLast(artist['ArtWorks'], ArtWork)


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

def newArtist(name):
    """
    Crea una nueva estructura para modelar las obras de
    un artista
    """

    artist = {"name": "", "ArtWorks": None}
    artist["name"] = name
    artist["ArtWorks"] = lt.newList("ARRAY_LIST")
    return artist

def newArtWork(ObjectID, Title, ConstituentID, Date, Medium, Dimensions, CreditLine, AccesionNumber, Classification, Department, DateAcquired, Catalogued, URL, Circumference, Depth, Diameter, Height, Length, Weight, Width, SeatHeight, Duration):

    ArtWork = {"ObjectID": "", "Title": "", "ConstituentID": "", "Date": "", "Medium": "", "Dimensions": "", "CreditLine": "", "AccesionNumber": "", "Classification": "", "Department": "", "DateAcquired": "", "Catalogued": "", "URL": "", "Circumference": "", "Depth": "", "Diameter": "", "Height": "", "Length": "", "Weight": "", "Width": "", "SeatHeight": "", "Duration": ""}
    ArtWork["ObjectID"] = ObjectID
    ArtWork["Title"] = Title
    ArtWork["ConstituentID"] = ConstituentID
    ArtWork["Date"] = Date
    ArtWork["Medium"] = Medium
    ArtWork["Dimensions"] = Dimensions
    ArtWork["CreditLine"] = CreditLine
    ArtWork["AccesionNumber"] = AccesionNumber
    ArtWork["Classification"] = Classification
    ArtWork["Department"] = Department
    ArtWork["DateAcquired"] = DateAcquired
    ArtWork["Catalogued"] = Catalogued
    ArtWork["URL"] = URL
    ArtWork["Circumference"] = Circumference
    ArtWork["Depth"] = Depth
    ArtWork["Diameter"] = Diameter
    ArtWork["Height"] = Height
    ArtWork["Length"] = Length
    ArtWork["Weight"] = Weight
    ArtWork["Width"] = Width
    ArtWork["SeatHeight"] = SeatHeight
    ArtWork["Duration"] = Duration

# Funciones de consulta

def requ1(catalog, Año_inicial, Año_final):
    artist = {}
    suma = 0
    catalog["Artists"]["BeginDate"] = int(catalog["Artists"]["BeginDate"])
    catalog["Artists"]["EndDate"] = int(catalog["Artists"]["EndDate"])
    for elem in catalog:
        if Año_inicial >= elem["BeginDate"] and Año_final <= elem["EndDate"]:
            artist["Nombre"] = elem["DisplayName"] 
            artist["Año de inicio"] = elem["BeginDate"]
            artist["Año final"] = elem["EndDate"]
            artist["Nacionalidad"] = elem["Nationality"]
            artist["Genero"] = elem["Gender"]
            suma += 1
    total = str("Total de artistas", suma)
    return (artist, total)

def requ2(catalog, Fecha_inicial, Fecha_final):
    adquisi={}
    suma = 0
    catalog["ArtWorks"]["DateAcquired"]= str(catalog["ArtWorks"]["DateAcquired"])
    for elem in catalog["ArtWorks"]:
        if elem["DateAcquired"] >= Fecha_inicial and elem["DateAcquired"] <= Fecha_final:
            adquisi["Titulo"] = elem["Title"]
            adquisi["Fecha"] = elem["Date"]
            adquisi["Medio"] = elem["Classification"]
            adquisi["Dimensiones"] = elem["Dimensions"]
            if elem["CreditLine"] == "Purchase":
                suma += 1
    adquisi["Total"] = suma
    return adquisi

def requ3(catalog, Artista):
    Artist = {}
    sumaObras = 0
    sumaTecnicas = 0
    for elem in catalog["ArtWorks"]:
        

def reque4(catalog, )

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento