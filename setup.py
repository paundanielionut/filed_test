from setuptools import setup, find_packages

setup(
    name='Filed Test',
    version='0.0.1',
    description='Source code for the test.',
    long_description='Made by me!',
    url='https://github.com/paundanielionut/filed_test.git',
    author='Daniel Paun',
    author_email='paundanielionut@gmail.com',
    packages=find_packages(),
    install_requires=['Flask', 'Flask_assets'],
    extras_require={
        'dev': [],
        'test': [],
        'prod': [],
        'env': ['python-dotenv']
    },
    entry_points={
        'console_scripts': [
            'install=wsgi:__main__',
        ],
    },
)