from parse_participants import *
from send_invitaton import *

async def main():
    # парсинг участников канала и чата
    channel_url = 'https://t.me/Merge_test2' #input("Введите ссылку на канал: ")
    channel = await client.get_entity(channel_url)
    await dump_all_participants(channel, "data/channel_users.json")

    chat_url = 'https://t.me/merge_test' #input("Введите ссылку на чат: ")
    chat = await client.get_entity(chat_url)
    await dump_all_participants(chat, "data/chat_users.json")

    # отсортирование тех участников, которые есть в чате, но нет в канале
    with open("data/channel_users.json", mode="r", encoding="utf-8") as file:
        channel_users_data = json.load(file)

    with open("data/chat_users.json", mode="r", encoding="utf-8") as file:
        chat_users_data = json.load(file)

    chat_users_dict = {}
    chat_users_data_id = set()
    for user in chat_users_data:
        chat_users_data_id.add(user["id"])
        chat_users_dict[user["id"]] = user["first_name"]

    channel_users_data_id = set()
    for user in channel_users_data:
        channel_users_data_id.add(user["id"])

    invite_users_id = chat_users_data_id.difference(channel_users_data_id)

    invite_users_dict = {}
    for user_id in invite_users_id:
        invite_users_dict[user_id] = chat_users_dict[user_id]

    with open("data/invite_users.json", mode="w", encoding="utf-8") as file:
        json.dump(invite_users_dict, file, ensure_ascii=False)

    # отправка сообщений пользователям
    send_main()

with client:
    client.loop.run_until_complete(main())


