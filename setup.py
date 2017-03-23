#!/usr/bin/python

import sys
import os
import askquora

if sys.version_info > (3,0):
        sys.exit("AskQuora requires python 2.")

from setuptools import setup, find_packages

setup(name='AskQuora',
      version='0.1.2',
      description='Quora Q&A right from the command line!',
      author='Ritiek Malhotra',
      author_email='ritiekmalhotra123@gmail.com',
      #scripts=['bin/askquora'],
      packages = find_packages(),
      entry_points={
            'console_scripts': [
                  'askquora = askquora.askquora',
            ]
      },
      url='https://www.github.com/Ritiek/AskQuora',
      keywords=['quora', 'terminal', 'command-line', 'question', 'python'],
      license='MIT',
      download_url='https://github.com/Ritiek/AskQuora/archive/v0.1.2.tar.gz',
      classifiers=[],
      install_requires=[
            'requests',
            'BeautifulSoup4',
            'colorama',
            'requests-cache'
      ]
     )

