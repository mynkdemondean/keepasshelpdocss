import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'Keepass Login Account Guide'
author = 'Keepass Login Account Guide'
release = '1.0'

extensions = []

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'alabaster'
html_static_path = ['_static']

html_sidebars = {
    '**': ['globaltoc.html', 'searchbox.html']
}
