import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(name='keras-notify',
      description='Keras Model notifier on Telegram and Slack',
      long_description=long_description,
      long_description_content_type="text/markdown",
      version='0.0.1',
      url='https://github.com/forkbabu/keras-notify',
      author='Sayantan Das',
      author_email='sayantandas30011998@gmail.com',
      license='GNU General Public License v3 (GPLv3)',
      classifiers=[
          'Development Status :: Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Programming Language :: Python 3'
      ],
      keywords='api python keras training callback tensorflow notifications deep learning nlp',
      install_requires=[
        'python-telegram-bot>=12',
        'matplotlib>=3',
        'tensorflow>=2'
        'requests>=2'
      ],
      packages=setuptools.find_packages(),
      python_requires='>=3.6'
)
