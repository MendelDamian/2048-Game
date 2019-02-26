# 2048 Game
Developer: [Damian Mendel](https://github.com/MendelDamian)  
Start: 22-12-2018
## How to play
In the 2048 game, you have to combine blocks of the same value into one block of twice the value, taking care that the entire board is not filled. Download project and run "2048 Game.exe". Thanks for every download :)

## Control
- Arrow keys - Moving blocks
- Backspace - Undo your max 3 last moves
- ESC - Pausing/leaving from the game

## Currently working on
- Highest score won't reset every time you close game

## To-do list
- Log files
- Sounds
- Lose Screen
- Continue button in menu
- The drop-down language list

## Content
- main.py
  - Executes the game loop
- Screen.py
  - File of Screen class that include information about window, handle events, appearing text
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
- Fonts folder
  - Folder with fonts
- 2048 Game.exe
  - Execution file
- config.ini
  - Contains current and default settings
