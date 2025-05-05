import os
import multiprocessing
import time
import math
import openai
import telebot
import subprocess

# === CONFIG ===
openai.api_key = os.getenv("OPENAI_API_KEY") or "sk-...replace_me..."
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN") or "YOUR_TELEGRAM_BOT_TOKEN"
AUTHORIZED_USER_ID = os.getenv("USER_ID") or 123456789  # Ton ID Telegram ici
MAGIC_COMMAND = os.getenv("MAGIC_COMMAND") or "/stop_calc_trhacknon"

UNLOCK_FILE = os.getenv("UNLOCK_FILE") or "/tmp/.unlock_ultracalc"
SERVICE_NAME = "gpt4_calc.service"

# === GPT-4 Generator ===
def get_expr():
    try:
        r = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": "Génère une expression mathématique Python très complexe."}],
            temperature=1.0,
        )
        expr = r.choices[0].message['content'].strip()
        if "```" in expr:
            expr = expr.split("```")[1].strip()
        return expr
    except:
        return "math.log(math.sqrt(42)*math.sin(123))"

# === Worker ===
def worker():
    while not os.path.exists(UNLOCK_FILE):
        try:
            e = get_expr()
            _ = eval(e, {"math": math, "__builtins__": {}})
        except:
            pass
        time.sleep(0.1)

# === Telegram Thread ===
def telegram_listener():
    bot = telebot.TeleBot(TELEGRAM_TOKEN)

    @bot.message_handler(func=lambda m: True)
    def handle_msg(message):
        if message.from_user.id != AUTHORIZED_USER_ID:
            return
        if message.text.strip() == MAGIC_COMMAND:
            bot.send_message(AUTHORIZED_USER_ID, "Arrêt du chaos en cours...")
            stop_all()
            bot.send_message(AUTHORIZED_USER_ID, "Tous les process et le service ont été arrêtés.")

    bot.polling()

# === Stop Function ===
def stop_all():
    try:
        with open(UNLOCK_FILE, "w") as f:
            f.write("UNLOCKED")
        subprocess.run(["systemctl", "stop", SERVICE_NAME])
        subprocess.run(["systemctl", "disable", SERVICE_NAME])
        subprocess.run(["rm", "-f", f"/etc/systemd/system/{SERVICE_NAME}"])
        subprocess.run(["pkill", "-f", "ultra_calc_bot.py"])
    except:
        pass

# === Main ===
def main():
    procs = []
    for _ in range(os.cpu_count() * 2):
        p = multiprocessing.Process(target=worker)
        p.start()
        procs.append(p)

    telegram_proc = multiprocessing.Process(target=telegram_listener)
    telegram_proc.start()
    procs.append(telegram_proc)

    try:
        while not os.path.exists(UNLOCK_FILE):
            time.sleep(2)
    finally:
        for p in procs:
            p.terminate()
        for p in procs:
            p.join()
        if os.path.exists(UNLOCK_FILE):
            os.remove(UNLOCK_FILE)

if __name__ == "__main__":
    main()
