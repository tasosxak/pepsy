from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'A pythonic reactjs-like web framework for Python'
LONG_DESCRIPTION = 'ReactJS-like web framework that runs on Brython'

setup(
    name="pepsy",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author="Tasos Temperekidis",
    author_email="tasosxakx@gmail.com",
    license='MIT',
    packages=find_packages(),
    install_requires=[],
    keywords='web framework',
    classifiers= [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 3",
    ]
)