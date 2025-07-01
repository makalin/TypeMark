from setuptools import setup, find_packages

setup(
    name='typemark',
    version='0.1.0',
    description='Markdown to Aesthetic PDF converter with themes and doodles',
    author='makalin',
    packages=find_packages(),
    install_requires=[
        'pandocfilters',
        'weasyprint',
    ],
    extras_require={
        'web': ['flask'],
    },
    entry_points={
        'console_scripts': [
            'typemark=typemark.cli:main',
        ],
    },
    include_package_data=True,
) 