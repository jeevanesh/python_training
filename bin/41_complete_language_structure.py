"""
In this section,

What Python Library Means?
and
Complete Python Programming Language Structure
"""

# ---------
# What Python Library Means?
# ##########
# - python library can be one or more module like mymodule.py
# - python library can be one or more package like mypackage
# - python library can be one or more frameworks
#       -- frameworks are like mymodule.py or mypackage
#       -- Difference
#           --- in mymodule.py/mypackage we are keeping only definitions
#           --- In case of frameworks, not only definitions, some of the
#               common tasks are implemented
#               example: unittest framework where we can use this framework
#               for any type of project and writing testcases are different
#               executing all testcases, producing summary, reports etc. are common
#               so in framework these type of common tasks are implemented.
# ###########################

# ---------
# Complete Python Programming Language Structure
# ##########
# PART-1: Python Programming Language
#           - data types, if, for, while, file operations, functions, classes etc
#           - Using PART-1, we can develop anything from the scratch
#           - We already developed: program-1 to program-10
#
# PART-2: Builtins
#           - Few variables, functions & classes are predefined
#           - by default imported
#           - Complete List: print(dir(__builtins__))
#
# PART-3: Standard Libraries
#           - Few libraries are getting installed when we install python
#           - Difference is
#               -- builtins are by default imported
#               -- standard libraries, we need to import and use
#           - Location: C:\Python312\Lib
#           - Documentation: https://docs.python.org/3/library/index.html
#
# PART-4: 3rd Party/External Libraries
#           - this is MAIN BIG REPOSITORY
#           - Location: https://pypi.org/
#           - Documentation: https://pypi.org/
#           - We need to download and install required libraries
#
# PART-5: User defined libraries
#           - Which we develop
#           - We already developed
#           1) mymodule.py
#           2) mypackage
# ###########################