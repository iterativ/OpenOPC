from setuptools import setup, find_packages
from OpenOPC import __version__ as version

setup(name="OpenOPC",
      version=version,
      download_url='https://github.com/iterativ/OpenOPC/tarball/master',
      description="This is a clone of http://openopc.sourceforge.net modified to be used with distutils",
      keywords='python, opc, openopc',
      url='http://openopc.sourceforge.net',
      license='GPLv2',
      packages=find_packages(exclude=['ez_setup']),
      zip_safe=False,
      )
