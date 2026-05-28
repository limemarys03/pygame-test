# Pygame Touch Test 🎮

My very first test project using the **Pygame** library. I created this while learning the basics of 2D game development in Python and experimenting with mobile touch control adaptation.

## 🚀 Features
* **Cross-platform Control**: The screen is divided into virtual zones (thirds). This allows emulating d-pad presses via mouse clicks or smartphone touch screens.
* **Fallback System**: If the player sprite (`hero.png`) is missing, the game doesn't crash. It automatically renders a red square instead.
* **Clean Game Loop**: Implemented proper event handling for closing the window and screen updates.

## 📺 Gameplay Screenshot

![Gameplay](screenshot.jpg)

*(Note: Replace "screenshot.jpg" with your actual image filename if you upload it to GitHub)*

## 🛠️ How to Run

1. Install the Pygame library if you haven't already:
   ```bash
   pip install pygame
   ```
2. (Optional) Place any character image in the project folder and name it `hero.png`.
3. Run the script:
   ```bash
   python main.py
   ```

## 📱 Controls
* Click or tap in the **left/right** or **top/bottom** thirds of the window to move the square in that direction.

---
*Created for educational purposes.*
