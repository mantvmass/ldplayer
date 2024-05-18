@echo off

@REM clear old build folder
rmdir /s /q dist
rmdir /s /q build
rmdir /s /q ldplayer_tools.egg-info

@REM building...
python setup.py sdist bdist_wheel

@REM pause