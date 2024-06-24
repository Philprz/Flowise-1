@echo off

REM Télécharger le script get-pip.py
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

REM Installer pip
python get-pip.py

REM Détecter le système d'exploitation
python detect_os.py

REM Installer les packages nécessaires
pip install requests beautifulsoup4

REM Lancer votre application Flask
python app.py
