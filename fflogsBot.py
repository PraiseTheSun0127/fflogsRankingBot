import traceback
from conf import loadConf
from discord.ext import commands

TOKEN = loadConf.discordTokenLoad()

INITIAL_EXTENSIONS = [
    
    'cogs.fflogsCog'

]

class FflogsBot(commands.Bot):

    def __init__(self, command_prefix):

        super().__init__(command_prefix)

        for cog in INITIAL_EXTENSIONS:

            try:

                self.load_extension(cog)

            except Exception:

                traceback.print_exc()

    async def on_ready(self):
        
        print('-----')
        
        print('login success')
        
        print('-----')

# fflogsBotのインスタンス化及び起動処理。
if __name__ == '__main__':
    
    bot = FflogsBot(command_prefix='!')
    
    bot.run(TOKEN)