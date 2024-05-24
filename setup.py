from setuptools import setup, find_packages

VERSION = "0.0.1"

NAME = "pyquantms"
LICENSE = "MIT License"
DESCRIPTION = "Python package with scripts and helpers for the QuantMS workflow"
AUTHOR = ("Yasset Perez-Riverol, Dai Chengxin")
AUTHOR_EMAIL = "ypriverol@gmail.com"
URL = "https://www.github.com/bigbio/pyquantms"
PROJECT_URLS = {
    "Documentation": "https://docs.quantms.org/en/latest/",
    "quantms Workflow": "https://github.com/bigbio/quantms",
    "Tracker": "https://github.com/bigbio/pyquantms/issues",
}

KEYWORDS = [
    "quantms",
    "Proteomics",
]

CLASSIFIERS = [
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: Apache Software License",
    "Operating System :: POSIX :: Linux",
    "Programming Language :: Python :: 3 :: Only",
    "Topic :: Scientific/Engineering :: Bio-Informatics",
    "Development Status :: 5 - Production/Stable",
]

INSTALL_REQUIRES = ["click", "sdrf_pipelines", "pyopenms", "ms2rescore", "psm-utils", "pydantic"]
PYTHON_REQUIRES = ">=3.7,<4"

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

setup(
    name=NAME,
    version=VERSION,
    license=LICENSE,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    project_urls=PROJECT_URLS,
    keywords=KEYWORDS,
    classifiers=CLASSIFIERS,
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        "console_scripts": [
        ],
    },
    install_requires=INSTALL_REQUIRES,
    python_requires=PYTHON_REQUIRES,
)