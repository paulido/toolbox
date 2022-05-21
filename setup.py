import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="toolbox",
    version="0.0.1",
    author="IDO PAUL",
    author_email="paulido92@gmail.com",
    description="toolbox is python machine learning package. It is serve for generate randoms regression and classification problems",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/paulido/toolbox",
    project_urls={
        "Bug Tracker": "https://github.com/ido/toolbox/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)