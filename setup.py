from setuptools import setup, find_packages

setup(
    name="scrimmage-sdk",
    version="1.0.3",
    description="Simple rewards for your app or website",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Scrimmage Co <founders@scrimmage.co>",
    author_email="founders@scrimmage.co",
    license="MIT",
    url="https://github.com/Scrimmage-co/python-sdk",
    packages=find_packages(),
    install_requires=[
        "dependency-injector",
        "httpx",
        "pydantic",
    ],
    keywords=[
        "scrimmage",
        "reward",
        "rewards",
        "loyalty",
        "api",
        "sdk",
        "python"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)