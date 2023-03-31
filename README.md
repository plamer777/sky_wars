
  
## SkyWars game  
The application is the old-style browser game. A user should choose a hero to play and his opponent. After that game will start.   
  
**A user have just four possible actions:**  
  
 - hit opponent - the most commonly used action to hit an enemy  
 - use skill - both hero an his opponent have a special skill to use once for the game  
 - skip step - just do nothing an to be hit by opponent  
 - finish game - to capitulate or start a new game  
   
User can choose any hero and opponent with different combinations of armor and weapon but not similar.   
Thus if for hero were chosen class thief with dagger and leather armor then these options won't available for opponent.  

**There are new functions added in the latest version such as:**
1. Admin register and login
2. Admin menu to add new entities to the game
3. Pages with detailed forms to add new weapons, armors, hero classes, etc.
As for now, only users having 'admin' role can add new things in the game and only admin can register another admin.

**How to run the project:**
The project was adapted to deploy on the VPS. So you have to do some preparations:

1. Create a new GitHub repository
2. Add GitHub secrets following the project_deploy.yaml file
3. Clone the repo to your PC
4. Create local git repo, add all files, commit and push to your GitHub repo
5. The project will be automatically deployed on your VDS
6. Check if all work correctly and if not double check your secrets and settings

---  
The project's structure:   
 - classes - classes representing game entities  
 - .github - workflow files  
 - blueprints - flask views processing user's request  
 - data - there are json files with available classes, weapon, armor, etc.  
 - factories - classes to create another units 
 - dao - data access objects for game entities and users
 - db - db models and SQLAlchemy instances
 - managers - there is only hash manager in the folder to create hashed passwords and tokens
 - migrations - Flask migrations
 - services - business logic classes
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
 - add_admin.py - special file to create first admin record in the db
 - config.py - configuration object for Flask app
 - create_db.py - logic to create database in fill it up by the records from data folded
 - docker-compose-ci.yaml - docker-compose file to create all containers
 - Dockerfile - file describing docker container for this only application
 - init_app.py - Flask app initialization and configuration - 
 - README.md - this file with app info  
 - .gitignore - file with folders and files to exclude from the repository  

 ---  The project was updated in 31 March 2023 by Aleksey Mavrin