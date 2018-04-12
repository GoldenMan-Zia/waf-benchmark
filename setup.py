from os import path
from os.path import join, abspath, dirname
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst')) as f:
    readme = f.read()

with open(join(here, 'requirements.txt')) as f:
    required = f.read().splitlines()

with open(join(abspath(dirname(__file__)), "VERSION"), "r") as v:
    VERSION = v.read().replace("\n", "")

setup(
    name='waf_benchmark',
    version=VERSION,
    packages=find_packages(),
    long_description=readme,
    install_requires=required,
    include_package_data=True,
    url='https://github.com/bbva/waf-benchmark',
    license='BSD',
    author='Daniel Garcia (cr0hn)',
    description='A benchmarking test for WAF systems',
    entry_points={'console_scripts': [
        'waf-bench = waf_benchmark.__main__:main',
    ]},
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3.6',
    ],
)

