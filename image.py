from PIL import Image, ImageDraw, ImageFont
import textwrap

def saveSubmission(title):
    lines = textwrap.wrap(title, width=90)

    img = Image.new('RGB', (1920, 1080), color = (24, 25, 26))

    font = ImageFont.truetype("font/OpenSans-Regular.ttf", 42)
    fontAskReddit = ImageFont.truetype("font/OpenSans-Regular.ttf", 32)

    d = ImageDraw.Draw(img)
    d.text((30,320), "/r/AskReddit", fill=(255,255,205), font=fontAskReddit)

    y_text = 350
    for line in lines:
        width, height = font.getsize(line)
        d.text((30, y_text), line, font=font, fill=(207, 206, 207))
        y_text += height

    img.save('images/frame1.png')

def saveComment(author, text, fontSize, frame):
    lines = textwrap.wrap(text, width=90)

    font = ImageFont.truetype("font/OpenSans-Regular.ttf", fontSize)
    authorFont = ImageFont.truetype("font/OpenSans-Regular.ttf", 32)

    img = Image.new('RGB', (1920, 1080), color = (24, 25, 26))
    d = ImageDraw.Draw(img)

    d.text((30, 205), author, font=authorFont, fill=(103, 174, 217))

    y_text = 240
    for line in lines:
        width, height = font.getsize(line)
        d.text((30, y_text), line, font=font, fill=(207, 206, 207))
        y_text += height

    img.save("images/frame" + str(frame) + ".png")