"""
About Virtual Environment

- Using same python installation for every project
will be difficult to manage because
for project_1 we may need to install some library
for project_2 we may need to install same library with different versions
etc
So,
finally using same python installation for all projects
will be difficult manage


SOLUTION:
For each project we can create virtual environment
- creating virtual environment will create seperate python
installation directory with minimal files
- We can create n number of virtual environments
- We can switch b/n each virtual environmnet using activate/deactive
 OR some IDEs like pycharm given option to select virtual environment
 while selecting pyton_interpreter
 File-> settings-> project:some_thing-> select python_interprete -> select virtual environment

So finally,

OPTION-1:

we can create virtual environement using command prompt
command:
# Steps
C:\Users\mahad>cd\

C:\>cd python_training
C:\python_training>python -m venv my_venv_1

C:\python_training>cd my_venv_1

C:\python_training\my_venv_1>cd Scripts

C:\python_training\my_venv_1\Scripts>activate

(my_venv_1) C:\python_training\my_venv_1\Scripts>cd ..

(my_venv_1) C:\python_training\my_venv_1>cd ..

(my_venv_1) C:\python_training>cd bin

(my_venv_1) C:\python_training\bin>python 1_docstring_and_comments.py

(my_venv_1) C:\python_training\bin>pip install selenium

(my_venv_1) C:\python_training\bin>cd ..

(my_venv_1) C:\python_training>cd my_venv_1

(my_venv_1) C:\python_training\my_venv_1>cd Scripts

(my_venv_1) C:\python_training\my_venv_1\Scripts>deactivate

THIS WILL ACTIVATE TO THAT TERMINAL ONLY

OPTION-2:
Using IDE like pycharm
"""

