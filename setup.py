import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="timeoutqueue",
    version="0.0.1",
    author="Kate Brune",
    author_email="",
    description="a queue that maintains items based on time",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/katebrune/timeout-queue",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
