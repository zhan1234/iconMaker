from distutils.core import setup
import py2exe
import sys
import glob

#this allows to run it with a simple double click.
sys.argv.append('py2exe')
 
py2exe_options = {
        "dll_excludes": ["MSVCP90.dll",],
        "compressed": 0,
        "optimize": 2,
        "ascii": 0,
        "bundle_files": 1,
        }
 
setup(
      name = 'iconMaker',
      version = '1.0',
      windows = ['run.py',], 
      zipfile = None,
      options = {'py2exe': py2exe_options},
      data_files=[
                  ("",
                   glob.glob("*.ini")),
                ]
    )
