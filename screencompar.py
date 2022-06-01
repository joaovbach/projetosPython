from importlib.resources import path
from tkinter import Image
from playwright.sync_api import Playwright, sync_playwright
from PIL import Image
import os

INPUT_FOLDER = "input"
OUTPUT_FOLDER = "output"


img = Image.open("scre4.png",'r')
result = list(img.getdata())

def in_path(fileName):
    return os.path.join(INPUT_FOLDER, fileName)


imagem = Image.open("screen1.png")

imagem.show()