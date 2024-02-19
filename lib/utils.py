import yaml
def read_config(file_path):
    with open(file_path, 'r') as stream:
        config = yaml.load(stream, Loader=yaml.FullLoader)
        return config
