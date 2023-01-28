# -*- coding: utf-8 -*-
#
# gmpy2 documentation build configuration file.
#
# This file is execfile()d with the current directory set to its containing dir.

import sys, os

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.imgmath',
              'sphinx.ext.intersphinx', 'sphinx_rtd_theme']

# Contains mapping the locations and names of other projects that
# should be linked to in this documentation.
intersphinx_mapping = {'python': ('https://docs.python.org/3/', None)}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# General information about the project.
project = 'gmpy2'
copyright = '2012 - 2022, Case Van Horsen'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '2.2'
# The full version, including alpha/beta/rc tags.
release = '2.2.0a1'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme'

# Output file base name for HTML help builder.
htmlhelp_basename = 'gmpy2doc'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', 'gmpy2.tex', 'gmpy2 Documentation',
   'Case Van Horsen', 'manual'),
]

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'gmpy2', 'gmpy2 Documentation',
     ['Case Van Horsen'], 3)
]
