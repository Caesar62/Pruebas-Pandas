__author__ = 'Cesar Sainz'

# coding: utf-8
import re
from ftplib import FTP
import tarfile
import os, os.path
import shutil
import glob
import pandas as pd
import datetime
import requests
import smtplib
import time
from bs4 import BeautifulSoup as bs
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Extracción de datos de la página del IEO para la boya AGL
request_boya_agl = requests.get('https://bancodatos.puertos.es/TablaAccesoSimplificado/?p=3138035&name=Santander', timeout=5)
#print(request_boya_agl)
soup_boya_agl = bs(request_boya_agl.content, "html.parser")
#print(soup_boya_agl)
busca_altura = soup_boya_agl.find_all('table')
texto_busca_altura = re.search(r'Valor(.*)', busca_altura[0].text, re.DOTALL)
lista_lecturas = texto_busca_altura.group(1).strip().split('\n')
ultima_altura = float(lista_lecturas[3])