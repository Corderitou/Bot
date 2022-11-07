# This example requires the 'message_content' privileged intents
import telebot
import requests
import threading
from flask import Flask, request, abort

app = Flask(__name__)
@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        a = request.json
        b = a["content"]
        if b == "buy":
            print("compra")
        elif b == "sell": 
            print("venta")   
        else:
            print("no paso nada")     
        return 'success', 200
    
    else:
        abort(400)

bot = telebot.TeleBot("5777810159:AAFRLseImr310gVmCorL_ZoD7Mz6uaHHKc0")

@bot.message_handler(commands=["start","test"])
def cmd_start(message):
    bot.send_message(-1001880307694, "hola:D") #-1001523347078



def setInterval(func,time):
    e = threading.Event()
    while not e.wait(time):
        func()

def foo():
    response = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT")

    a = response.json()

    priceBTC = a["price"]
    price = int(float(priceBTC))
    a = str(price)
  
    bot.send_message(-1001880307694, "BTC: "+ a)

# using
setInterval(foo,0.5)

if __name__ == "__main__":
  print("iniciando")
  bot.infinity_polling()
  print("Fin")