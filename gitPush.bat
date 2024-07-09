echo || "Iniciando"

git init
git add .
git commit -m "Atualizado"
git branch -M main
git push -u origin main

echo || "Terminou"
pause