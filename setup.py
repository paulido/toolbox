import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='toolbox',
    version='dev',
    author='IDO Paul',
    author_email='paulido92mail.com',
    description='toolbox is a package for machine learning. it is used to generate randoms problems of regression and classification',
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir='https://github.com/paulido/toolbox',
    license='MIT',
    packages=['toolbox'],
    install_requires=['requests'],
)