"""Setup script for ``{{ cookiecutter.project_slug }}``.

Written by Jesse Bloom.
"""

import re
from setuptools import setup
import sys

if not (sys.version_info[0] == 3 and sys.version_info[1] >= 6):
    raise RuntimeError(
                '{{ cookiecutter.project_slug }} requires Python 3.6 or higher.\n'
                'You are using Python {0}.{1}'.format(
                sys.version_info[0], sys.version_info[1])
                )

# get metadata from package `__init__.py` file as here:
# https://packaging.python.org/guides/single-sourcing-package-version/
metadata = {}
init_file = '{{ cookiecutter.project_slug }}/__init__.py'
with open(init_file) as f:
    init_text = f.read()
for dataname in ['version', 'author', 'email', 'url']:
    matches = re.findall(
            '__' + dataname + r'__\s+=\s+[\'"]([^\'"]+)[\'"]',
            init_text)
    if len(matches) != 1:
        raise ValueError(f"found {len(matches)} matches for {dataname} "
                         f"in {init_file}")
    else:
        metadata[dataname] = matches[0]

with open('README.rst') as f:
    readme = f.read()

# main setup command
setup(
    name='{{ cookiecutter.project_slug }}',
    version=metadata['version'],
    author=metadata['author'],
    author_email=metadata['email'],
    url=metadata['url'],
    download_url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/tarball/' +
                 metadata['version'],  # tagged version on GitHub
    description='{{ cookiecutter.project_short_description }}',
    long_description=readme,
    license='GPLv3',
    install_requires=[],
    platforms='Linux and Mac OS X.',
    packages=['{{ cookiecutter.project_slug }}'],
    package_dir={'{{ cookiecutter.project_slug }}': '{{ cookiecutter.project_slug }}'},
)
