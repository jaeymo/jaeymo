import random
import re

quotes = [
    '"Greatness demands sacrifice." — *The Rage of Dragons* by Evan Winters',
    '"The days without difficulty are the days you do not improve." — *The Rage of Dragons* by Evan Winters',
    '"It\'s never acceptable to be less than you are." — *The Rage of Dragons* by Evan Winters',
    '"To defend against failure, every day must be hard. Every day must strengthen you. For it\'s in the crucible of hard days that potential becomes power." — *The Rage of Dragons* by Evan Winters',
    '"Alliances made from convenience only ever weaken a cause." — *The Light of All That Falls* by James Islington',
    '"You should never judge the sides of an argument simply by who is doing the arguing." — *The Light of All That Falls* by James Islington',
    '"Truth can be a burden, but secrets are poison." — *The Light of All That Falls* by James Islington',
    '"The muscle of willpower is invisible, but it\'s there." — *My Friend\'s Dad*',
    '"The measure of a man is what he does when he has power." — *Red Rising* by Pierce Brown',
    '"But of all the things in all the worlds, words are power." — *Red Rising* by Pierce Brown',
    '"Our lives mean so much more than the frail bodies that carry them." — *Golden Son* by Pierce Brown',
    '"We each survive in our own way." — *Throne of Glass* by Sarah J. Maas',
    '"The fear of loss... it can destroy you as much as the loss itself." — *Empire of Storms* by Sarah J. Maas',
    '"Better terrible truths than kind lies." — *Six of Crows* by Leigh Bardugo',
    '"Without the threat of suffering, we can\'t experience true joy." — *Scythe* by Neal Shusterman',
    '"Guilt is the idiot cousin of remorse." — *Scythe* by Neal Shusterman',
    '"Friendships take minutes to make, moments to break, and years to repair." — *Golden Son* by Pierce Brown',
    '"Stories are the wealth of humanity!" — *Iron Gold* by Pierce Brown',
    '"Your \"Plan B\" is the exact reason your \"Plan A\" failed." — *Blue Lock*',
    '"Friendship—my definition—is built on two things. Respect and trust. Both elements have to be there. And it has to be mutual. You can have respect for someone, but if you don\'t have trust, the friendship will crumble." — *The Girl With the Dragon Tattoo* by Stieg Larsson',
    '"*CLANG CLANG CLANG*\nCONFESS" — *Lightbringer* by Pierce Brown',
    '"It\'s hard knowing when you\'ll go bankrupt when the currency you spend is time." — *Legend 2026*'
]

quote = random.choice(quotes)

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

readme = re.sub(
    r'(_\*\*Quote of the Day.*?\*\*_\s*\n>[\s\S]*?\n)',
    f'_**Quote of the Day (yes this does update everyday)**_ \n> {quote}\n',
    readme,
    count=1
)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)
