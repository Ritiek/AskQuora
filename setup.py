#!/usr/bin/env python

from setuptools import setup, find_packages
import askquora

with open("README.rst", "r") as f:
    long_description = f.read()

setup(name='AskQuora',
      version=askquora.__version__,
      description='Quora Q&A right from the command line',
      long_description=long_description,
      author='Ritiek Malhotra',
      author_email='ritiekmalhotra123@gmail.com',
      packages = find_packages(),
      entry_points={
            'console_scripts': [
                  'askquora = askquora.askquora:command_line',
            ]
      },
      url='https://www.github.com/Ritiek/AskQuora',
      keywords=['quora', 'terminal', 'command-line', 'question', 'python'],
      license='MIT',
      download_url='https://github.com/Ritiek/AskQuora/archive/v' + askquora.__version__ + '.tar.gz',
      classifiers=[],
      install_requires=[
            'requests',
            'BeautifulSoup4',
            'colorama',
            'requests-cache'
      ]
     )
