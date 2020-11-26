# flute
Some Python utilities to aid MIDI scripting in FL Studio

## Installation

### Windows

Clone this repository somewhere. Open an elevated command prompt.

Find your Image-Line install folder, typically C:\Program Files\Image-Line

Create a junction pointing to the flute module inside FL Studio's Python search path:

```
mklink /J [Image-Line install folder]\Shared\Python\Lib\flute [path to the cloned repo]\src\flute
```
