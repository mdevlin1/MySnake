
import argparse
from md3v_snake.controller.snake import Snake

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument( 'config_file', type=str, help='Configuration file for the snake game')
    args = parser.parse_args()
    
    driver = Snake( args.config_file )
    driver.run()