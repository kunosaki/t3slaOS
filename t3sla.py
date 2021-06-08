#!/usr/bin/env python3
import discord
import datetime

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_member_join(self, member):
        if ("h0nde" in member.name.lower()) and ("twitter" in member.name.lower()):
            try:
                await member.ban(reason="triggered an automatic spam filter")
                return
            except discord.Forbidden:
                print("I don't have perms to ban")

        # thanks AlexFlipnote#0001 for this second approach
        time_between_insertion = datetime.datetime.utcnow() - member.created_at
        if time_between_insertion < datetime.timedelta(days=1):
            await member.ban(reason="triggered an automatic spam filter, account too new")
            return

intents = discord.Intents.default()
intents.members = True
client = MyClient(intents=intents)
client.run('ODUxODc2Njc1NDA2Mzk3NDUw.YL-p-g.IU1Pv3xIGmH9GgA7Ju-C_6v5icQ')
