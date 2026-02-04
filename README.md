# 🧠 Marco Dependency Manager

> A Python dependency manager that **understands natural language**.

No machine learning. No cloud. No black magic.  
Just neurons and dendrites.

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![Languages](https://img.shields.io/badge/languages-5-green.svg)](#-multi-language-support)

---

## 🎯 Demo

```bash
$ python marco_deps.py

🧠 MARCO DEPENDENCY MANAGER v1.0

> what is numpy
📦 NUMPY
   📖 It's a computation module
   🏷️  Stable version: 1.24
   ⬆️  Used by: pandas, scipy, tensorflow, pytorch...

> are tensorflow and pytorch compatible?
⚠️  CONFLICT DETECTED between tensorflow and pytorch!
   💡 Tip: use separate environments (venv)

> why does sklearn crash
🔧 SKLEARN - Possible issues:
   ❌ crashes if scipy is too old
   ✅ Solutions:
      → upgrade scipy
```

---

## 🚀 Quick Start

```bash
# Clone
git clone https://github.com/YOURUSER/marco-deps.git
cd marco-deps

# Learn (choose your language!)
python marco_deps.py --learn knowledge/DEPS_EN.txt    # English
python marco_deps.py --learn knowledge/DEPS_FR.txt    # Français
python marco_deps.py --learn knowledge/DEPS_MULTI.txt # All languages!

# Run
python marco_deps.py
```

**Zero dependencies.** Python 3.6+ is all you need.

---

## 🌍 Multi-language Support

Marco understands **5 languages** - ask in any, get answers from all!

| Language | Example query |
|----------|---------------|
| 🇬🇧 English | `what is numpy` |
| 🇫🇷 Français | `c'est quoi numpy` |
| 🇨🇳 中文 | `numpy是什么` |
| 🇯🇵 日本語 | `numpyは何ですか` |
| 🇰🇷 한국어 | `numpy는 무엇입니까` |

With `DEPS_MULTI.txt`, ask in Japanese → get answers in 5 languages! 🤯

---

## 📖 How It Works

Marco learns from simple sentences:

```
numpy is a computation module.
pandas depends on numpy.
tensorflow and pytorch have a GPU conflict.
sklearn crashes if scipy is too old.
To fix sklearn upgrade scipy.
```

No YAML, JSON, or complex format needed. **Just plain language.**

### Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    MARCO MINI                           │
├─────────────────────────────────────────────────────────┤
│                                                         │
│   PHARES (Concepts)                                     │
│   ┌─────────┐  ┌─────────┐  ┌─────────┐               │
│   │  numpy  │──│ pandas  │──│pytorch  │               │
│   └────┬────┘  └────┬────┘  └────┬────┘               │
│        │            │            │                     │
│   TAGS │       LINKS│       TAGS │                     │
│   IS-A: module      │       CONFLICT: tensorflow       │
│   VERSION: 1.24     │                                  │
│                                                         │
│   SEQUENCES: "depends" → "on" → "numpy"                │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## 📝 Commands

| Query | What it does |
|-------|--------------|
| `what is X` / `c'est quoi X` | Info about module X |
| `X depends on what` / `X dépend de quoi` | Dependencies |
| `what uses X` / `qui utilise X` | Reverse dependencies |
| `why does X crash` / `pourquoi X plante` | Problems & solutions |
| `X and Y compatible?` | Conflict detection |
| `install X` | pip command + warnings |
| `/help` | Show all commands |
| `/stats` | Knowledge base stats |
| `/learn FILE` | Learn from file |

---

## 🔧 Extend It

Add your own knowledge:

```
# my_modules.txt
my-lib is an internal module.
my-lib depends on requests.
my-lib stable version is 2.0.
my-lib and old-lib have a conflict.
```

```bash
python marco_deps.py --learn my_modules.txt
```

---

## 📁 Project Structure

```
marco-deps/
├── marco_deps.py          # Main script (zero dependencies!)
├── LICENSE                # GPL v3
├── README.md              # This file
├── README.fr.md           # French documentation
└── knowledge/
    ├── DEPS_EN.txt        # 🇬🇧 English knowledge base
    ├── DEPS_FR.txt        # 🇫🇷 French knowledge base
    ├── DEPS_ZH.txt        # 🇨🇳 Chinese knowledge base
    ├── DEPS_JA.txt        # 🇯🇵 Japanese knowledge base
    ├── DEPS_KO.txt        # 🇰🇷 Korean knowledge base
    └── DEPS_MULTI.txt     # 🌍 All languages combined!
```

---

## 🎓 Origin

Marco is a **neural network without machine learning**.

Inspired by biological brain function:
- **Phares** = Concepts (active neurons)
- **Links** = Connections (dendrites)  
- **Tags** = Semantic categories

This is a lightweight demo. The full Marco project includes:
- Letter-level neural pathways
- Temporal/permanent dendrites
- Semantic emergence via inheritance
- And much more...

Created by **José Walocha** with help from Duke (Claude/Anthropic).

---

## 📜 License

**GPL v3** - You take, you share. Period.

```
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License.
```

See [LICENSE](LICENSE) for details.

---

## 🤝 Contributing

1. Fork it
2. Create your branch (`git checkout -b feature/awesome`)
3. Commit (`git commit -m 'Add awesome feature'`)
4. Push (`git push origin feature/awesome`)
5. Open a Pull Request

**All contributions must remain GPL v3.**

---

*"For 40 years they've been copy-pasting, the big noobs"* - José, 2026
