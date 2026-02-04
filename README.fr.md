# 🧠 Marco Dependency Manager

> Un gestionnaire de dépendances Python qui **comprend le français**.

Pas de machine learning. Pas de cloud. Pas de magie noire.  
Juste des neurones et des dendrites.

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![Langues](https://img.shields.io/badge/langues-5-green.svg)](#-support-multilingue)

---

## 🎯 Démo

```bash
$ python marco_deps.py

🧠 MARCO DEPENDENCY MANAGER v1.0

> c'est quoi numpy
📦 NUMPY
   📖 C'est un module de calcul
   🏷️  Version stable : 1.24
   ⬆️  Utilisé par : pandas, scipy, tensorflow, pytorch...

> tensorflow et pytorch compatible ?
⚠️  CONFLIT DÉTECTÉ entre tensorflow et pytorch !
   💡 Conseil : utiliser des environnements séparés (venv)

> pourquoi sklearn plante
🔧 SKLEARN - Problèmes possibles :
   ❌ plante si scipy est trop vieux
   ✅ Solutions :
      → mettre à jour scipy
```

---

## 🚀 Démarrage Rapide

```bash
# Cloner
git clone https://github.com/YOURUSER/marco-deps.git
cd marco-deps

# Apprendre (choisis ta langue !)
python marco_deps.py --learn knowledge/DEPS_FR.txt     # Français
python marco_deps.py --learn knowledge/DEPS_EN.txt     # English
python marco_deps.py --learn knowledge/DEPS_MULTI.txt  # Toutes les langues !

# Lancer
python marco_deps.py
```

**Zéro dépendance.** Python 3.6+ suffit.

---

## 🌍 Support Multilingue

Marco comprend **5 langues** - pose ta question dans n'importe laquelle !

| Langue | Exemple |
|--------|---------|
| 🇫🇷 Français | `c'est quoi numpy` |
| 🇬🇧 English | `what is numpy` |
| 🇨🇳 中文 | `numpy是什么` |
| 🇯🇵 日本語 | `numpyは何ですか` |
| 🇰🇷 한국어 | `numpy는 무엇입니까` |

Avec `DEPS_MULTI.txt`, pose en japonais → reçois des réponses en 5 langues ! 🤯

---

## 📖 Comment ça marche

Marco apprend depuis des phrases simples :

```
numpy est un module de calcul.
pandas dépend de numpy.
tensorflow et pytorch ont un conflit GPU.
sklearn plante si scipy est trop vieux.
Pour sklearn qui plante il faut mettre à jour scipy.
```

Pas de YAML, JSON, ou format compliqué. **Du français.**

---

## 📝 Commandes

| Question | Réponse |
|----------|---------|
| `c'est quoi X` | Infos sur le module X |
| `X dépend de quoi` | Dépendances de X |
| `qui utilise X` | Modules qui dépendent de X |
| `pourquoi X plante` | Problèmes et solutions |
| `X et Y compatible ?` | Détection de conflits |
| `installer X` | Commande pip + avertissements |
| `/help` | Afficher l'aide |
| `/stats` | Stats de la base |
| `/learn FICHIER` | Apprendre depuis un fichier |

---

## 🔧 Personnalisation

Ajoute tes propres connaissances :

```
# mes_modules.txt
mon-lib est un module interne.
mon-lib dépend de requests.
mon-lib version stable est 2.0.
```

```bash
python marco_deps.py --learn mes_modules.txt
```

---

## 🎓 Origine

Marco est un **réseau de neurones sans machine learning**.

Inspiré par le fonctionnement biologique du cerveau :
- **Phares** = Concepts (neurones actifs)
- **Liens** = Connexions (dendrites)
- **Tags** = Catégories sémantiques

Ceci est une démo légère. Le projet Marco complet inclut :
- Chemins neuronaux lettre par lettre
- Dendrites temporaires/permanentes
- Émergence sémantique par héritage
- Et bien plus...

Créé par **José Walocha** avec l'aide de Duke (Claude/Anthropic).

---

## 📜 Licence

**GPL v3** - Tu prends, tu partages. Point.

```
Ce programme est un logiciel libre : vous pouvez le redistribuer
et/ou le modifier selon les termes de la GNU General Public License.
```

Voir [LICENSE](LICENSE) pour les détails.

---

*"Depuis 40 ans ils font du copier-coller les gros nazes"* - José, 2026
