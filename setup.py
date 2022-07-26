from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in qr_demo/__init__.py
from qr_demo import __version__ as version

setup(
	name="qr_demo",
	version=version,
	description="Demo app for printing QR codes",
	author="ALYF GmbH",
	author_email="hallo@alyf.de",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
