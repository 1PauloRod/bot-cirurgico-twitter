from PIL import Image, ImageDraw, ImageFont
import textwrap

# Carregar a imagem
image = Image.open('image.png')


# Inicializar o objeto de desenho
draw = ImageDraw.Draw(image)

def textsize(text, max_width):
    wrapped_lines = textwrap.wrap(text, width=max_width)
            
    return len(wrapped_lines)
        

# Definir o texto e a posição
texto = "'so mina feia e muleque lerdao nessa porra da escola vai tomar no cu porra tomar no cu crl aaa'"
posicao = (image.width/2 - 310, image.height/2 - 200)  # Exemplo de posição (x, y)

lenlines = textsize(texto, (image.width - (image.width/2 - 310))//(85//2))
subtexto = "- leofreire98, integrante fudido do fundão."
posicaosub = (posicao[0], posicao[1] + lenlines*85)

wrapped_text = textwrap.fill(texto, width=(image.width - (image.width/2 - 310))//(85//2))

wrapped_subtext = textwrap.fill(subtexto, width=55)

# Definir a fonte e o tamanho (opcional)
try:
    fonte1 = ImageFont.truetype("arial.ttf", 85)
    fonte2 = ImageFont.truetype("arial.ttf", 50)
except IOError:
    fonte1 = ImageFont.load_default()  # Use a fonte padrão se não encontrar o arquivo .ttf
    fonte2 = ImageFont.load_default()

draw.multiline_text(posicao, wrapped_text, font=fonte1, fill="black")
draw.multiline_text(posicaosub, wrapped_subtext, font=fonte2, fill="black")


# Salvar a imagem com o texto
image.save('imagem_com_texto.jpg')
