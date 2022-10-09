"""
    Для генерации доки нужно прописать такие команды:
    с нуля:
     - sphinx-quickstart
     - Добавить modules в index.rst
     - sphinx-apidoc -o . ..
     - make html
    если не с нуля:
     - make html
"""

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os
import sys


sys.path.insert(0, os.path.abspath('..'))        # Указывает на каталог src

from src.config import PROJECT_NAME, VERSION

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information


project = PROJECT_NAME
copyright = '2022, moonvent'
author = 'moonvent'
version = VERSION

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.todo', 'sphinx.ext.viewcode', 'sphinx.ext.autodoc']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'ru'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'

html_static_path = ['_static']
