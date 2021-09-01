# A simple script to calculate profit or loss
import pywebio
from pywebio.input import input, FLOAT
from pywebio.output import put_text, put_html, put_markdown, put_table

def profitAndLoss():
    sp = input("Input your Selling Price：", type=FLOAT)
    cp = input("Input your Cost Price：", type=FLOAT)

    value = cp - sp
    put_markdown('# **Results**')
    if value > 0 :
        put_text('Your profit is %.1f' %(value))
    elif value < 0:
        put_text('Your loss is %.1f' %(value))
    else : 
        put_text('You got neither profit nor loss')

if __name__ == '__main__':
    pywebio.start_server(profitAndLoss, port=8000)
