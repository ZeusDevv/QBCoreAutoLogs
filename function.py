    async def logs(self, ctx):
        await ctx.message.delete()
        print("Attempting To Create All Channels Now")

        category_id = category_id # Change this to your category ID
        guild_id = guild_id # Change this to your guild (Discord Server) IDguild = discord.utils.get(self.client.guilds, id=guild_id)
        category = discord.utils.get(guild.categories, id=category_id)
        channel_names = [    'default',    'testwebhook',    'playermoney',    'playerinventory',    'robbing',    'cuffing',    'drop',    'trunk',    'stash',    'glovebox',    'banking',    'vehicleshop',    'vehicleupgrades',    'shops',    'dealers',    'storerobbery',    'bankrobbery',    'powerplants',    'death',    'joinleave',    'ooc',    'report',    'me',    'pmelding',    '112',    'bans',    'anticheat',    'weather',    'moneysafes',    'bennys',    'bossmenu',    'robbery',    'casino',    'traphouse',    '911',    'palert',    'house',]
        webhooks = {}
        for name in channel_names:
            channel = await guild.create_text_channel(name, category=category)
            webhook = await channel.create_webhook(name=name, reason=f"Create webhook for channel {name}")
            webhooks[name] = webhook.url
        with open("webhook_links.txt", "w") as f:
            for name, url in webhooks.items():
                print(f"New Entry | ['{name}'] = '{url}',\n")
                f.write(f"['{name}'] = '{url}',\n")
            print("Finished")

        await asyncio.sleep(1)  # Sleep for 1 second to avoid rate limiting
