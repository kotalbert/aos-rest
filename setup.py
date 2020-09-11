from distutils.core import setup

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
    name="aos-rest",
    version="0.1-snapshot",
    packages=["src"],
    url="https://github.com/kotalbert/aos-rest",
    license="WTFPL",
    author="pd",
    author_email="pawel@daniluk.waw.pl",
    description="saos.org.pl scrapper",
)
