import discord
from discord.ext import commands
import os, random
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def repeat(ctx, times: int, content: str):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
        await ctx.send(f"{dice} formatı alındı: {rolls} zar atılacak.")
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

@bot.command()
async def bölme(ctx, sayı1: float, sayı2: float):
    """İki sayıyı böler ve sonucu gönderir."""
    if sayı2 == 0:
        await ctx.send("Hata: Bir sayıyı sıfıra bölemezsiniz!")
    else:
        sonuç = sayı1 / sayı2
        await ctx.send(f"{sayı1} / {sayı2} = {sonuç}")

@bot.command()
async def duck(ctx):
    img_name = random.choice(os.listdir('duck'))
    with open(f'duck/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def doometernal(ctx):
    img_name = random.choice(os.listdir('doom'))
    with open(f'doom/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def yardımkomut(ctx):
    await ctx.send(
        'komutlar şöyledir: her komut $ işareti ile çalışır $kitap $led $ elektriklicihaz '
        '$tekkullanımlıkürünler bu komutlar kirlilik hakkında bilgi edinmemizi sağlar '
        '$kirlilik ise kirlilik hakkında görseller atar $mem komik görseller atar '
        '$bölme 2 sayı ekleyin ve onları böler $roll ise dediğiniz kelimeyi kaç kere '
        'tekrar etmesini istiyorsanız yazın ve tekrar eder.'
    )

@bot.command()
async def kitap(ctx):
    await ctx.send('Basılı kitaplar ve dergiler yerine dijital formatları tercih etmek kağıt kullanımını azaltmamız gereklidir.')

@bot.command()
async def led(ctx):
    await ctx.send('LED lambalar gibi enerji tasarruflu aydınlatmalar kullanmak, enerji tüketimini önemli ölçüde azaltır.')

@bot.command()
async def elektriklicihaz(ctx):
    await ctx.send('Elektrikli cihazları kullanırken enerji verimli modelleri seçmek, gereksiz enerji israfını engeller.')

@bot.command()
async def tekkullanımlıkürünler(ctx):
    await ctx.send('Tek kullanımlık ürünler yerine yeniden kullanılabilir ürünler (su şişesi, torba) kullanın.')

@bot.command()
async def oyunönerisi(ctx):
    await ctx.send(
        'Ne demek istediğini anladım oyun önerisi istiyorsun bana tam olarak hangi tür oyun '
        'sevdiğini yazar mısın örnek olarak: aksiyon, macera, dövüş,2 3 4 kişilik arkadaş '
        'oyunları, yarış oyunu gibi..'
    )



@bot.command()
async def kirlilik(ctx):
    img_name = random.choice(os.listdir('kirlilik'))
    with open(f'kirlilik/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def minecraftmaden(ctx):
    img_name = random.choice(os.listdir('minecraftmadenb'))
    with open(f'minecraftmadenb/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def heh(ctx, count_heh=5):
    await ctx.send("he" * count_heh)

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def uncharted(ctx):
    img_name = random.choice(os.listdir('uncharted'))
    with open(f'uncharted/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def reddead(ctx):
    img_name = random.choice(os.listdir('red dead redemption 2'))
    with open(f'red dead redemption 2/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            await attachment.save(f'./images/{file_name}')
            await ctx.send(f'Saved the image to ./images/{file_name}')


            class_name, confidence_score = get_class(f"./images/{file_name}")
            await ctx.send(f"Model tahmini: {class_name}, Güven: {confidence_score:.2f}")


            if class_name == 'Demir':
                await ctx.send(
                    'Bu bir demir. Minecraft demir Y:72\'den Y:-64\'e kadar bir aralıkta bulunabiliyor. '
                    'En fazla bulunduğu yükseklik ise Y:15\'tir.'
                )
            elif class_name == 'Elmas':
                await ctx.send(
                    'Bu bir elmas. En yoğun olarak -59. katmanda yer alır. '
                    'Lav tehlikesine karşı -54 ile -59 arasında aramanız önerilir.'
                )
            elif class_name == 'Bakır':
                await ctx.send(
                    'Bu bir bakır. Bakır cevherleri genellikle Y seviyeleri 0 ile 96 arasında bulunur. '
                    'Özellikle dağlık biyomlarda daha sık görülür.'
                )
            else:
                await ctx.send("I don't know what this is :(")
    else:
        await ctx.send('You forgot to upload the image')



@bot.event
async def on_message(message):
    if message.author == bot.user:
        return



    await bot.process_commands(message)

bot.run('')
