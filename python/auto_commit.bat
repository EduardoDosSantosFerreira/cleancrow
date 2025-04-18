@echo off
cd /d "C:\Users\Eduardo\Documents\cleancrow\python"
echo ----------- %date% %time% ------------- >> log_autocommit.txt
"C:\Users\Eduardo\AppData\Local\Programs\Python\Python313\python.exe" auto_commit.py >> log_autocommit.txt 2>&1
echo ---------------------------------------- >> log_autocommit.txt
exit
