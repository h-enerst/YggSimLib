from setuptools import setup, find_packages

setup(
  name="YggSimLib",
  version="0.1",
  author="Håkon Enerstvedt",  
  description="A library for interfacing with the kspice API for the Yggdrasil project",
  long_description="open("README.md").read(),
  long_description_content_type="text/markdown",
  packages=find_packages(),
  install_requires=[
    "tkinter",
    "networkx"
    ]
  python_requires='>=3.12'
)

