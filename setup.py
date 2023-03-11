from setuptools import setup, find_packages

setup(
    name='py_ocv',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
)
