proyecto = input("Nombre del proyecto: ")
horas_estimadas = int(input("Horas estimadas: "))
costo_hora = float(input("Costo por hora: "))
tiempo_estimado = int(input("Tiempo estimado (en meses): "))
valor_total = horas_estimadas * costo_hora



from fpdf import FPDF

pdf = FPDF()

pdf.add_page()
pdf.set_font("Arial", size=12)

pdf.image("Template.png", 0, 0)

pdf.text(115, 145, str(proyecto))
pdf.text(115, 160, str(horas_estimadas))
pdf.text(115, 175, str(costo_hora))
pdf.text(115, 190, str(tiempo_estimado))
pdf.text(115, 205, f"{valor_total:.2f}")

pdf.output("presupuesto.pdf")
print("El presupuesto ha sido generado exitosamente.")

