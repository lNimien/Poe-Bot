# Path of Exile Automation Bot

This is an automation bot for **Path of Exile (PoE)** that interacts with items in the game, particularly for creating **blue-gray items**. The bot uses **OpenCV** for color detection and **pyautogui**/**pydirectinput** to simulate mouse clicks.

## How It Works

- **Input:** The bot receives a number as input, which corresponds to a specific grid action.
- **Image Processing:** The bot captures screenshots of specific areas and processes them to detect the desired color.
- **Action:** The bot clicks on items that do not match the target color.
- **Recursive Execution:** The bot repeats the process unless stopped manually by pressing the **F7** key.

## How to Run

### Requirements

- Python 3.x
- Dependencies: `pyautogui`, `pydirectinput`, `opencv-python`, `numpy`, `keyboard`

### Functions
- **funcion_para_numero(n):** Executes the action based on the input number.
- **comprobar_color_con_opencv(region_x, region_y, region_ancho, region_alto):** Captures and processes a screenshot to detect the target color.
- **click_cuadricula_*:** Functions to click on grids of items with various slot configurations.

You can install the required libraries by running:

```bash
pip install pyautogui pydirectinput opencv-python numpy keyboard

