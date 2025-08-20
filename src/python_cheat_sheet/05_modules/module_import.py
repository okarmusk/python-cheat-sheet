import fib

print(fib.fibonacci(128))

from fib import fibonacci

print(fibonacci(1024))

# Packaging
# sound/                          Top-level package
#       __init__.py               Initialize the sound package
#       formats/                  Subpackage for file format conversions
#               __init__.py
#               wavread.py
#               wavwrite.py
#               aiffread.py
#               aiffwrite.py
#               auread.py
#               auwrite.py
#               ...
#       effects/                  Subpackage for sound effects
#               __init__.py
#               echo.py
#               surround.py
#               reverse.py
#               ...
#       filters/                  Subpackage for filters
#               __init__.py
#               equalizer.py
#               vocoder.py
#               karaoke.py

# Note:
# The __init__.py files are required to make Python treat directories containing the file as packages (unless using a namespace package,
# a relatively advanced feature). This prevents directories with a common name, such as string,
# from unintentionally hiding valid modules that occur later on the module search path.
# In the simplest case, __init__.py can just be an empty file, but it can also execute initialization code for
# the package or set the __all__ variable, described later.

# Imports based on dir structure
# import sound.effects.echo
# import sound.effects.surround
# from sound.effects import *
