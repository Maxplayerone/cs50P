from fpdf import FPDF

def main():
    create_user_shirt( input("What is your name? ") )

def create_user_shirt(s):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", "B", 40)
    pdf.cell(200, 40, "CS50 shirtificate", align='C')
    pdf.image("shirtificate.png", 50, 50, 120, 120)
    pdf.set_font("Times", size=30)
    pdf.set_text_color(255, 255, 255)
    pdf.ln(60)
    pdf.cell(200, 40, f"{s} took CS50", align='C')
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()