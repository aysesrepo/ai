isim = input("isminiz Nedir?")

yemek = input("En sevdiginiz yemek nedir?")

print(isim +" "+ yemek+" "+"sever")

echo "# {repo_name}" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/{username}/{repo_name}.git
git push -u origin main