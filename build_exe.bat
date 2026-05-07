@echo off
echo =====================================
echo     正在安裝必要套件...
echo =====================================
pip install pyinstaller --quiet

echo.
echo =====================================
echo     正在打包成 .exe 執行檔...
echo =====================================
pyinstaller --onefile --windowed --icon=icon.ico --name=multiplication_table_gui multiplication_table_gui.py

echo.
echo =====================================
echo     打包完成！
echo     執行檔位置： dist\multiplication_table_gui.exe
echo =====================================
pause