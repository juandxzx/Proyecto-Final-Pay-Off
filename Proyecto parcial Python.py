from tkinter import *
import random
import os
import sys
from tkinter import messagebox

class Inventario_novo:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1350x700")

        self.root.title("Pay Off System™")
        title=Label(self.root,text="CREAR FACTURA Pay Off™",font=("Tw Cen MT Condensed Extra Bold", 35)).pack(fill=X)


##variables del programa
        self.iphone13=IntVar()
        self.iphone11=IntVar()
        self.samsungs22=IntVar()
        self.iphoneSE=IntVar()
        self.motog22=IntVar()
        self.samsungzfold=IntVar()
        self.mi12lite=IntVar()
        self.parlantebose = IntVar()
        self.speakerjbl = IntVar()
        self.speakerhuawei = IntVar()
        self.airpods = IntVar()
        self.freebuds = IntVar()
        self.wacom = IntVar()
        self.powerbank = IntVar()
        self.applewatch = IntVar()
        self.galaxywatch = IntVar()
        self.huaweiwatch = IntVar()
        self.total_celuares= StringVar()
        self.total_speakers = StringVar()
        self.total_accesorios = StringVar()
        self.a = StringVar()
        self.b = StringVar()
        self.c = StringVar()
        self.nombre_c = StringVar()
        self.fact_no = StringVar()
        x = random.randint(1000, 9999)
        self.fact_no.set(str(x))
        self.telef = StringVar()

#seccion clientes-------------------------------------------------------------------------------------------------------------------------------------
        details = LabelFrame(self.root, text="Datos del Cliente", font=("Tw Cen MT Condensed Extra Bold", 12), fg="black")
        details.place(x=0, y=80)
        nombre_name = Label(details, text="Nombre del Cliente", font=("Tw Cen MT Condensed Extra Bold", 14), fg="black").grid(row=0, column=0, padx=15)
        nombre_entry = Entry(details, borderwidth=4, width=30,textvariable=self.nombre_c).grid(row=0, column=1, padx=8)

        telefono = Label(details, text="No. Telefonico", font=("Tw Cen MT Condensed Extra Bold", 14), fg="black").grid(row=0, column=2, padx=10)
        telefono_entry = Entry(details, borderwidth=4, width=30,textvariable=self.telef).grid(row=0, column=3, padx=8)

        fact_name = Label(details, text="No. Factura", font=(
            "Tw Cen MT Condensed Extra Bold", 14), fg="black").grid(row=0, column=4, padx=10)
        fact_entry = Entry(details, borderwidth=4, width=30,textvariable=self.fact_no).grid(row=0, column=5, padx=8)

# celulares-------------------------------------------------------------------------------------------------------------------------------------
        
        celulares = LabelFrame(self.root, text="Smarthphones", font=("Tw Cen MT Condensed Extra Bold", 12), fg="black", relief=GROOVE, bd=10)
        celulares.place(x=5, y=180, height=380, width=325)

        prod_1 = Label(celulares, text="iPhone 13", font=("Tw Cen MT Condensed Extra Bold", 11), fg="black").grid(row=0, column=0, pady=11)
        prod_1_entry = Entry(celulares, borderwidth=2, width=15,textvariable=self.iphone13).grid(row=0, column=1, padx=10)

        prod_2 = Label(celulares, text="iPhone 11", font=("Tw Cen MT Condensed Extra Bold", 11), fg="black").grid(row=1, column=0, pady=11)
        prod_2_entry = Entry(celulares, borderwidth=2, width=15,textvariable=self.iphone11).grid(row=1, column=1, padx=10)

        prod_3 = Label(celulares, text="Samsung S22", font=("Tw Cen MT Condensed Extra Bold", 11), fg="black").grid(row=2, column=0, pady=11)
        item3_entry = Entry(celulares, borderwidth=2, width=15,textvariable=self.samsungs22).grid(row=2, column=1, padx=10)

        prod_4 = Label(celulares, text="iPhone SE", font=("Tw Cen MT Condensed Extra Bold", 11), fg="black").grid(row=3, column=0, pady=11)
        prod_4_entry = Entry(celulares, borderwidth=2, width=15,textvariable=self.iphoneSE).grid(row=3, column=1, padx=10)

        prod_5 = Label(celulares, text="Moto G22", font=("Tw Cen MT Condensed Extra Bold", 11), fg="black").grid(row=4, column=0, pady=11)
        prod_5_entry = Entry(celulares, borderwidth=2, width=15,textvariable=self.motog22).grid(row=4, column=1, padx=10)

        prod_6 = Label(celulares, text="Samsung Z Fold", font=("Tw Cen MT Condensed Extra Bold", 11), fg="black").grid(row=5, column=0, pady=11)
        prod_6_entry = Entry(celulares, borderwidth=2, width=15,textvariable=self.samsungzfold).grid(row=5, column=1, padx=10)

        prod_7 = Label(celulares, text="Mi 12lite", font=("Tw Cen MT Condensed Extra Bold", 11), fg="black").grid(row=6, column=0, pady=11)
        prod_7_entry = Entry(celulares, borderwidth=2, width=15,textvariable=self.mi12lite).grid(row=6, column=1, padx=10)


