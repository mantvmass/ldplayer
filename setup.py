from setuptools import setup, find_packages

VERSION = "0.0.2"
DESCRIPTION = "This is package for ldplayer emulator control software. (unofficial)"

setup(
    name="ldplayer-tools",
    packages=find_packages(),
    version=VERSION,
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=open("README.md").read(),
    author="mantvmass (Phumin Maliwan)",
    author_email="kliop2317@gmail.com",
    maintainer="mantvmass (Phumin Maliwan)",
    maintainer_email="kliop2317@gmail.com",
    url="https://github.com/mantvmass/ldplayer",
    install_requires=["pure-python-adb"],
    keywords=["python", "ldplayer", "ldplayer-tools", "python-ldplayer"]
)
