#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import setuptools

if __name__ == '__main__':
    setuptools.setup(
        name='OhlohWidgetsMacro',
        version='0.1',
        
        description='Trac macro to embed Ohloh widgets',
        author='Felix Schwarz',
        author_email='felix.schwarz@oss.schwarz.eu',
        #url=url,
        #download_url=download_url,
        license='MIT',
        
        install_requires=['genshi', 'trac >= 0.11', 'pycerberus >= 0.3'],
        
        zip_safe=True,
        packages=setuptools.find_packages(),
        classifiers = [
            'Development Status :: 4 - Beta',
            'Framework :: Trac',
            'Intended Audience :: System Administrators',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Software Development :: Libraries :: Python Modules',
        ],
        entry_points = {
            'trac.plugins': [
                'ohloh_widgets.macro = ohloh_widgets.macro',
                'ohloh_widgets.modifiers = ohloh_widgets.modifiers',
            ]
        }
    )


