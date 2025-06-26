import discord
from discord.ext import commands
import os, random

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
async def yardımkomut(ctx):
    await ctx.send(f'komutlar şöyledir: her komut $ işareti ile çalışır $kitap $led $ elektriklicihaz $tekkullanımlıkürünler bu komutlar kirlilik hakkında bilgi edinmemmizi sağlar $kirlilik ise kirlilik hakkında görseller atar $mem komik görseller atar $bölme 2 sayı ekleyin ve onları böler $roll ise dediğiniz kelimeyi kaç kere tekrar etmesini istiyorsanız yazın ve tekrar eder.')

@bot.command()
async def kitap(ctx):
    await ctx.send(f'Basılı kitaplar ve dergiler yerine dijital formatları tercih etmek kağıt kullanımını azaltmamız gereklidir.')

@bot.command()
async def led(ctx):
    await ctx.send(f'LED lambalar gibi enerji tasarruflu aydınlatmalar kullanmak, enerji tüketimini önemli ölçüde azaltır.')

@bot.command()
async def elektriklicihaz(ctx):
    await ctx.send(f' Elektrikli cihazları kullanırken enerji verimli modelleri seçmek, gereksiz enerji israfını engeller.')

@bot.command()
async def tekkullanımlıkürünler(ctx):
    await ctx.send(f'Tek kullanımlık ürünler yerine yeniden kullanılabilir ürünler (su şişesi, torba) kullanın.')

@bot.command()
async def oyunönerisi(ctx):
    await ctx.send(f'Ne demek istediğini anladım oyun önerisi istiyorsun bana tam olarak hangi tür oyun sevdiğini yazar mısın örnek olarak: aksiyon, macera, dövüş,2 3 4 kişilik arkadaş oyunları, yarış oyunu gibi..')

@bot.command()
async def aksiyon(ctx):
    await ctx.send(f' 🎮 1. DOOM Eternal Neden Seçtim? Hızlı tempolu çatışmalar, agresif yapay zekâ düşmanlar ve muazzam silah çeşitliliği ile saf aksiyonun tanımını yapıyor. Oyuncuyu sürekli hareket etmeye zorlayan yapısıyla "aksiyon" kelimesini iliklerine kadar hissettiriyor. 🗡️ 2. Devil May Cry 5 Neden Seçtim? Stilize dövüş mekaniği, havalı kombolar ve hikaye anlatımıyla tam bir hack & slash aksiyon deneyimi sunuyor. Her karakterin kendine özgü savaş tarzı var ve bu da tekrar oynanabilirliği artırıyor.🔫 3. Call of Duty: Modern Warfare (2019) Neden Seçtim? Gerçekçi çatışmalar, sürükleyici sinematik sahneler ve online çok oyunculu modu sayesinde hem tek kişilik hem de çok oyunculu aksiyonu bir arada yaşatıyor. Özellikle görev tasarımlarıyla tempoyu hiç düşürmüyor.🐉 4. Sekiro: Shadows Die Twice Neden Seçtim? Reflekslere dayalı yoğun dövüş sistemiyle "saf aksiyon"u zorlukla birleştiriyor. Boss savaşları, düşman çeşitliliği ve Japonya temalı dünyasıyla adrenalini sürekli yüksek tutuyor.🧨 5. Just Cause 4 Neden Seçtim? Patlayıcı aksiyonun kitabını yazan oyunlardan biri. Açık dünya üzerinde çılgınca fizik kurallarını zorlayan araçlar, paraşütle süzülmeler ve zincirleme patlamalarla sürekli hareket halindesin. 🚁 6. Titanfall 2 Neden Seçtim? FPS türünde benzersiz bir mekanik sunuyor: dev robotlarla savaş! Hem pilot hem de Titan olarak oynamak; hızlı koşu, duvar tırmanma ve zekice tasarlanmış görevlerle birleşince aksiyon zirveye ulaşıyor.')


@bot.command()
async def elmaskordinat(ctx):
    await ctx.send(f' Minecraftta y seviyesi -59da elmas bulabilirsiniz, ancak madencilik yaparken lavlardan korunmak için 1.21de Minecraft elmaslarını bulmak için en iyi seviye olarak y seviyesi -53ü öneriyoruz..')

@bot.command()
async def demirkordinat(ctx):
    await ctx.send(f' Demir cevherleri Y=0 yerine geçici olarak Y=-64ten üretiliyor.')

