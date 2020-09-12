#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

setup(
    install_requires=[
        "beautifulsoup4==4.9.1",
        "boto3==1.14.59",
        "botocore==1.17.59",
        "certifi==2020.6.20",
        "chardet==3.0.4",
        "docutils==0.15.2; python_version >= '2.6' and python_version not in '3.0, 3.1, 3.2, 3.3'",
        "idna==2.10; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
        "jmespath==0.10.0; python_version >= '2.6' and python_version not in '3.0, 3.1, 3.2, 3.3'",
        "python-dateutil==2.8.1; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
        "requests==2.24.0",
        "s3transfer==0.3.3",
        "six==1.15.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
        "soupsieve==2.0.1; python_version >= '3.5'",
        "urllib3==1.25.10; python_version != '3.4'",
    ],
    author="Pawel Daniluk",
    author_email="pawel@daniluk.waw.pl",
    python_requires=">=3.5",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="Client for downloading court judjements from open government api.",
    entry_points={"console_scripts": ["aos_rest=aos_rest.cli:main",],},
    license="Apache Software License 2.0",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="aos_rest",
    name="aos_rest",
    packages=find_packages(include=["aos_rest", "aos_rest.*"]),
    url="https://github.com/kotalbert/aos_rest",
    version="0.1.0",
    zip_safe=False,
)
