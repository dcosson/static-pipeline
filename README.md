## StaticPipeline.py

A simple, configurable asset pipeline and static site generator in python.  You give it some settings and it compiles your assets accordingly.

It's a work in progress, right now it handles Jinja2 templates (fully-featured, with inheritance, etc) and arbitrary command-line commands that take an input and output file as args (e.g. less-css, sass, etc), as well as a couple of convenience commands for filtering and re-arranging the output files.
