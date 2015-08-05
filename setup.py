#!/usr/bin/env python


from setuptools import setup, find_packages

setup(
    name='django-dps',
    version='0.2',
    packages=find_packages(),
    license='BSD License',
    url="https://github.com/gregplaysguitar/django-dps/",

    maintainer="Greg Brown",
    maintainer_email="gregplaysguitar@gmail.com",

    description='Django integrations for the DPS payment gateway',
    long_description=open('README.md').read(),

    install_requires=[
        'Django>=1.6',
    ],

    include_package_data=True,
    package_data={},

    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
    ],
)
