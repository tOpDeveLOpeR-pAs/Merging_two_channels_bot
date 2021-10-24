from parse_participants import *
# from send_invitaton import *


async def main():
    # парсинг участников канала и чата
    channel_url = input("Введите ссылку на канал: ")
    channel = await client.get_entity(channel_url)
    await dump_all_participants(channel, "data/channel_users.json")

    chat_url = input("Введите ссылку на чат: ")
    chat = await client.get_entity(chat_url)
    await dump_all_participants(chat, "data/chat_users.json")

    # отсортирование тех участников, которые есть в чате, но нет в канале
    with open("data/channel_users.json", mode="r", encoding="utf-8") as file:
        channel_users_data = json.load(file)

    with open("data/chat_users.json", mode="r", encoding="utf-8") as file:
        chat_users_data = json.load(file)

    chat_users_dict = {}
    chat_users_data_tag = set()
    for user in chat_users_data:
        chat_users_data_tag.add(user["user"])
        chat_users_dict[user["user"]] = user["first_name"]

    channel_users_data_tag = set()
    for user in channel_users_data:
        channel_users_data_tag.add(user["user"])

    invite_users_tag = chat_users_data_tag.difference(channel_users_data_tag)

    invite_users_dict = {}
    for user_tag in invite_users_tag:
        invite_users_dict[user_tag] = chat_users_dict[user_tag]

    with open("data/invite_users.json", mode="w", encoding="utf-8") as file:
        json.dump(invite_users_dict, file, ensure_ascii=False)

    # отправка сообщений пользователям
    # send_main()

with client:
    client.loop.run_until_complete(main())


