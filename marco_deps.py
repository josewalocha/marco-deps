#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║   🧠 MARCO DEPENDENCY MANAGER                                                ║
║   ─────────────────────────────────────────────────────────────────────────  ║
║   A Python dependency manager that UNDERSTANDS what you say.                 ║
║                                                                              ║
║   No machine learning. No cloud. No black magic.                             ║
║   Just neurons and dendrites.                                                ║
║                                                                              ║
║   Author: José Walocha + Duke (Claude)                                       ║
║   Date: February 2026                                                        ║
║   License: GPL v3                                                            ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

USAGE:
    python marco_deps.py                    # Interactive mode
    python marco_deps.py --learn FILE       # Learn from a file
    python marco_deps.py --query "question" # Direct question

EXAMPLES:
    > what is numpy
    > what does pytorch depend on
    > why does sklearn crash
    > are tensorflow and pytorch compatible?
    > I want to install keras

"""

import re
import json
import os
from collections import defaultdict
from typing import Dict, List, Optional, Tuple

# ============================================================================
# CONFIGURATION
# ============================================================================

VERSION = "1.0.0"
MATRIX_FILE = "marco_deps_matrix.json"

# Terminal colors (ANSI)
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'

def colored(text, color):
    """Returns colored text (if terminal supports it)."""
    try:
        if os.isatty(1):
            return f"{color}{text}{Colors.END}"
    except:
        pass
    return text

# ============================================================================
# MARCO MINI - Lightweight version for demo
# ============================================================================

class MarcoMini:
    """
    Minimalist version of Marco for demo.
    
    No letter neurons, just:
    - Beacons (concepts)
    - Links (cooccurrences)
    - Tags (IS-A, DEPENDS-ON, etc.)
    - Sequences (word order)
    """
    
    def __init__(self):
        self.beacons: Dict[str, dict] = {}
        self.sequences: Dict[str, Dict[str, int]] = defaultdict(lambda: defaultdict(int))
        self.cooccurrences: Dict[str, Dict[str, int]] = defaultdict(lambda: defaultdict(int))
        
        # Specialized tags for dependencies
        self.TAGS = [
            "IS-A", "ALIAS-OF", "DEPENDS-ON", "CONFLICTS-WITH",
            "STABLE-VERSION", "SOLUTION-FOR", "REQUIRED-BY"
        ]
    
    def _get_or_create_beacon(self, word: str) -> dict:
        """Gets or creates a beacon."""
        word_lower = word.lower().strip().rstrip('.,;:!?')
        if word_lower not in self.beacons:
            self.beacons[word_lower] = {
                "word": word_lower,
                "links": {},
                "tags": {tag: [] for tag in self.TAGS},
                "activations": 0,
                "contexts": []
            }
        return self.beacons[word_lower]
    
    def learn_sentence(self, sentence: str):
        """Learns from a sentence."""
        # Clean
        sentence = sentence.strip()
        if not sentence or sentence.startswith('#'):
            return
        
        # Tokenize
        words = re.findall(r'\b\w+\b', sentence.lower())
        if len(words) < 2:
            return
        
        # Detect patterns
        self._detect_patterns(sentence)
        
        # Cooccurrences (words that appear together)
        for i, word in enumerate(words):
            beacon = self._get_or_create_beacon(word)
            beacon['activations'] += 1
            beacon['contexts'].append(sentence[:100])
            
            # Link with neighbors (window of 3)
            for j in range(max(0, i-3), min(len(words), i+4)):
                if i != j:
                    other = words[j]
                    self.cooccurrences[word][other] += 1
                    beacon['links'][other] = beacon['links'].get(other, 0) + 1
            
            # Sequences (next word)
            if i < len(words) - 1:
                next_word = words[i + 1]
                self.sequences[word][next_word] += 1
    
    def _detect_patterns(self, sentence: str):
        """Detects semantic patterns in the sentence."""
        s = sentence.lower()
        
        # IS-A: "X is a Y", "X is a Y"
        patterns_is_a = [
            r"(\w+)\s+is\s+(?:a|an)\s+(\w+)",
            r"(\w+)\s+are\s+(\w+)s?",
        ]
        for pattern in patterns_is_a:
            match = re.search(pattern, s)
            if match:
                subject, category = match.groups()
                beacon = self._get_or_create_beacon(subject)
                if category not in beacon['tags']['IS-A']:
                    beacon['tags']['IS-A'].append(category)
        
        # ALIAS: "X is an alias of Y", "X = Y"
        patterns_alias = [
            r"(\w+)\s+is\s+(?:an\s+)?alias\s+(?:of|for)\s+(\w+)",
            r"(\w+)\s*=\s*(\w+)",
        ]
        for pattern in patterns_alias:
            match = re.search(pattern, s)
            if match:
                alias, original = match.groups()
                beacon = self._get_or_create_beacon(alias)
                if original not in beacon['tags']['ALIAS-OF']:
                    beacon['tags']['ALIAS-OF'].append(original)
        
        # DEPENDS-ON: "X depends on Y", "X requires Y"
        patterns_depends = [
            r"(\w+)\s+depends?\s+on\s+(\w+)",
            r"(\w+)\s+requires?\s+(\w+)",
            r"(\w+)\s+needs?\s+(\w+)",
        ]
        for pattern in patterns_depends:
            match = re.search(pattern, s)
            if match:
                dependent, dependency = match.groups()
                beacon = self._get_or_create_beacon(dependent)
                if dependency not in beacon['tags']['DEPENDS-ON']:
                    beacon['tags']['DEPENDS-ON'].append(dependency)
                # Reverse link
                beacon_dep = self._get_or_create_beacon(dependency)
                if dependent not in beacon_dep['tags']['REQUIRED-BY']:
                    beacon_dep['tags']['REQUIRED-BY'].append(dependent)
        
        # CONFLICTS: "X and Y conflict", "X conflicts with Y"
        patterns_conflict = [
            r"(\w+)\s+and\s+(\w+)\s+(?:have\s+a\s+)?conflict",
            r"(\w+)\s+conflicts?\s+with\s+(\w+)",
            r"(\w+)\s+(?:is\s+)?incompatible\s+with\s+(\w+)",
        ]
        for pattern in patterns_conflict:
            match = re.search(pattern, s)
            if match:
                mod1, mod2 = match.groups()
                beacon1 = self._get_or_create_beacon(mod1)
                beacon2 = self._get_or_create_beacon(mod2)
                if mod2 not in beacon1['tags']['CONFLICTS-WITH']:
                    beacon1['tags']['CONFLICTS-WITH'].append(mod2)
                if mod1 not in beacon2['tags']['CONFLICTS-WITH']:
                    beacon2['tags']['CONFLICTS-WITH'].append(mod1)
        
        # VERSION: "X stable version is Y"
        patterns_version = [
            r"(\w+)\s+stable\s+version\s+(?:is\s+)?(\d+[\d\.]*)",
            r"(\w+)\s+version\s+(\d+[\d\.]*)\s+(?:is\s+)?stable",
        ]
        for pattern in patterns_version:
            match = re.search(pattern, s)
            if match:
                module, version = match.groups()
                beacon = self._get_or_create_beacon(module)
                beacon['tags']['STABLE-VERSION'] = [version]
        
        # SOLUTION: "to fix X you need Y", "solution for X is Y"
        patterns_solution = [
            r"to\s+fix\s+(\w+).*?(?:you\s+need|install|use)\s+(\w+)",
            r"solution\s+for\s+(\w+).*?(?:is|:)\s+(\w+)",
            r"if\s+(\w+)\s+crashes?.*?(?:upgrade|update|install)\s+(\w+)",
        ]
        for pattern in patterns_solution:
            match = re.search(pattern, s)
            if match:
                problem, solution = match.groups()
                beacon = self._get_or_create_beacon(problem)
                if solution not in beacon['tags']['SOLUTION-FOR']:
                    beacon['tags']['SOLUTION-FOR'].append(solution)
        
        # CRASH: "X crashes if Y"
        patterns_crash = [
            r"(\w+)\s+crashes?\s+(?:if|when|because)\s+(.+)",
        ]
        for pattern in patterns_crash:
            match = re.search(pattern, s)
            if match:
                module, reason = match.groups()
                beacon = self._get_or_create_beacon(module)
                beacon['contexts'].append(f"crashes: {reason[:50]}")
    
    def learn_file(self, filepath: str) -> int:
        """Learns from a file. Returns number of sentences learned."""
        count = 0
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                # Split on periods for multiple sentences
                for sentence in re.split(r'[.!?\n]', line):
                    sentence = sentence.strip()
                    if sentence:
                        self.learn_sentence(sentence)
                        count += 1
        return count
    
    def save_matrix(self, filepath: str = None):
        """Saves the matrix to JSON."""
        filepath = filepath or MATRIX_FILE
        data = {
            "version": VERSION,
            "beacons": self.beacons,
            "stats": {
                "beacons": len(self.beacons),
                "cooccurrences": sum(len(v) for v in self.cooccurrences.values())
            }
        }
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    
    def load_matrix(self, filepath: str = None) -> bool:
        """Loads a saved matrix."""
        filepath = filepath or MATRIX_FILE
        if not os.path.exists(filepath):
            return False
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        self.beacons = data.get('beacons', {})
        return True
    
    def answer(self, question: str) -> str:
        """Answers a question."""
        q = question.lower().strip()
        
        # WHAT IS X
        patterns_what = [
            r"what\s+is\s+(\w+)",
            r"what'?s\s+(\w+)",
            r"tell\s+me\s+about\s+(\w+)",
        ]
        for pattern in patterns_what:
            match = re.search(pattern, q)
            if match:
                return self._answer_what_is(match.group(1))
        
        # X DEPENDS ON WHAT
        patterns_depends = [
            r"what\s+does\s+(\w+)\s+depend\s+on",
            r"(\w+)\s+depends?\s+on\s+what",
            r"dependencies\s+(?:of|for)\s+(\w+)",
        ]
        for pattern in patterns_depends:
            match = re.search(pattern, q)
            if match:
                return self._answer_dependencies(match.group(1))
        
        # WHO USES X
        patterns_uses = [
            r"who\s+uses?\s+(\w+)",
            r"what\s+uses?\s+(\w+)",
            r"what\s+requires?\s+(\w+)",
        ]
        for pattern in patterns_uses:
            match = re.search(pattern, q)
            if match:
                return self._answer_required_by(match.group(1))
        
        # WHY DOES X CRASH
        patterns_crash = [
            r"why\s+(?:does\s+)?(\w+)\s+crash",
            r"(\w+)\s+(?:is\s+)?crashing",
            r"(\w+)\s+doesn'?t?\s+work",
        ]
        for pattern in patterns_crash:
            match = re.search(pattern, q)
            if match:
                return self._answer_why_crash(match.group(1))
        
        # X AND Y COMPATIBLE?
        patterns_compat = [
            r"(?:are\s+)?(\w+)\s+and\s+(\w+)\s+compatible",
            r"can\s+(?:i\s+)?use\s+(\w+)\s+with\s+(\w+)",
            r"(\w+)\s+(?:works?\s+)?with\s+(\w+)\s*\?",
        ]
        for pattern in patterns_compat:
            match = re.search(pattern, q)
            if match:
                return self._answer_compatibility(match.group(1), match.group(2))
        
        # INSTALL X
        patterns_install = [
            r"(?:how\s+(?:do\s+i\s+)?)?install\s+(\w+)",
            r"i\s+want\s+(?:to\s+)?install\s+(\w+)",
        ]
        for pattern in patterns_install:
            match = re.search(pattern, q)
            if match:
                return self._answer_install(match.group(1))
        
        # Default: search for relevant beacon
        words = re.findall(r'\b\w+\b', q)
        for word in words:
            if word in self.beacons:
                return self._answer_what_is(word)
        
        return "❓ I don't understand the question. Try: what is numpy"
    
    def _answer_what_is(self, module: str) -> str:
        """Answers 'what is X'."""
        beacon = self.beacons.get(module.lower())
        if not beacon:
            return f"❓ I don't know '{module}'. Use /learn file.txt to teach me."
        
        lines = [f"📦 {colored(module.upper(), Colors.BOLD)}"]
        
        # IS-A
        is_a = beacon['tags'].get('IS-A', [])
        if is_a:
            lines.append(f"   📖 It's a {', '.join(is_a)}")
        
        # ALIAS
        aliases = beacon['tags'].get('ALIAS-OF', [])
        if aliases:
            lines.append(f"   🔗 Alias of: {', '.join(aliases)}")
        
        # VERSION
        version = beacon['tags'].get('STABLE-VERSION', [])
        if version:
            lines.append(f"   🏷️ Stable version: {version[0]}")
        
        # DEPENDS-ON
        deps = beacon['tags'].get('DEPENDS-ON', [])
        if deps:
            lines.append(f"   📋 Depends on: {', '.join(deps)}")
        
        # CONFLICTS
        conflicts = beacon['tags'].get('CONFLICTS-WITH', [])
        if conflicts:
            lines.append(f"   ⚠️ Conflicts with: {colored(', '.join(conflicts), Colors.YELLOW)}")
        
        return '\n'.join(lines)
    
    def _answer_dependencies(self, module: str) -> str:
        """Answers 'what does X depend on'."""
        beacon = self.beacons.get(module.lower())
        if not beacon:
            return f"❓ I don't know '{module}'."
        
        deps = beacon['tags'].get('DEPENDS-ON', [])
        if not deps:
            return f"📦 {module} has no known dependencies."
        
        lines = [f"📦 {colored(module.upper(), Colors.BOLD)} depends on:"]
        for dep in deps:
            lines.append(f"   └─ {dep}")
        
        return '\n'.join(lines)
    
    def _answer_required_by(self, module: str) -> str:
        """Answers 'who uses X'."""
        beacon = self.beacons.get(module.lower())
        if not beacon:
            return f"❓ I don't know '{module}'."
        
        required = beacon['tags'].get('REQUIRED-BY', [])
        if not required:
            return f"📦 No known module depends on {module}."
        
        lines = [f"📦 {colored(module.upper(), Colors.BOLD)} is used by:"]
        for r in required:
            lines.append(f"   └─ {r}")
        
        return '\n'.join(lines)
    
    def _answer_why_crash(self, module: str) -> str:
        """Answers 'why does X crash'."""
        beacon = self.beacons.get(module.lower())
        if not beacon:
            return f"❓ I don't know '{module}'."
        
        # Search in contexts
        problems = [c for c in beacon.get('contexts', []) if 'crash' in c]
        solutions = beacon['tags'].get('SOLUTION-FOR', [])
        deps = beacon['tags'].get('DEPENDS-ON', [])
        
        lines = [f"🔧 {colored(module.upper(), Colors.BOLD)} - Possible issues:"]
        
        if problems:
            for p in problems:
                lines.append(f"   ❌ {p}")
        
        if deps:
            lines.append(f"\n   📋 Check dependencies: {', '.join(deps)}")
        
        if solutions:
            lines.append(f"\n   ✅ Solutions:")
            for s in solutions:
                lines.append(f"      → {s}")
        
        if not problems and not solutions:
            lines.append("   🤷 No crash info for this module.")
        
        return '\n'.join(lines)
    
    def _answer_compatibility(self, mod1: str, mod2: str) -> str:
        """Answers 'are X and Y compatible?'."""
        beacon1 = self.beacons.get(mod1.lower())
        beacon2 = self.beacons.get(mod2.lower())
        
        if not beacon1 or not beacon2:
            unknown = 'both' if not beacon1 and not beacon2 else mod1 if not beacon1 else mod2
            return f"❓ I don't know {unknown}."
        
        conflicts1 = beacon1['tags'].get('CONFLICTS-WITH', [])
        conflicts2 = beacon2['tags'].get('CONFLICTS-WITH', [])
        
        if mod2.lower() in conflicts1 or mod1.lower() in conflicts2:
            return f"⚠️ {colored('CONFLICT DETECTED', Colors.RED)} between {mod1} and {mod2}!\n   💡 Tip: use separate environments (venv)"
        
        return f"✅ {colored('Compatible', Colors.GREEN)}: {mod1} and {mod2} can coexist."
    
    def _answer_install(self, module: str) -> str:
        """Answers 'install X'."""
        beacon = self.beacons.get(module.lower())
        
        lines = [f"📥 Installing {colored(module, Colors.BOLD)}:"]
        lines.append(f"   $ pip install {module}")
        
        if beacon:
            deps = beacon['tags'].get('DEPENDS-ON', [])
            if deps:
                lines.append(f"\n   📋 Will also install: {', '.join(deps)}")
            
            conflicts = beacon['tags'].get('CONFLICTS-WITH', [])
            if conflicts:
                lines.append(f"\n   ⚠️ {colored('Warning', Colors.YELLOW)}: may conflict with {', '.join(conflicts)}")
                lines.append("   💡 Tip: check with 'pip list' first")
        
        return '\n'.join(lines)
    
    def stats(self) -> str:
        """Returns statistics."""
        total_links = sum(len(b.get('links', {})) for b in self.beacons.values())
        total_tags = sum(
            sum(len(v) for v in b.get('tags', {}).values())
            for b in self.beacons.values()
        )
        
        return f"""
