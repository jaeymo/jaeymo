import time
import random
import re
import urllib.parse

cache_buster = str(int(time.time()))

quotes = [
    '"The days without difficulty are the days you do not improve." — The Rage of Dragons by Evan Winters',
    '"Truth can be a burden, but secrets are poison." — The Light of All That Falls by James Islington',
    '"It\'s never acceptable to be less than you are." — The Rage of Dragons by Evan Winters',
    '"The measure of a man is what he does when he has power." — Red Rising by Pierce Brown',
    '"It\'s hard knowing when you\'ll go bankrupt when the currency you spend is time."',
    '"The muscle of willpower is invisible, but it\'s there." — My Friend\'s Dad',
    '"To have no peace is to feel like a guest in your own home." — Legend 2026',
    '"Better terrible truths than kind lies." — Six of Crows by Leigh Bardugo',
    '"An investment in knowledge pays the best interest" — Benjamin Franklin',
    '"Greatness demands sacrifice." — The Rage of Dragons by Evan Winters',
    '"Guilt is the idiot cousin of remorse." — Scythe by Neal Shusterman',
    '"CLANG. CLANG. CLANG. — CONFESS" — Lightbringer by Pierce Brown',
    '"An addiction to learning is difficult to satiate" — Unknown',
]

quote = random.choice(quotes)

encoded_quote = urllib.parse.quote(quote)

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()
    
readme = re.sub(
    r'lines=.*?&v=\d+',
    f'lines={encoded_quote}&cacheSeconds=0&v={cache_buster}',
    readme,
    count=1
)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)