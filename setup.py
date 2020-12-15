import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bitman-subimal", # Replace with your own username
    version="0.0.1",
    author="Subimal Deb",
    author_email="subimal.deb@gmail.com",
    description="A purepython bit manager",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/subimal/bitman",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU GPLv3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
)