📊 MARCO STATS
────────────────────────────
Beacons (concepts):  {len(self.beacons):>6}
Links:               {total_links:>6}
Tags:                {total_tags:>6}
"""


# ============================================================================
# INTERACTIVE CLI
# ============================================================================

def banner():
    """Displays the startup banner."""
    print(colored("""
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║   🧠 MARCO DEPENDENCY MANAGER v1.0                        ║
║   ──────────────────────────────────────────────────────  ║
║   The dependency manager that UNDERSTANDS English.        ║
║                                                           ║
║   Commands: /help, /stats, /quit                          ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
""", Colors.CYAN))


def help_message():
    """Displays help."""
    print("""
📖 HELP
────────────────────────────────────────────────

COMMANDS:
  /help              Show this help
  /stats             Show statistics
  /learn FILE        Learn from a text file
  /save              Save the matrix
  /quit              Quit

QUESTIONS (in English):
  what is numpy
  what does pytorch depend on
  why does sklearn crash
  are tensorflow and pytorch compatible?
  install keras

LEARNING (example content):
  numpy is a computation module.
  pandas depends on numpy.
  tensorflow and pytorch have a conflict.
  sklearn crashes if scipy is too old.
  To fix sklearn upgrade scipy.
""")


def interactive():
    """Interactive mode."""
    banner()
    
    marco = MarcoMini()
    
    # Try to load existing matrix
    if marco.load_matrix():
        print(f"📂 Matrix loaded: {len(marco.beacons)} beacons")
    else:
        print(colored("💡 Empty base. Use '/learn file.txt' to learn.", Colors.YELLOW))
    
    while True:
        try:
            query = input(colored("\n> ", Colors.GREEN)).strip()
        except (EOFError, KeyboardInterrupt):
            print("\n👋 Bye!")
            break
        
        if not query:
            continue
        
        # Commands
        if query.startswith('/'):
            parts = query.split(maxsplit=1)
            cmd = parts[0].lower()
            
            if cmd == '/quit' or cmd == '/q':
                print("👋 Bye!")
                break
            
            elif cmd == '/help' or cmd == '/h':
                help_message()
            
            elif cmd == '/stats':
                print(marco.stats())
            
            elif cmd == '/save':
                marco.save_matrix()
                print("✅ Matrix saved.")
            
            elif cmd == '/learn':
                if len(parts) < 2:
                    print("❌ Usage: /learn filename.txt")
                else:
                    filepath = parts[1].strip('"\'')
                    if os.path.exists(filepath):
                        count = marco.learn_file(filepath)
                        marco.save_matrix()
                        print(f"✅ {count} sentences learned. Matrix saved.")
                    else:
                        print(f"❌ File not found: {filepath}")
            
            else:
                print(f"❓ Unknown command: {cmd}")
        
        else:
            # Question
            response = marco.answer(query)
            print(response)


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        # CLI mode
        if sys.argv[1] == '--learn' and len(sys.argv) > 2:
            marco = MarcoMini()
            count = marco.learn_file(sys.argv[2])
            marco.save_matrix()
            print(f"✅ {count} sentences learned. Matrix saved.")
        
        elif sys.argv[1] == '--query' and len(sys.argv) > 2:
            marco = MarcoMini()
            marco.load_matrix()
            question = ' '.join(sys.argv[2:])
            print(marco.answer(question))
        
        else:
            print("Usage:")
            print("  python marco_deps.py                    # Interactive")
            print("  python marco_deps.py --learn FILE       # Learn")
            print("  python marco_deps.py --query 'question' # Query")
    else:
        # Interactive mode
        interactive()
