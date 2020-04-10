# Changelog
All notable changes to this project will be documented in this file.

## 2020-04-09
### Featues
- Correct resizing window
- Simplified code

## [2.0] - 2020-04-09
### Started working on version 2.0
### Featues
- Better tiles placement
- Working with fullscreen

### Bugs
- Resizing doesn't update tiles position

### Removed
- placing version of application in CHANGELOG

## [0.4.3] - 2019-02-23
### Added
- Advanced settings
- New option in menu - save settings, load default settings

### Fixed
- Moving is now possible
- Program remembers language changes which were done in GUI

## [0.4.2] - 2019-02-21
### Added
- Config file with current and default settings
- Settings are now remembered 

### Fixed
- No more error message while closing game

## [0.4.1] - 2019-02-19
### Added
- Execution (.exe) file
- file with fonts

### Fixed
- Fonts work correctly

## [0.4.0] - 2019-02-11
### Added
- Settings are available in all 3 languages
- Simple background in menu

### Fixed
- Game doesn't crash anymore after selecting 0 for undo moves

## [0.3.5] - 2019-02-09
### Added
- Fully working settings

## [0.3.4] - 2019-02-08
### Added
- You can set size and languange in the console before the game starts

### Changed
- 4 spaces instead of tab

### Deleted
- Settings GUI

## [0.3.3] - 2019-01-24
### Added
- Number of possible undo moves displays on the screen

## [0.3.2] - 2019-01-22
### Added
- New Theme (Pastels)
- New buttons in settings

## [0.3.1] - 2019-01-17
### Added
- Current score and the best score of this session
- You can undo your max 3 last moves (using stack)
- Instructions in README file about how to play

### Changed
- Re-builded README file
- Now it's 10% chance to appear 4 then 2

### Fixed
- Game doesn't crash anymore after re-entering to game
- If you don't have Clear Sans font, the game doesn't crash anymore

## [0.3.0] - 2019-01-16
### Added
- Switching languages by clicking on the name or flag

## [0.2.4] - 2019-01-15
### Changed
- Screen.py += game.py

### Removed
- game.py file

### Fixed
- Game doesn't crash after re-enter to the game

## [0.2.3] - 2019-01-15
### Added
- Raw options view

### Changed
- Some methods became @classmethods

### Fixed
- Game doesn't crash while reaching the score over the max value in a current color theme

## [0.2.2] - 2019-01-14
### Added
- Languages (en-GB, pl-PL, de-DE)

### Changed
- theme variable has been moved to Screen class

## [0.2.1] - 2019-01-14
### Added
- File with colors themes of fields
- Example file that will introduce you into creating your own color theme

### Changed
- The way of reading colors
- Font

### Removed
- Testing lines

## [0.2.0] - 2019-01-14
### Added
- Main menu (2 of 3 buttons only works)
- Button file

### Changed
- Way of filling and checking which key was pressed

### Removed
- Some useless variables and lines for testing

## [0.1.4] - 2019-01-13
### Added
- Move in all directions

### Fixed
- Game doesn't crash after reaching score above 1024

## [0.1.3] - 2019-01-13
### Added
- CHANGELOG file

## [0.1.2] - 2019-01-13
### Removed
- Files under tracking from pycharm environment

## [0.1.1] - 2019-01-13
### Added
- Move left

### Changed
- Way of moving the squares

## [0.1.0] - 2019-01-12
### Added
- Move up

### Changed
- Color values for the squares

## [0.0.6] - 2019-01-12
### Added
- main.py file that executes the main game loop

### Changed
- Renamed old main.py -> game.py

## [0.0.5] - 2019-01-11
### Added
- Colors for each value of field

## [0.0.4] - 2019-01-11
### Added
- Setting the value of the random square to 2

## [0.0.3] - 2018-12-31
### Added
- Showing the value of fields
- Added 2 functions for text display in Screen.py file

## [0.0.2] - 2018-12-30
### Added
- Screen file for the class
- Square file for the class
- main.py file with game loop

### Changed
- Showing fields mechanic

## [0.0.1] - 2018-12-23
### Added
- README file
- First mechanic to showing fields

## [0.0.0] - 2018-12-22
- The project has started
