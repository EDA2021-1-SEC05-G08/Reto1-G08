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


from sys import call_tracing
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""
#Funciones Adicionales

def convertirFecha(fecha):
    fecha = fecha.split("-")
    año = fecha[0]
    mes = fecha[1]
    dia = fecha[2]
    if dia[0] == "0":
        dia = dia[1:]
    if mes[0] == "0":
        mes = mes[1:]
    fecha = datetime.datetime(int(año), int(mes), int(dia))
    return fecha
def quitarcorcheas(constitude):
    constitude = constitude.split("[")
    constitude = constitude.split("]")
    constitude = int(constitude)
    return constitude

# Construccion de modelos

def newCatalog():
    catalog = {
        'Artists': None,
        'ArtWorks': None
    }

    catalog['Artists'] = lt.newList('ARRAY_LIST')
    catalog['ArtWorks'] = lt.newList('ARRAY_LIST')
    """
    Inicializa el catálogo de obras de arte. Crea una lista vacia para guardar
    todas las obras, adicionalmente, crea una lista vacia para los artistas.
    Retorna el catalogo inicializado.
    """        
    return catalog
# Funciones para agregar informacion al catalogo

def addArtWork(catalog, ArtWork):
    # Se adiciona la obra a la lista de obras
    lt.addLast(catalog['ArtWorks'], ArtWork)
    # Se obtienen los autores de la obra


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


def addArtist(catalog, Artista):
    lt.addLast(catalog["Artists"], Artista)


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
def comparteYear(author1, author2):
    return (author1["BeginDate"] < author2["BeginDate"])

def compareDate(artwork1, artwork2):
    return(convertirFecha(artwork1["DateAcquired"]) < convertirFecha(artwork2["DateAcquired"]))

def comparateConstituteID(constitudeID1, constitudeID2):
    return(quitarcorcheas(constitudeID1["ConstituentID"]) < quitarcorcheas(constitudeID2["ConstituentID"]))


# Funciones de consulta
def requ1(catalog, Año_inicial, Año_final):
    authors = lt.subList(catalog["Artists"], 1, lt.size(catalog["Artists"]))
    authors = sa.sort(authors, comparteYear)
    authorsRange = lt.newList()
    for i in range(1, lt.size(authors)+1):
        author = lt.getElement(authors, i)
        if int(author["BeginDate"]) >= Año_inicial and int(author["BeginDate"]) <= Año_final:
            lt.addLast(authorsRange, author)
    output = "\n\n------------------Req No. 1 Inputs------------------\nArtists born between {} and {}\n\n------------------Req No. 1 Answer------------------\nThere are {} artits born between {} and {}\n\nThe first and last 3 artists in range are...\nConstituentID\tDisplatName\tBeginDate\tNationality\tGender\tArtistBio\tWikiQID\tULAN\n{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}"
    output = output.format(Año_inicial, Año_final, lt.size(authorsRange), Año_inicial, Año_final,
            lt.getElement(authorsRange,1)["ConstituentID"], lt.getElement(authorsRange,1)["DisplayName"], lt.getElement(authorsRange,1)["BeginDate"], lt.getElement(authorsRange,1)["Nationality"], lt.getElement(authorsRange,1)["Gender"], lt.getElement(authorsRange,1)["ArtistBio"], lt.getElement(authorsRange,1)["Wiki QID"], lt.getElement(authorsRange,1)["ULAN"],
            lt.getElement(authorsRange,2)["ConstituentID"], lt.getElement(authorsRange,2)["DisplayName"], lt.getElement(authorsRange,2)["BeginDate"], lt.getElement(authorsRange,2)["Nationality"], lt.getElement(authorsRange,2)["Gender"], lt.getElement(authorsRange,2)["ArtistBio"], lt.getElement(authorsRange,2)["Wiki QID"], lt.getElement(authorsRange,2)["ULAN"],
            lt.getElement(authorsRange,3)["ConstituentID"], lt.getElement(authorsRange,3)["DisplayName"], lt.getElement(authorsRange,3)["BeginDate"], lt.getElement(authorsRange,3)["Nationality"], lt.getElement(authorsRange,3)["Gender"], lt.getElement(authorsRange,3)["ArtistBio"], lt.getElement(authorsRange,3)["Wiki QID"], lt.getElement(authorsRange,3)["ULAN"],
            lt.getElement(authorsRange,lt.size(authorsRange)-2)["ConstituentID"], lt.getElement(authorsRange,lt.size(authorsRange)-2)["DisplayName"], lt.getElement(authorsRange,lt.size(authorsRange)-2)["BeginDate"], lt.getElement(authorsRange,lt.size(authorsRange)-2)["Nationality"], lt.getElement(authorsRange,lt.size(authorsRange)-2)["Gender"], lt.getElement(authorsRange,lt.size(authorsRange)-2)["ArtistBio"], lt.getElement(authorsRange,lt.size(authorsRange)-2)["Wiki QID"], lt.getElement(authorsRange,lt.size(authorsRange)-2)["ULAN"], 
            lt.getElement(authorsRange,lt.size(authorsRange)-1)["ConstituentID"], lt.getElement(authorsRange,lt.size(authorsRange)-1)["DisplayName"], lt.getElement(authorsRange,lt.size(authorsRange)-1)["BeginDate"], lt.getElement(authorsRange,lt.size(authorsRange)-1)["Nationality"], lt.getElement(authorsRange,lt.size(authorsRange)-1)["Gender"], lt.getElement(authorsRange,lt.size(authorsRange)-1)["ArtistBio"], lt.getElement(authorsRange,lt.size(authorsRange)-1)["Wiki QID"], lt.getElement(authorsRange,lt.size(authorsRange)-1)["ULAN"],
            lt.getElement(authorsRange,lt.size(authorsRange))["ConstituentID"], lt.getElement(authorsRange,lt.size(authorsRange))["DisplayName"], lt.getElement(authorsRange,lt.size(authorsRange))["BeginDate"], lt.getElement(authorsRange,lt.size(authorsRange))["Nationality"], lt.getElement(authorsRange,lt.size(authorsRange))["Gender"], lt.getElement(authorsRange,lt.size(authorsRange))["ArtistBio"], lt.getElement(authorsRange,lt.size(authorsRange))["Wiki QID"], lt.getElement(authorsRange,lt.size(authorsRange))["ULAN"])

    return output

