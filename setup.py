import setuptools
from nlpwiz.version import Version


setuptools.setup(name='nlpwiz',
                 version=Version('1.1.1').number,
                 description='Python Package Boilerplate',
                 long_description=open('README.md').read().strip(),
                 author='Author Name',
                 author_email='email@domain.com',
                 url='https://github.com/vymana/nlpwiz',
                 py_modules=['nlpwiz'],
                 install_requires=[],
                 packages=setuptools.find_packages(),
                 license='MIT License',
                 zip_safe=False,
                 keywords='boilerplate package',
                 classifiers=['Packages', 'nlpwiz'],
                 packages=['nlpwiz'])
