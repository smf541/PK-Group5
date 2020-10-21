#
# pkmodel setuptools script
#
from setuptools import setup, find_packages


def get_version():
    """
    Get version number from the pkmodel module.

    The easiest way would be to just ``import pkmodel ``, but note that this may
    fail if the dependencies have not been installed yet. Instead, we've put
    the version number in a simple version_info module, that we'll import here
    by temporarily adding the oxrse directory to the pythonpath using sys.path.
    """
    import os
    import sys

    sys.path.append(os.path.abspath('pkmodel'))
    from version_info import VERSION as version
    sys.path.pop()

    return version


def get_readme():
    """
    Load README.md text for use as description.
    """
    with open('README.md') as f:
        return f.read()


# Go!
setup(
    # Module name (lowercase)
    name='pkmodel',

    # Version
    version=get_version(),

    description='An example Python project.',

    long_description=get_readme(),

    license='MIT license',

    # author='',

    # author_email='',

    maintainer='Martin Robinson',

    maintainer_email='martin.robinson@cs.ox.ac.uk',

    url='https://github.com/SABS-R3/2020-software-engineering-projects-pk',

    # Packages to include
    packages=find_packages(include=('pkmodel', 'pkmodel.*')),

    # List of dependencies
    install_requires=[
        # Dependencies go here!
        'numpy',
        'matplotlib',
        'scipy',
    ],
    extras_require={
        'docs': [
            # Sphinx for doc generation. Version 1.7.3 has a bug:
            'sphinx>=1.5, !=1.7.3',
            # Nice theme for docs
            'sphinx_rtd_theme',
        ],
        'dev': [
            # Flake8 for code style checking
            'flake8>=3',
        ],
    },
)
