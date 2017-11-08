import re
from pathlib import Path
from setuptools import setup


PACKAGE = 'timeout'
SRC_DIR = 'src'

INIT_PATH = Path(__file__).parent / SRC_DIR / PACKAGE / '__init__.py'

VERSION = re.search(
    r'''^__version__ *= *["']([.\d]+)["']$''',
    INIT_PATH.read_text(),
    re.M,
).group(1)

setup(
    name='signalled-timeout',
    author="Center for Data Science and Public Policy",
    author_email='datascifellows@gmail.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
    ],
    url='https://github.com/dssg/signalled-timeout',
    package_dir={'': SRC_DIR},
    packages=[PACKAGE],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    version=VERSION,
)
