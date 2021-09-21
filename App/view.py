"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Req.1 listar cronológicamente los artistas")
    print("3- Req.2 listar cronológicamente las adquisiciones")



def initCatalog():
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalog()


def loadData(catalog):
    """
    Carga los libros en la estructura de datos
    """
    return controller.LoadData(catalog)

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = initCatalog()
        loadData(catalog)
        print(lt.size(catalog["Artists"]))
        print(lt.size(catalog["ArtWorks"])) 
        print(catalog["ArtWorks"])

    elif int(inputs[0]) == 2:
        Año_inicial = int(input("Año Inicial(YYYY)" ))
        Año_final = int(input("Año Final(YYYY)" ))
        Año = controller.req1(catalog, Año_inicial, Año_final)
        print(Año)

    elif int(inputs[0]) == 3:
        Fecha_inicial = str(input("Fecha inicial (AAAA-MM-DD): "))
        Fecha_final = str(input("Fecha final (AAAA-MM-DD):"))
        fecha = controller.req2(catalog, Fecha_inicial, Fecha_final)
        print(fecha)

    elif int(inputs[0]) == 4:
        Artista_Nombre = str(input("Nombre de artista: "))
        info = controller.req3(catalog, Artista_Nombre)
        print(info)
    
    elif int(inputs[0]) == 5:
        Obra_Museo = str(input("Obra del museo: "))
        info = controller.req4(catalog, Obra_Museo)
        print(info)

    else:
        sys.exit(0)
sys.exit(0)
