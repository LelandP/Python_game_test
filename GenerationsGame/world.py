"""
World module, contains everything for the game world.
"""
from GenerationsGame.terrain import Terrain
from GenerationsGame.const_manager import constants
import pygame



class World():
    """
    Main world class, should have everything needed to serialize a save file.
    """
    def __init__(self):
        """
        Initialises the world.
        """
        self.chunk_size = constants.get("DEFAULT_CHUNK_SIZE")
        init_chunk = constants.get("INIT_CHUNKS")

        self.seed = 0

        self.terrain = Terrain(self.chunk_size, self.seed)
        self.terrain.init_chunks(pygame.Rect((0,0),(init_chunk,init_chunk)))
