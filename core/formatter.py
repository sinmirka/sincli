from pyfiglet import Figlet
from configparser import ConfigParser

config = ConfigParser()
config.read("config.ini")

DEFAULT_FONT = config['appearance']['default_font']

def format_string(string: str, font=DEFAULT_FONT):
    figlet = Figlet(font=font)
    return figlet.renderText(string)


print(format_string("test"))