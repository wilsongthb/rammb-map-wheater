from PIL import Image

background = Image.open("data/005_004.png")

countries = Image.open("data/countries-005_004.png")
# cities11 = Image.open("data/cities-010_008.png")
# cities12 = Image.open("data/cities-010_009.png")
# cities21 = Image.open("data/cities-011_008.png")
# cities22 = Image.open("data/cities-011_009.png")
borders11 = Image.open("data/borders-010_008.png")
borders12 = Image.open("data/borders-010_009.png")
borders21 = Image.open("data/borders-011_008.png")
borders22 = Image.open("data/borders-011_009.png")
city_lights = Image.open("data/city_lights-005_004.png")


# background.show()



currentw, currenth = background.size
newsize = (currentw*2,currenth*2)
background = background.resize(newsize)


# background.paste(countries, (0, 0), countries)
# background.paste(cities, (0, 0), cities)
zoom4sizew, zoom4sizeh = borders11.size

background.paste(borders11, (0, 0), borders11)
background.paste(borders12, (zoom4sizew, 0), borders12)
background.paste(borders21, (0, zoom4sizeh), borders21)
background.paste(borders22, (zoom4sizew, zoom4sizeh), borders22)
# background.paste(city_lights, (0, 0), city_lights)

background.save("data/output01.png")