#speakers-------------------------------------------------------------------------------------------------------------------------------------
        speakers = LabelFrame(self.root, text="Speakers", font=("Tw Cen MT Condensed Extra Bold", 12), relief=GROOVE, bd=10, fg="black")
        speakers.place(x=340, y=180, height=380, width=325)

        prod_8  = Label(speakers, text="Parlante Bose", font=("Tw Cen MT Condensed Extra Bold", 11), fg="black").grid(row=0, column=0, pady=11)
        prod_8_entry = Entry(speakers, borderwidth=2, width=15,textvariable=self.parlantebose).grid(row=0, column=1, padx=10)

        prod_9 = Label(speakers, text="Parlante JBL", font=("Tw Cen MT Condensed Extra Bold", 11), fg="black").grid(row=1, column=0, pady=11)
        prod_9_entry = Entry(speakers, borderwidth=2, width=15,textvariable=self.speakerjbl).grid(row=1, column=1, padx=10)

        prod_10 = Label(speakers, text="Speaker Huawei", font=("Tw Cen MT Condensed Extra Bold", 11), fg="black").grid(row=2, column=0, pady=11)
        prod_10_entry = Entry(speakers, borderwidth=2, width=15,textvariable=self.speakerhuawei).grid(row=2, column=1, padx=10)

        prod_11 = Label(speakers, text="Airpods", font=("Tw Cen MT Condensed Extra Bold", 11), fg="black").grid(row=3, column=0, pady=11)
        prod_11_entry = Entry(speakers, borderwidth=2, width=15,textvariable=self.airpods).grid(row=3, column=1, padx=10)

        prod_12 = Label(speakers, text="Freebuds", font=("Tw Cen MT Condensed Extra Bold", 11), fg="black").grid(row=4, column=0, pady=11)
        prod_12_entry = Entry(speakers, borderwidth=2, width=15, textvariable=self.freebuds).grid(row=4, column=1, padx=10)

# accesorios-------------------------------------------------------------------------------------------------------------------------------------
      
        accesorios = LabelFrame(self.root, text="Accesorios", font=("Tw Cen MT Condensed Extra Bold", 12), relief=GROOVE, bd=10, fg="black")
        accesorios.place(x=677, y=180, height=380, width=325)

        prod_13 = Label(accesorios, text="WACOM", font=("Tw Cen MT Condensed Extra Bold", 11), fg="black").grid(row=0, column=0, pady=11)
        prod_13_entry = Entry(accesorios, borderwidth=2, width=15,textvariable=self.wacom).grid(row=0, column=1, padx=10)

        prod_14 = Label(accesorios, text="Powerbank", font=("Tw Cen MT Condensed Extra Bold", 11), fg="black").grid(row=1, column=0, pady=11)
        prod_14_entry = Entry(accesorios, borderwidth=2, width=15,textvariable=self.powerbank).grid(row=1, column=1, padx=10)

        prod_15 = Label(accesorios, text="AppleWatch", font=("Tw Cen MT Condensed Extra Bold", 11), fg="black").grid(row=2, column=0, pady=11)
        prod_15_entry = Entry(accesorios, borderwidth=2, width=15,textvariable=self.applewatch).grid(row=2, column=1, padx=10)

        prod_16 = Label(accesorios, text="GalaxyWatch", font=("Tw Cen MT Condensed Extra Bold", 11), fg="black").grid(row=3, column=0, pady=11)
        prod_16_entry = Entry(accesorios, borderwidth=2, width=15,textvariable=self.galaxywatch).grid(row=3, column=1, padx=10)

        prod_16 = Label(accesorios, text="Huawei watch", font=("Tw Cen MT Condensed Extra Bold", 11), fg="black").grid(row=4, column=0, pady=11)
        prod_16_entry = Entry(accesorios, borderwidth=2, width=15,textvariable=self.huaweiwatch).grid(row=4, column=1, padx=10)


