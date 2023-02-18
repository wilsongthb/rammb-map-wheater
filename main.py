# https://rammb-slider.cira.colostate.edu/data/imagery/2023/02/18/goes-16---full_disk/eumetsat_ash/20230218011020/03/004_005.png
import requests
import uuid
from PIL import Image

env = {
    "rammb_url": "https://rammb-slider.cira.colostate.edu",
    "disk_path": "goes-16---full_disk",
    "asset_disk_path": "data/maps/goes-16/full_disk",
    "asset_location": "20171201010000"
}

inputs = {
    "year": "2023",
    "month": "02",
    "day": "18",
    "product": "eumetsat_ash",
    "instance": "20230218011020",
    "zoom": "03",
    "location": "005_004",
    "locationy": "005",
    "locationx": "004"
}

def mainProcess(inputs):
    mapaBase = obtenerMapaBase(inputs)
    mapaBase = insertarAsset(inputs, mapaBase, "cities")
    mapaBase = insertarAsset(inputs, mapaBase, "city_lights")
    mapaBase = insertarAsset(inputs, mapaBase, "borders")
    mapaBase = insertarAsset(inputs, mapaBase, "countries")
    guardarMapa(mapaBase)
    pass

def formatMapImageUrl(inputs):
    base_url = env['rammb_url']
    year = inputs['year']
    month = inputs['month']
    day = inputs['day']
    disk_path = env['disk_path']
    product = inputs['product']
    instance = inputs['instance']
    zoom = inputs['zoom']
    location = inputs['location']
    return f'{base_url}/data/imagery/{year}/{month}/{day}/{disk_path}/{product}/{instance}/{zoom}/{location}.png'

def obtenerMapaBase(inputs):
    mapTempPath = generateMapRandomPath()
    guardarImagenDeUrl(formatMapImageUrl(inputs), mapTempPath)
    return Image.open(mapTempPath)

def guardarImagenDeUrl(url, path):
    res = requests.get(url, stream=True)
    if res.status_code == 200:
        with open(path, 'wb') as f:
            for chunk in res:
                f.write(chunk)

def insertarAsset(inputs, mapaImagen, asset, color="red"):
    # https://rammb-slider.cira.colostate.edu/data/maps/goes-16/full_disk/borders/red/20171201010000/03/005_004.png
    assetUrl = env['rammb_url'] + '/' + env['asset_disk_path'] + f'/{asset}/{color}/' + env['asset_location'] + '/' + inputs['zoom'] + '/' +  inputs['location'] + '.png'
    pathAsset = f"data/assets/{asset}/" + inputs['location'] + '.png'
    guardarImagenDeUrl(assetUrl, pathAsset)
    assetImagen = Image.open(pathAsset)
    mapaImagen.paste(assetImagen, (0,0), assetImagen)
    return mapaImagen

def guardarMapa(mapaImagen):
    mapaImagen.save('outputs/' + inputs['instance'] + '_' + inputs['location'] + '.png')

def generateMapRandomPath():
    return "data/temp_locations/" + str(uuid.uuid4()) + ".png"

mainProcess(inputs)