from configparser import ConfigParser

#child
def read_configuration(category, key):
    config = ConfigParser()
    config.read("ChildFrameworkMain/configurations/config.ini")
    return config.get(category, key)