import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="proportional_navigation",
    version="1.1.1",
    author="Jan-Hendrik Ewers",
    author_email="jh.ewers@gmail.com",
    description="A package to do proportional navigation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/iwishiwasaneagle/proportional_navigation",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
