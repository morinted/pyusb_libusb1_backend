#!/usr/bin/env python3

__requires__ = '''
setuptools>=34.4.0
'''

from setuptools import setup
import subprocess
from distutils.cmd import Command

class CopyLibusbDylib(Command):
    description = 'copy the brew-installed libusb1 dylib to the package and make it portable'
    user_options = []
    extra_args = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        cmd = ['bash', 'copy_libusb.sh']
        subprocess.check_call(cmd)

setup(cmdclass={'copy_libusb': CopyLibusbDylib})
