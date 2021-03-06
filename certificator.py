import xlrd
import os
import sys
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

# Meant to convert full names to abbreviations
def shorten( text, _max ):
    t = text.split(" ")
    text = ''
    if len(t)>1:
        for i in t[:-1]:
            text += i[0] + '.'
    text += ' ' + t[-1]
    if len(text) < _max :
        return text
    else :
        return -1

# Add name, institute and project to certificate
def make_certi( cpf, name, institute='Universidade Federal do Para', project='gerador de certificado' ):
    img = Image.open("Template.jpg")
    draw = ImageDraw.Draw(img)
    # Load font
    font = ImageFont.truetype("a.TTF", 60)

    # Check sizes and if it is possible to abbreviate
    # if not the IDs are added to an error list
    if ( len( name ) > 20 ):
        name = shorten( name, 20 )
    if ( len( institute ) > 30 ):
        institute = shorten( institute, 30 )
    if ( len( project ) > 20 ):
        project = shorten( project, 20 )

    if name == -1 or project == -1 or institute == -1 :
        return -1
    else:
        # Insert text into image template
        draw.text( (900, 520), name, (0,0,255), font=font )
        draw.text( (600, 580), institute, (0,0,255), font=font )
        draw.text( (450, 685), project, (0,0,255), font=font )

        if not os.path.exists( 'certificates' ) :
            os.makedirs( 'certificates' )

        # Save as a PDF
        img.save( 'certificates/'+str(cpf)+'.pdf', "PDF", resolution=100.0)
        return 'certificates/'+str(cpf)+'.pdf'

if __name__ == "__main__":
    pass
