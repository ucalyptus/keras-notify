import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="keras-notify", 
    version="0.0.1",
    author="Sayantan Das",
    author_email="sayantandas30011998@gmail.com",
    description="A small notification package providing keras events on Telegram or Slack",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/forkbabu/keras-notify",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    keywords='api python keras training callback tensorflow notifications deep learning nlp',
    install_requires=[
      'python-telegram-bot>=12',
      'matplotlib>=3',
      'tensorflow>=2'
      'requests>=2'
    ],    
)
