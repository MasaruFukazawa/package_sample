from setuptools import setup, find_packages

setup(
    name='sample_package',
    description='Demonstrate packaging and distribution',

    version='1.0',
    author='Masaru Fukazawa',
    author_email='masaru@fukazawasoftwaredevelopment.com',
    url='https://github.com/MasaruFukazawa',
    
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
)
