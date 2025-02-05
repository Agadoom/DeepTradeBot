import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import openai

# 🔑 Clés API (Remplace avec tes vraies clés)
API_TOKEN = "TON_TELEGRAM_BOT_TOKEN"  # Token Telegram de @BotFather
OPENAI_API_KEY = "TA_CLE_OPENAI"  # Clé API OpenAI

# 🔥 Initialise le bot
bot = telebot.TeleBot(API_TOKEN)
openai.api_key = OPENAI_API_KEY

# 📌 Commande /start (Message de bienvenue avec boutons interactifs)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    keyboard = InlineKeyboardMarkup()
    
    # Boutons interactifs
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

    # Envoie l’image avec le menu
    with open("deeptrade_hub_banner.png", "rb") as photo:
        bot.send_photo(
            message.chat.id, 
            photo, 
            caption="🚀 **Bienvenue sur DeepTrade Hub !**\n\n"
                    "📊 L'IA et la finance au service de tes gains passifs 💰\n"
                    "Clique sur un bouton ci-dessous pour explorer 👇",
            reply_markup=keyboard
        )

# 📌 Gestion des boutons
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
    elif call.data == "invest":
        bot.send_message(call.message.chat.id, "📊 **Investissements et Opportunités** 📊\n\n"
                                               "📌 DeepTrade Hub propose des placements stratégiques avec IA.\n"
                                               "💡 Explore les options ici ➡️ [deeptrade.bio.link](https://deeptrade.bio.link)")

# 📌 Intégration OpenAI - Réponse IA
@bot.message_handler(func=lambda message: True)
def ai_response(message):
    try:
        user_input = message.text
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": user_input}]
        )
        bot.reply_to(message, response["choices"][0]["message"]["content"])
    except Exception as e:
        bot.reply_to(message, "❌ Erreur avec OpenAI, réessaie plus tard !")
        print(e)  # Debug

# 📌 Lancer le bot en continu
print("✅ DeepTrade Hub Bot en ligne !")
bot.polling(none_stop=True, interval=0, timeout=20)
