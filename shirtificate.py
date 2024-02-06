# CS50 Shirtificate
# Problem Set 8

from fpdf import FPDF

class PDF():
    def __init__(self, name):
        self._pdf = FPDF()
        self._pdf.add_page()
        self._pdf.set_font("helvetica", "B", 50)
        self._pdf.cell(0,60, "CS50 Shirtificate", new_x = "LMARGIN", new_y = "NEXT", align = "C")
        self._pdf.image("shirtificate.png", w = self._pdf.epw)
        self._pdf.set_font_size(30)
        self._pdf.set_text_color(255,255,255)
        self._pdf.text(x = 45, y = 150, text = f"{name} took CS50")

    def save(self,name):
        self._pdf.output(name)

name = input ("Name: ")
pdf = PDF(name)
pdf.save("shirtificate.pdf")



"""
# Below is same, but not object oriented

name = input ("Name: ")
pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", "B", 45)
pdf.cell(0,60, "CS50 Shirtificate", align = "C")
pdf.image("shirtificate.png", x = 0, y = 70)
pdf.set_font_size(30)
pdf.set_text_color(255,255,255)
pdf.text(x = 45, y = 150, text = f"{name} took CS50")
pdf.output("shirtificate.pdf")
"""
