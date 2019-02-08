# 2048 Game
## How to play
In the 2048 game, you have to combine blocks of the same value into one block of twice the value, taking care that the entire board is not filled.

## Control
- Arrow keys - Moving blocks
- Backspace - Undo your max 3 last moves
- ESC - Pausing/leaving from the game

## Important
If any problems with font I recommend to install the [Clear Sans font](https://01.org/clear-sans)

## Currently working on
- Options
- Highest score

## To-do list
- Log files
- Sounds
- Lose Screen
- File with current settings and default settings
- Highest score won't reset with every closing game
- Continue button in menu
- The drop-down language list

## Content
- main.py
  - Executes the game loop
- Screen.py
  - File of Screen class that include information about window, handle events, appearing text and quiting the game nad makes it all works
- Square.py
  - File of Square class that include information about a single square on the screen
- Button.py
  - File of Button class that include information about button and checks if was pressed
- Stack.py
  - File of Stack class that contains shift backs information for tiles value and scores
- README.md
  - You are reading this right now, include basic information about the project
- CHANGELOG.md
  - Changelog file
- Themes folder
  - Folder which contains colors themes for tiles
- Lang folder
  - Folder which contains languages
- Images folder
  - Folder with images
