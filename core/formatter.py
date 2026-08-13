from pyfiglet import Figlet
from configparser import ConfigParser

config = ConfigParser()
config.read("config.ini")

DEFAULT_FONT = config['appearance']['default_font']

def format_string(string: str, font: str = DEFAULT_FONT) -> str:
    """Returns a formatted string."""
    figlet = Figlet(font=font)
    return figlet.renderText(string)

def _line_gradient(line: str, start_color: tuple, end_color: tuple) -> str:
    result = ""
    for i, char in enumerate(line):
        t = i / max(len(line) - 1, 1)
        r = int(start_color[0] * (1 - t) + end_color[0] * t)
        g = int(start_color[1] * (1 - t) + end_color[1] * t)
        b = int(start_color[2] * (1 - t) + end_color[2] * t)
        result += f"\033[38;2;{r};{g};{b}m{char}"
    return result

def gradient_string(string, start_color, end_color):
    """Returns a gradient variant of string. Supports multiple lines."""
    lines = string.strip().split("\n")
    result = []
    for line in lines:
        result.append(_line_gradient(line=line, start_color=start_color, end_color=end_color))

    return "\n".join(result)