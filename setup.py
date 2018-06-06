from setuptools import setup
import os
setup(
    name='mpi-master-slave',
    version='0.1.0',
    author='luca-s',
    author_email='luca.scarabello@gmail.com',
    packages=['mpi_master_slave'],
    install_requires=['mpi4py'],
    description='An MPI master-slave library for Python',
    long_description='mpi-master-slave is a Python library that provides \
    an abstraction for a master-slave work paradigm. It rests on top of \
    mpi4py and handles communication between master and slave ranks.',
    url = 'https://github.com/TerraFusion/mpi-master-slave',
    keywords = ['mpi', 'master', 'slave']
)

