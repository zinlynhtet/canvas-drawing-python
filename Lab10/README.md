# Line Drawing Visualizer with Turtle Graphics

A Python program that reads line drawing descriptions from a text file and visualizes them using the turtle graphics library.

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [File Format](#file-format)
- [Code Structure](#code-structure)
- [Examples](#examples)
- [Troubleshooting](#troubleshooting)

## Overview

This program reads coordinate data from a text file and uses Python's turtle graphics library to draw connected line segments on screen. It supports multiple disconnected components in a single drawing by using empty lines as separators.

### Features
- Reads (x, y) coordinate pairs from text files
- Draws connected line segments
- Supports multiple separate shapes in one drawing
- Error handling for invalid file formats
- Visual feedback with turtle graphics

## Installation

### Prerequisites
- Python 3.x installed on your system
- Turtle library (included with Python by default)

### Setup
1. Download or clone this repository
2. Ensure you have a `picture.txt` file with your drawing coordinates
3. Update the file path in the script to point to your text file

## Usage

### Basic Usage

1. **Prepare your drawing file** (e.g., `picture.txt`) with coordinates
2. **Update the file path** in the script:
   \`\`\`python
   base_path = r"C:\your\path\here"  # Change this to your folder
   file_name = "picture.txt"
   \`\`\`
3. **Run the script**:
   \`\`\`bash
   python draw_picture.py
   \`\`\`
4. **View the drawing** in the turtle graphics window that opens
5. **Close the window** when finished

### Alternative Usage (Simplified Version)

If using the simplified version without the main block:
\`\`\`bash
python scripts/draw_picture.py
\`\`\`

## File Format

### Coordinate Format
Each line in the input file should contain a single coordinate pair in the format:
\`\`\`
x, y
\`\`\`

### Rules
- **x** and **y** must be integers
- Coordinates are separated by a comma
- Spaces around the comma are optional
- **Empty lines** indicate the start of a new disconnected component

### Example File Structure
\`\`\`
10, -10
10, 10
-10, 10
-10, -10
10, -10

5, 5
-5, -5
-5, 5
5, 5
\`\`\`

This creates:
- **First component**: A square from (10,-10) → (10,10) → (-10,10) → (-10,-10) → (10,-10)
- **Second component**: A triangle from (5,5) → (-5,-5) → (-5,5) → (5,5)

## Code Structure

### Main Components

#### 1. Messages Class
\`\`\`python
class Messages:
    WELCOME = "Welcome to the Line Drawing Visualizer!"
    ERROR_FILE_NOT_FOUND = "Error: File not found."
    ERROR_INVALID_FORMAT = "Error: Invalid line format."
    DRAWING_COMPLETE = "Drawing complete! Close the window to exit."
\`\`\`
**Purpose**: Centralized storage for all user-facing messages

#### 2. draw_canvas() Function
\`\`\`python
def draw_canvas(filename):
\`\`\`
**Purpose**: Sets up the turtle graphics environment
- Creates the drawing window (800x800 pixels)
- Initializes the turtle pen
- Handles file reading errors
- Calls the data reading function

**Parameters**:
- `filename` (str): Path to the text file containing coordinates

#### 3. read_data() Function
\`\`\`python
def read_data(filename, pen, screen):
\`\`\`
**Purpose**: Reads and processes the coordinate file
- Opens and reads the file line by line
- Parses coordinate pairs
- Controls pen up/down for connected vs. disconnected segments
- Handles empty lines to start new components
- Draws lines between consecutive points

**Parameters**:
- `filename` (str): Path to the coordinate file
- `pen` (turtle.Turtle): The turtle object used for drawing
- `screen` (turtle.Screen): The turtle screen object

### Program Flow

\`\`\`
1. Start Program
   ↓
2. draw_canvas() - Setup window and pen
   ↓
3. read_data() - Read file and parse coordinates
   ↓
4. For each line:
   - If empty → Lift pen (new component)
   - If valid coordinates → Move to point and draw
   - If invalid → Show error
   ↓
5. Complete drawing and wait for user to close window
\`\`\`

### Key Variables

| Variable | Type | Purpose |
|----------|------|---------|
| `screen` | turtle.Screen | The drawing window |
| `pen` | turtle.Turtle | The drawing cursor |
| `first_point` | bool | Tracks if we're starting a new shape |
| `lines` | list | All lines read from the file |
| `x, y` | int | Parsed coordinate values |

## Examples

### Example 1: Simple Square
**File: square.txt**
\`\`\`
0, 0
100, 0
100, 100
0, 100
0, 0
\`\`\`
**Result**: Draws a 100x100 square starting at origin

### Example 2: Two Separate Triangles
**File: triangles.txt**
\`\`\`
0, 0
50, 100
100, 0
0, 0

200, 0
250, 100
300, 0
200, 0
\`\`\`
**Result**: Draws two triangles separated by space

### Example 3: House Shape
**File: house.txt**
\`\`\`
-50, -50
50, -50
50, 50
-50, 50
-50, -50

-50, 50
0, 100
50, 50
\`\`\`
**Result**: Draws a house with a square base and triangular roof

## Troubleshooting

### Common Issues

#### 1. "Error: File not found"
**Problem**: The program cannot locate your text file

**Solutions**:
- Check that the file path is correct
- Use raw strings for Windows paths: `r"C:\path\to\file"`
- Ensure the file exists in the specified location
- Check file name spelling and extension

#### 2. "Error: Invalid line format"
**Problem**: A line in the file doesn't match the expected format

**Solutions**:
- Ensure each line has exactly two numbers separated by a comma
- Remove any extra characters or text
- Check for missing commas
- Verify numbers are integers (no decimals)

#### 3. Nothing Draws on Screen
**Problem**: Window opens but no drawing appears

**Solutions**:
- Check if coordinates are within visible range (-400 to 400 typically)
- Verify file is not empty
- Ensure file has valid coordinate pairs

#### 4. Drawing is Too Small/Large
**Problem**: Drawing doesn't fit well in the window

**Solutions**:
- Adjust coordinate values in your text file
- Modify window size in `screen.setup(width=800, height=800)`
- Scale all coordinates proportionally

#### 5. Window Closes Immediately
**Problem**: The turtle window closes before you can see the drawing

**Solutions**:
- Ensure `screen.mainloop()` is called at the end
- Check for errors in the console output
- Verify the script completes successfully

### Debug Tips

1. **Print coordinates as they're read**:
   \`\`\`python
   print(f"Drawing to: ({x}, {y})")
   \`\`\`

2. **Check file contents**:
   \`\`\`python
   print(lines)  # After reading the file
   \`\`\`

3. **Slow down drawing**:
   \`\`\`python
   pen.speed(1)  # Slowest speed for debugging
   \`\`\`

## Advanced Customization

### Change Pen Color
\`\`\`python
pen.color("red")  # Add after pen = turtle.Turtle()
\`\`\`

### Change Background Color
\`\`\`python
screen.bgcolor("lightblue")  # Add after screen.setup()
\`\`\`

### Change Pen Size
\`\`\`python
pen.pensize(5)  # Thicker lines
\`\`\`

### Add Fill Color
\`\`\`python
pen.fillcolor("yellow")
pen.begin_fill()
# ... draw shape ...
pen.end_fill()
\`\`\`

## License

This project is open source and available for educational purposes.

## Contributing

Feel free to submit issues or pull requests for improvements!

---

**Created for beginners learning Python turtle graphics and file I/O operations.**
