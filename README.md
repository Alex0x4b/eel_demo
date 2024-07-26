# Demo to test eel

## Building distributable binary with PyInstaller

If you want to package your app into a program that can be run on a computer without a
Python interpreter installed, you should use **PyInstaller**.

1. Configure a virtualenv with desired Python version and minimum necessary Python
   packages
2. Install PyInstaller `pip install PyInstaller`
3. In your app's folder, run `python -m eel main.py web`
4. This will create a new folder `dist/`
5. Valid PyInstaller flags can be passed through, such as excluding modules with the
   flag: `--exclude module_name`. For example, you might run `python -m eel file_access.py web --exclude win32com --exclude numpy --exclude cryptography`
6. When happy that your app is working correctly, add `--onefile --noconsole` flags too
   build a single executable file. e.g. `python -m eel main.py web --onefile --noconsole`

Consult the [documentation for PyInstaller](http://PyInstaller.readthedocs.io/en/stable/) for more options.
