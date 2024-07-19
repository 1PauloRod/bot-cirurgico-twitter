from database import Database
from botImage import BotImage
import tweepy as tw
from config import *
from utils import create_filename
import os
from time import sleep

class BotTwitter:
    
    def __init__(self):
        self.database = Database()
        self.botImage = BotImage()
        self.client = tw.Client(consumer_key=API_KEY, 
                                consumer_secret=API_KEY_SECRET, 
                                access_token=ACCESS_TOKEN, 
                                access_token_secret=ACCESS_TOKEN_SECRET)
                                
        auth = tw.OAuth1UserHandler(API_KEY, API_KEY_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        self.api = tw.API(auth, wait_on_rate_limit=True)
    
    def process_content(self):
        try:
            random_content = self.database.get_random_content()
            content_autor_subtext = ''
            if random_content:
                content_id = random_content[0][0]
                content_text = random_content[0][1]
                content_subtext = random_content[0][2]
                content_autor = random_content[0][3]
                content_autor_subtext = content_autor + ', ' + content_subtext
                #content_processed = random_content[0][4]
                #content_date = random_content[0][5]
                
                print("---- Conteúdo: {} -----".format(content_autor_subtext))
                print("content id: ", content_id)
                print("content text: ", content_text)
                print("content subtext: ", content_subtext)
                print("content autor: ", content_autor)
                
                
                self.botImage.create_image(content_text, content_autor_subtext)
                print("[1] - imagem criada")
                sleep(3)
                self.database.update_processed_content(content_id)
                print("[2] - banco de dados atualizado")
                sleep(3)
                post_content_dir = "createdImage" + "//" + create_filename(content_autor_subtext) + ".jpg"
                self.__post_content(post_content_dir, self.api, self.client)
                print("[3] - imagem postada")
                sleep(3)
            else:
                print("Todos já foram processados.")
        
        except Exception as err:
            print(err)
            
        finally:
            if content_autor_subtext:
                self.__delete_image(create_filename(content_autor_subtext))
                print("[4] - imagem deletada")
                sleep(3)
    
    @staticmethod
    def __post_content(image_filename, api, client):
        try:
            media = api.media_upload(filename=image_filename)
            media_id = media.media_id
            client.create_tweet(media_ids=[media_id])
        
        except Exception as err:
            print(err)
        
      
    
    @staticmethod
    def __delete_image(image_filename):
        os.remove("createdImage//" + image_filename + ".jpg")
        
    
