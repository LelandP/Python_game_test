"""
Constants class, handles all constants and saves them to disk as a config file.
"""
#Consts with _ prefix will never save to disk
#Consts with no prefix will save to disk on first start
class Constants:
    """
    Constants class, this uses a class attribute to hold all the constants.
    """
    _consts = {
        #debug options
        "SHOW_DEBUG":True,
        "FPS_SMOOTHING": 0.9,

        #window options
        "WINDOW_X" : 700,
        "WINDOW_Y" : 600,

        #terrain options
        "DEFAULT_CHUNK_SIZE": 10,
        "INIT_CHUNKS": 2
    }

    def __init__(self):
        """
        Loads the constants and will overwrite using a config file. It will also
        ensure they are all upper case.
        """
        self._constants = {k.upper(): v for k, v in Constants._consts.items()}

    def get(self, name):
        """
        Get the value of a constant using the constant name. This method will take
        care of case for you.
        :return: the value of of the constant
        """
        if name.upper() in self._constants:
            return self._constants[name.upper()]

#global var, can be imported using a `from GenerationsGame.const_manager import constants`
constants = Constants()
