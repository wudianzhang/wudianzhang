import subprocess as subprocess

subprocess.check_call(['pip', 'install', 'numpy'])
import numpy as numpy
del numpy

subprocess.check_call(['pip', 'uninstall', '-y', 'numpy'])
del subprocess

raise Exception('successful')
