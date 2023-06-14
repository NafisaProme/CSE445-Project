@echo off
start %windir%\System32\cmd.exe "/K" D:\ProgramData\Anaconda3\Scripts\activate.bat D:\ProgramData\Anaconda3 
cd webview 
conda activate myenv
streamlit run main.py