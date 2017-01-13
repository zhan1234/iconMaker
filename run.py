#coding=utf-8
__author__ = 'zhanxianbo'
import PIL.Image
import os
import ConfigParser

class MyConfigParser(ConfigParser.ConfigParser):  
    def __init__(self,defaults=None):  
        ConfigParser.ConfigParser.__init__(self,defaults=None)  
    def optionxform(self, optionstr):  
        return optionstr

def make_icon():
    im = PIL.Image.open("512.png")
    if os.path.isfile("512X512.png"):
        im2 = PIL.Image.open("512X512.png")
        im.paste(im2,(0,0),mask = im2)
    im.save("512Icon.png")
    config = MyConfigParser()
    config.read("config.ini")
    imgNames = config.items("iconSize")

    for value in imgNames:
        imt = im
        size = (int(value[1]),int(value[1]))
        name = value[0]
        imt_r = imt.resize(size,PIL.Image.ANTIALIAS)
        imt_r.save(name)

make_icon()