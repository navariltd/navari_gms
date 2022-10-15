from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in grants_management_system/__init__.py
from grants_management_system import __version__ as version

setup(
	name="grants_management_system",
	version=version,
	description="A non profit app for grants management",
	author="Navari Limited",
	author_email="info@navari.co.ke",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
