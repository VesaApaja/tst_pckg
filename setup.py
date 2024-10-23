from setuptools import setup, find_packages

setup(
    name="tst_pckg",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    author="Vesa",
    author_email="vesa.apaja@iki.fi",
    description="Test package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/VesaApaja/tst_pckg",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
