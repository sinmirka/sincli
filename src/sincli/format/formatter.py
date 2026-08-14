from pyfiglet import Figlet, FigletFont
from sincli.format.presets import presets, DEFAULT_FONT


class Formatter:
    def __init__(self):
        self.default_font = DEFAULT_FONT
        self.presets = presets

    def _reset_color(self):
        """Sets all future outputs color to default."""
        print("\033[39m", end="")

    def _line_gradient(
        self,
        line: str,
        start_color: tuple[int, int, int],
        end_color: tuple[int, int, int]
    ) -> str:
        """Returns a gradient variant of string. Only one line supported."""
        result = ""

        for i, char in enumerate(line):
            t = i / max(len(line) - 1, 1)
            r = int(start_color[0] * (1 - t) + end_color[0] * t)
            g = int(start_color[1] * (1 - t) + end_color[1] * t)
            b = int(start_color[2] * (1 - t) + end_color[2] * t)
            result += f"\033[38;2;{r};{g};{b}m{char}"
        return result


    def get_fonts(self, normalize: bool = False):
        """Returns list of FIGlet fonts by default. Use 'normalize' parameter to remove brackets."""
        fonts = FigletFont.getFonts()

        if normalize:
            return ", ".join(fonts)
        return fonts
    
    def format_string(
        self,
        string: str,
        font: str | None = None
    ) -> str:
        """Returns a string rendered using the specified FIGlet font."""
        if font is None:
            font = self.default_font
        figlet = Figlet(font=font)
        return figlet.renderText(string)
    
    def gradient_string(
        self,
        string: str,
        start_color: tuple[int, int, int] = None,
        end_color: tuple[int, int, int] = None,
        preset: str = None,
        reset_after: bool = True,
    ) -> str:
        """Returns a gradient variant of string. Supports multiple lines. Supports presets of RGB gradients."""
        lines = string.strip().split("\n")
        result = []

        if preset: 
            gradient = self.presets.get(preset)
            if gradient is None:
                raise ValueError("Invalid gradient preset")
            
            start_color = gradient.get("start_color")
            end_color = gradient.get("end_color")

        for line in lines:
            result.append(
                self._line_gradient(
                    line=line, start_color=start_color, end_color=end_color
                )
            )

        return "\n".join(result) + ("\033[39m" if reset_after else "") # resets color

    def test_presets(self):
        for i, preset in enumerate(self.presets):
            gradient = self.presets.get(preset)
            start_color = gradient.get("start_color")
            end_color = gradient.get("end_color")
            print(f"{i + 1}. Preset: {preset}")
            print(self.gradient_string(string="Hello, World! This is a", start_color=start_color, end_color=end_color))
            print(
                self.gradient_string(
                    string=self.format_string(
                        "TEST"
                    ),
                    start_color=start_color,
                    end_color=end_color,
                )
            )
            print()