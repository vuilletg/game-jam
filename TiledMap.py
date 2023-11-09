#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Romain
#
# Created:     09/11/2023
# Copyright:   (c) Romain 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import pytmx
import pygame

class TiledMap:
    def __init__(self,filename):
        tm = pytmx.load_pygame(filename, pixelalpha=True)
        self.width=tm.width * tm.tilewidth
        self.height=tm.height*tm.tileheight
        self.tmxdata=tm

    def scroll(self,surface,scroll):
        ti = self.tmxdata.get_tile_image_by_gid
        for layer in self.tmxdata.visible_layers:
            if isinstance(layer,pytmx.TiledTileLayer):
                for x,y,gid, in layer:
                    tile=ti(gid)
                    if tile:
                        if (x*self.tmxdata.tilewidth+scroll)>0:
                            surface.blit(tile, (x*self.tmxdata.tilewidth+scroll, y*self.tmxdata.tileheight))
