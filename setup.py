from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="eros_api",
    version="0.0.1",
    author="cop",
    author_email="cop@catgir.ls",
    description="an api wrapper for fetching all kinds of social media data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cop-discord/eros",
    download_url = "https://github.com/cop-discord/eros",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "aiohttp>=3.6.1",
        "orjson>=3.8.0",
    ],
    python_requires='>=3.6',
)