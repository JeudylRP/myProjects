#!/bin/bash

# Versuche, ein einfaches Python-Skript auszuführen, das die openai Bibliothek importiert
python - <<EOF
try:
    import openai
    print("Die 'openai' Bibliothek ist korrekt installiert.")
except ImportError:
    print("Die 'openai' Bibliothek ist nicht installiert.")
EOF
