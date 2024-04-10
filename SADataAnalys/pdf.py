from fpdf import FPDF 

def create_pdf(content='test', name='Andrew'):
    pdf = FPDF(format='letter', orientation='portrait', unit='mm')

    pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf')

    pdf.add_page()
    pdf.set_left_margin(25.4)
    pdf.set_right_margin(25.4)

    pdf.set_font(family='courier', style='bu', size=24)
    pdf.cell(w=0, h=10, text=f'GETTING TO KNOW {name}', border=0, align='C', fill=False, link='')
    pdf.set_xy(pdf.l_margin, pdf.get_y() + 10)
    pdf.set_font(family='DejaVu', style='', size=9)
    pdf.ln(h=5)
    pdf.multi_cell(w=0, h=3, text=content, border=0, align='L')

    pdf.output(name='testpdf.pdf')


def main():
    create_pdf()

if __name__ == '__main__':
    main()