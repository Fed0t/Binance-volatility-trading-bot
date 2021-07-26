import telegram
from helpers.parameters import (
    load_config
)


def notify(message):
    parsed_config = load_config('config.yml')
    bot = telegram.Bot(token=parsed_config['script_options']['TELEGRAM_TOKEN'])
    bot.sendMessage(chat_id=parsed_config['script_options']['TELEGRAM_GROUP'], parse_mode="markdown",
                    text='*RichieRich*: ' + message)
