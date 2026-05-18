import time
import random
import re
import urllib.parse

cache_buster = str(int(time.time()))

quotes = [
    '"It\'s never acceptable to be less than you are." — The Rage of Dragons by Evan Winters',
    '"The measure of a man is what he does when he has power." — Red Rising by Pierce Brown',
    '"It\'s hard knowing when you\'ll go bankrupt when the currency you spend is time."',
    '"The muscle of willpower is invisible, but it\'s there." — My Friend\'s Dad',
    '"To have no peace is to feel like a guest in your own home." — Legend 2026',
    '"An investment in knowledge pays the best interest" — Benjamin Franklin',
    '"Greatness demands sacrifice." — The Rage of Dragons by Evan Winters',
    '"Guilt is the idiot cousin of remorse." — Scythe by Neal Shusterman',
    '"Do everything or nothing—death still comes" — The Iliad by Homer',
    '"CLANG. CLANG. CLANG. — CONFESS" — Lightbringer by Pierce Brown',
    '"An addiction to learning is difficult to satiate"',
]

quote = random.choice(quotes)

encoded_quote = urllib.parse.quote(quote)

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()
    
readme = re.sub(
    r'lines=.*?&cacheSeconds=0&v=\d+',
    f'lines={encoded_quote}&cacheSeconds=0&v={cache_buster}',
    readme
)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)
