import telebot
import requests
import time
from getuseragent import UserAgent

bot_token = "YOUR_BOT_TOKEN_HERE"
bot = telebot.TeleBot(bot_token)

password_correct = False
program_running = True
last_link_used = {}
link_usage_interval = 600  # 10 minutes in seconds

@bot.message_handler(commands=['start'])
def start(message):
    global password_correct
    if not password_correct:
        bot.send_message(message.chat.id, """
Welcome to Fox bot for social media services. 🥰
To get the password to run the script, click below 👇👇👇
https://linkjust.com/yICLpvJpIzl6jHs9EjioKWu4QAWB
""")
    else:
        bot.send_message(message.chat.id, "You are already logged in.", parse_mode='Markdown')
        send_keyboard_again(message)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    global password_correct, program_running, last_link_used
    
    if not program_running:
        bot.send_message(message.chat.id, """"
The bot has been successfully stopped. To run it again, click on👇 
Restart Bot 🔄
""")
        return
    
    if not password_correct:
        url = "https://raw.githubusercontent.com/foxfox0/Fox/main/Fox"
        try:
            response = requests.get(url)
            correct_password = response.text.strip()
            if message.text.strip() == "fox1900":
                password_correct = True
                bot.send_message(message.chat.id, """
💥 You have successfully logged in! 🌟 Choose the service you want ⚜️
""", parse_mode='Markdown', reply_markup=telebot.types.InlineKeyboardMarkup().add(
                    telebot.types.InlineKeyboardButton(text="Bot Channel 🔰", url="https://t.me/F_0_oX"),
                    telebot.types.InlineKeyboardButton(text="Stop Bot ❌", callback_data="stop_bot"),
                    telebot.types.InlineKeyboardButton(text="Restart Bot 🔄", callback_data="restart_bot"),
                    telebot.types.InlineKeyboardButton(text="Like YouTube 🎥", callback_data="like_youtube"),
                    telebot.types.InlineKeyboardButton(text="Reactions Telegram 📲", callback_data="reactions_telegram"),
                ))
            else:
                bot.send_message(message.chat.id, """
Incorrect password, please get it and use the bot again 😇🥰
To get the password👇👇👇
https://linkjust.com/yICLpvJpIzl6jHs9EjioKWu4QAWB
""")
        except Exception as e:
            print("Error:", e)
            bot.send_message(message.chat.id, "An error occurred while fetching the password. Please try again later.")
            
        return
    
@bot.callback_query_handler(func=lambda call: call.data == "like_youtube")
def like_youtube(call):
    bot.send_message(call.message.chat.id, "Send me the YouTube link to boost")
    bot.register_next_step_handler(call.message, handle_youtube_link)

def handle_youtube_link(message):
    if message.text.startswith('http'):
        link = message.text.strip()
        current_time = time.time()
        if link in last_link_used:
            if current_time - last_link_used[link] < link_usage_interval:
                bot.send_message(message.chat.id, """
You've boosted this link. You can boost another link after ten minutes 🥺
or use another link 🤗💥
""")
                send_keyboard_again(message)
                return
            else:
                last_link_used[link] = current_time
        else:
            last_link_used[link] = current_time
        
        ua = UserAgent("ios").Random()        
        url = "https://ston12345.com/wp-admin/admin-ajax.php"
        params = {'action': "fsc_request_service"}
        files = [
            ('_wpnonce', (None, '9a3cdc27e3')),
            ('shortcode', (None, 'cmJzb0haWkx5YUx1SDY4c3ovSmpiRnhON05OV3VESUNQakZ5WTlqV0VDYXpGaUVabEFmY0o5aUd3WWxRWUhMODYwOXRnNWROUHc1OXB4cWY1cXEzSVlrOXNmR2R4WU1zR0NkcE4xUUg3YWdmQ3ZjWlQzckFpRFQ4YzlrRTFlWkpHNFphdHIvWFI4Wi9yTURrKzFJczM3cnRVblRDNjQxdkNWWDY1d0RMTVhhN0R4Ly85bmpWNFdvWSt3azA4MkFLVFpzYTFVVVo3SU5COEdmdG8xS2tuWU8yWVRVcXFaZnkxclFJc1ZlaHVxYz0=')),
            ('pagename', (None, link))
        ]
        headers = {
            'User-Agent': ua,
            'sec-ch-ua': "\"Chromium\";v=\"122\", \"Not(A:Brand\";v=\"24\", \"Google Chrome\";v=\"122\"",
            'sec-ch-ua-platform': "\"Android\"",
            'sec-ch-ua-mobile': "?0",
            'origin': "https://smmstone.com",
            'sec-fetch-site': "cross-site",
            'sec-fetch-mode': "cors",
            'sec-fetch-dest': "empty",
            'referer': "https://smmstone.com/",
            'accept-language': "ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7"
        }
        response = requests.post(url, params=params, files=files, headers=headers)
        if "request submitted successfully." in response.text:
            fff = "Boost request sent successfully. Please wait, delivery will be done within minutesᥬ😍᭄"
            bot.send_message(message.chat.id, f"{fff}.", parse_mode='Markdown')
        else:
            foox = response.json()["message"]
            bot.send_message(message.chat.id, f"{foox}.", parse_mode='Markdown')
        
        send_keyboard_again(message)

    else:
        bot.send_message(message.chat.id, """
Please enter the link correctly
""", parse_mode='Markdown') 

