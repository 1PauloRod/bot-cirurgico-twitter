API_KEY = "tR1rG9FlFKodv7WG6cD4uyrvW"
API_KEY_SECRET = "####"
BEARER_TOKEN = "####"
ACCESS_TOKEN = "####"
ACCESS_TOKEN_SECRET = "####"
CLIENT_ID = "####"
CLIENT_SECRET = "####"
HOST = 'localhost'
USER = 'root'
PASSWORD = '####'
DATABASE = 'fundaocirurgicodb'

VERIFY_DATABASE_EXIST = "SHOW DATABASES LIKE 'fundaocirurgicodb'"
CREATE_DATABASE = "CREATE DATABASE fundaocirurgicodb"

VERIFY_TABLE_EXIST = "SHOW TABLES LIKE 'fundaocirurgicotb'"
CREATE_TABLE = """
            CREATE TABLE fundaocirurgicotb(
                id          INT AUTO_INCREMENT PRIMARY KEY, 
                text        VARCHAR(255) NOT NULL, 
                subtext     VARCHAR(255) NOT NULL, 
                autor     VARCHAR(255) NOT NULL, 
                processed   bit          DEFAULT  0,
                date        datetime 
            )
"""

INSERT_CONTENT = """
            insert into fundaocirurgicodb.fundaocirurgicotb(text, subtext, keyword, processed)
            VALUES ('%s', '%s', '%s', %d);
"""

GET_RANDOM_NOT_PROCESSED_CONTENT = """
            SELECT * 
            FROM fundaocirurgicodb.fundaocirurgicotb 
            WHERE processed = 0
            ORDER BY RAND() LIMIT 1

"""

UPDATE_CONTENT = """
            UPDATE fundaocirurgicodb.fundaocirurgicotb
            SET processed = %d
            WHERE id = %d
"""
