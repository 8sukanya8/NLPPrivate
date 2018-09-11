from setuptools import setup, find_packages

setup(name='NLPprivate',
      version='0.1',
      license='MIT',
      author='Sukanya Nath',
      author_email='8sukanya8@gmail.com',
      description='contains processing functions for text for noise removal, normalization',
      packages=find_packages(exclude=['tests']),
      long_description=open('README.md').read(),
      zip_safe=False)