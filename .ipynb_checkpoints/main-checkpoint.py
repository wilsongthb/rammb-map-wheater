from PIL import Image

background = Image.open("data/005_004.png")

countries = Image.open("data/countries-005_004.png")
cities = Image.open("data/cities-005_004.png")
borders = Image.open("data/borders-005_004.png")
city_lights = Image.open("data/city_lights-005_004.png")

background.paste(countries, (0, 0), countries)
background.paste(cities, (0, 0), cities)
background.paste(borders, (0, 0), borders)
background.paste(city_lights, (0, 0), city_lights)
# background.show()

size1 = (64,64)

background.resize(size1)
background.save("data/output01.png")