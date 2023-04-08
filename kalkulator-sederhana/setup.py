from setuptools import setup, find_packages


setup(
    name='kalkulator-sederhana',
    version='0.6',
    license='MIT',
    author="Sopyan Syauri",
    author_email='rifai.sopyan04@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/sopyansyauri/module/tree/master/kalkulator',
    keywords='example project',
    install_requires=[
          'numpy',
      ],

)