from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in human_resource/__init__.py
from human_resource import __version__ as version

setup(
	name="human_resource",
	version=version,
	description="New Human Resource App",
	author="mtabualatta",
	author_email="mtabualatta@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
