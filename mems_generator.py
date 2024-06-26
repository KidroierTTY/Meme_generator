from PIL import Image, ImageDraw, ImageFont

print("Генератор мемов запущен!")

top_text = input("Введите верхний текст: ")
bottom_text = input("Введите нижний текст: ")

print(top_text, bottom_text)

print("Список картинок:")
print("1. Кот в ресторане")
print("2. Кот в очках")

image_number = int(input("Введи номер нужной тебе картинки:"))

if image_number == 1:
    image_file = "Кот в ресторане.png"
else:
    image_file = "Кот в очках.png"

image = Image.open(image_file)
wigth, height = image.size

draw = ImageDraw.Draw(image)

font = ImageFont.truetype("arial.ttf", size=70)

text = draw.textbbox((0, 0), top_text, font)
text_wight = text[2]

draw.text(((wigth - text_wight) / 2, 0), top_text, font=font, fill="black")

text = draw.textbbox((0, 0), bottom_text, font)
text_wight = text[2]
text_heidht = text[3]

draw.text(((wigth - text_wight) / 2, height - text_heidht - 10), bottom_text, font=font, fill="black")


image.save("new_meme.jpg")
