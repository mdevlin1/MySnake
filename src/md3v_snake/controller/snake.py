
from md3v_snake.view.start_up_menu import StartupMenu
from md3v_snake.config.load_config import load as conf_load

class Snake:
    def __init__( self, config_file ):
        self.config = conf_load( config_file )
            
        self.start_up_menu = StartupMenu( self.config )

    def run( self ):    
        self.start_up_menu.Start()