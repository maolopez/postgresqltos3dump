from setuptools import setup, find_packages

with open('README.rst', encoding='UTF-8') as f:
    readme = f.read()

setup(
    name='postgresqltos3dump',
    version='1.0',
    description='Database backups locally or to AWS S3.',
    long_description=readme,
    install_requires=['boto3'], #2
    packages=find_packages('src'),
    package_dir={'': 'src'},
    entry_points={
    'console_scripts': [
    'postgresqltos3dump=postgresqltos3dump.cli:main',
    ]
    }
    ) #2

#https://setuptools.readthedocs.io/en/latest/setuptools.html#automatic-script-creation
#https://docs.python.org/3/library/time.html#time.strftime