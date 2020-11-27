# flute
Some Python utilities to aid MIDI scripting in FL Studio

## Installation

### Windows

Clone this repository somewhere. Open an elevated command prompt.

Find your Image-Line install folder, typically `C:\Program Files\Image-Line`

Create a junction pointing to the flute module inside FL Studio's Python search
path:

```
mklink /J [Image-Line install folder]\Shared\Python\Lib\flute [path to the cloned repo]\src\flute
```

### macOS

I haven't tried this on macOS, but given the instructions from the FL Studio
documentation, it probably looks like this:

Clone this repository somewhere. Open your terminal.

Create a symlink pointing to the flute module inside FL Studio's Python search path:

```
sudo ln -s [path to the cloned repo]/src/flute /Library/Application\ Support/Image-Line/Shared/Python/Lib/flute
```
