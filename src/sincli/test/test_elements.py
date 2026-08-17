from sincli.core.builder import Builder
from sincli.format.formatter import Formatter

builder = Builder()
f = Formatter()

logo = f.format_string("DISPARSE")

builder.separator(type=builder.separators.bold)
print(f.gradient_string(logo, preset='doppler'))
builder.separator(type=builder.separators.bold)