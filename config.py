API_KEY = "tR1rG9FlFKodv7WG6cD4uyrvW"
API_KEY_SECRET = "KC3poYOFK7do4FrhWhtOeGMLQrpdzuapoohz00UYVAfS3kIVRJ"
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAPF2sAEAAAAAjBmKuAvfMKZ65p%2BojC0%2FXX6bFP4%3Ddg8kFWUYfnTaO2sQT8CCAzdULK5YlwbYkYWYbuDItpEWVVzELy"
ACCESS_TOKEN = "1751379506403688448-gJoiJuljsf7R4MnfsNe2E2MRaivdMm"
ACCESS_TOKEN_SECRET = "WViE6iid8w1sOO5kgdwHXKKz5yd0BKJXdZzfgykIElVmC"
CLIENT_ID = "YzUxMWJLYTdSZ0lFXzVpMl9yME86MTpjaQ"
CLIENT_SECRET = "RbSIoWrPFMHyauYMla7imqr7IWfBzTcu99N6cHsYagwqDl8iYv"
HOST = 'localhost'
USER = 'root'
PASSWORD = 'Windows10+'
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