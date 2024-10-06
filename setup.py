import glob
import os
import unittest

from setuptools import find_packages, setup
from setuptools.command.build_py import build_py

with open("README.md", "rt") as fh:
    long_description = fh.read()

with open("requirements.txt", "rt") as f:
    requirements = [r.strip() for r in f.readlines()]


class PublishCommand(build_py):
    """Publish package to PyPI"""
    def run(self):
        os.system("rm -rf dist")
        os.system("python3 setup.py sdist"
                  "&& python3 setup.py bdist_wheel"
                  "&& python3 -m twine upload dist/*whl dist/*gz")

setup(
    name='SMNCopyNumberCaller',
    version="1.1.2",
    description="A copy number caller for SMN1 and SMN2 to enable SMA diagnosis and carrier screening with WGS",
    install_requires=requirements,
    cmdclass={
        'publish': PublishCommand,
    },
    entry_points = {
        'console_scripts': [
            'smn_caller = smn_caller.smn_caller:main',
            'smn_charts = smn_caller.smn_charts:main',            
        ],
    },
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=[
    	"smn_caller",
    	"smn_caller.caller",
    	"smn_caller.charts",
    	"smn_caller.charts.svgs",
    	"smn_caller.charts.pdfs",
		"smn_caller.depth_calling",
		"smn_caller.data",
    ],
    package_dir={"": ""},
    include_package_data=True,
    python_requires=">=3.9",
    license="PolyForm Strict License 1.0.0",
    keywords="",
    url="https://github.com/Illumina/SMNCopyNumberCaller",
    classifiers=[
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
)
