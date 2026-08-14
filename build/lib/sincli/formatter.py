from pyfiglet import Figlet


class Formatter:
    def __init__(self):
        self.default_font = "ansi_shadow"

    def _reset_color(self):
        """Sets all future outputs color to default."""
        print("\033[39m", end="")

    def _line_gradient(self, line: str, start_color: tuple, end_color: tuple) -> str:
        """Returns a gradient variant of string. Only one line supported."""
        result = ""
        for i, char in enumerate(line):
            t = i / max(len(line) - 1, 1)
            r = int(start_color[0] * (1 - t) + end_color[0] * t)
            g = int(start_color[1] * (1 - t) + end_color[1] * t)
            b = int(start_color[2] * (1 - t) + end_color[2] * t)
            result += f"\033[38;2;{r};{g};{b}m{char}"
        return result

    def format_string(self, string: str, font: str | None = None) -> str:
        """Returns a formatted string."""
        if font is None:
            font = self.default_font
        figlet = Figlet(font=font)
        return figlet.renderText(string)

    def gradient_string(self, string: str, start_color: tuple, end_color: tuple):
        """Returns a gradient variant of string. Supports multiple lines."""
        lines = string.strip().split("\n")
        result = []
        for line in lines:
            result.append(self._line_gradient(line=line, start_color=start_color, end_color=end_color))

        return "\n".join(result)