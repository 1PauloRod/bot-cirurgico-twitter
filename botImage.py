from PIL import Image, ImageDraw, ImageFont
import textwrap
from utils import create_filename

class BotImage:
        
    def create_image(self, text, subtext):
        image = Image.open("baseImage/image.png")
        font_size_text = 85
        font_size_subtext = 40
        max_width_text = (image.width - (image.width/2 - 310))//(font_size_text//2) 
        max_width_subtext = 55
        position_text = (image.width/2 - 310, image.height/2 - 200)
        
        draw = ImageDraw.Draw(image)
        
        number_of_lines = self.number_of_lines(text, max_width_text)
        margin_between_text_subtext = 15
        position_subtext = (position_text[0], position_text[1] + number_of_lines * font_size_text + margin_between_text_subtext)

        wrapped_text = textwrap.fill(text, width=max_width_text)
        wrapped_subtext = textwrap.fill(subtext, width=max_width_subtext)
        
        try:
            font_text = ImageFont.truetype("arial.ttf", font_size_text)
            font_subtext = ImageFont.truetype("arial.ttf", font_size_subtext)
        except IOError:
            font_text = ImageFont.load_default()
            font_subtext = ImageFont.load_default()
            
        draw.multiline_text(position_text, wrapped_text, font=font_text, fill="black")
        draw.multiline_text(position_subtext, wrapped_subtext, font=font_subtext, fill="black")
        
        image_name = create_filename(subtext)
        image.save('createdImage/{}.jpg'.format(image_name))
        
    def number_of_lines(self, text, max_width_text):
        wrapped_lines = textwrap.wrap(text, width=max_width_text)   
        return len(wrapped_lines)
        
        