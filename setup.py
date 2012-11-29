# -*- encoding: utf-8 -*-
#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name = 'ooniprobe',
      version = '0.0.7-alpha',
      description = 'The Open Observatory of Network Interference',
      long_description = open('README.md').read(),
      author = 'Arturo Filastò',
      author_email = 'art@torproject.org',
      url = 'https://ooni.torproject.org/',
      scripts = [
          'bin/ooniprobe',
          'bin/oonib'
          ],
      license = 'LICENSE',
      install_requires = open('requirements.txt').readlines(),
      packages = find_packages()
)