@bot.command()
async def ikiüçdörtkişilikoyunlar(ctx):
    await ctx.send(f' 2 kişilik: Portal 2 – yaratıcı iş birliği bulmacaları, It Takes Two – duygusal ve komik platform macerası, Mortal Kombat 11 – rekabetçi dövüş heyecanı, Stardew Valley – rahatlatıcı çiftlik kurarken ortak ilerleme, Don’t Starve Together – zorlu hayatta kalmayı paylaşmak, Cuphead – retro stilde zorlayıcı boss savaşları, A Way Out – sinematik kaçış hikâyesi; 3 kişilik: Deep Rock Galactic – üçlü ekip ile maden kazıp canavar avlama, Phasmophobia – hayalet avlarken takım korku gerilimi, Valheim – Viking temalı keşif ve inşa macerası, Gang Beasts – fizik tabanlı absürt dövüş, Overcooked 2 – mutfak kaosu yönetimi, Unrailed – birlikte ray döşeyip treni kurtarma, Sea of Thieves – ortak korsan serüveni; 4 kişilik: Left 4 Dead 2 – kooperatif zombi aksiyonu, Payday 2 – takım halinde soygun planlama, Minecraft – sınırsız inşa ve keşif, Raft – okyanusta hayatta kalma ve üs kurma, Keep Talking and Nobody Explodes – iletişim odaklı bomba çözme, Moving Out – esprili taşınma kaosu, Castle Crashers – çizgi film tarzı hack-and-slash')

@bot.command()
async def macera(ctx):
    await ctx.send(f' The Legend of Zelda: Breath of the Wild devasa bir açık dünya sunar, oyuncuya tam bir özgürlük hissi verir ve çevreyle etkileşimi çok üst düzeydedir. Red Dead Redemption 2 ise Vahşi Batı’da geçen derin ve duygusal hikâyesi, detaylı dünyası ve gerçekçi yaşam ögeleriyle büyüler. Uncharted 4: A Thief’s End, sinematik anlatımı ve eğlenceli karakter diyaloglarıyla hazine avcılığı temasını heyecanlı bir şekilde sunar. Hollow Knight 2D olmasına rağmen gizemli dünyası, atmosferi ve zorlayıcı oynanışıyla bağımlılık yaratır. Life is Strange serisi, oyuncunun kararlarıyla şekillenen duygusal hikâyeleri ve doğaüstü ögeleriyle öne çıkar. Tomb Raider (2013 sonrası), Lara Croft’un gelişimini gösteren aksiyon ve keşif dolu bir deneyim sunar. Firewatch ise aksiyon içermese de yalnızlık ve merak duygusunu ormanda geçen gizemli bir hikâyeyle başarıyla aktarır. The Witcher 3: Wild Hunt, derin karakterler, zengin yan görevler ve epik bir fantastik dünya ile unutulmaz bir macera sunar. Grafik öncelikli değilse klasikleşmiş Grim Fandango, Syberia ve Monkey Island serileri de nostaljik ve zekice kurgulanmış hikâyeleriyle tavsiye edilir')

@bot.command()
async def zümrütkordinat(ctx):
    await ctx.send(f' Zümrüt cevherleri Y=0 yerine geçici olarak Y=-64ten üretiliyor. Zümrüt cevheri artık Y=32 ile Y=320 arasında üçgen spread şeklinde oluşmakta ve Y=256da zirve yapmaktadır..')

@bot.command()
async def macera2(ctx):
    await ctx.send(f' Outer Wilds, zamanda sıkışmış bir güneş sistemi içinde geçer ve oyuncuya çevreyi gözlemleyerek gizemi çözme imkânı sunar. A Plague Tale: Innocence, Orta Çağ Fransa’sında geçen duygusal bir kardeşlik hikâyesi anlatır ve karanlık atmosferiyle dikkat çeker. Subnautica, su altı dünyasında hayatta kalma ve keşif ögelerini mükemmel bir şekilde harmanlar. What Remains of Edith Finch, aile geçmişini keşfetmeye dayalı kısa ama çok etkileyici bir anlatı deneyimi sunar. Sea of Thieves, arkadaşlarla birlikte oynanabilen korsan temalı açık dünya macerasıdır, hazine aramak, gemi kullanmak ve keşif yapmak oldukça keyiflidir. Assassin’s Creed Odyssey, antik Yunan’da geçen, tarihî öğelerle dolu devasa bir RPG-macera deneyimi sunar. Bioshock Infinite, alternatif tarih, felsefi temalar ve etkileyici anlatımıyla klasikleşmiş birinci şahıs macera oyunlarındandır. The Long Dark, kıyamet sonrası Kanada’da geçen sessiz ama zorlu bir hayatta kalma macerasıdır. Ori and the Blind Forest ve Ori and the Will of the Wisps, platform ögeleri, duygusal hikâyesi ve görsel güzelliğiyle macera tutkunlarının mutlaka denemesi gereken oyunlardandır. Kena: Bridge of Spirits ise hem savaş hem keşif içeren sevimli ve etkileyici bir animasyon film tadında oynanış sunar. Journey ise kısa ama ruhsal bir keşif deneyimiyle sanatsal bir oyun arayanlar için birebirdir.')

