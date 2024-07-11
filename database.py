import mysql.connector
from mysql.connector import errorcode
from config import *


class Database:
    def __init__(self):
        try:
            self.__create_database()
            self.__create_table()
        except Exception as err:
            print(err)
            return [-5]
        
        
    def insert_content(self, content):
        try:
            text, subtext, autor, processed = content
            
            script = INSERT_CONTENT % (text, subtext, autor, processed)
            
            return self.__execute_script(script)
        
        except Exception as err:
            print(err)
            return [-5]
        
    def get_random_content(self):
        try:
            
            script = GET_RANDOM_NOT_PROCESSED_CONTENT 
            
            return self.__execute_script(script)
        except Exception as err:
            print(err)
            return [-5]
        
    def update_processed_content(self, content_id):
        try:
            
            script = UPDATE_CONTENT % (1, content_id)
            
            return self.__execute_script(script)
            
        except Exception as err:
            print(err)
            return [-5]
        
    @staticmethod
    def __create_database():
        try:
            cnx = mysql.connector.connect(host=HOST, 
                                          user=USER, 
                                          password=PASSWORD)

            cursor = cnx.cursor()
            cursor.execute(VERIFY_DATABASE_EXIST)
            result = cursor.fetchall()
            
            if result:
                print("Banco de dados já existe.")
            else:
                print("Criando banco de dados.")
                cursor.execute(CREATE_DATABASE)
            
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Algo deu errado com usuário ou senha.")
                return [-1]
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Banco de dados não existe.") 
                return [-2]
            else:
                print(err)
                return [-3]
        
        finally:
            if cnx:
                cnx.close()
         
    @staticmethod       
    def __create_table():
        try: 
            cnx = mysql.connector.connect(host=HOST, 
                                          user=USER, 
                                          password=PASSWORD, 
                                          database=DATABASE)
            
            cursor = cnx.cursor()
            cursor.execute(VERIFY_TABLE_EXIST)
            result = cursor.fetchall()
            
            if result:
                print("Tabela já existe.")
            else:
                print("Criando tabela.")
                cursor.execute(CREATE_TABLE)
                
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Algo deu errado com o usuário ou senha.")
                return [-1]
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Banco de dados não existe.")
                return [-2]
            else:
                print(err)
                return [-3]          
        
        finally:
            if cnx:
                cnx.close()
           
    @staticmethod 
    def __execute_script(script):
        try:
            cnx = mysql.connector.connect(host=HOST,
                                          user=USER,
                                          password=PASSWORD,
                                          database=DATABASE)
            
            cursor = cnx.cursor()
            cursor.execute(script)
            result = cursor.fetchall()
            cnx.commit()
            
            return result
        
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Algo deu errado com o usuário ou senha.")
                return [-1]
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Banco de dados não existe.")
                return [-2]
            else:
                print(err)
                return [-3]          
        
        finally:
            if cnx:
                cnx.close()
                

'''if __name__=='__main__':
    database = Database()
    #content = ["esse é o texto 3", "esse é o subtexto 3", "chave 3", 0]
    #database.insert_content(content)
    cont = database.get_random_content()
    print(cont)
    if cont:
        database.update_processed_content(cont[0][0])
    else:
        print("todos já processados.")'''
    
            
            