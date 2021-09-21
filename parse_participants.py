import configparser
import json

from telethon.sync import TelegramClient
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch


# Первичная инициализация API
# Считываем учетные данные
config = configparser.ConfigParser()
config.read("config.ini")

# Присваиваем значения внутренним переменным
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
username = config['Telegram']['username']

client = TelegramClient(username, api_id, api_hash)
client.start()


# сбор данных участников канала
async def dump_all_participants(channel, file_name):
    """Записывает json-файл с информацией о всех участниках канала/чата"""
    offset_user = 0  # номер участника, с которого начинается считывание
    limit_user = 80  # максимальное число записей, передаваемых за один раз | лимит телеграмма - 100

    all_participants = []  # список всех участников канала
    filter_user = ChannelParticipantsSearch('')

    while True:
        participants = await client(GetParticipantsRequest(channel,
                                                           filter_user,
                                                           offset_user,
                                                           limit_user,
                                                           hash=0
                                                           ))
        # нерассмотренных пользователей не осталось
        if not participants.users:
            break
        all_participants.extend(participants.users)
        offset_user += len(participants.users)

    # словарь с необходимыми данными
    all_users_details = []

    for participant in all_participants:
        all_users_details.append({"id": participant.id,
                                  "first_name": participant.first_name,
                                  "last_name": participant.last_name,
                                  "user": participant.username,
                                  })

    with open(file_name, 'w', encoding='utf8') as file:
        json.dump(all_users_details, file, ensure_ascii=False)
