import os
import platform
inc = '''
include mu/*
include README.rst
include CHANGES.rst
include LICENSE
include conf/*
include mu/resources/css/*
include mu/resources/images/*
include mu/resources/fonts/*
include mu/resources/pygamezero/*
recursive-include mu/resources/web *
include run.py
recursive-include mu/locale *
'''
file = open('MANIFEST.in', 'w')
file.write('include mu/resources/seeed/*\n')
if os.name == 'posix':
    if platform.uname().system == 'Darwin':
        file.write('include mu/resources/seeed/tools-darwin/*' + inc)
    else:
        file.write('include mu/resources/seeed/tools-posix/*' + inc)
elif os.name == 'nt':
    file.write('include mu/resources/seeed/tools-win/*' + inc)
file.close()
