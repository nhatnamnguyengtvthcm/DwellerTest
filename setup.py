# Copyright 2010 Bastian Bowe
#
# This file is part of JayDeBeApi.
# JayDeBeApi is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# JayDeBeApi is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with JayDeBeApi.  If not, see
# <http://www.gnu.org/licenses/>.
#

import sys

from setuptools import setup

install_requires = [
    'greenlet=="2.0.1"',
    'importlib-metadata=="4.8.3"',
    'JayDeBeApi=="1.2.3"',
    'JPype1=="1.3.0"',
    'python-dotenv==0.20.0'
    'SQLAlchemy==1.4.44',
    'typing_extensions==4.1.1',
    'zipp==3.6.0'
 ]

setup(
    #basic package data
    name = 'Nam',
    version = '1.0.0',
    author = 'Nam Nguyen',
    author_email = 'nhatnamnguyen.gtvthcm@gmail.com',
    license = 'GNU LGPL',
    url='',
    description=('Connect python with postgre throught JDBC'),
    long_description=open('README.md').read(),
    keywords = ('db api java jdbc bridge connect sql jpype jython'),
    classifiers = [

        ],

    packages=['jaydebeapi'],
    install_requires=install_requires,
    )