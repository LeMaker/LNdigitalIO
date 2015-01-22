import sys
from distutils.core import setup


PY3 = sys.version_info[0] >= 3
VERSION_FILE = "LNdigitalIO/version.py"


def get_version():
    if PY3:
        version_vars = {}
        with open(VERSION_FILE) as f:
            code = compile(f.read(), VERSION_FILE, 'exec')
            exec(code, None, version_vars)
        return version_vars['__version__']
    else:
        execfile(VERSION_FILE)
        return __version__


setup(
    name='LNdigitalIO',
    version=get_version(),
    description='The LN Digital I/O module.',
    author='Lemaker',
    author_email='support@lemaker.org',
    url='https://github.com/LeMaker/LNdigitalIO/',
    packages=['LNdigitalIO'],
    long_description=open('README.md').read(),
    classifiers=[
        "License :: OSI Approved :: GNU Affero General Public License v3 or "
        "later (AGPLv3+)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='LN digital IO modules bananapi',
    license='GPLv3+',
    requires=['pifacecommon']
)
