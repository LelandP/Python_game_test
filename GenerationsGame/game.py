"""
Main game class, basically the engine of the game, contains all the helper and
pygame constructor logic, as well as the main game loop
"""
import time
import pygame
from GenerationsGame.const_manager import constants
from GenerationsGame.world import World

class GameMain():
    """
    The game class, contains the init logic and main game loop.
    """
    def __init__(self):
        """
        Initialises the game and the pygame classes.
        """
        #init pygame
        pygame.font.init()

        #setup window
        self.window_size = constants.get("WINDOW_X"), constants.get("WINDOW_Y")
        self.screen = pygame.display.set_mode(self.window_size)

        #define class vars
        self.last_frame = self._get_time()
        self.fps = 0
        self.fps_smoothing = constants.get("FPS_SMOOTHING")
        self.delta = 0
        self.running = True
        self.frame_counter = 0
        self.world = World()

        #statics
        self.simple_font = pygame.font.Font(None, 20)
        self.debug_surface = None

    def _parse_events(self):
        """
        Parses the game events, stupid class currently
        To-do: add callback class that can be registered by game objects.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT: self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: self.running = False

    def _get_time(self):
        """
        Get time using ns acuracy.
        :return: float, seconds since epoch in ns accuracy
        """
        return time.time_ns() / (10 ** 9)

    def _update_time(self):
        """
        Update the delta and FPS data.
        """
        new_time = self._get_time()
        self.delta = new_time - self.last_frame
        self.last_frame = new_time
        if self.delta > 0:
            self.fps = int((self.fps * self.fps_smoothing) + (1.0 / self.delta * (1.0-self.fps_smoothing)))

    def _display_debug(self):
        """
        Build the debug pannel so it can be displayed.
        Use the SHOW_DEBUG config to toggle this option.
        """
        if constants.get("SHOW_DEBUG"):
            if self.frame_counter % 100 == 0:
                surfaces = []
                #append font surfaces to the list
                surfaces.append(self.simple_font.render("FPS: " + str(self.fps), True, [255, 0, 0]))
                surfaces.append(self.simple_font.render("Frames: " + str(self.frame_counter), True, [255, 0, 0]))

                #calculate the width and height needed for the entire debug surface.
                width = height = 0
                for surface in surfaces:
                    height = height + surface.get_height()
                    width = max(width, surface.get_width())
                self.debug_surface = pygame.Surface((width, height))
                for i, surface in enumerate(surfaces):
                    self.debug_surface.blit(surface, (0,i*surface.get_height()))

            if self.debug_surface:
                self.screen.blit(self.debug_surface, (0,0))

    def run_game_loop(self):
        """
        The main game loop.
        """
        while self.running:
            self.screen.fill((0,0,0))
            self.frame_counter = self.frame_counter + 1
            #do gameloop stuff
            self._parse_events()
            self._update_time()
            self._display_debug()

            pygame.display.flip()


class Renderable:
    def __init__():
        self.id = 0


class Updatable:
    def __init__():
        self.id = 0
