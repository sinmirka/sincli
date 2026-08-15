from sincli.format.elements import Separators
from sincli.core.terminal import terminal_size

class Builder:
    def __init__(self):
        self.separators = Separators
        self.terminal_size = terminal_size

    def separator(self, type: Separators = Separators.default):
        separator_part = type.value
        print("\n")
        print(separator_part * (self.terminal_size.columns - 1))