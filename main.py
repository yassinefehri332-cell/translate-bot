import discord
from discord.ext import commands
from deep_translator import GoogleTranslator
import os

TOKEN = os.environ.get("TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

LANGUAGES = {
    "arabic": "ar", "english": "en", "french": "fr",
    "spanish": "es", "german": "de", "russian": "ru",
    "chinese": "zh-CN", "japanese": "ja", "korean": "ko",
    "turkish": "tr", "italian": "it", "portuguese": "pt",
    "polish": "pl", "hindi": "hi", "bengali": "bn",
    "urdu": "ur", "persian": "fa", "hebrew": "he",
    "indonesian": "id", "thai": "th", "vietnamese": "vi",
    "filipino": "tl", "swedish": "sv", "norwegian": "no",
    "danish": "da", "finnish": "fi", "dutch": "nl",
    "greek": "el", "czech": "cs", "romanian": "ro",
    "hungarian": "hu", "ukrainian": "uk", "malay": "ms",
    "afrikaans": "af", "albanian": "sq", "armenian": "hy",
    "azerbaijani": "az", "bulgarian": "bg", "catalan": "ca",
    "croatian": "hr", "estonian": "et", "georgian": "ka",
    "gujarati": "gu", "icelandic": "is", "irish": "ga",
    "kazakh": "kk", "khmer": "km", "lao": "lo",
    "latvian": "lv", "lithuanian": "lt", "macedonian": "mk",
    "maltese": "mt", "mongolian": "mn", "nepali": "ne",
    "serbian": "sr", "sinhala": "si", "slovak": "sk",
    "slovenian": "sl", "somali": "so", "swahili": "sw",
    "tamil": "ta", "telugu": "te", "uzbek": "uz",
    "welsh": "cy", "burmese": "my", "amharic": "am",
    # اختصارات وبلدان
    "chine": "zh-CN", "china": "zh-CN", "france": "fr",
    "spain": "es", "germany": "de", "japan": "ja",
    "korea": "ko", "italy": "it", "russia": "ru",
    "turkey": "tr", "morocco": "ar", "tunisia": "ar",
    "algeria": "ar", "egypt": "ar", "brazil": "pt",
    "mexico": "es", "india": "hi", "iran": "fa",
    "israel": "he", "greece": "el", "sweden": "sv",
}

@bot.command()
async def translate(ctx, *, args: str):
    try:
        if " to " not in args.lower():
            await ctx.send("❌ الاستخدام الصحيح:\n`!translate مرحبا to english`")
            return

        parts = args.lower().split(" to ")
        text = args[:args.lower().index(" to ")].strip()
        lang = parts[-1].strip()

        if lang not in LANGUAGES:
            await ctx.send(f"❌ اللغة `{lang}` مش موجودة!\n✅ مثال: `!translate مرحبا to english`")
            return

        translated = GoogleTranslator(source='auto', target=LANGUAGES[lang]).translate(text)
        embed = discord.Embed(title="🌍 الترجمة", color=0x5865F2)
        embed.add_field(name="📝 النص الأصلي", value=text, inline=False)
        embed.add_field(name=f"✅ {lang.capitalize()}", value=translated, inline=False)
        await ctx.send(embed=embed)

    except Exception as e:
        await ctx.send(f"❌ صار خطأ: {e}")

@bot.event
async def on_ready():
    print(f"✅ البوت شغال: {bot.user}")

bot.run(TOKEN)
