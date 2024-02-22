from telethon.sync import TelegramClient
from telethon.tl.types import InputMessagesFilterPhotos, InputMessagesFilterDocument
from telethon.errors import SessionPasswordNeededError
from telethon import functions, types

api_id = input("Input your api_id: ")
api_hash = input("Input your api_hash: ")
phone_number = input("Input your phone number it should start with +251: ")
client = TelegramClient('session_name', api_id, api_hash)

async def main():
    await client.start(phone=phone_number)
    num_channels = int(input("How many channels do you want to scrape? "))

    channels = []
    for i in range(num_channels):
        channel_name = input("Enter the link of channel, it should start with @ {}: ".format(i + 1))
        channels.append(channel_name)

    print("You have selected the following channels:")
    for channel_name in channels:
        print(channel_name)

    num_messages = int(input("how many messages/posts would you like to scrape from each channels: "))
            
    for channel_name in channels:
        channel = await client.get_entity(channel_name)
        photos = await client.get_messages(channel, None, filter=InputMessagesFilterPhotos)
        message_counter = 0  

        async for message in client.iter_messages(channel):
            if message.text:
                message_counter += 1  
                if message_counter > num_messages: 
                    break

                message_photo = []
                photos = await client.get_messages(channel, ids=[message.id], filter=InputMessagesFilterPhotos)
                
                for photo in photos:
                    downloaded_photo = await client.download_media(photo)
                    message_photo.append(downloaded_photo)
                '''
                if you'd like to upload the post/message you scraped to your
                database, this is where you should write/call
                your uploader function
                
                '''
            print(message.text)

        async for doc in client.iter_messages(channel, filter=InputMessagesFilterDocument):
            await client.download_media(doc)
            
        if message_counter > num_messages: 
            continue
        

with client:
    client.loop.run_until_complete(main())