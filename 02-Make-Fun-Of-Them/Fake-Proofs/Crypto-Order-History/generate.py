from datetime import datetime
from PIL import Image, ImageFont, ImageDraw

currency = input("Currency ticker: ")
amount = float(input("Traded amount: "))
fee = float(input("Exchange fee (in float): "))
date = input("Date (%Y-%m-%d %H:%M:%S): ") or datetime.now()

if type(date) is str:
	date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")

# Font styles
normal = 0
bold = 1

img = Image.open("base.png")
draw = ImageDraw.Draw(img)

def text(x, y, text, color=(0, 0, 0), size=16, style=normal, **kwargs):
	styles = ["Regular", "Medium"]

	font = ImageFont.truetype(f"Ubuntu-{styles[style]}.ttf", size)
	draw.text((x, y), text, color, font=font, **kwargs)

# Draw your current clock
text(60, 40, "10:50", size=32)

# Draw currency name
text(220, 300, currency, color=(172, 173, 192), size=40, style=bold)
text(80, 540, currency, size=40, style=bold)
text(80, 897, currency, size=40, style=bold)

# Draw Date
year = date.year
m = date.month
d = date.day
h = date.hour
mn = date.minute
s = date.second
text(90, 430, f"{year}-{m:02}", size=28)
text(80, 600, f"{year}-{m:02}-{d:02}   {h:02}:{mn:02}:{s:02}", color=(172, 173, 192), size=34)
text(80, 957, f"{year}-{m:02}-{d:02}   {h:02}:{mn:02}:{s:02}", color=(172, 173, 192), size=34)

# Draw first order (The fee order)
text(80, 720, "-%.8f" % (amount * fee), color=(255, 0, 0), size=34, style=bold)
after_fee = "%.8f" % (amount - amount * fee)
text(1000, 720, after_fee, size=34, style=bold, anchor="ra")

# Draw second order
text(80, 1070, "+%.8f" % amount, color=(37, 176, 154), size=34, style=bold)
text(1000, 1070, "%.8f" % amount, size=34, anchor="ra", style=bold)

# Save the result
img.save("result.png")
