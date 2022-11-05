# Field Fire
Simulates a field of plants growing as fire randomly ignites and spreads across. Starting from an empty field, plants will 
randomly grow depending on the set growth probability. Cells that become plants will have a life 
span of 500 frames (or generations) before dying out, if not consumed by fire first. Fire will 
randomly start on plant cells depending on the set ignition probability. This fire will then spread 
to neighboring plant cells at a 50% probability. The fire quickly burns out and resets the plant 
cells it interacts with back to ground, allowing for new plant cells to grow.

## Usage
Made with Python 3.7 and appropriate Pygame module. Download FieldFire.py and run with Python, make sure Pygame is installed as well.

## Parameters
```
size - the size of each cell (default 8)
fps - the frame rate limit (default 30)
burnChance - the burn probability (default 0.00001)
growChance - the growth probability (default 0.01)
```

## Cellular Automata
![Field fire cellular automata running](running.gif?raw=true)
