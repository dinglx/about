#!/usr/bin/env python

from setuptools import setup

setup(
    name='AboutMe',
    version='1.0',
    description='About Me, Based on Syte',
    author='dinglx',
    author_email='dlx1986@gmail.com',
    url='http://about-dinglx.rhcloud.com/',
    install_requires=[
        'Django==1.4.3', 
        'requests==0.14.2',
        'wsgiref==0.1.2',
        'psycopg2==2.4.5',
        'gunicorn==0.16.1',
        'pybars==0.0.4',
        'rauth==0.4.17'
    ],
)

