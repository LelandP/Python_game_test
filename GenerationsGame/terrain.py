"""
Terrain module, for contruction of the terrain.
"""
import pygame

class Terrain():
    """
    Terrain class, creates and manages a large terrain structure using chunking
    as a way to ease the processing power.
    """
    def __init__(self, chunk_size, seed):
        """
        initialises the terrain class
        # TODO: Find a way to save this, i think the seed may be enough.
        :param chunk_size: the size of each chunk
        :param seed: the random seed used to create the world
        """
        self.chunk_size = chunk_size
        self.chunks = {}
        self.seed = seed

    def init_chunks(self, rect):
        """
        Initialize multiple chunks.
        :param rect: pygame rectangle xy and width and height of the chunks to load.
        """
        for x in range(int (rect.x - rect.w/2), int(rect.x + rect.w/2)):
            for y in range(int(rect.y - rect.h/2), int(rect.y + rect.h/2)):
                self.init_chunk((x,y))

    def init_chunk(self, pos):
        """
        Initialize a chunk.
        :param pos: x and y tuple of what chunk to load.
        """
        x = pos[0]
        y = pos[1]
        if not x in self.chunks:
            self.chunks[x] = {}

        if not y in self.chunks[x]:
            self.chunks[x][y] = Chunk(pos, self.chunk_size, self.seed)

class Chunk():
    """
    Chunk class, loads and handles the data associated with a chunk.
    """
    def __init__(self, pos, size, seed):
        """
        Sets all the data for a chunk.
        :param pos: position of the chunk
        :param size: size of the chunk
        :param seed: seed used to randomize the chunk
        """
        print("init Chunk: ", pos, size, seed)