@bot.command()
async def aksiyon2(ctx):
    await ctx.send(f'Resident Evil 4 Remake, hem hayatta kalma hem de aksiyon unsurlarını mükemmel şekilde harmanlıyor. Gerilim dolu atmosferin ortasında hızlı çatışmalar ve taktiksel düşman etkileşimleri sunuyor. God of War (2018), sinematik anlatımı ve etkileyici dövüş mekanikleriyle duygusal bir hikayeyi yoğun aksiyonla birleştiriyor. Kratos’un baltasını kullanmak, her darbenin ağırlığını hissettiriyor. Bayonetta 2, stilize ve hızlı tempolu dövüşleri, absürt ama eğlenceli sahneleri ve harika animasyonlarıyla klasik bir aksiyon deneyimi sunuyor. Metal Gear Rising: Revengeance, müzikle senkronize çılgın kılıç dövüşleri ve unutulmaz boss savaşlarıyla temposunu hiç düşürmeyen bir aksiyon oyunu. Shadow of Mordor, Orta Dünya’da geçen açık dünyasıyla RPG ögelerini aksiyonla harmanlıyor, Nemesis sistemi sayesinde her düşman karşılaşması kendine özel. Control, telekinetik yeteneklerle çatışmanın ortasında olmanın nasıl hissettirdiğini çok iyi yansıtıyor, çevreyi silah gibi kullanmak aksiyonu eşsiz kılıyor. Far Cry 5, geniş bir açık dünya, çeşit çeşit silahlar ve kaotik çatışmalarla özgür bir aksiyon sunuyor. Parkur ve aksiyon isteyenler için Dying Light 2 harika bir seçenek; zombilerden kaçarken çatılardan atlarken aynı anda savaşıyorsun. Dead Space Remake, klasik korku öğelerine rağmen yüksek tempolu anlarıyla tam bir aksiyon-gerilim deneyimi sunuyor. Ninja Gaiden Sigma, refleks gerektiren hızlı kılıç dövüşleriyle zamanının ötesinde bir aksiyon oyunu. Max Payne 3 ise sinematik kamera açıları, ağır çekim çatışmalar ve karanlık atmosferiyle eski tarz aksiyon sevenler için birebir. The Last of Us Part II, sadece hikayesiyle değil, çatışma anlarında sunduğu yoğunluk ve gerçekçilikle de etkileyici bir aksiyon deneyimi sunuyor. Wolfenstein II: The New Colossus, alternatif tarih temasıyla bol silahlı ve tempolu çatışmalar sunuyor. Vanquish, bilimkurgu temalı hızlı kaymalar ve yavaşlatılmış çatışma mekanikleriyle benzersiz bir deneyim sunuyor..')

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
async def heh(ctx, count_heh = 5):
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
    
@bot.event
async def on_message(message):

    if message.author == bot.user:
        return


    if message.attachments:
        for attachment in message.attachments:
            if any(attachment.filename.lower().endswith(ext) for ext in ['.png']):
                await message.channel.send("bu bir elmas en yoğun olarak -59. katmanda yer alır. Lav tehlikesine karşı dikkatli olarak -54 ve -59 arasında ihtiyacınız olan elmas madenini kolaylıkla bulabilirsiniz.")  
                break  


    if message.attachments:
        for attachment in message.attachments:
            if any(attachment.filename.lower().endswith(ext) for ext in ['.jpeg']):
                await message.channel.send("Bu bir demir Minecraft demir Y: 72'den en altı olan Y: -64'e kadar bir aralıkta bulunabiliyor. Bunun yanında en fazla bulunduğu yükseklik ise Y: 15'tir.")  
                break 
    await bot.process_commands(message)


print

    
bot.run('')