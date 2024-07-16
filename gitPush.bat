echo || "Iniciando"

git init
git add assets
git add gitPush.bat
git add main.py
git add README.MD
git add req.py
git add requirements.txt
git status
git commit -m "Atualizado"
git branch -M main
git push -u origin main

echo || "Terminou"
pause