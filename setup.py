from setuptools import setup, find_packages

setup(
      name='django-softhyphen',
      version='0.1.6',
      description='A Python library for hyphenating HTML in your Django project',
      author='Ben Welsh',
      author_email='ben.welsh@gmail.com',
      url='https://github.com/datadesk/django-softhyphen/',
      packages=find_packages(),
      zip_safe=False,
      include_package_data=True,
      install_requires=['BeautifulSoup>=3.2.0'],
)
