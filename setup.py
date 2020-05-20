import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nnAudio2",
    version="0.0.1",
    author="Helin Wang",
    author_email="wanghl15@pku.edu.cn",
    description="PyTorch implemention of audio processing functions based on nnAudio.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/WangHelin1997/nnAudio2",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
