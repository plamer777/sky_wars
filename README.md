
## Course Work 5
The application is the old-style browser game. A user should choose a hero to play and his opponent. After that game will start. 

A user have just four possible actions:

 - hit opponent - the most commonly used action to hit an enemy
 - use skill - both hero an his opponent have a special skill to use once for the game
 - skip step - just do nothing an to be hit by opponent
 - finish game - to capitulate or start a new game
 
User can choose any hero and opponent with different combinations of armor and weapon but not similar. Thus if for hero were chosen class thief with dagger and leather armor then these options won't available for opponent.
 
---
The project's structure: 
 - classes - classes representing game entities
 - .github - workflow files
 - blueprints - flask views processing user's request
 - data - there are json files with available classes, weapon, armor, etc.
 - factories - classes to create another units
 - help_files - files provided by SkyPro
 - static - pictures to render html templates
 - templates - source of html templates
 - tests - test classes to check if all factories and views work correct
 - .flake8 - config file for flake8
 - mypy.ini - config file for mypy
 - container.py - there're instances of required classes and dictionaries
 - constants.py - file paths and lists with default unit phrases
 - utils.py - additional functions to load data from json, etc.
 - skywars.service - service file to deploy the application
 - requirements.txt - file with the project's dependencies
 - app.py - a main file to start the application
 - README.md - this file with app info
 - .gitignore - file with folders and files to exclude from the repository
 ---
 The project was created in 21 January 2023 by Aleksey Mavrin