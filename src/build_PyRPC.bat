@echo off
echo Building PyRPC

echo Installing pyinstaller...
pip install pyinstaller > NUL 2>&1
echo Installed pyinstaller!

echo Building exe...
pyinstaller --onefile PyRPC.py > build_log.txt 2>&1
echo Built exe!

echo Copying exe file...
copy /Y dist\PyRPC.exe . > NUL
echo Copied exe file!

echo Cleaning up...
rmdir /s /q build > NUL
rmdir /s /q dist > NUL
del /q PyRPC.spec > NUL
echo Cleaned up!

echo Done!
pause > NUL
