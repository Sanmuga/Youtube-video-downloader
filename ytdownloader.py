import yt_dlp
import telebot
import os


bot_token = 'YOUR_BOT_TOKEN'


bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Welcome to the YouTube Video Downloader Bot! Send me a YouTube video URL to download.")

@bot.message_handler(func=lambda message: True)
def download_video(message):
    try:
        url = message.text
        ydl_opts = {
            'format': 'best[ext=mp4]/best',  
            'outtmpl': 'downloaded_video.mp4',  
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
        
        
        with open('downloaded_video.mp4', 'rb') as video_file:
            bot.send_video(message.chat.id, video_file)
        
        
        os.remove('downloaded_video.mp4')
    except Exception as e:
        bot.reply_to(message, f"An error occurred: {str(e)}")


bot.polling()
