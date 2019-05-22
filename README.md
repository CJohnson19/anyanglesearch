# Any Angle Search

## Usage


### Quick Start

Run grid_translate.py and input a grid file. Then select which algorithm you'd like to run on the grid.

### Custom Grids
You may create a grid to translate by gridtranslate by writing it in a text file beforehand.

An example 2x2 grid with the top left blocked is:

```
1 1 0
1 1 0
0 0 0
```

Give this file to the grid_translate.py and select the algorithm. A visual representation will appear and 

#### Vertex values

| Char | Meaning |
|------|---------|
| 0 | Passable |
| 1 | Blocked |
| S | Start Position |
| G | Goal Position |

### Random Grids

Grids can be generated with a given sparcity with grid_random.py.


## Algorithms Implemented

 * Dijkstra's
 * Uniform Cost Search
 * A*
 * Theta*
 * Lazy Theta*
 * Basic Link*


## Purpose

This repo was created for a class in AI to compare the effectiveness on different search algorithms in realtime computing environments. See the paper with the repo to see the results.
