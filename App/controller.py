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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

def initCatalog():
    catalog = model.newCatalog()
    return catalog


# Funciones para la carga de datos

def LoadData(catalog):
    LoadArtists(catalog)
    LoadArtWorks(catalog)

def LoadArtists(catalog):
    Artistsfile = cf.data_dir + 'MoMA/Artists-utf8-small.csv'
    input_file = csv.DictReader(open(Artistsfile, encoding='utf-8'))
    for Artist in input_file:
        model.addArtist(catalog, Artist)

def LoadArtWorks(catalog):
    ArtWorksfile = cf.data_dir + 'MoMA/Artworks-utf8-small.csv'
    input_file = csv.DictReader(open(ArtWorksfile, encoding='utf-8'))
    for ArtWork in input_file:
        model.addArtWork(catalog, ArtWork)


# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo

def req1 (catalog, Año_inicial, Año_final):
    artist = model.requ1(catalog, Año_inicial, Año_final)
    return artist

def req2 (catalog, Fecha_inicial, Fecha_final):
    adquisi = model.requ2(catalog, Fecha_inicial, Fecha_final)
    return adquisi

def req3 (catalog, Artista_Nombre):
    info_Art = model.requ3(catalog, Artista_Nombre)
    return info_Art

def req4 (catalog, Obra_Museo):
    info_Museo = model.requ4(catalog, Obra_Museo)
    return info_Museo

def req5 (catalog, Dept_Museo):
    Dept_Museo = model.requ5(catalog, Dept_Museo)
    return Dept_Museo