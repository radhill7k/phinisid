import sys
import os

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


setup(
    name='phinisid',
    version='0.1.0',
    author='R Hilman Hermarian',
    author_email='radhill7k@gmail.com',
    description='A Desktop Phinisi App',
    long_description=read('README.rst'),
    license='MIT',
    keywords=(
        "Python, cookiecutter, kivy, buildozer, pytest, projects, project "
        "templates, example, documentation, tutorial, setup.py, package, "
        "android, touch, mobile, NUI"
    ),
    url='https://github.com/radhill7k/phinisid',
    install_requires=[
        'kivy>=1.10.0',
        'click',
    ],
    zip_safe=False,
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'phinisid=phinisid.cli:main'
        ]
    },
    tests_require=['pytest'],
    cmdclass={'test': PyTest},
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: X11 Applications',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Artistic Software',
        'Topic :: Multimedia :: Graphics :: Presentation',
        'Topic :: Software Development :: User Interfaces',
    ],
)
