from setuptools import setup, find_packages
import os

setup(
    name='chiafan-plotting-simulator',
    version='1.0.0',
    description='The Chia Plotter Simulator',
    author='Break Yang',
    author_email='breakds@gmail.com',
    # find_package() without any arguments will serach the same
    # directory as the setup.py for modules and packages.
    packages=find_packages(),
    package_data = {
        '': ['*.txt'],
    },
    data_files = [
        ('templates', ['chiafan_simulator/templates/sample_log.txt']),
    ],
    entry_points={
        'console_scripts': [
            'chiafan-plot-sim=chiafan_simulator.app:main',
        ],
    },
    python_requires='>=3.6',
)
