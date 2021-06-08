#!/usr/bin/env python3
import discord
import datetime

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_member_join(self, member):
        if ("h0nde" in member.name.lower()) and ("twitter" in member.name.lower()):
            try:
                await member.ban(reason="t3sla is better, h0nde spam")
                return
            except discord.Forbidden:
                print("why you no perm set for me ban ")

        time_between_insertion = datetime.datetime.utcnow() - member.created_at
        if time_between_insertion < datetime.timedelta(days=1):
            await member.ban(reason="t3sla is better, h0nde spam")
            return

intents = discord.Intents.default()
intents.members = True
client = MyClient(intents=intents)
client.run('put token here')
