# 🦫 MARMOTTE - Installation GitHub pour Marco-Deps

## 📋 Pré-requis

1. **Un compte GitHub** : https://github.com (gratuit)
2. **Git installé** sur ton PC :
   - Windows : https://git-scm.com/download/win
   - Ou dans le Microsoft Store : "Git for Windows"

---

## 🚀 ÉTAPE 1 : Créer le repo sur GitHub

1. Va sur https://github.com
2. Clique sur le **+** en haut à droite → **"New repository"**
3. Remplis :
   - **Repository name** : `marco-deps`
   - **Description** : `A Python dependency manager that understands natural language`
   - ✅ Coche **"Public"**
   - ❌ Ne coche PAS "Add a README file" (on a le nôtre)
   - ❌ Ne coche PAS "Add .gitignore" (on a le nôtre)
   - **License** : Laisse "None" (on a notre fichier LICENSE)
4. Clique **"Create repository"**

---

## 🚀 ÉTAPE 2 : Préparer ton dossier local

Tu as reçu un fichier `marco-deps.zip`. 

1. **Décompresse-le** où tu veux (ex: `C:\Projets\marco-deps`)

2. **Vérifie la structure** :
```
marco-deps/
├── marco_deps.py          ← Le script principal
├── LICENSE                ← GPL v3
├── README.md              ← Doc anglaise
├── README.fr.md           ← Doc française
├── .gitignore             ← Fichiers à ignorer
└── knowledge/
    ├── DEPS_EN.txt        ← Base anglaise
    ├── DEPS_FR.txt        ← Base française
    ├── DEPS_ZH.txt        ← Base chinoise
    ├── DEPS_JA.txt        ← Base japonaise
    ├── DEPS_KO.txt        ← Base coréenne
    └── DEPS_MULTI.txt     ← Base multilingue
```

---

## 🚀 ÉTAPE 3 : Envoyer sur GitHub

Ouvre un terminal (PowerShell ou CMD) dans le dossier `marco-deps` :

```bash
# 1. Initialiser Git
git init

# 2. Ajouter tous les fichiers
git add .

# 3. Premier commit
git commit -m "🚀 Initial release - Marco Dependency Manager v1.0"

# 4. Créer la branche main
git branch -M main

# 5. Connecter à GitHub (remplace TONUSER par ton pseudo GitHub)
git remote add origin https://github.com/TONUSER/marco-deps.git

# 6. Envoyer !
git push -u origin main
```

**GitHub va te demander de te connecter** (une seule fois).

---

## ✅ ÉTAPE 4 : Vérifier

1. Retourne sur https://github.com/TONUSER/marco-deps
2. Tu dois voir tous tes fichiers !
3. Le README.md s'affiche automatiquement en bas

---

## 🎨 BONUS : Ajouter des badges (optionnel)

Dans les paramètres du repo, tu peux :
- Ajouter des "Topics" : `python`, `dependency-manager`, `natural-language`, `multilingual`
- Ajouter une description
- Mettre une URL de site web si tu en as un

---

## 📝 Pour les mises à jour futures

Quand tu modifies un fichier :

```bash
# Voir ce qui a changé
git status

# Ajouter les changements
git add .

# Commiter avec un message
git commit -m "Description de ce que tu as changé"

# Envoyer
git push
```

---

## 🆘 En cas de problème

### "git n'est pas reconnu"
→ Ferme et rouvre le terminal, ou redémarre le PC

### "Permission denied"
→ GitHub te demande de te connecter. Utilise ton pseudo + token (pas le mot de passe).
→ Créer un token : https://github.com/settings/tokens

### "Repository not found"
→ Vérifie l'URL : `https://github.com/TONUSER/marco-deps.git`
→ Vérifie que le repo existe sur GitHub

---

## 📞 Contact

Si t'es bloqué, demande à Marcel (ou à Duke 😉).

---

*"Depuis 40 ans ils font du copier-coller les gros nazes"* - José, 2026
