from tkinter import *
from yahoo_fin import stock_info as si
from gtts import gTTS # Import the gTTS module for text to speech conversion 
import os # import Os module to play the audio file, run play in linux ubuntu, for windows run start

janela: Tk = Tk()   # create the window
janela.title('VIX monitor')
janela.resizable(False, False)  # Prevents anyone from being able to resize the window

label1 = Label(janela, text='VIX = ', bg='white', fg='blue', font=("Arial", 20), padx=20, pady=20).grid(row=2, column= 2)  

tempo_att = 10000 #ms

alert = True

def neue_fenster(mensagem):
    fenster: Tk = Tk()   # create the new window
    fenster.title('ALERT')
    fenster.resizable(False, False)  # Prevents anyone from being able to resize the window
    Label(fenster, text=mensagem, bg='red', fg='blue', font=("Arial", 20), padx=20, pady=20).grid(row=2, column= 2)  
    
def sprechen(mensagem):
    language = 'en'  # english
    myobj = gTTS(text=mensagem, lang=language, slow=False) 
    myobj.save("output.mp3") 
    os.system("play output.mp3")   #  Play the converted file in linux terminal

def upd():   
    vix_cotacao = round(si.get_live_price('^VIX'),2) 
    label2.configure(text=round(vix_cotacao, 2))
    global alert
    if alert == True:
        if vix_cotacao > 25.1 and vix_cotacao < 36:
            mensagem = 'Volatility requires attention'
            neue_fenster(mensagem)
            sprechen(mensagem)
            alert = False
        elif vix_cotacao > 36.1 and vix_cotacao < 48.8:    
            mensagem =  'High volatility, be carefull'
            neue_fenster(mensagem)
            sprechen(mensagem)
            alert = False
        elif vix_cotacao > 48.9:     
            mensagem = 'Critical volatility, urgently use hedging strategies'
            neue_fenster(mensagem)
            sprechen(mensagem)
            alert = False
    janela.after(tempo_att, upd)    
    
vix_cotacao = round(si.get_live_price('^VIX'),2) # get the current value of VIX
label2 = Label(janela, text=vix_cotacao, bg='white', fg='blue', font=("Arial", 20), padx=20, pady=20)
label2.grid(row=2, column= 3) 
   
janela.after(tempo_att, upd)   # keeps Vix updated every 10000 millisecond interval
janela.mainloop() 
