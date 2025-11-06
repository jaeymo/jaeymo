import random
import re

quotes = [
    '"Greatness demands sacrifice." — *The Rage of Dragons* by Evan Winters',
    '"The days without difficulty are the days you do not improve." — *The Rage of Dragons* by Evan Winters',
]

quote = random.choice(quotes)

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

readme = re.sub(
    r'(> ".*?"\s*\n> — .*?\n)',
    f'> {quote}\n',
    readme,
    count=1
)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)
