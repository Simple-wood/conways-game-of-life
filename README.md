# Conway's Game of Life

A Python implementation of Conway's Game of Life using Pygame, featuring an interactive grid where you can create patterns and watch them evolve according to cellular automaton rules.

## Overview

Conway's Game of Life is a zero-player game that evolves based on its initial state. Each cell on a grid can be either alive or dead, and the state of cells changes each generation based on the number of alive neighbors they have.

### Game Rules
- A live cell with fewer than 2 neighbors dies (underpopulation)
- A live cell with 2-3 neighbors survives
- A live cell with more than 3 neighbors dies (overpopulation)
- A dead cell with exactly 3 alive neighbors becomes alive (reproduction)

## Features

- **Interactive Grid**: Click to place cells (creation mode) or remove them with right-click
- **Two Modes**: 
  - **Creation Mode** (Red indicator): Place and remove cells manually
  - **Simulation Mode** (Green indicator): Watch the pattern evolve
- **Camera Controls**: Pan around the infinite grid
- **Zoom Levels**: 6 different zoom levels for detailed or wide views
- **Speed Control**: Adjust simulation speed from 1 to 30 updates per render frame
- **Generation Tracking**: Monitor current population and generation count

## File Structure

- **main.py**: Entry point; initializes pygame and runs the main game loop
- **Display.py**: Contains `Display` (base window management) and `Simulation` (handles events and game logic)
- **Map.py**: Manages the grid of cells and applies Conway's rules each generation
- **Cell.py**: Represents individual cells with position, size, and alive state
- **utils.py**: Contains `StatusSymbol` class for the mode indicator
- **requirements.txt**: Project dependencies

## Requirements

- Python 3.x
- Pygame

## Installation

1. Clone or download this project
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## How to Run

```bash
python main.py
```

The game window will open showing an empty grid in creation mode (red indicator).

## Controls

### Camera Movement
- **A / D**: Continuous panning left/right
- **W / S**: Continuous panning up/down
- **Arrow Keys**: Single-step camera adjustments

### Cell Placement (Creation Mode)
- **Left Click**: Place a live cell
- **Right Click**: Remove a cell

### Zoom
- **Mouse Wheel Up**: Zoom in (larger cells)
- **Mouse Wheel Down**: Zoom out (smaller cells)

### Simulation
- **SPACE**: Toggle between creation mode (red) and simulation mode (green)
- **Comma (,)**: Decrease simulation speed
- **Period (.)**: Increase simulation speed

## Configuration

Edit these settings in `main.py` to customize the game:

```python
SCREEN_DIMENSIONS = (640, 480)  # Window size
CELL_SIZES = (16, 20, 32, 40, 80, 160)  # Available zoom levels
CURRENT_ZOOM = 2  # Starting zoom level
SPEEDS = (1, 2, 3, 5, 6, 10, 15, 30)  # Available simulation speeds
CURRENT_SPEED = 5  # Starting speed
FRAME_RATE = 30  # Display refresh rate
```

## Class Architecture

### Cell
Represents a single cell in the grid with position, size, and alive state.
- `check_neighbours()`: Counts alive neighbors
- `update_cell()`: Applies Conway's rules
- `draw_cell()`: Renders the cell

### Map
Manages the entire grid and simulation updates.
- `add_cell()` / `remove_cell()`: Modify grid
- `update_cells()`: Apply one generation of rules
- `to_grid_coordinates()`: Convert screen pixels to grid positions

### Display / Simulation
Handles rendering and user input.
- `handle_events()`: Process keyboard and mouse input
- `update_offset_directions()`: Handle camera panning

### StatusSymbol
Visual indicator showing current game mode.
- Red: Creation mode
- Green: Simulation mode

## Tips for Interesting Patterns

- **Gliders**: Small patterns that move across the grid
- **Blinkers**: Simple oscillators that alternate states
- **Still Life**: Stable patterns that don't change
- **Gosper Glider Gun**: Complex pattern that generates gliders

Try searching for "Conway's Game of Life patterns" for classic examples!

## Troubleshooting

**Window doesn't respond**: The game is running. The loop only updates when events occur.

**Cells not showing**: Check your zoom level or pan to where you placed cells.

**Simulation not advancing**: Make sure to press SPACE to enter simulation mode (green indicator).

## License

This project is provided as-is for educational and personal use.

## Author

Kishal's Game of Life implementation