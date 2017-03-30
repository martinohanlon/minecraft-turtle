#!/usr/bin/env python
import io
from setuptools import setup, find_packages

with io.open('README.md', mode='r', encoding='utf8') as f:
    readme = f.read()


setup(name='mcturtle',
      version='0.1',
      description='A better minecraft pi library.',
      url='https://github.com/martinohanlon/minecraft-turtle',
      packages=find_packages(exclude=['*.tests', '*.tests.*', 'tests.*', 'tests']),
      zip_safe=True,
      include_package_data=True,
      keywords='minecraft raspberry pi mcpi py3minepi turtle',
      long_description=readme,
#      install_requires=['py3minepi'],
      classifiers=[
          'Development Status :: Development Status :: 3 - Alpha',
          'Environment :: X11 Applications',
          'Intended Audience :: Education',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: POSIX',
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
      ],
      )
