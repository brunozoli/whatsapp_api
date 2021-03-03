# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 13:31:46 2021

@author: bzs_1
"""

from whatsapp_api import WhatsApp
import pandas as pd

agenda = pd.read_csv('agenda.csv')

wp = WhatsApp()

input('Enter quando ler o QR code')

for contato in agenda['Nome'].unique():
    mensagem = agenda.loc[agenda['Nome']==contato, 'Mensagem'].values
    print(contato,mensagem)
    wp.search_contact(contato)
    wp.write_message(mensagem)