#factura---------------------------------------------------------------------------------------------------------------

        fact_area = Frame(self.root, bd=10, relief=GROOVE)
        fact_area.place(x=1010, y=188, width=330, height=372)

        fact_title = Label(fact_area, text="Factura Previa", font=("Tw Cen MT Condensed Extra Bold", 17), bd=7, relief=GROOVE, fg="black").pack(fill=X)

##      scrol_y = Scrollbar(fact_area, orient=VERTICAL)
##      self.txtarea = Text(fact_area, yscrollcommand=scrol_y.set)    CORREGIR
##      scrol_y.pack(side=RIGHT, fill=Y)
##      scrol_y.config(command=self.txtarea.yview)
##      self.txtarea.pack(fill=BOTH, expand=1)

#parte inferior fact---------------------------------------------------------------------------------------------------------------

        factur_menu=LabelFrame(self.root, text="Facturaciòn individual", font=("Tw Cen MT Condensed Extra Bold", 12), relief=GROOVE, bd=10, fg="black")
        factur_menu.place(x=0, y=560, relwidth=1, height=137)

        total_cel = Label(factur_menu, text="Valor total telefonos", font=("Tw Cen MT Condensed Extra Bold", 11), bg="#3891c8", fg="black").grid(row=0, column=0)
        total_cel_entry = Entry(factur_menu, width=30, borderwidth=2,textvariable=self.total_celuares).grid(row=0, column=1, padx=10, pady=7)

        total_speaks = Label(factur_menu, text="Valor total Speakers", font=("Tw Cen MT Condensed Extra Bold", 11), bg="#3891c8", fg="black").grid(row=1, column=0)
        total_speaks_entry = Entry(factur_menu, width=30, borderwidth=2,textvariable=self.total_speakers).grid(row=1, column=1, padx=10, pady=7)

        total_acc = Label(factur_menu, text="Valor total Accesorios", font=("Tw Cen MT Condensed Extra Bold", 11), bg="#3891c8", fg="black").grid(row=2, column=0)
        total_acc_entry = Entry(factur_menu, width=30, borderwidth=2,textvariable=self.total_accesorios).grid(row=2, column=1, padx=10, pady=7)

        IVA_cel = Label(factur_menu, text="IVA celulares", font=("Tw Cen MT Condensed Extra Bold", 11), bg="#3891c8", fg="black").grid(row=0, column=2)
        IVA_cel_entry = Entry(factur_menu, width=30, borderwidth=2, textvariable=self.a).grid(row=0, column=3, padx=10, pady=7)

        IVA_speaks = Label(factur_menu, text="IVA speakers", font=("Tw Cen MT Condensed Extra Bold", 11), bg="#3891c8", fg="black").grid(row=1, column=2)
        IVA_speaks_entry = Entry(factur_menu, width=30, borderwidth=2, textvariable=self.b).grid(row=1, column=3, padx=10, pady=7)

        IVA_acc = Label(factur_menu, text="IVA accesorios", font=("Tw Cen MT Condensed Extra Bold", 11), bg="#3891c8", fg="black").grid(row=2, column=2)
        IVA_acc_entry = Entry(factur_menu, width=30, borderwidth=2, textvariable=self.c).grid(row=2, column=3, padx=10, pady=7)

        button_frame = Frame(factur_menu, bd=7, relief=GROOVE, bg="#fd7e1b")
        button_frame.place(x=830, width=500, height=95)

        button_total = Button(button_frame, text="Valor Facturado", font=("Franklin Gothic Demi", 15), pady=10, fg="black", command=lambda: total(self)).grid(row=0, column=0, padx=12)
        button_delete = Button(button_frame, text="Reiniciar", font=("Franklin Gothic Demi", 15), pady=10, fg="black", command=lambda: clear(self)).grid(row=0, column=1, padx=10, pady=6)
        button_salir= Button(button_frame, text="Salir", font=("Franklin Gothic Demi", 15), pady=10,fg="black", width=8, command=lambda: exit1(self)).grid(row=0, column=2, padx=10, pady=6)
        intro(self)