def requ2(catalog, Fecha_inicial, Fecha_final):
    artworks = lt.subList(catalog["ArtWorks"], 1, lt.size(catalog["ArtWorks"]))
    artworksOut = lt.newList()
    for i in range(1, lt.size(artworks)+1):
        if len(lt.getElement(artworks, i)["DateAcquired"]) != 0:
            lt.addLast(artworksOut, lt.getElement(artworks, i))
    artworks = sa.sort(artworksOut, compareDate)
    artworksRange = lt.newList()
    Fecha_inicial = convertirFecha(Fecha_inicial)
    Fecha_final = convertirFecha(Fecha_final)
    for i in range(1, lt.size(artworks)+1):
        if len(lt.getElement(artworks, i)["DateAcquired"]) != 0 :
            fecha = convertirFecha(lt.getElement(artworks, i)["DateAcquired"])
            if fecha >= Fecha_inicial and fecha <= Fecha_final:
                lt.addLast(artworksRange, lt.getElement(artworks, i))

    return artworksRange

def requ3(catalog, Nombre_Artista):
    totalobras = 0
    totaltecnicas = 0
    listaobras = lt.newList()
    obras = lt.subList(catalog["ArtWorks"], 1, lt.size(catalog["ArtWorks"]))
    artista = lt.subList(catalog["Artists"]), 1, lt.size(catalog["Artists"])
    artista = sa.sort(artista, comparateConstituteID)
    obras = sa.sort(obras, comparateConstituteID)
    final = lt.newList()
    for i in range(1, lt.size(artista)+1):
        if lt.isPresent(Nombre_Artista) > 0:
            Id = lt.getElement(artista["ConstituentID"])
            for j in range(1, lt.size(obras)+1):
                obra = lt.getElement(obras["ConstituentID"], j)
                if obra == Id:
                    lt.addLast(final, obras)
                    totalobras += 1
                    totaltecnicas += 1
    return final

#def requ4(catalog, obra_museo):



# def reque4(catalog, )