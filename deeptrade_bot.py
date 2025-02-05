import telebot

# 🔑 Remplace par ton Token API donné par BotFather
API_TOKEN = "7376769587:AAGGT6n40XaMVk4OP1FpDEQYRyHVJRRgF6c"

# Initialise le bot
bot = telebot.TeleBot(API_TOKEN)

# 📌 Commande /start (Message de bienvenue)
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Création du menu interactif avec boutons
    keyboard = InlineKeyboardMarkup()
    
    # Bouton principal vers DeepTrade
    deeptrade_button = InlineKeyboardButton("🌐 Accéder à DeepTrade", url="https://deeptrade.bio.link")
    keyboard.add(deeptrade_button)

    # Boutons pour les autres sections
    keyboard.add(
        InlineKeyboardButton("📝 Inscription", callback_data="inscription"),
        InlineKeyboardButton("📌 FAQ", callback_data="faq")
    )
    keyboard.add(
        InlineKeyboardButton("💰 Parrainage", callback_data="parrainage"),
        InlineKeyboardButton("📊 Gains", callback_data="gains")
    )

    # Envoyer l’image en premier
    with open("A_futuristic_and_professional_landing_page_preview.png", "rb") as photo:
        bot.send_photo(
            message.chat.id, 
            photo, 
            caption="🚀 **Bienvenue sur DeepTrade !**\n\n"
                    "📊 L'IA et la finance au service de tes gains passifs 💰\n"
                    "Clique sur un bouton ci-dessous pour commencer 👇",
            reply_markup=keyboard
        )

# Gestion des boutons cliqués
@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    if call.data == "inscription":
        bot.send_message(call.message.chat.id, "📝 **Comment s’inscrire ?**\n\n"
                                               "1️⃣ Clique ici ➡️ [deeptrade.bio.link](https://deeptrade.bio.link)\n"
                                               "2️⃣ Remplis le formulaire et valide ton inscription.\n"
                                               "3️⃣ Accède aux offres et commence à gagner ! 🚀")
    elif call.data == "faq":
        bot.send_message(call.message.chat.id, "❓ **FAQ DeepTrade** ❓\n\n"
                                               "📌 **Comment commencer ?**\n➡️ Inscris-toi ici : [deeptrade.bio.link](https://deeptrade.bio.link)\n\n"
                                               "📌 **Comment fonctionne le parrainage ?**\n➡️ Chaque inscription avec ton lien te rapporte une commission.\n\n"
                                               "📌 **Quels sont les gains possibles ?**\n➡️ Jusqu'à 220€ offerts aux nouveaux utilisateurs.")
    elif call.data == "parrainage":
        bot.send_message(call.message.chat.id, "🔗 **Programme de Parrainage DeepTrade** 🔗\n\n"
                                               "📌 **Tu veux gagner encore plus ?** Partage ton lien et touche des commissions sur chaque nouvelle inscription !\n\n"
                                               "📌 **Comment ça marche ?**\n"
                                               "1️⃣ Inscris-toi ici ➡️ [deeptrade.bio.link](https://deeptrade.bio.link)\n"
                                               "2️⃣ Obtiens ton lien de parrainage dans ton compte.\n"
                                               "3️⃣ Partage-le partout et regarde tes gains exploser !\n\n"
                                               "🔥 Plus tu invites, plus tu gagnes ! 🔥")
    elif call.data == "gains":
        bot.send_message(call.message.chat.id, "💰 **Gagne jusqu'à 220€ avec DeepTrade !** 💰\n\n"
                                               "📌 1. Inscris-toi ici ➡️ [deeptrade.bio.link](https://deeptrade.bio.link)\n"
                                               "📌 2. Active ton compte et découvre les bonus.\n"
                                               "📌 3. Parraine et touche des commissions à chaque inscription.\n\n"
                                               "🔥 Plus tu invites, plus tu gagnes ! 🔥")





import openai  # Assure-toi d’avoir `openai` installé (pip install openai)
import os
from telebot.types import Message

# 🔑 Mets ici ta clé API OpenAI
OPENAI_API_KEY = "TON_OPENAI_API_KEY"
openai.api_key = OPENAI_API_KEY

@bot.message_handler(func=lambda message: True)  # Répond à tous les messages
def ai_response(message: Message):
    try:
        user_input = message.text
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )
        bot.reply_to(message, response["choices"][0]["message"]["content"])
    except Exception as e:
        bot.reply_to(message, "❌ Erreur avec l'IA, réessaie plus tard !")
        print(e)  # Debug
        
        
        
        
        
       @bot.message_handler(commands=['start'])
def send_welcome(message):
    print(f"✅ Commande /start reçue de {message.chat.id}")
    bot.reply_to(message, "🚀 Bienvenue sur DeepTradeBot !")


# 📌 Lancer le bot en continu
print("✅ DeepTrade Bot en ligne !")
bot.polling()