#Precios
def total(self):
    if (self.nombre_c.get == "" or self.telef.get() == ""):
        messagebox.showerror("Error", "Las casillas de datos del cliente son obligatorias")
    self.ip13 = self.iphone13.get()*3800
    self.ip11 = self.iphone11.get()*2500
    self.sg22 = self.samsungs22.get()*2700
    self.se = self.iphoneSE.get()*2000
    self.mot = self.motog22.get()*2100
    self.sgzf = self.samsungzfold.get()*7500
    self.xmil = self.mi12lite.get()*2350
    total_celulares_valor = (
        self.ip13 +
        self.ip11 +
        self.sg22 +
        self.se +
        self.mot +
        self.sgzf +
        self.xmil)
    self.total_celuares.set(str(total_celulares_valor)+" COP")
    self.a.set(str(round(total_celulares_valor*0.05, 3))+" COP")

    
    self.bose = self.parlantebose.get()*4500
    self.jbl = self.speakerjbl.get()*1250
    self.huawei = self.speakerhuawei.get()*11300
    self.air = self.airpods.get()*160050
    self.free = self.freebuds.get()*5550
    total_speakers_valor = (
        self.bose +
        self.jbl +
        self.huawei +
        self.air +
        self.free)

    self.total_speakers.set(str(total_speakers_price)+" COP")
    self.b.set(str(round(total_speakers_price*0.1, 3))+" COP")


    self.wa = self.wacom.get()*3000
    self.pw = self.powerbank.get()*18000
    self.aw = self.applewatch.get()*130000
    self.gw = self.galaxywatch.get()*50000
    self.hw = self.huaweiwatch.get()*8500
   

    total_acc_valor = (
        self.wa +
        self.pw +
        self.aw +
        self.gw +
        self.hw)

    self.total_accesorios.set(str(total_acc_valor)+" COP")
    self.c.set(str(round(total_acc_valor*0.07, 3))+" COP")
    self.total_all_fact = (total_celulares_valor +
                           total_speakers_valor +
                           total_acc_valor +
                           (round(total_acc_valor*0.1, 3)) +
                           (round(total_speakers_valor*0.07, 3)) +
                           (round(total_celulares_valor*0.05, 3)))
    self.total_all_fact = str(self.total_all_fact)+" COP"
    fact_area(self)

def intro(self):
    self.txtarea.delete(1.0, END)
    self.txtarea.insert(
        END, "\tBienvenid@ a tu NOMBRE TIENDA\n\tTeléfono +57 123456")
    self.txtarea.insert(END, f"\n\nFactura Número. : {self.fact_no.get()}")
    self.txtarea.insert(END, f"\nNombre Cliente : {self.c_name.get()}")
    self.txtarea.insert(END, f"\nTeléfono : {self.telef.get()}")
    self.txtarea.insert(END, "\n====================================\n")
    self.txtarea.insert(END, "\nProducto\t\tCant\tPrecio\n")
    self.txtarea.insert(END, "\n====================================\n")