@bot.callback_query_handler(func=lambda call: call.data == "reactions_telegram")
def reactions_telegram(call):
    bot.send_message(call.message.chat.id, "Send me the Telegram link to boost")
    bot.register_next_step_handler(call.message, handle_telegram_link)
    
def handle_telegram_link(message):
    if message.text.startswith('http'):
        link = message.text.strip()
        current_time = time.time()
        if link in last_link_used:
            if current_time - last_link_used[link] < link_usage_interval:
                bot.send_message(message.chat.id, """
You've boosted this link. You can boost another link after ten minutes 🥺
or use another link 🤗💥
""")
                send_keyboard_again(message)
                return
            else:
                last_link_used[link] = current_time
        else:
            last_link_used[link] = current_time
        
        ua = UserAgent("ios").Random()        
        url = "https://ston12345.com/wp-admin/admin-ajax.php"
        params = {'action': "fsc_request_service"}
        files = [
            ('_wpnonce', (None, '9a3cdc27e3')),
            ('shortcode', (None, 'Qm8zMklEczJhWGEyZDdTcHo5K3ErUjVFNCtLS01nNVV3d2JNMGUyUElhQUVucHpzdThoVS80TmdNRWJUZHhvK3dNSm92V1ZaR0VSenRGVVo3eGhaYnRLMzhUemxqUTJnNHo2V0ZqMTFpTWNJR0hqenJTSzRwd3MvdnFSVWhZYW9pUHR4NkV2M3hXSUhLeHkrRG1qUisyTkJhVlVIQmVXa21tNEQvRFRHYmVaeHh0QVdPU21BRU00N3pydXVCbDBVUmFSSC9GVnVhQkVyOXdQS1pHUEhRcmJhSy9WLytxSkcxYlV0UW9nSHQ4cWRHRFJ4T1phSjNPTy9oQ0dFR0FuYnZrMXQvYklZTkFOb05wWWRrZzMwNlE9PQ==')),
            ('pagename', (None, link))
        ]
        headers = {
            'User-Agent': ua,
            'sec-ch-ua': "\"Chromium\";v=\"122\", \"Not(A:Brand\";v=\"24\", \"Google Chrome\";v=\"122\"",
            'sec-ch-ua-platform': "\"Android\"",
            'sec-ch-ua-mobile': "?0",
            'origin': "https://smmstone.com",
            'sec-fetch-site': "cross-site",
            'sec-fetch-mode': "cors",
            'sec-fetch-dest': "empty",
            'referer': "https://smmstone.com/",
            'accept-language': "ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7"
        }
        response = requests.post(url, params=params, files=files, headers=headers)
        if "request submitted successfully." in response.text:
            fff = "Boost request sent successfully. Please wait, delivery will be done within minutesᥬ😍᭄"
            bot.send_message(message.chat.id, f"{fff}.", parse_mode='Markdown')
        else:
            foox = response.json()["message"]
            bot.send_message(message.chat.id, f"{foox}.", parse_mode='Markdown')
        
        send_keyboard_again(message)

    else:
        bot.send_message(message.chat.id, """
Please enter the link correctly
""", parse_mode='Markdown') 

@bot.callback_query_handler(func=lambda call: call.data == "stop_bot")
def stop_bot(call):
    global program_running
    program_running = False
    bot.send_message(call.message.chat.id, "The bot has been stopped.")

@bot.callback_query_handler(func=lambda call: call.data == "restart_bot")
def restart_bot(call):
    global program_running
    program_running = True
    bot.send_message(call.message.chat.id, "Bot restarted successfully.")

def send_keyboard_again(message):
    bot.send_message(message.chat.id, """
Choose the service you want from hereᥬ👇᭄ᥬ😂᭄
""", reply_markup=telebot.types.InlineKeyboardMarkup().add(
    telebot.types.InlineKeyboardButton(text="Like YouTube 🎥", callback_data="like_youtube"),
    telebot.types.InlineKeyboardButton(text="Reactions Telegram 📲", callback_data="reactions_telegram")
))

bot.polling()
