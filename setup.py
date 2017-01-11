import os

from setuptools import setup, find_packages

Area = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(Area, 'README.txt')) as f:
    README = f.read()

requires = [
    'pyramid',
    'pyramid_chameleon',
    'pyramid_debugtoolbar',
    'pyramid_tm',
    'SQLAlchemy',
    'transaction',
    'zope.sqlalchemy']

setup(name='pyramid_pizza',
      version='0.0',
      description='pyramid_pizza',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='Ovchinnickova and Taranenko',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='pyramid_pizza',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = pyramid_blogr:main
      [console_scripts]
      initialize_pyramid_pizza_db = pyramid_pizza.scripts.initdb:main
      """,
      )