def fact_area(self):
    intro(self)
    if self.iphone13.get() != 0:
        self.txtarea.insert(
            END, f"iPhone 13\t\t {self.iphone13.get()}\t{self.ip13}\n")
    if self.iphone11.get() != 0:
        self.txtarea.insert(
            END, f"iPhone 11\t\t {self.iphone11.get()}\t{self.ip11}\n")
    if self.samsungs22.get() != 0:
        self.txtarea.insert(
            END, f"Samsung s22\t\t {self.samsungs22.get()}\t{self.sg22}\n")
    if self.iphoneSE.get() != 0:
        self.txtarea.insert(
            END, f"iPhone SE\t\t {self.iphoneSE.get()}\t{self.se}\n")
    if self.motog22.get() != 0:
        self.txtarea.insert(
            END, f"Motorola G22\t\t {self.motog22()}\t{self.mot}\n")
    if self.samsungzfold.get() != 0:
        self.txtarea.insert(
            END, f"Samsung ZFold\t\t {self.samsungzfold.get()}\t{self.sgzf}\n")
    if self.mi12lite.get() != 0:
        self.txtarea.insert(
            END, f"Xiaomi mi12 lite\t\t {self.mi12lite.get()}\t{self.xmil}\n")


    if self.parlantebose.get() != 0:
        self.txtarea.insert(
            END, f"Parlante BOSE\t\t {self.parlantebose.get()}\t{self.bose}\n")
    if self.speakerjbl.get() != 0:
        self.txtarea.insert(
            END, f"Parlante JBL\t\t {self.speakerjbl.get()}\t{self.jbl}\n")
    if self.speakerhuawei.get() != 0:
        self.txtarea.insert(
            END, f"Speaker Huawei\t\t {self.speakerhuawei.get()}\t{self.huawei}\n")
    if self.airpods.get() != 0:
        self.txtarea.insert(
            END, f"AirPods\t\t {self.airpods.get()}\t{self.air}\n")
    if self.freebuds.get() != 0:
        self.txtarea.insert(
            END, f"Freebuds\t\t {self.freebuds.get()}\t{self.free}\n")

    if self.wacom.get() != 0:
        self.txtarea.insert(
            END, f"Wacom\t\t {self.wacom.get()}\t{self.wa}\n")
    if self.powerbank.get() != 0:
        self.txtarea.insert(
            END, f"Powerbank\t\t {self.powerbank.get()}\t{self.pw}\n")
    if self.applewatch.get() != 0:
        self.txtarea.insert(
            END, f"Apple Watch\t\t {self.applewatch.get()}\t{self.aw}\n")
    if self.galaxywatch.get() != 0:
        self.txtarea.insert(
            END, f"Galaxy Watch\t\t {self.galaxywatch.get()}\t{self.gw}\n")
    if self.huaweiwatch.get() != 0:
        self.txtarea.insert(
            END, f"Huawei-Watch\t\t {self.huaweiwatch.get()}\t{self.hw}\n")

    self.txtarea.insert(END, f"------------------------------------\n")
    if self.a.get() != "0.0 COP":
        self.txtarea.insert(END, f"Total IVA SmartPhones: {self.a.get()}\n")
    if self.b.get() != "0.0 COP":
        self.txtarea.insert(
            END, f"Total IVA Speakers: {self.b.get()}\n")
    if self.c.get() != "0.0 COP":
        self.txtarea.insert(
            END, f"Total IVA Accesorios: {self.c.get()}\n")
    self.txtarea.insert(END, f"Monto total facturado : {self.total_all_bil}\n")
    self.txtarea.insert(END, f"------------------------------------\n")


def clear(self):
    self.txtarea.delete(1.0, END)
    self.iphone13.set(0)
    self.iphone11.set(0)
    self.samsungs22.set(0)
    self.iphoneSE.set(0)
    self.motog22.set(0)
    self.samsungzfold.set(0)
    self.mi12lite.set(0)
    self.parlantebose.set(0)
    self.speakerjbl.set(0)
    self.speakerhuawei.set(0)
    self.airpods.set(0)
    self.freebuds.set(0)
    self.wacom.set(0)
    self.powerbank.set(0)
    self.applewatch.set(0)
    self.galaxywatch.set(0)
    self.huaweiwatch.set(0)
    self.total_celuares.set(0)
    self.total_speakers.set(0)
    self.total_accesorios.set(0)
    self.a.set(0)
    self.b.set(0)
    self.c.set(0)
    self.nombre_c.set(0)
    self.inventario_no.set(0)
    self.bill_no.set(0)
    self.telef.set(0)



def exit1(self):
    self.root.destroy()


root = Tk()
obj = Inventario_novo(root)
root.mainloop()
