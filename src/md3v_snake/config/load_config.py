import ast

# Function to turn a python literal file into a
# dictionary of config values
def load( config_file ):
    with open(config_file, 'r') as f:
        config_dict = {}
        try:
            config_dict = ast.literal_eval( f.read() )
        except Exception as ex:
            print( ex )

    return config_dict