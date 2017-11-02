python C:\Python34\Lib\site-packages\PyQt4\uic\pyuic.py .\window.ui -o window.py

echo "# pyqt4Bio" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/mohamedhamidat/pyqt4Bio.git
git push -u origin master