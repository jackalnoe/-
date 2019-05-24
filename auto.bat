@echo off

cd d:\python\auto

echo 自动签到 lxwc starting...
"d:\ProgramData\python.exe"  d:\python\auto\lxwcqd.py
echo 自动签到结束
echo 自动签到 pinggu starting...
"d:\ProgramData\python.exe"  d:\python\auto\pg.py
echo 自动签到结束
exit
