from setuptools import setup
import os, sys

# check Python version
if sys.version_info >= (3,8):
  sys.exit('Sorry, Intertext requires Python 3.7 or earlier')

setup(
  name='intertext',
  version='0.0.1',
  packages=['intertext'],
  keywords = ['text-mining', 'data-visualization', 'text-reuse', 'plagiarism'],
  description='Discover and visualize text reuse',
  url='https://github.com/yaledhlab/intertext',
  author='Yale DHLab',
  author_email='douglas.duhaime@gmail.com',
  license='MIT',
  install_requires=[
    'beautifulsoup4==4.5.1',
    'datasketch==0.2.6',
    'networkx==2.5',
    'nltk==3.4.5',
    'pymongo==3.3.1',
    'requests==2.24.0',
  ],
  entry_points={
    'console_scripts': [
      'intertext=intertext:parse',
    ],
  },
)
