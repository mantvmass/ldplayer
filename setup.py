from setuptools import setup, find_packages

setup(
    name="ldplayer",
    packages=find_packages(),
    version="0.0.1",
    description="This is package for ldplayer emulator control software. (unofficial)",
    author="mantvmass",
    maintainer="Phumin Maliwan",
    maintainer_email="kliop2317@gmail.com",
    url="https://github.com/mantvmass/ldplayer",
    # long_description=open("README.md").read(),
    install_requires=[
        "pure-python-adb",
    ]
)
