import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='krules-dispatcher-cloudevents',
    version="0.2.0",
    author="Alberto Degli Esposti",
    author_email="alberto@arispot.tech",
    description="KRules cloudevents dispatcher",
    licence="Apache Licence 2.0",
    keywords="krules cloudevents router",
    url="https://github.com/airspot-dev/krules-dispatcher-cloudevents",
    packages=['krules_cloudevents'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: Apache Software License",
    ],
    install_requires=[
        'pycurl==7.43.0.3',
        'krules-core==0.2.0',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
        'pytest-localserver',
    ],
)