from fpdf import FPDF
#Set header
class PDF(FPDF):
    def header(self):
        self.image("images.jpeg", 10, 8, 33)
        self.set_font("helvetica", style="B", size=15)
        self.cell(50)
        self.cell(100, 10, "Ramjas Public School Day Boarding", align="C")
        self.ln(10)
        self.cell(50)
        self.cell(100, 10, "Anand Parbat New Delhi-110009", align="C")
        self.ln(35)

pdf = PDF()
pdf.add_page()
#Set image
pdf.image("hiten.jpeg", x=160, y=55,h=30,w=30)
#Set watermark
with pdf.local_context(fill_opacity=0.25):
    pdf.image( "images.jpeg", x=55,y=108.5,h=pdf.eph/2,w=pdf.epw/2)


pdf.set_font('helvetica', size=12,style="B")
#Information
pdf.cell(150,10,"Name: Hiten Mehra",1,new_x="LEFT",new_y="NEXT")
pdf.cell(150,10,"Roll number: 14",1,new_x="LEFT",new_y="NEXT")
pdf.cell(150,10,"Address: Karol Bagh",1,new_x="LEFT",new_y="NEXT")
pdf.ln(13)
#Heading
pdf.cell(20,15,"S.No.",1,align="C")
pdf.cell(83,15,"Subject",1,align="C")
pdf.cell(83,15,"Marks",1,align="C",new_x="LMARGIN",new_y="NEXT")
#1st row
pdf.cell(20,15,"1",1,align="C")
pdf.cell(83,15,"Physics",1,align="C")
pdf.cell(83,15,"98",1,align="C",new_x="LMARGIN",new_y="NEXT")
#2nd row
pdf.cell(20,15,"2",1,align="C")
pdf.cell(83,15,"Chemistry",1,align="C")
pdf.cell(83,15,"100",1,align="C",new_x="LMARGIN",new_y="NEXT")
#3rd row
pdf.cell(20,15,"3",1,align="C")
pdf.cell(83,15,"Maths",1,align="C")
pdf.cell(83,15,"100",1,align="C",new_x="LMARGIN",new_y="NEXT")
#4th row
pdf.cell(20,15,"4",1,align="C")
pdf.cell(83,15,"English",1,align="C")
pdf.cell(83,15,"98",1,align="C",new_x="LMARGIN",new_y="NEXT")
#5th row
pdf.cell(20,15,"5",1,align="C")
pdf.cell(83,15,"Computer Science",1,align="C")
pdf.cell(83,15,"100",1,align="C",new_x="LMARGIN",new_y="NEXT")
#Aggregate
pdf.cell(103,15,"Aggregate",1,align="C")
pdf.cell(83,15,"496",1,align="C",new_x="LMARGIN",new_y="NEXT")
#Percentage
pdf.cell(103,15,"Percentage",1,align="C")
pdf.cell(83,15,"99.2",1,align="C",new_x="LMARGIN",new_y="NEXT")
#Result
pdf.cell(103,15,"Result",1,align="C")
pdf.cell(83,15,"Pass",1,align="C",new_x="LMARGIN",new_y="NEXT")
#Division
pdf.cell(103,15,"Division",1,align="C")
pdf.cell(83,15,"99.2",1,align="C",new_x="LMARGIN",new_y="NEXT")



pdf.output("report_card.pdf")