import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='actoolbox',
    version='0.0.3',
    author='AC',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/arunrajChandran/toolbox',
    project_urls = {
        "Bug Tracker": "https://github.com/arunrajChandran/toolbox/issues"
    },
    license='MIT',
    packages=['toolbox'],
    install_requires=['requests'],
)
