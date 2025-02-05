import telebot
import openai
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# 🔑 Clés API
API_TOKEN = "TON_TOKEN_TELEGRAM"
OPENAI_API_KEY = "TA_CLE_OPENAI"
openai.api_key = OPENAI_API_KEY

# 🔥 Initialisation du bot
bot = telebot.TeleBot(API_TOKEN)

# ✅ 📌 **Commande /start** : Accueil interactif avec DeepTrade Hub
@bot.message_handler(commands=['start'])
def send_welcome(message):
    keyboard = InlineKeyboardMarkup()
    deeptrade_hub = InlineKeyboardButton("🌐 Accéder à DeepTrade Hub", url="https://deeptrade.bio.link")
    keyboard.add(deeptrade_hub)

    keyboard.add(
        InlineKeyboardButton("📝 Inscription", callback_data="inscription"),
        InlineKeyboardButton("📌 FAQ", callback_data="faq")
    )
    keyboard.add(
        InlineKeyboardButton("💰 Parrainage", callback_data="parrainage"),
        InlineKeyboardButton("📊 Investissements", callback_data="invest")
    )

    with open("deeptrade_hub_banner.png", "rb") as photo:
        bot.send_photo(
            message.chat.id, 
            photo, 
            caption="🚀 **Bienvenue sur DeepTrade Hub !**\n\n"
                    "📊 L'IA et la finance au service de tes gains passifs 💰\n"
                    "Clique sur un bouton ci-dessous pour explorer 👇",
            reply_markup=keyboard
        )


# 🎯 **Gestion des réponses des boutons interactifs**
@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    if call.data == "inscription":
        bot.send_message(call.message.chat.id, "📝 **Comment s’inscrire ?**\n\n"
                                               "1️⃣ Clique ici ➡️ [DeepTrade Hub](https://deeptrade.bio.link)\n"
                                               "2️⃣ Remplis le formulaire et valide ton inscription.\n"
                                               "3️⃣ Accède aux offres et commence à gagner ! 🚀")
    elif call.data == "faq":
        bot.send_message(call.message.chat.id, "❓ **FAQ DeepTrade** ❓\n\n"
                                               "📌 **Comment commencer ?**\n➡️ Inscris-toi ici : [DeepTrade Hub](https://deeptrade.bio.link)\n\n"
                                               "📌 **Comment fonctionne le parrainage ?**\n➡️ Chaque inscription avec ton lien te rapporte une commission.\n\n"
                                               "📌 **Quels sont les gains possibles ?**\n➡️ Jusqu'à 220€ offerts aux nouveaux utilisateurs.")
    elif call.data == "parrainage":
        bot.send_message(call.message.chat.id, "🔗 **Programme de Parrainage DeepTrade** 🔗\n\n"
                                               "📌 **Tu veux gagner encore plus ?** Partage ton lien et touche des commissions sur chaque nouvelle inscription !\n\n"
                                               "📌 **Comment ça marche ?**\n"
                                               "1️⃣ Inscris-toi ici ➡️ [DeepTrade Hub](https://deeptrade.bio.link)\n"
                                               "2️⃣ Obtiens ton lien de parrainage dans ton compte.\n"
                                               "3️⃣ Partage-le partout et regarde tes gains exploser !\n\n"
                                               "🔥 Plus tu invites, plus tu gagnes ! 🔥")
    elif call.data == "invest":
        bot.send_message(call.message.chat.id, "📊 **Investissements DeepTrade** 💰\n\n"
                                               "📌 **Envie d’investir intelligemment avec l’IA ?**\n"
                                               "➡️ Découvre les opportunités ici : [DeepTrade Hub](https://deeptrade.bio.link)\n\n"
                                               "📌 **Pourquoi investir ?**\n"
                                               "- 🔥 Profite des analyses prédictives avancées\n"
                                               "- 💰 Génère des revenus passifs\n"
                                               "- 🚀 Rentre dans le game avant tout le monde !")

# 🤖 **Réponse de l’IA OpenAI pour toutes les autres questions**
@bot.message_handler(func=lambda message: True)
def ai_response(message):
    try:
        user_input = message.text
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo",
            messages=[{"role": "user", "content": user_input}]
        )
        bot.reply_to(message, response["choices"][0]["message"]["content"])
    except Exception as e:
        bot.reply_to(message, "❌ Erreur avec OpenAI, réessaie plus tard !")
        print(e)  # Debug

# 📌 **Lancement du bot**
print("✅ DeepTrade Hub Bot en ligne !")
bot.polling(none_stop=True, interval=0, timeout=20)
