from setuptools import setup

setup(
    name="django-bfstpw",
    version="1.0.1",
    packages=["bfstpw"],
    include_package_data=True,
    install_requires=["markdown"],
    license="MIT License",
    description="Basic forum software",
    author="Daniel Kessler",
    author_email="sinani201@gmail.com",
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Communications :: BBS",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Message Boards",
    ]
)
