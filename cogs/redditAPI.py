import asyncpraw
import discord
import random
from discord.ext import commands
defsearch='datasciencememes'
class MemeLord(commands.Cog):

    def __init__(self,client):
        self.client=client

    @commands.command()
    async def reddit(self,ctx,search='datasciencememes',num=1):
        reddit=asyncpraw.Reddit(client_id='uX3s7sv8hM7n0x0kJsjU9g',client_secret='IGhwX4QxXf_0eU3-Rw0hPr7tJxLicw',username='missioneducation_me',password='AbhiDeboRohan',user_agent='missioneducation_me')

        subreddit=await reddit.subreddit(search)
        hot=subreddit.hot(limit=100)
        sub_list=[]
        async for submission in hot:
            sub_list.append(submission)
        for x in range(num):
            random_sub=random.choice(sub_list)
            title=random_sub.title
            url=random_sub.url
            author=random_sub.author

            embed=discord.Embed(title=f'{title}',colour=discord.Colour.red())
            embed.set_author(name=f'Requested by {ctx.author}')
            embed.set_image(url=url)
            embed.set_footer(text=f'Posted by {author}')
            await ctx.send(embed=embed)
        await reddit.close()

    @commands.command()
    async def redditdef(self,ctx,num=1):
        reddit=asyncpraw.Reddit(client_id='uX3s7sv8hM7n0x0kJsjU9g',client_secret='IGhwX4QxXf_0eU3-Rw0hPr7tJxLicw',username='missioneducation_me',password='AbhiDeboRohan',user_agent='missioneducation_me')
        print (defsearch)
        subreddit=await reddit.subreddit(defsearch)
        hot=subreddit.hot(limit=100)
        sub_list=[]
        async for submission in hot:
            sub_list.append(submission)
        for x in range(num):
            random_sub=random.choice(sub_list)
            title=random_sub.title
            url=random_sub.url
            author=random_sub.author

            embed=discord.Embed(title=f'{title}',colour=discord.Colour.red())
            embed.set_author(name=f'Requested by {ctx.author}')
            embed.set_image(url=url)
            embed.set_footer(text=f'Posted by {author}')
            await ctx.send(embed=embed)
        await reddit.close()

    @commands.command()
    async def changedef(self,ctx,newsearch):
        defsearch=newsearch
        await ctx.send(f'Default search keyword changed to {defsearch}')

def setup(client):
    client.add_cog(MemeLord(client)) 