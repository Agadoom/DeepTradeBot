import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import openai

# 🔑 Remplace par ton Token API donné par BotFather
API_TOKEN = "7376769587:AAGGT6n40XaMVk4OP1FpDEQYRyHVJRRgF6c"
OPENAI_API_KEY = "TON_TOKEN_OPENAI"

# Initialise le bot Telegram et OpenAI
bot = telebot.TeleBot(API_TOKEN)
client = openai.OpenAI(api_key=OPENAI_API_KEY)

# 📌 Commande /start (Message de bienvenue)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    keyboard = InlineKeyboardMarkup()
    
    deeptrade_button = InlineKeyboardButton("🌐 Accéder à DeepTrade Hub", url="https://deeptrade.bio.link")
    keyboard.add(deeptrade_button)
    keyboard.add(
        InlineKeyboardButton("📝 Inscription", callback_data="inscription"),
        InlineKeyboardButton("📌 FAQ", callback_data="faq")
    )
    keyboard.add(
        InlineKeyboardButton("💰 Parrainage", callback_data="parrainage"),
        InlineKeyboardButton("📊 Gains", callback_data="gains")
    )

    with open("deeptrade_hub_banner.png", "rb") as photo:
        bot.send_photo(
            message.chat.id, 
            photo, 
            caption="🚀 **Bienvenue sur DeepTrade Hub !**\n\n"
                    "📊 L'IA et la finance au service de tes gains passifs 💰\n"
                    "Clique sur un bouton ci-dessous pour commencer 👇",
            reply_markup=keyboard
        )

# 📌 Gestion des boutons interactifs
@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    responses = {
        "inscription": "📝 **Comment s’inscrire ?**\n\n"
                       "1️⃣ Clique ici ➡️ [deeptrade.bio.link](https://deeptrade.bio.link)\n"
                       "2️⃣ Remplis le formulaire et valide ton inscription.\n"
                       "3️⃣ Accède aux offres et commence à gagner ! 🚀",
        "faq": "❓ **FAQ DeepTrade Hub** ❓\n\n"
               "📌 **Comment commencer ?**\n➡️ Inscris-toi ici : [deeptrade.bio.link](https://deeptrade.bio.link)\n\n"
               "📌 **Comment fonctionne le parrainage ?**\n➡️ Chaque inscription avec ton lien te rapporte une commission.\n\n"
               "📌 **Quels sont les gains possibles ?**\n➡️ Jusqu'à 220€ offerts aux nouveaux utilisateurs.",
        "parrainage": "🔗 **Programme de Parrainage DeepTrade** 🔗\n\n"
                      "📌 **Tu veux gagner encore plus ?** Partage ton lien et touche des commissions sur chaque nouvelle inscription !\n\n"
                      "📌 **Comment ça marche ?**\n"
                      "1️⃣ Inscris-toi ici ➡️ [deeptrade.bio.link](https://deeptrade.bio.link)\n"
                      "2️⃣ Obtiens ton lien de parrainage dans ton compte.\n"
                      "3️⃣ Partage-le partout et regarde tes gains exploser !\n\n"
                      "🔥 Plus tu invites, plus tu gagnes ! 🔥",
        "gains": "💰 **Gagne jusqu'à 220€ avec DeepTrade !** 💰\n\n"
                 "📌 1. Inscris-toi ici ➡️ [deeptrade.bio.link](https://deeptrade.bio.link)\n"
                 "📌 2. Active ton compte et découvre les bonus.\n"
                 "📌 3. Parraine et touche des commissions à chaque inscription.\n\n"
                 "🔥 Plus tu invites, plus tu gagnes ! 🔥"
    }
    if call.data in responses:
        bot.send_message(call.message.chat.id, responses[call.data])

# 📌 Commande d'intelligence artificielle
@bot.message_handler(func=lambda message: True)
def ai_response(message):
    try:
        user_input = message.text
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )
        bot.reply_to(message, response.choices[0].message.content)
    except Exception as e:
        bot.reply_to(message, f"❌ Erreur avec OpenAI : {str(e)}")

# 📌 Lancer le bot en continu
print("✅ DeepTrade Hub Bot en ligne !")
bot.polling(none_stop=True, interval=0, timeout=20)
