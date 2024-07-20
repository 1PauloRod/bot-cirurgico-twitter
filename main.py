from botTwitter import BotTwitter
from time import sleep

def main() -> None:
    botTwitter = BotTwitter()
    botTwitter.process_content()
    sleep(5)


if __name__ == '__main__':
    main()
