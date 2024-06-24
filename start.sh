#!/bin/bash

# Télécharger le script get-pip.py
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

# Installer pip
python get-pip.py

# Installer les packages nécessaires
pip install requests beautifulsoup4

# Lancer votre application Flask
python app.py
