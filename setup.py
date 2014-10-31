from codecs import open  # To use a consistent encoding
from setuptools import setup, find_packages
import sys, os


version = '1.0'


# Get the long description from the relevant file
with open('README.md', encoding='utf-8') as f:
    long_description = f.read()


setup(name='pyskel',
      version=version,
      description="PSkeleton of a Python package",
      long_description=long_description,
      classifiers=[],
      keywords='',
      author='Sean Gillies',
      author_email='sean@mapbox.com',
      url='https://github.com/mapbox/pyskel',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'click'
      ],
      extras_require = {
          'test': ['pytest'],
      },
      entry_points="""
      [console_scripts]
      pyskel=pyskel.scripts:cli
      """
      )
