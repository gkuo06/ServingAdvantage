import os
from fpdf import FPDF 

def create_pdf():
    pdf = FPDF()

    pdf.add_page()
    pdf.set_margins(2.54, 2.54)
    pdf.set_font(family='courier', style='bu', size=24)
    pdf.cell(w=0, h=10, txt='AHHHH', border=0, ln=1, align='c', fill=False, link='')
    pdf.set_font(family='arial', style='', size=9)
    pdf.cell(w=0, h=10, txt='THIS IS A BIGGER AND BETTER TEST LOOOOL', border=0, ln=1, align='r', fill=False, link='')

    pdf.output(dest='f', name='test.pdf')


def main():
    create_pdf()

if __name__ == '__main__':
    main()