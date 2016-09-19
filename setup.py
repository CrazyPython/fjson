from distutils.core import setup
import platform
if platform.python_implementation() == 'PyPy':
    dependencies = []
else:
    

setup(
  name = 'fjson',
  packages = ['fjson'],
  version = '0.9',
  description = 'fjson figures out what JSON library is the fastest for you.',
  author = 'CrazyPython',
  author_email = 'CrazyPython@users.noreply.github.com',
  url = 'https://github.com/CrazyPython/fjson',
  download_url = 'https://github.com/CrazyPython/fjson/tarball/v0.9.0',
  keywords = ['json', 'speed', 'performance', 'simple'],
  classifiers = [],
  install_requires=dependencies,
)
