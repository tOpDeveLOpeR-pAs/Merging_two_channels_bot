from parse_participants import *


async def main():
    # парсинг участников канала и чата
    channel_url = input("Введите ссылку на канал: ")
    channel = await client.get_entity(channel_url)
    await dump_all_participants(channel, "data/channel_users.json")

    chat_url = input("Введите ссылку на чат: ")
    chat = await client.get_entity(chat_url)
    await dump_all_participants(chat, "data/chat_users.json")

    # отсортирование тех участников, которые есть в чате, но нет в канале



# https://t.me/merge_test - chat
# https://t.me/Merge_test2 - channel

with client:
    client.loop.run_until_complete(main())


