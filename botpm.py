import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

img_url = ["https://pibig.info/uploads/posts/2022-12/1670611245_1-pibig-info-p-khlam-art-podelki-vkontakte-1.jpg",
           "https://avatars.mds.yandex.net/i?id=a076fcef02b0df95e03c856c7b2f3046_l-5276635-images-thumbs&n=13",
           "https://1000000diy.ru/images/stati/6/5155/klass-10-igrushek-iz-musora-9.jpg",
           "https://i3.wp.com/pushinka.top/uploads/posts/2023-04/thumbs/1681891909_pushinka-top-p-art-khlam-podelki-iz-brosovogo-materiala-k-26.webp?ssl=1",
           "https://balthazar.club/uploads/posts/2023-01/1674244580_balthazar-club-p-podelki-iz-musora-svoimi-rukami-pinterest-19.jpg"]

@bot.command()
async def buy_sort(ctx):
    await ctx.send("https://aliexpress.ru/popular/composter-kitchen-waste.html?utm_referrer=https%3A%2F%2Fyandex.ru%2F")

@bot.command()
async def sort(ctx):
    await ctx.send('''Сверхурочную работу за первые два часа оплачивают не менее чем в 1,5 размере, а за каждые последующие 2 часа – не менее чем в двойном (ст. 152 ТК). 
                   Нагружать такой работой можно не больше двух дней подряд и не больше 4 часов за раз.
                   За год сотрудник может отработать сверх нормы не более 120 часов. Именно к этой части относятся поправки, которые вступят в силу с 1 сентября 2024.''')

@bot.command()
async def diy(ctx):
    await ctx.send(random.choice(img_url))

@bot.command()
async def info(ctx):
    await ctx.send('''                                                  ПРАВИЛА:
                    1. Раздельный сбор. Разделяйте мусор на категории: бумага, пластик, стекло, металлы и органические отходы следует выделять в отдельные контейнеры.

                    2. Очистка от остатков. Прежде чем выбросить упаковку или контейнер, убедитесь, что они полностью очищены от остатков продуктов.

                    3. Специфические виды отходов. Такие как батарейки, электроника, термометры и другие, помещайте в специальные контейнеры для последующей безопасной утилизации.

                    4. Компостирование. Органические отходы, такие как пищевые и растительные остатки, можно использовать для производства компоста.

                    5. Не сжигайте мусор. Это может привести к выбросу вредных веществ в атмосферу.''')
    


bot.run('MTI2NDIxNjMzNjAzNzMxODc2Ng.G5kK-J.yq7EKvxIydAx1iyUOvKkSp1sCp5YihUizuC7-Y')
