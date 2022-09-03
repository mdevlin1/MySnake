#!/usr/bin/env python
from setuptools import setup,find_packages
from glob import glob

setup(name='md3v_snake',
      version='1.0',
      description='My rendition of the classic arcade game Snake',
      author='Mitchell Devlin',
      packages=['src/md3v_snake'],
      data_files=[
          ('images', glob('assets/*'))
      ],
      install_requires=[
          'pygame'
      ],
      include_package_data=True,
)