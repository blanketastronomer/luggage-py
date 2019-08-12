import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name="luggage-py",
    version='0.0.1',
    author='blanketastronomer <Nicholas S.>',
    description='Take your programs with you wherever you go!',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/blanketastronomer/luggage-py',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ]
)