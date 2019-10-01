from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(name='invert_pdf_color',
      version='1.0.0',
      description='A package for easily inverting the color of pdf documents',
      url='https://github.com/Lyonk71/invert-pdf-color',
      author='Keith Lyons',
      author_email='lyonk71@gmail.com',
      license='',
      packages=['invert_pdf_color'],
      install_requires=[
          'pdf2image',
          'pillow',
          'img2pdf',
      ],
      zip_safe=False,
      
      #Enable pypi description
      long_description=long_description,
      long_description_content_type="text/markdown")
