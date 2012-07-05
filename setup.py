#!/usr/bin/env python

from distutils.core import setup

setup(name='static-pipeline',
      version='0.1',
      description='Static site renderer / asset pipeliney thing in python',
      author='Danny Cosson',
      author_email='danny@tourbie.com',
      url='https://dcosson@github.com/dcosson/static-pipeline.git',
      license='BSD',
      packages=['static_pipeline', 'static_pipeline.lib'],
      scripts=['bin/static-pipeline'],
      install_requires=['Jinja2'],)
