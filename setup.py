from distutils.core import setup
setup(
  name = 'isbnpy',
  packages = ['isbnpy'],
  version = '0.0.1',
  description = 'Librería para obtener número estándar internacional de libro (ISBN)',
  author = 'Alejandro Farías',
  author_email = 'farias@8loop.cl',
  url = 'https://github.com/fariascl/isbnpy',
  packages=setuptools.find_packages(),
  install_requires=['bs4==0.0.1'],
  download_url = 'https://github.com/fariascl/pyemailscaper/tarball/0.0.1',
  keywords = ['isbn', 'book', 'libro'],
  classifiers = [],
)
