# Multi-Form Bubble Application

## Project Introduction

This is a multi-form bubble application developed based on Python Tkinter, which can generate multiple bubble windows with fade-in and fade-out effects on the screen. Each bubble window will randomly display a romantic love message and automatically disappear after a certain period of display.

## Features

- 💬 Random Text Display: Each bubble randomly displays a preset romantic love message
- 🎨 Beautiful Visual Effects: Supports custom colors and random color generation
- 🌟 Smooth Fade-in and Fade-out Animations: Bubble windows have elegant appearance and disappearance effects
- ⏱️ Automatic Lifecycle Management: Each bubble window automatically fades out after a specified time
- 🔄 Progressive Creation: Bubble windows are created one by one at set time intervals, forming a gradually increasing effect

## Technical Implementation

- Uses Python Tkinter library to create graphical interface
- Adopts object-oriented design, including the following main classes:
  - `BubbleWindow`: Responsible for creating individual bubble windows and animation effects
  - `BubbleManager`: Manages the creation and lifecycle of multiple bubble windows
  - `MultiFormBubbleApp`: Main application class that coordinates component work
- Implements custom fade-in and fade-out animation effects
- Controls the lifecycle of bubble windows through timers

## Usage

### Requirements

- Python 3.x
- Tkinter library (usually installed with Python)

### Running the Program

1. Ensure Python environment is installed
2. Download or clone this project to your local machine
3. Make sure all Python files are in the same directory
4. Execute the following command in the project directory:

```bash
python main.py
```

### Customization

You can customize the behavior of the application by modifying parameters in the `main.py` file:

- `bubble_count`: Set the number of bubble windows to create
- `fade_out_duration`: Set the duration of the bubble fade-out animation (seconds)
- `life_duration`: Set the total display time for each bubble window (seconds)
- `gradual_interval`: Set the time interval for creating bubble windows (seconds)
- `default_texts`: Customize the text content displayed in the bubbles
- `default_colors`: Customize the background color of the bubbles

## Project Structure

```
muliti_form_bubble/
├── main.py                   # Main program file (entry point)
├── bubble_window.py          # Contains BubbleWindow class
├── bubble_manager.py         # Contains BubbleManager class
├── multi_form_bubble_app.py  # Contains MultiFormBubbleApp class
├── README.md                 # Project documentation (English)
├── README_cn.md              # Project documentation (Chinese)
└── LICENSE                   # MIT License file
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Example Effect

After running the program, multiple bubble windows will gradually appear on the screen. Each bubble window displays a random romantic love message and automatically fades out after 40 seconds. As new bubbles are continuously created and old ones disappear, the visual effect remains dynamic and engaging.

## License

This project is licensed under the MIT License.

## Acknowledgments

- Thanks to Python and Tkinter for their powerful features
- Thanks to all users who use and support this project