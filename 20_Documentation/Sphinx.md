# Sphinx Documentation

# 1. Installation

~~~bash
> pip install -U Sphinx
> pip install sphinx_rtd_theme
> pip install --upgrade myst-parser
~~~


# 2. Starting the Project
We create two folders:
- source folder (src) where the python code will be stored
- docs folder (where sphinx will be created)


After that navigate to the docs folder and run the command
~~~bash
docs > sphinx-quickstart
~~~

And answer the questions.... The Sphinx will create the file structure under **docs** folder


# 3. Reconfiger Sphinx (conf.py)

~~~python
import os
import sys
sys.path.insert(0, os.path.abspath('../src/'))   # the place of python source code


extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    'myst_parser'
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'restructuredtext',
    '.md': 'markdown',
}

~~~


# 4. Generate Sphinx Files from the source code
~~~bash
docs> sphinx-apidoc -o docs ../src
~~~

The command will create files (rst) und **docs/docs** folder


# 5. RST Files

1. index.rst ( The Main rst File for Index.html)
2. app.rst 



# 6. Build the Sphinx Project

~~~bash
docs> make clean html      # to delete build files
docs> make html            # to make html file
~~~