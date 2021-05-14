from setuptools import setup, find_packages

setup(
    name='chiafan-plotting-simulator',
    version='1.0.0',
    description='The Chia Plotter Simulator',
    author='Break Yang',
    author_email='breakds@gmail.com',
    # find_package() without any arguments will serach the same
    # directory as the setup.py for modules and packages.
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'chiafan-plot-sim=chiafan_simulator.app:main',
        ],
    },
    python_requires='>=3.6',
)
