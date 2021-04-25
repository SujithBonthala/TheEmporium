from tkinter import *
from tkinter import messagebox
import PIL as p
import PIL.ImageTk as ptk
import os
from datetime import datetime
root=Tk()
root.title("theemporium.in")
root.geometry("1360x1000")
Heading=LabelFrame(root,bd=2,relief="groove",bg="light yellow")
Heading.place(x=0,y=0,width=1380,height=55)
image_logo=p.Image.open("Images\Logo.png")
image_logo_1=ptk.PhotoImage(image_logo)
label_logo=Label(Heading,image=image_logo_1)
label_logo.grid(row=0,column=0)
image_logo_large=ptk.PhotoImage(p.Image.open("Images\Logo_Large.jpg"))
grocery1_image=ptk.PhotoImage(p.Image.open("Images\Grocery_1.jpg"))
grocery2_image=ptk.PhotoImage(p.Image.open("Images\Grocery_2.jpeg"))
grocery3_image=ptk.PhotoImage(p.Image.open("Images\Grocery_3.jpeg"))
grocery4_image=ptk.PhotoImage(p.Image.open("Images\Grocery_4.jpeg"))
grocery5_image=ptk.PhotoImage(p.Image.open("Images\Grocery_5.jpeg"))
grocery6_image=ptk.PhotoImage(p.Image.open("Images\Grocery_6.jpeg"))
grocery7_image=ptk.PhotoImage(p.Image.open("Images\Grocery_7.jpeg"))
grocery8_image=ptk.PhotoImage(p.Image.open("Images\Grocery_8.jpeg"))
grocery9_image=ptk.PhotoImage(p.Image.open("Images\Grocery_9.jpeg"))
grocery10_image=ptk.PhotoImage(p.Image.open("Images\Grocery_10.jpg"))
electronics1_image=ptk.PhotoImage(p.Image.open("Images\Electronics_1.jpeg"))
electronics2_image=ptk.PhotoImage(p.Image.open("Images\Electronics_2.jpeg"))
electronics3_image=ptk.PhotoImage(p.Image.open("Images\Electronics_3.jpeg"))
electronics4_image=ptk.PhotoImage(p.Image.open("Images\Electronics_4.jpeg"))
electronics5_image=ptk.PhotoImage(p.Image.open("Images\Electronics_5.jpeg"))
electronics6_image=ptk.PhotoImage(p.Image.open("Images\Electronics_6.jpeg"))
electronics7_image=ptk.PhotoImage(p.Image.open("Images\Electronics_7.jpeg"))
electronics8_image=ptk.PhotoImage(p.Image.open("Images\Electronics_8.jpeg"))
electronics9_image=ptk.PhotoImage(p.Image.open("Images\Electronics_9.jpeg"))
electronics10_image=ptk.PhotoImage(p.Image.open("Images\Electronics_10.jpeg"))
sportsgym1_image=ptk.PhotoImage(p.Image.open("Images\SportsGym_1.jpg"))
sportsgym2_image=ptk.PhotoImage(p.Image.open("Images\SportsGym_2.jpg"))
sportsgym3_image=ptk.PhotoImage(p.Image.open("Images\SportsGym_3.jpg"))
sportsgym4_image=ptk.PhotoImage(p.Image.open("Images\SportsGym_4.jpg"))
sportsgym5_image=ptk.PhotoImage(p.Image.open("Images\SportsGym_5.jpg"))
sportsgym6_image=ptk.PhotoImage(p.Image.open("Images\SportsGym_6.jpg"))
sportsgym7_image=ptk.PhotoImage(p.Image.open("Images\SportsGym_7.jpg"))
sportsgym8_image=ptk.PhotoImage(p.Image.open("Images\SportsGym_8.jpg"))
sportsgym9_image=ptk.PhotoImage(p.Image.open("Images\SportsGym_9.jpg"))
sportsgym10_image=ptk.PhotoImage(p.Image.open("Images\SportsGym_10.jpg"))
furniture1_image=ptk.PhotoImage(p.Image.open("Images\Furniture_1.jpeg"))
furniture2_image=ptk.PhotoImage(p.Image.open("Images\Furniture_2.jpeg"))
furniture3_image=ptk.PhotoImage(p.Image.open("Images\Furniture_3.jpeg"))
furniture4_image=ptk.PhotoImage(p.Image.open("Images\Furniture_4.jpeg"))
furniture5_image=ptk.PhotoImage(p.Image.open("Images\Furniture_5.jpeg"))
furniture6_image=ptk.PhotoImage(p.Image.open("Images\Furniture_6.jpeg"))
furniture7_image=ptk.PhotoImage(p.Image.open("Images\Furniture_7.jpeg"))
furniture8_image=ptk.PhotoImage(p.Image.open("Images\Furniture_8.jpeg"))
furniture9_image=ptk.PhotoImage(p.Image.open("Images\Furniture_9.jpeg"))
furniture10_image=ptk.PhotoImage(p.Image.open("Images\Furniture_10.jpeg"))
appliances1_image=ptk.PhotoImage(p.Image.open("Images\Appliances_1.jpeg"))
appliances2_image=ptk.PhotoImage(p.Image.open("Images\Appliances_2.jpeg"))
appliances3_image=ptk.PhotoImage(p.Image.open("Images\Appliances_3.jpeg"))
appliances4_image=ptk.PhotoImage(p.Image.open("Images\Appliances_4.jpeg"))
appliances5_image=ptk.PhotoImage(p.Image.open("Images\Appliances_5.jpeg"))
appliances6_image=ptk.PhotoImage(p.Image.open("Images\Appliances_6.jpeg"))
appliances7_image=ptk.PhotoImage(p.Image.open("Images\Appliances_7.jpeg"))
appliances8_image=ptk.PhotoImage(p.Image.open("Images\Appliances_8.jpeg"))
appliances9_image=ptk.PhotoImage(p.Image.open("Images\Appliances_9.jpeg"))
appliances10_image=ptk.PhotoImage(p.Image.open("Images\Appliances_10.jpeg"))
#Grocery Variables
clicked_grocery1=StringVar()
clicked_grocery1.set("250g - Rs.93")
clicked_grocery2=StringVar()
clicked_grocery2.set("5kg – Rs.235")
clicked_grocery3=StringVar()
clicked_grocery3.set("1kg – Rs.18")
clicked_grocery4=StringVar()
clicked_grocery4.set("1L – Rs.195")
clicked_grocery5=StringVar()
clicked_grocery5.set("500g – Rs.95")
clicked_grocery6=StringVar()
clicked_grocery6.set("55g – Rs.76")
clicked_grocery7=StringVar()
clicked_grocery7.set("120g – Rs.23")
clicked_grocery8=StringVar()
clicked_grocery8.set("200g – Rs.65")
clicked_grocery9=StringVar()
clicked_grocery9.set("500g – Rs.104")
clicked_grocery10=StringVar()
clicked_grocery10.set("70g – Rs.25")
grocery_list=[]
#Electronics Variables
clicked_electronics1=StringVar()
clicked_electronics1.set("Aurora Blue")
clicked_electronics2=StringVar()
clicked_electronics2.set("Aquamarine Green")
clicked_electronics3=StringVar()
clicked_electronics3.set("Black")
clicked_electronics4=StringVar()
clicked_electronics4.set("Black")
clicked_electronics5=StringVar()
clicked_electronics5.set("Charcoal Grey")
clicked_electronics6=StringVar()
clicked_electronics6.set("Shadow Black")
clicked_electronics7=StringVar()
clicked_electronics7.set("Black")
clicked_electronics8=StringVar()
clicked_electronics8.set("Black")
clicked_electronics9=StringVar()
clicked_electronics9.set("Jet Black")
clicked_electronics10=StringVar()
clicked_electronics10.set("Blue & White")
electronics_list=[]
#Sports and Gym variables
sportsgym_list=[]
#Furniture variables
furniture_list=[]
#Appliances variables
appliances_list=[]
name=Label(Heading,text="The Emporium",font="arial 20 bold italic",bg="light pink",fg="blue").grid(row=0,column=1)
tagline=Label(Heading,text="Shopping made easier!",font="magneto 16 italic",fg="gold",bg="black").grid(row=0,column=2,padx=280)
Products_frame=LabelFrame(root,bd=2,relief="groove",text="Products",font="arial 16 bold",fg="dark blue")
Products_frame.place(x=310,y=60,width=1040,height=620)
label_logo_large=Label(Products_frame,image=image_logo_large,bd=2).place(x=250,y=100)
label_enjoy=Label(Products_frame,text="Enjoy Shopping",font="castellar 20 bold").place(x=370,y=370)
Button_frame=LabelFrame(root,bd=2,relief="groove")
Button_frame.place(x=2,y=60,width=300,height=380)
def save_invoice(text):
    op=messagebox.askyesno("Invoice Saving Confirmation","Do you want to save the invoice in a file?")
    if op:
        t=datetime.now()
        s=str(t.day)+str(t.month)+str(t.year)+str(t.hour)+str(t.minute)+str(t.second)
        f=open("Invoices/"+s+".txt","w")
        f.write(text)
        f.close()
        messagebox.showinfo("Invoice Saving Status","Invoice is saved successfully as a text document with name "+s+".txt")
    else:
        messagebox.showinfo("Invoice Saving Status","The invoice is not saved into a file.")
def HideAllFrames():
    for widget in Products_frame.winfo_children():
        widget.destroy()
def Spaces(n,s1=" "):
    s=""
    for i in range(n):
        s+=s1
    return s
def GroceryCall():
    HideAllFrames()
    Grocery_Label=Label(Products_frame,text="Grocery",font="times 15 bold",fg="gold",bg="black").grid(row=0,column=0,padx=20)
    lf_grocery1=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_grocery1.place(x=5,y=35,width=180,height=280)
    lf_grocery2=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_grocery2.place(x=210,y=35,width=180,height=280)
    lf_grocery3=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_grocery3.place(x=415,y=35,width=180,height=280)
    lf_grocery4=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_grocery4.place(x=620,y=35,width=180,height=280)
    lf_grocery5=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_grocery5.place(x=825,y=35,width=180,height=280)
    lf_grocery6=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_grocery6.place(x=5,y=310,width=180,height=280)
    lf_grocery7=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_grocery7.place(x=210,y=310,width=180,height=280)
    lf_grocery8=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_grocery8.place(x=415,y=310,width=180,height=280)
    lf_grocery9=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_grocery9.place(x=620,y=310,width=180,height=280)
    lf_grocery10=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_grocery10.place(x=825,y=310,width=180,height=280)
    label_grocery_1=Label(lf_grocery1,image=grocery1_image,bd=2).grid(row=0,column=0)
    label_grocery_2=Label(lf_grocery2,image=grocery2_image,bd=2).grid(row=0,column=0)
    label_grocery_3=Label(lf_grocery3,image=grocery3_image,bd=2).grid(row=0,column=0,padx=13)
    label_grocery_4=Label(lf_grocery4,image=grocery4_image,bd=2).grid(row=0,column=0)
    label_grocery_5=Label(lf_grocery5,image=grocery5_image,bd=2).grid(row=0,column=0)
    label_grocery_6=Label(lf_grocery6,image=grocery6_image,bd=2).grid(row=0,column=0)
    label_grocery_7=Label(lf_grocery7,image=grocery7_image,bd=2).grid(row=0,column=0)
    label_grocery_8=Label(lf_grocery8,image=grocery8_image,bd=2).grid(row=0,column=0)
    label_grocery_9=Label(lf_grocery9,image=grocery9_image,bd=2).grid(row=0,column=0)
    label_grocery_10=Label(lf_grocery10,image=grocery10_image,bd=2).grid(row=0,column=0)
    name_grocery1=Label(lf_grocery1,text="Kellogg's Corn Flakes Original",font="arial 9").grid(row=1,column=0)
    name_grocery2=Label(lf_grocery2,text="Aashirwaad Superior Atta",font="arial 9",justify="center").grid(row=1,column=0,padx=15)
    name_grocery3=Label(lf_grocery3,text="Tata Iodized Salt",font="arial 9",justify="center").grid(row=1,column=0)
    name_grocery4=Label(lf_grocery4,text="Safal Filtered Groundnut Oil",font="arial 9",justify="center").grid(row=1,column=0,padx=9)
    name_grocery5=Label(lf_grocery5,text="24 Mantra Organic Toor Dal",font="arial 9",justify="center").grid(row=1,column=0,padx=9)
    name_grocery6=Label(lf_grocery6,text="Dairy Milk Silk Fruit & Nut",font="arial 9",justify="center").grid(row=1,column=0,padx=15)
    name_grocery7=Label(lf_grocery7,text="Yippee Noodles Magic Masala",font="arial 9",justify="center").grid(row=1,column=0)
    name_grocery8=Label(lf_grocery8,text="Kissan Mixed Fruit Jam",font="arial 9",justify="center").grid(row=1,column=0,padx=20)
    name_grocery9=Label(lf_grocery9,text="Mother's Recipe Mango Pickle",font="arial 9",justify="center").grid(row=1,column=0,padx=2)
    name_grocery10=Label(lf_grocery10,text="Parle's Cream & Onion Wafers",font="arial 9",justify="center").grid(row=1,column=0)
    label_qty_grocery1=Label(lf_grocery1,text="Qty:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_qty_grocery2=Label(lf_grocery2,text="Qty:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_qty_grocery3=Label(lf_grocery3,text="Qty:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_qty_grocery4=Label(lf_grocery4,text="Qty:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_qty_grocery5=Label(lf_grocery5,text="Qty:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_qty_grocery6=Label(lf_grocery6,text="Qty:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_qty_grocery7=Label(lf_grocery7,text="Qty:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_qty_grocery8=Label(lf_grocery8,text="Qty:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_qty_grocery9=Label(lf_grocery9,text="Qty:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_qty_grocery10=Label(lf_grocery10,text="Qty:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    options_grocery1=["250g – Rs.93","475g – Rs.166"]
    options_grocery2=["5kg – Rs.235","10kg – Rs.394"]
    options_grocery3=["1kg – Rs.18"]
    options_grocery4=["1L – Rs.195"]
    options_grocery5=["500g – Rs.95","1kg – Rs.165"]
    options_grocery6=["55g – Rs.76","137g – Rs.175"]
    options_grocery7=["120g – Rs.23","250g – Rs.48"]
    options_grocery8=["200g – Rs.65","500g – Rs.150","700g – Rs.215"]
    options_grocery9=["500g – Rs.104","1kg – Rs.160"]
    options_grocery10=["70g – Rs.25","150g – Rs.40"]
    global clicked_grocery1,clicked_grocery2,clicked_grocery3,clicked_grocery4,clicked_grocery5,grocery_list
    global clicked_grocery6,clicked_grocery7,clicked_grocery8,clicked_grocery9,clicked_grocery10
    drop_grocery1=OptionMenu(lf_grocery1,clicked_grocery1,*options_grocery1).place(x=30,y=212)
    drop_grocery2=OptionMenu(lf_grocery2,clicked_grocery2,*options_grocery2).place(x=30,y=212)
    drop_grocery3=OptionMenu(lf_grocery3,clicked_grocery3,*options_grocery3).place(x=30,y=212)
    drop_grocery4=OptionMenu(lf_grocery4,clicked_grocery4,*options_grocery4).place(x=30,y=212)
    drop_grocery5=OptionMenu(lf_grocery5,clicked_grocery5,*options_grocery5).place(x=30,y=212)
    drop_grocery6=OptionMenu(lf_grocery6,clicked_grocery6,*options_grocery6).place(x=30,y=212)
    drop_grocery7=OptionMenu(lf_grocery7,clicked_grocery7,*options_grocery7).place(x=30,y=212)
    drop_grocery8=OptionMenu(lf_grocery8,clicked_grocery8,*options_grocery8).place(x=30,y=212)
    drop_grocery9=OptionMenu(lf_grocery9,clicked_grocery9,*options_grocery9).place(x=30,y=212)
    drop_grocery10=OptionMenu(lf_grocery10,clicked_grocery10,*options_grocery10).place(x=30,y=212)
    def GroceryPrice(s):
        s1=""
        for i in range(len(s)-1,0,-1):
            if s[i]!='.':
                s1=s1+s[i]
            else:
                break
        return int(s1[::-1])
    def GroceryQty(s):
        s1=""
        for i in range(len(s)):
            s1=s1+s[i]
            if s[i]=='g' or s[i]=='L':
                break
        return s1
    def AddG1():
        global grocery_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            grocery_list.append(["Corn Flakes",GroceryPrice(clicked_grocery1.get()),GroceryQty(clicked_grocery1.get()),Spaces(40-len("Corn Flakes"))])
            messagebox.showinfo("Product Status","Kellogg's Corn Flakes Original ("+clicked_grocery1.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Kellogg's Corn Flakes Original ("+clicked_grocery1.get()+") is not added to the cart.")
    def AddG2():
        global grocery_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            grocery_list.append(["Aashirwaad Atta",GroceryPrice(clicked_grocery2.get()),GroceryQty(clicked_grocery2.get()),Spaces(40-len("Aashirwaad Atta"))])
            messagebox.showinfo("Product Status","Aashirwaad Superior Atta ("+clicked_grocery2.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Aashirwaad Superior Atta ("+clicked_grocery2.get()+") is not added to the cart.")
    def AddG3():
        global grocery_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            grocery_list.append(["Iodized Salt",GroceryPrice(clicked_grocery3.get()),GroceryQty(clicked_grocery3.get()),Spaces(40-len("Iodized Salt"))])
            messagebox.showinfo("Product Status","Tata Iodized Salt ("+clicked_grocery3.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Tata Iodized Salt ("+clicked_grocery3.get()+") is not added to the cart.")
    def AddG4():
        global grocery_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            grocery_list.append(["Filtered Groundnut Oil",GroceryPrice(clicked_grocery4.get()),GroceryQty(clicked_grocery4.get()),Spaces(40-len("Filtered Groundnut Oil"))])
            messagebox.showinfo("Product Status","Safal Filtered Groundnut Oil ("+clicked_grocery4.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Safal Filtered Groundnut Oil ("+clicked_grocery4.get()+") is not added to the cart.")
    def AddG5():
        global grocery_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            grocery_list.append(["Organic Toor Dal",GroceryPrice(clicked_grocery5.get()),GroceryQty(clicked_grocery5.get()),Spaces(40-len("Organic Toor Dal"))])
            messagebox.showinfo("Product Status","24 Mantra Organic Toor Dal ("+clicked_grocery5.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","24 Mantra Organic Toor Dal ("+clicked_grocery5.get()+") is not added to the cart.")
    def AddG6():
        global grocery_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            grocery_list.append(["Dairy Milk Silk",GroceryPrice(clicked_grocery6.get()),GroceryQty(clicked_grocery6.get()),Spaces(40-len("Dairy Milk Silk"))])
            messagebox.showinfo("Product Status","Dairy Milk Silk Fruit & Nut ("+clicked_grocery6.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Dairy Milk Silk Fruit & Nut ("+clicked_grocery6.get()+") is not added to the cart.")
    def AddG7():
        global grocery_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            grocery_list.append(["Yippee Noodles",GroceryPrice(clicked_grocery7.get()),GroceryQty(clicked_grocery7.get()),Spaces(40-len("Yippee Noodles"))])
            messagebox.showinfo("Product Status","Yippee Noodles Magic Masala ("+clicked_grocery7.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Yippee Noodles Magic Masala ("+clicked_grocery7.get()+") is not added to the cart.")
    def AddG8():
        global grocery_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            grocery_list.append(["Mixed Fruit Jam",GroceryPrice(clicked_grocery8.get()),GroceryQty(clicked_grocery8.get()),Spaces(40-len("Mixed Fruit Jam"))])
            messagebox.showinfo("Product Status","Kissan Mixed Fruit Jam ("+clicked_grocery8.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Kissan Mixed Fruit Jam ("+clicked_grocery8.get()+") is not added to the cart.")
    def AddG9():
        global grocery_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            grocery_list.append(["Mango Pickle",GroceryPrice(clicked_grocery9.get()),GroceryQty(clicked_grocery9.get()),Spaces(40-len("Mango Pickle"))])
            messagebox.showinfo("Product Status","Mother's Recipe Mango Pickle ("+clicked_grocery9.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Mother's Recipe Mango Pickle ("+clicked_grocery9.get()+") is not added to the cart.")
    def AddG10():
        global grocery_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            grocery_list.append(["Parle's Wafers",GroceryPrice(clicked_grocery10.get()),GroceryQty(clicked_grocery10.get()),Spaces(40-len("Parle's Wafers"))])
            messagebox.showinfo("Product Status","Parle's Cream & Onion Wafers ("+clicked_grocery10.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Parle's Cream & Onion Wafers ("+clicked_grocery10.get()+") is not added to the cart.")
    add_grocery1=Button(lf_grocery1,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG1).place(x=60,y=245)
    add_grocery2=Button(lf_grocery2,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG2).place(x=60,y=245)
    add_grocery3=Button(lf_grocery3,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG3).place(x=60,y=245)
    add_grocery4=Button(lf_grocery4,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG4).place(x=60,y=245)
    add_grocery5=Button(lf_grocery5,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG5).place(x=60,y=245)
    add_grocery6=Button(lf_grocery6,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG6).place(x=60,y=245)
    add_grocery7=Button(lf_grocery7,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG7).place(x=60,y=245)
    add_grocery8=Button(lf_grocery8,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG8).place(x=60,y=245)
    add_grocery9=Button(lf_grocery9,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG9).place(x=60,y=245)
    add_grocery10=Button(lf_grocery10,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG10).place(x=60,y=245)
def ElectronicsCall():
    HideAllFrames()
    Electronics_Label=Label(Products_frame,text="Electronics",font="times 15 bold",fg="gold",bg="black").grid(row=0,column=0,padx=10)
    lf_electronics1=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_electronics1.place(x=5,y=35,width=200,height=280)
    lf_electronics2=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_electronics2.place(x=210,y=35,width=200,height=280)
    lf_electronics3=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_electronics3.place(x=415,y=35,width=200,height=280)
    lf_electronics4=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_electronics4.place(x=620,y=35,width=200,height=280)
    lf_electronics5=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_electronics5.place(x=825,y=35,width=200,height=280)
    lf_electronics6=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_electronics6.place(x=5,y=310,width=200,height=280)
    lf_electronics7=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_electronics7.place(x=210,y=310,width=200,height=280)
    lf_electronics8=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_electronics8.place(x=415,y=310,width=200,height=280)
    lf_electronics9=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_electronics9.place(x=620,y=310,width=200,height=280)
    lf_electronics10=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_electronics10.place(x=825,y=310,width=200,height=280)
    label_electronics_1=Label(lf_electronics1,image=electronics1_image,bd=2,justify="center").grid(row=0,column=0)
    label_electronics_2=Label(lf_electronics2,image=electronics2_image,bd=2,justify="center").grid(row=0,column=0)
    label_electronics_3=Label(lf_electronics3,image=electronics3_image,bd=2,justify="center").grid(row=0,column=0)
    label_electronics_4=Label(lf_electronics4,image=electronics4_image,bd=2,justify="center").grid(row=0,column=0)
    label_electronics_5=Label(lf_electronics5,image=electronics5_image,bd=2,justify="center").grid(row=0,column=0)
    label_electronics_6=Label(lf_electronics6,image=electronics6_image,bd=2,justify="center").grid(row=0,column=0)
    label_electronics_7=Label(lf_electronics7,image=electronics7_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_electronics_8=Label(lf_electronics8,image=electronics8_image,bd=2,justify="center").grid(row=0,column=0,padx=7)
    label_electronics_9=Label(lf_electronics9,image=electronics9_image,bd=2,justify="center").grid(row=0,column=0)
    label_electronics_10=Label(lf_electronics10,image=electronics10_image,bd=2,justify="center").grid(row=0,column=0,padx=7)
    name_electronics1=Label(lf_electronics1,text="Redmi Note 9 Pro(Storage:64GB)",font="arial 9",justify="center").grid(row=1,column=0,padx=3)
    name_electronics2=Label(lf_electronics2,text="OnePlus 8T 5G(Storage:128GB)",font="arial 9",justify="center").grid(row=1,column=0,padx=6)
    name_electronics3=Label(lf_electronics3,text="boAt Bassheads Wired Earphones",font="arial 9",justify="center").grid(row=1,column=0)
    name_electronics4=Label(lf_electronics4,text="JBL T460BT On-Ear Headphones",font="arial 9",justify="center").grid(row=1,column=0,padx=3)
    name_electronics5=Label(lf_electronics5,text="Logitech M221 Wireless Mouse",font="arial 9",justify="center").grid(row=1,column=0,padx=9)
    name_electronics6=Label(lf_electronics6,text="HP Pavilion 15.6-inch",font="arial 9",justify="center").grid(row=1,column=0)
    name_electronics6=Label(lf_electronics6,text="FHD Gaming Laptop",font="arial 9",justify="center").grid(row=2,column=0)
    name_electronics6=Label(lf_electronics6,text="Storage:1TB HDD + 256GB SSD",font="arial 9",justify="center").grid(row=3,column=0,padx=6)
    price_electronics6=Label(lf_electronics6,text="Price: Rs.67,900",font="arial 9 bold",justify="center").grid(row=4,column=0)
    name_electronics7=Label(lf_electronics7,text="Acer Aspire 5 15.6 inch Laptop",font="arial 9",justify="center").grid(row=1,column=0)
    name_electronics7=Label(lf_electronics7,text="Intel Core i5 11th Generation",font="arial 9",justify="center").grid(row=2,column=0)
    name_electronics7=Label(lf_electronics7,text="Storage: 512GB SSD",font="arial 9",justify="center").grid(row=3,column=0)
    price_electronics7=Label(lf_electronics7,text="Price: Rs.49,990",font="arial 9 bold",justify="center").grid(row=4,column=0)
    name_electronics8=Label(lf_electronics8,text="OnePlus Y Series Full HD",font="arial 9",justify="center").grid(row=1,column=0)
    name_electronics8=Label(lf_electronics8,text="LED Smart Android TV 43Y1",font="arial 9",justify="center").grid(row=2,column=0)
    price_electronics8=Label(lf_electronics8,text="Price: Rs.15,499  Inches: 32",font="arial 9 bold",justify="center").grid(row=3,column=0)
    name_electronics9=Label(lf_electronics9,text="Noise Colorfit Pro 2 Smartwatch",font="arial 9",justify="center").grid(row=1,column=0,padx=6)
    name_electronics10=Label(lf_electronics10,text="EPSON L3115 Color A4",font="arial 9",justify="center").grid(row=1,column=0)
    name_electronics10=Label(lf_electronics10,text="All in ONE Printer",font="arial 9",justify="center").grid(row=2,column=0)
    price_electronics10=Label(lf_electronics10,text="Price: Rs.12,250",font="arial 9 bold",justify="center").grid(row=3,column=0)
    label_clr_electronics1=Label(lf_electronics1,text="Colour:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_clr_electronics2=Label(lf_electronics2,text="Colour:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_clr_electronics3=Label(lf_electronics3,text="Colour:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_clr_electronics4=Label(lf_electronics4,text="Colour:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_clr_electronics5=Label(lf_electronics5,text="Colour:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_clr_electronics6=Label(lf_electronics6,text="Colour:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_clr_electronics7=Label(lf_electronics7,text="Colour:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_clr_electronics8=Label(lf_electronics8,text="Colour:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_clr_electronics9=Label(lf_electronics9,text="Colour:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_clr_electronics10=Label(lf_electronics10,text="Colour:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    options_electronics1=["Aurora Blue","Interstellar Black","Glacier White","Champagne Gold"]
    options_electronics2=["Aquamarine Green","Lunar Silver"]
    options_electronics3=["Black","Forest Green","Molten Orange","Neon Lime"]
    options_electronics4=["Black","Blue","White"]
    options_electronics5=["Charcoal Grey","Red","Blue"]
    options_electronics6=["Shadow Black","Fiery Red"]
    options_electronics7=["Black"]
    options_electronics8=["Black"]
    options_electronics9=["Jet Black","Cherry Red","Mist Grey","Royal Blue"]
    options_electronics10=["Blue & White"]
    global clicked_electronics1,clicked_electronics2,clicked_electronics3,clicked_electronics4,clicked_electronics5,electronics_list
    global clicked_electronics6,clicked_electronics7,clicked_electronics8,clicked_electronics9,clicked_electronics10
    drop_electronics1=OptionMenu(lf_electronics1,clicked_electronics1,*options_electronics1).place(x=48,y=212)
    drop_electronics2=OptionMenu(lf_electronics2,clicked_electronics2,*options_electronics2).place(x=48,y=212)
    drop_electronics3=OptionMenu(lf_electronics3,clicked_electronics3,*options_electronics3).place(x=48,y=212)
    drop_electronics4=OptionMenu(lf_electronics4,clicked_electronics4,*options_electronics4).place(x=48,y=212)
    drop_electronics5=OptionMenu(lf_electronics5,clicked_electronics5,*options_electronics5).place(x=48,y=212)
    drop_electronics6=OptionMenu(lf_electronics6,clicked_electronics6,*options_electronics6).place(x=48,y=212)
    drop_electronics7=OptionMenu(lf_electronics7,clicked_electronics7,*options_electronics7).place(x=48,y=212)
    drop_electronics8=OptionMenu(lf_electronics8,clicked_electronics8,*options_electronics8).place(x=48,y=212)
    drop_electronics9=OptionMenu(lf_electronics9,clicked_electronics9,*options_electronics9).place(x=48,y=212)
    drop_electronics10=OptionMenu(lf_electronics10,clicked_electronics10,*options_electronics10).place(x=48,y=212)
    def AddE1():
        global electronics_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            electronics_list.append(["Redmi Note 9 Pro",13650,"13,650",clicked_electronics1.get(),Spaces(40-len("Redmi Note 9 Pro"))])
            messagebox.showinfo("Product Status","Redmi Note 9 Pro(Storage:64GB) ("+clicked_electronics1.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Redmi Note 9 Pro(Storage:64GB) ("+clicked_electronics1.get()+") is not added to the cart.")
    def AddE2():
        global electronics_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            electronics_list.append(["OnePlus 8T 5G",42999,"42,999",clicked_electronics2.get(),Spaces(40-len("OnePlus 8T 5G"))])
            messagebox.showinfo("Product Status","OnePlus 8T 5G(Storage:128GB) ("+clicked_electronics2.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","OnePlus 8T 5G(Storage:128GB) ("+clicked_electronics2.get()+") is not added to the cart.")
    def AddE3():
        global electronics_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            electronics_list.append(["boAt Earphones",499,"499",clicked_electronics3.get(),Spaces(40-len("boAt Earphones"))])
            messagebox.showinfo("Product Status","boAt Bassheads Wired Earphones ("+clicked_electronics3.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","boAt Bassheads Wired Earphones ("+clicked_electronics3.get()+") is not added to the cart.")
    def AddE4():
        global electronics_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            electronics_list.append(["JBL Headphones",2799,"2,799",clicked_electronics4.get(),Spaces(40-len("JBL Headphones"))])
            messagebox.showinfo("Product Status","JBL T460BT On-Ear Headphones ("+clicked_electronics4.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","JBL T460BT On-Ear Headphones ("+clicked_electronics4.get()+") is not added to the cart.")
    def AddE5():
        global electronics_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            electronics_list.append(["Logitech Mouse",699,"699",clicked_electronics5.get(),Spaces(40-len("Logitech Mouse"))])
            messagebox.showinfo("Product Status","Logitech M221 Wireless Mouse ("+clicked_electronics5.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Logitech M221 Wireless Mouse ("+clicked_electronics5.get()+") is not added to the cart.")
    def AddE6():
        global electronics_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            electronics_list.append(["HP Pavilion Laptop",67900,"67,900",clicked_electronics6.get(),Spaces(40-len("HP Pavilion Laptop"))])
            messagebox.showinfo("Product Status","HP Pavilion 15.6-inch FHD Gaming Laptop Storage:1TB HDD + 256GB SSD ("+clicked_electronics6.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","HP Pavilion 15.6-inch FHD Gaming Laptop Storage:1TB HDD + 256GB SSD ("+clicked_electronics6.get()+") is not added to the cart.")
    def AddE7():
        global electronics_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            electronics_list.append(["Acer Aspire 5 Laptop",49990,"49,990",clicked_electronics7.get(),Spaces(40-len("Acer Aspire 5 Laptop"))])
            messagebox.showinfo("Product Status","Acer Aspire 5 15.6 inch Laptop Intel Core i5 11th Generation Storage: 512GB SSD ("+clicked_electronics7.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Acer Aspire 5 15.6 inch Laptop Intel Core i5 11th Generation Storage: 512GB SSD ("+clicked_electronics7.get()+") is not added to the cart.")
    def AddE8():
        global electronics_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            electronics_list.append(["OnePlus Android TV",15499,"15,499",clicked_electronics8.get(),Spaces(40-len("OnePlus Android TV"))])
            messagebox.showinfo("Product Status","OnePlus Y Series Full HD LED Smart Android TV 43Y1 ("+clicked_electronics8.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","OnePlus Y Series Full HD LED Smart Android TV 43Y1 ("+clicked_electronics8.get()+") is not added to the cart.")
    def AddE9():
        global electronics_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            electronics_list.append(["Noise Colorfit Smartwatch",2999,"2,999",clicked_electronics9.get(),Spaces(40-len("Noise Colorfit Smartwatch"))])
            messagebox.showinfo("Product Status","Noise Colorfit Pro 2 Smartwatch ("+clicked_electronics9.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Noise Colorfit Pro 2 Smartwatch ("+clicked_electronics9.get()+") is not added to the cart.")
    def AddE10():
        global electronics_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            electronics_list.append(["EPSON Color Printer",12250,"12,250",clicked_electronics10.get(),Spaces(40-len("EPSON Color Printer"))])
            messagebox.showinfo("Product Status","EPSON L3115 Color A4 All in ONE Printer ("+clicked_electronics10.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","EPSON L3115 Color A4 All in ONE Printer ("+clicked_electronics10.get()+") is not added to the cart.")
    price_electronics1=Label(lf_electronics1,text="Price: Rs.13,650",font="arial 9 bold").place(x=5,y=245)
    price_electronics2=Label(lf_electronics2,text="Price: Rs.42,999",font="arial 9 bold").place(x=5,y=245)
    price_electronics3=Label(lf_electronics3,text="Price: Rs.499",font="arial 9 bold").place(x=5,y=245)
    price_electronics4=Label(lf_electronics4,text="Price: Rs.2,799",font="arial 9 bold").place(x=5,y=245)
    price_electronics5=Label(lf_electronics5,text="Price: Rs.699",font="arial 9 bold").place(x=5,y=245)
    price_electronics9=Label(lf_electronics9,text="Price: Rs.2,999",font="arial 9 bold").place(x=5,y=245)
    add_electronics1=Button(lf_electronics1,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddE1).place(x=120,y=245)
    add_electronics2=Button(lf_electronics2,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddE2).place(x=120,y=245)
    add_electronics3=Button(lf_electronics3,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddE3).place(x=120,y=245)
    add_electronics4=Button(lf_electronics4,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddE4).place(x=120,y=245)
    add_electronics5=Button(lf_electronics5,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddE5).place(x=120,y=245)
    add_electronics6=Button(lf_electronics6,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddE6).place(x=60,y=245)
    add_electronics7=Button(lf_electronics7,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddE7).place(x=60,y=245)
    add_electronics8=Button(lf_electronics8,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddE8).place(x=60,y=245)
    add_electronics9=Button(lf_electronics9,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddE9).place(x=120,y=245)
    add_electronics10=Button(lf_electronics10,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddE10).place(x=60,y=245)
def SportsGymCall():
    HideAllFrames()
    Sports_Gym_Label=Label(Products_frame,text="Sports and Gym Equipment",font="times 15 bold",fg="gold",bg="black").grid(row=0,column=0,padx=10)
    lf_sportsgym1=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_sportsgym1.place(x=5,y=35,width=200,height=280)
    lf_sportsgym2=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_sportsgym2.place(x=210,y=35,width=200,height=280)
    lf_sportsgym3=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_sportsgym3.place(x=415,y=35,width=200,height=280)
    lf_sportsgym4=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_sportsgym4.place(x=620,y=35,width=200,height=280)
    lf_sportsgym5=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_sportsgym5.place(x=825,y=35,width=200,height=280)
    lf_sportsgym6=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_sportsgym6.place(x=5,y=310,width=200,height=280)
    lf_sportsgym7=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_sportsgym7.place(x=210,y=310,width=200,height=280)
    lf_sportsgym8=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_sportsgym8.place(x=415,y=310,width=200,height=280)
    lf_sportsgym9=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_sportsgym9.place(x=620,y=310,width=200,height=280)
    lf_sportsgym10=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_sportsgym10.place(x=825,y=310,width=200,height=280)
    label_sportsgym_1=Label(lf_sportsgym1,image=sportsgym1_image,bd=2,justify="center").grid(row=0,column=0)
    label_sportsgym_2=Label(lf_sportsgym2,image=sportsgym2_image,bd=2,justify="center").grid(row=0,column=0,padx=7)
    label_sportsgym_3=Label(lf_sportsgym3,image=sportsgym3_image,bd=2,justify="center").grid(row=0,column=0)
    label_sportsgym_4=Label(lf_sportsgym4,image=sportsgym4_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_sportsgym_5=Label(lf_sportsgym5,image=sportsgym5_image,bd=2,justify="center").grid(row=0,column=0)
    label_sportsgym_6=Label(lf_sportsgym6,image=sportsgym6_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_sportsgym_7=Label(lf_sportsgym7,image=sportsgym7_image,bd=2,justify="center").grid(row=0,column=0)
    label_sportsgym_8=Label(lf_sportsgym8,image=sportsgym8_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_sportsgym_9=Label(lf_sportsgym9,image=sportsgym9_image,bd=2,justify="center").grid(row=0,column=0)
    label_sportsgym_10=Label(lf_sportsgym10,image=sportsgym10_image,bd=2,justify="center").grid(row=0,column=0)
    name_sportsgym1=Label(lf_sportsgym1,text="GM Purist KW 202 Cricket Bat",font="arial 9",justify="center").grid(row=1,column=0,padx=13)
    name_sportsgym2=Label(lf_sportsgym2,text="GTS Dezir Cricket Leather Ball",font="arial 9",justify="center").grid(row=1,column=0)
    name_sportsgym3=Label(lf_sportsgym3,text="Yonex GR 303 Badminton Racquet",font="arial 9",justify="center").grid(row=1,column=0)
    name_sportsgym4=Label(lf_sportsgym4,text="Strauss Maxis Pro Shuttlecock",font="arial 9",justify="center").grid(row=1,column=0)
    name_sportsgym5=Label(lf_sportsgym5,text="Stag 4 Star Table Tennis Kit",font="arial 9",justify="center").grid(row=1,column=0,padx=14)
    name_sportsgym6=Label(lf_sportsgym6,text="Cockatoo CTM14A 2.5HP",font="arial 9",justify="center").grid(row=1,column=0)
    name_sportsgym6=Label(lf_sportsgym6,text="Treadmill with Auto-Incline",font="arial 9",justify="center").grid(row=2,column=0)
    name_sportsgym7=Label(lf_sportsgym7,text="Aurion HEX Rubber Coated Cast",font="arial 9",justify="center").grid(row=1,column=0,padx=4)
    name_sportsgym7=Label(lf_sportsgym7,text="Iron Hexagonal Dumbbells for",font="arial 9",justify="center").grid(row=2,column=0)
    name_sportsgym7=Label(lf_sportsgym7,text="Professional Exercise",font="arial 9",justify="center").grid(row=3,column=0)
    name_sportsgym8=Label(lf_sportsgym8,text="SPORTAL Foldable Multi Bench",font="arial 9",justify="center").grid(row=1,column=0)
    name_sportsgym8=Label(lf_sportsgym8,text="Press Workout Machine",font="arial 9",justify="center").grid(row=2,column=0)
    name_sportsgym9=Label(lf_sportsgym9,text="Reach Air Bike Exercise Cycle",font="arial 9",justify="center").grid(row=1,column=0,padx=12)
    name_sportsgym10=Label(lf_sportsgym10,text="RMOUR Filled Heavy Punch Bag",font="arial 9",justify="center").grid(row=1,column=0,padx=5)
    price_sportsgym1=Label(lf_sportsgym1,text="Price: Rs.1,970",font="arial 9 bold").grid(row=2,column=0)
    price_sportsgym2=Label(lf_sportsgym2,text="Price: Rs.160",font="arial 9 bold").grid(row=2,column=0)
    price_sportsgym3=Label(lf_sportsgym3,text="Price: Rs.550",font="arial 9 bold").grid(row=2,column=0)
    price_sportsgym4=Label(lf_sportsgym4,text="Price: Rs.350",font="arial 9 bold").grid(row=2,column=0)
    price_sportsgym5=Label(lf_sportsgym5,text="Price: Rs.980",font="arial 9 bold").grid(row=2,column=0)
    price_sportsgym6=Label(lf_sportsgym6,text="Price: Rs.28,990",font="arial 9 bold").grid(row=3,column=0)
    price_sportsgym7=Label(lf_sportsgym7,text="Price: Rs.949",font="arial 9 bold").grid(row=4,column=0)
    price_sportsgym8=Label(lf_sportsgym8,text="Price: Rs.6,799",font="arial 9 bold").grid(row=3,column=0)
    price_sportsgym9=Label(lf_sportsgym9,text="Price: Rs.6,999",font="arial 9 bold").grid(row=2,column=0)
    price_sportsgym10=Label(lf_sportsgym10,text="Price: Rs.2,999",font="arial 9 bold").grid(row=2,column=0)
    def AddS1():
        global sportsgym_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            sportsgym_list.append(["GM Cricket Bat",1970,"1,970",Spaces(40-len("GM Cricket Bat"))])
            messagebox.showinfo("Product Status","GM Purist KW 202 Cricket Bat is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","GM Purist KW 202 Cricket Bat is not added to the cart.")
    def AddS2():
        global sportsgym_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            sportsgym_list.append(["GTS Leather Ball",160,"160",Spaces(40-len("GTS Leather Ball"))])
            messagebox.showinfo("Product Status","GTS Dezir Cricket Leather Ball is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","GTS Dezir Cricket Leather Ball is not added to the cart.")
    def AddS3():
        global sportsgym_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            sportsgym_list.append(["Yonex Badminton Racquet",550,"550",Spaces(40-len("Yonex Badminton Racquet"))])
            messagebox.showinfo("Product Status","Yonex GR 303 Badminton Racquet is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Yonex GR 303 Badminton Racquet is not added to the cart.")
    def AddS4():
        global sportsgym_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            sportsgym_list.append(["Strauss Shuttlecock",350,"350",Spaces(40-len("Strauss Shuttlecock"))])
            messagebox.showinfo("Product Status","Strauss Maxis Pro Shuttlecock is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Strauss Maxis Pro Shuttlecock is not added to the cart.")
    def AddS5():
        global sportsgym_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            sportsgym_list.append(["Table Tennis Kit",980,"980",Spaces(40-len("Table Tennis Kit"))])
            messagebox.showinfo("Product Status","Stag 4 Star Table Tennis Kit is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Stag 4 Star Table Tennis Kit is not added to the cart.")
    def AddS6():
        global sportsgym_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            sportsgym_list.append(["Cockatoo Treadmill",28990,"28,990",Spaces(40-len("Cockatoo Treadmill"))])
            messagebox.showinfo("Product Status","Cockatoo CTM14A 2.5HP Treadmill with Auto-Incline is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Cockatoo CTM14A 2.5HP Treadmill with Auto-Incline is not added to the cart.")
    def AddS7():
        global sportsgym_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            sportsgym_list.append(["Aurion Dumbbells",949,"949",Spaces(40-len("Aurion Dumbbells"))])
            messagebox.showinfo("Product Status","Aurion HEX Rubber Coated Cast Iron Hexagonal Dumbbells for Professional Exercise is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Aurion HEX Rubber Coated Cast Iron Hexagonal Dumbbells for Professional Exercise is not added to the cart.")
    def AddS8():
        global sportsgym_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            sportsgym_list.append(["Bench Press Machine",6799,"6,799",Spaces(40-len("Bench Press Machine"))])
            messagebox.showinfo("Product Status","SPORTAL Foldable Multi Bench Press Workout Machine is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","SPORTAL Foldable Multi Bench Press Workout Machine is not added to the cart.")
    def AddS9():
        global sportsgym_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            sportsgym_list.append(["Reach Exercise Cycle",6999,"6,999",Spaces(40-len("Reach Exercise Cycle"))])
            messagebox.showinfo("Product Status","Reach Air Bike Exercise Cycle is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Reach Air Bike Exercise Cycle is not added to the cart.")
    def AddS10():
        global sportsgym_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            sportsgym_list.append(["RMOUR Punch Bag",2999,"2,999",Spaces(40-len("RMOUR Punch Bag"))])
            messagebox.showinfo("Product Status","RMOUR Filled Heavy Punch Bag is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","RMOUR Filled Heavy Punch Bag is not added to the cart.")
    add_sportsgym1=Button(lf_sportsgym1,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddS1).place(x=68,y=245)
    add_sportsgym2=Button(lf_sportsgym2,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddS2).place(x=68,y=245)
    add_sportsgym3=Button(lf_sportsgym3,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddS3).place(x=68,y=245)
    add_sportsgym4=Button(lf_sportsgym4,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddS4).place(x=68,y=245)
    add_sportsgym5=Button(lf_sportsgym5,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddS5).place(x=68,y=245)
    add_sportsgym6=Button(lf_sportsgym6,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddS6).place(x=68,y=245)
    add_sportsgym7=Button(lf_sportsgym7,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddS7).place(x=68,y=245)
    add_sportsgym8=Button(lf_sportsgym8,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddS8).place(x=68,y=245)
    add_sportsgym9=Button(lf_sportsgym9,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddS9).place(x=68,y=245)
    add_sportsgym10=Button(lf_sportsgym10,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddS10).place(x=68,y=245)
def FurnitureCall():
    HideAllFrames()
    Furniture_Label=Label(Products_frame,text="Furniture",font="times 15 bold",fg="gold",bg="black").grid(row=0,column=0,padx=20)
    lf_furniture1=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_furniture1.place(x=5,y=35,width=200,height=280)
    lf_furniture2=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_furniture2.place(x=210,y=35,width=200,height=280)
    lf_furniture3=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_furniture3.place(x=415,y=35,width=200,height=280)
    lf_furniture4=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_furniture4.place(x=620,y=35,width=200,height=280)
    lf_furniture5=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_furniture5.place(x=825,y=35,width=200,height=280)
    lf_furniture6=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_furniture6.place(x=5,y=310,width=200,height=280)
    lf_furniture7=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_furniture7.place(x=210,y=310,width=200,height=280)
    lf_furniture8=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_furniture8.place(x=415,y=310,width=200,height=280)
    lf_furniture9=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_furniture9.place(x=620,y=310,width=200,height=280)
    lf_furniture10=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_furniture10.place(x=825,y=310,width=200,height=280)
    label_furniture_1=Label(lf_furniture1,image=furniture1_image,bd=2,justify="center").grid(row=0,column=0)
    label_furniture_2=Label(lf_furniture2,image=furniture2_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_furniture_3=Label(lf_furniture3,image=furniture3_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_furniture_4=Label(lf_furniture4,image=furniture4_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_furniture_5=Label(lf_furniture5,image=furniture5_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_furniture_6=Label(lf_furniture6,image=furniture6_image,bd=2,justify="center").grid(row=0,column=0)
    label_furniture_7=Label(lf_furniture7,image=furniture7_image,bd=2,justify="center").grid(row=0,column=0)
    label_furniture_8=Label(lf_furniture8,image=furniture8_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_furniture_9=Label(lf_furniture9,image=furniture9_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_furniture_10=Label(lf_furniture10,image=furniture10_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    name_furniture1=Label(lf_furniture1,text="Julian Wood 2 Door Wardrobe",font="arial 9",justify="center").grid(row=1,column=0,padx=10)
    name_furniture2=Label(lf_furniture2,text="Zuari Niko Engineered Wood",font="arial 9",justify="center").grid(row=1,column=0)
    name_furniture2=Label(lf_furniture2,text="3 Door Wardrobe",font="arial 9",justify="center").grid(row=2,column=0)
    name_furniture3=Label(lf_furniture3,text="TADesign Vinicio Engineered",font="arial 9",justify="center").grid(row=1,column=0)
    name_furniture3=Label(lf_furniture3,text="Wood 3 Door Wardrobe",font="arial 9",justify="center").grid(row=2,column=0)
    name_furniture4=Label(lf_furniture4,text="Flipkart Perfect Homes Opus",font="arial 9",justify="center").grid(row=1,column=0)
    name_furniture4=Label(lf_furniture4,text="Engineered Wood",font="arial 9",justify="center").grid(row=2,column=0)
    name_furniture4=Label(lf_furniture4,text="Queen Box Bed",font="arial 9",justify="center").grid(row=3,column=0)
    name_furniture5=Label(lf_furniture5,text="Forzza Jasper Engineered",font="arial 9",justify="center").grid(row=1,column=0)
    name_furniture5=Label(lf_furniture5,text="Wood King Box Bed",font="arial 9",justify="center").grid(row=2,column=0)
    name_furniture6=Label(lf_furniture6,text="Zuari Wood TV Entertainment Unit",font="arial 9",justify="center").grid(row=1,column=0,padx=2)
    name_furniture7=Label(lf_furniture7,text="Forzza Belfast Engineered Wood",font="arial 9",justify="center").grid(row=1,column=0,padx=5)
    name_furniture7=Label(lf_furniture7,text="TV Entertainment Unit",font="arial 9",justify="center").grid(row=2,column=0)
    name_furniture8=Label(lf_furniture8,text="Kurlon Crescent Leatherette",font="arial 9",justify="center").grid(row=1,column=0)
    name_furniture8=Label(lf_furniture8,text="3 + 1 + 1 Black Sofa Set",font="arial 9",justify="center").grid(row=2,column=0)
    name_furniture9=Label(lf_furniture9,text="Suncrown Furniture Solid Wood",font="arial 9",justify="center").grid(row=1,column=0)
    name_furniture9=Label(lf_furniture9,text="Fabric 6 Seater Sofa",font="arial 9",justify="center").grid(row=2,column=0)
    name_furniture9=Label(lf_furniture9,text="3 + 2 + 1 Vanilla Cream Sofa Set",font="arial 9",justify="center").grid(row=3,column=0)
    name_furniture10=Label(lf_furniture10,text="Allie Wood Solid Wood",font="arial 9",justify="center").grid(row=1,column=0)
    name_furniture10=Label(lf_furniture10,text="6 Seater Dining Set",font="arial 9",justify="center").grid(row=2,column=0)
    price_furniture1=Label(lf_furniture1,text="Price: Rs.6,990",font="arial 9 bold").grid(row=2,column=0)
    price_furniture2=Label(lf_furniture2,text="Price: Rs.17,390",font="arial 9 bold").grid(row=3,column=0)
    price_furniture3=Label(lf_furniture3,text="Price: Rs.34,999",font="arial 9 bold").grid(row=3,column=0)
    price_furniture4=Label(lf_furniture4,text="Price: Rs.12,290",font="arial 9 bold").grid(row=4,column=0)
    price_furniture5=Label(lf_furniture5,text="Price: Rs.13,640",font="arial 9 bold").grid(row=3,column=0)
    price_furniture6=Label(lf_furniture6,text="Price: Rs.6,590",font="arial 9 bold").grid(row=2,column=0)
    price_furniture7=Label(lf_furniture7,text="Price: Rs.14,999",font="arial 9 bold").grid(row=3,column=0)
    price_furniture8=Label(lf_furniture8,text="Price: Rs.24,490",font="arial 9 bold").grid(row=3,column=0)
    price_furniture9=Label(lf_furniture9,text="Price: Rs.36,854",font="arial 9 bold").grid(row=4,column=0)
    price_furniture10=Label(lf_furniture10,text="Price: Rs.26,999",font="arial 9 bold").grid(row=3,column=0)
    def AddF1():
        global furniture_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            furniture_list.append(["Julian 2 Door Wardrobe",6990,"6,990",Spaces(40-len("Julian 2 Door Wardrobe"))])
            messagebox.showinfo("Product Status","Julian Wood 2 Door Wardrobe is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Julian Wood 2 Door Wardrobe is not added to the cart.")
    def AddF2():
        global furniture_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            furniture_list.append(["Zuari 3 Door Wardrobe",17390,"17,390",Spaces(40-len("Zuari 3 Door Wardrobe"))])
            messagebox.showinfo("Product Status","Zuari Niko Engineered Wood 3 Door Wardrobe is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Zuari Niko Engineered Wood 3 Door Wardrobe is not added to the cart.")
    def AddF3():
        global furniture_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            furniture_list.append(["TADesign 3 Door Wardrobe",34999,"34,999",Spaces(40-len("TADesign 3 Door Wardrobe"))])
            messagebox.showinfo("Product Status","TADesign Vinicio Engineered Wood 3 Door Wardrobe is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","TADesign Vinicio Engineered Wood 3 Door Wardrobe is not added to the cart.")
    def AddF4():
        global furniture_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            furniture_list.append(["Opus Queen Box Bed",12290,"12,290",Spaces(40-len("Opus Queen Box Bed"))])
            messagebox.showinfo("Product Status","Flipkart Perfect Homes Opus Engineered Wood Queen Box Bed is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Flipkart Perfect Homes Opus Engineered Wood Queen Box Bed is not added to the cart.")
    def AddF5():
        global furniture_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            furniture_list.append(["Jasper King Box Bed",13640,"13,640",Spaces(40-len("Jasper King Box Bed"))])
            messagebox.showinfo("Product Status","Forzza Jasper Engineered Wood King Box Bed is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Forzza Jasper Engineered Wood King Box Bed is not added to the cart.")
    def AddF6():
        global furniture_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            furniture_list.append(["Zuari TV Unit",6590,"6,590",Spaces(40-len("Zuari TV Unit"))])
            messagebox.showinfo("Product Status","Zuari Wood TV Entertainment Unit is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Zuari Wood TV Entertainment Unit is not added to the cart.")
    def AddF7():
        global furniture_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            furniture_list.append(["Forzza TV Unit",14999,"14,999",Spaces(40-len("Forzza TV Unit"))])
            messagebox.showinfo("Product Status","Forzza Belfast Engineered Wood TV Entertainment Unit is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Forzza Belfast Engineered Wood TV Entertainment Unit is not added to the cart.")
    def AddF8():
        global furniture_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            furniture_list.append(["Kurlon Black Sofa Set",24490,"24,490",Spaces(40-len("Kurlon Black Sofa Set"))])
            messagebox.showinfo("Product Status","Kurlon Crescent Leatherette 3 + 1 + 1 Black Sofa Set is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Kurlon Crescent Leatherette 3 + 1 + 1 Black Sofa Set is not added to the cart.")
    def AddF9():
        global furniture_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            furniture_list.append(["Suncrown Cream Sofa Set",36854,"36,854",Spaces(40-len("Suncrown Cream Sofa Set"))])
            messagebox.showinfo("Product Status","Suncrown Furniture Solid Wood Fabric 6 Seater Sofa 3 + 2 + 1 Vanilla Cream Sofa Set is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Suncrown Furniture Solid Wood Fabric 6 Seater Sofa 3 + 2 + 1 Vanilla Cream Sofa Set is not added to the cart.")
    def AddF10():
        global furniture_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            furniture_list.append(["Allie 6 Seater Dining Set",26999,"26,999",Spaces(40-len("Allie 6 Seater Dining Set"))])
            messagebox.showinfo("Product Status","Allie Wood Solid Wood 6 Seater Dining Set is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Allie Wood Solid Wood 6 Seater Dining Set is not added to the cart.")
    add_furniture1=Button(lf_furniture1,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddF1).place(x=68,y=245)
    add_furniture2=Button(lf_furniture2,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddF2).place(x=68,y=245)
    add_furniture3=Button(lf_furniture3,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddF3).place(x=68,y=245)
    add_furniture4=Button(lf_furniture4,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddF4).place(x=68,y=245)
    add_furniture5=Button(lf_furniture5,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddF5).place(x=68,y=245)
    add_furniture6=Button(lf_furniture6,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddF6).place(x=68,y=245)
    add_furniture7=Button(lf_furniture7,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddF7).place(x=68,y=245)
    add_furniture8=Button(lf_furniture8,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddF8).place(x=68,y=245)
    add_furniture9=Button(lf_furniture9,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddF9).place(x=68,y=245)
    add_furniture10=Button(lf_furniture10,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddF10).place(x=68,y=245)
def AppliancesCall():
    HideAllFrames()
    Appliances_Label=Label(Products_frame,text="Appliances",font="times 15 bold",fg="gold",bg="black").grid(row=0,column=0,padx=20)
    lf_appliances1=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_appliances1.place(x=5,y=35,width=200,height=280)
    lf_appliances2=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_appliances2.place(x=210,y=35,width=200,height=280)
    lf_appliances3=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_appliances3.place(x=415,y=35,width=200,height=280)
    lf_appliances4=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_appliances4.place(x=620,y=35,width=200,height=280)
    lf_appliances5=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_appliances5.place(x=825,y=35,width=200,height=280)
    lf_appliances6=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_appliances6.place(x=5,y=310,width=200,height=280)
    lf_appliances7=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_appliances7.place(x=210,y=310,width=200,height=280)
    lf_appliances8=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_appliances8.place(x=415,y=310,width=200,height=280)
    lf_appliances9=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_appliances9.place(x=620,y=310,width=200,height=280)
    lf_appliances10=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_appliances10.place(x=825,y=310,width=200,height=280)
    label_appliances_1=Label(lf_appliances1,image=appliances1_image,bd=2,justify="center").grid(row=0,column=0)
    label_appliances_2=Label(lf_appliances2,image=appliances2_image,bd=2,justify="center").grid(row=0,column=0)
    label_appliances_3=Label(lf_appliances3,image=appliances3_image,bd=2,justify="center").grid(row=0,column=0,padx=7)
    label_appliances_4=Label(lf_appliances4,image=appliances4_image,bd=2,justify="center").grid(row=0,column=0)
    label_appliances_5=Label(lf_appliances5,image=appliances5_image,bd=2,justify="center").grid(row=0,column=0,padx=7)
    label_appliances_6=Label(lf_appliances6,image=appliances6_image,bd=2,justify="center").grid(row=0,column=0)
    label_appliances_7=Label(lf_appliances7,image=appliances7_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_appliances_8=Label(lf_appliances8,image=appliances8_image,bd=2,justify="center").grid(row=0,column=0)
    label_appliances_9=Label(lf_appliances9,image=appliances9_image,bd=2,justify="center").grid(row=0,column=0,padx=22)
    label_appliances_10=Label(lf_appliances10,image=appliances10_image,bd=2,justify="center").grid(row=0,column=0,padx=6)
    name_appliances1=Label(lf_appliances1,text="Whirlpool 7kg Automatic Top Load",font="arial 9",justify="center").grid(row=1,column=0)
    name_appliances2=Label(lf_appliances2,text="IFB 6kg Fully Automatic Front Load",font="arial 9",justify="center").grid(row=1,column=0)
    name_appliances3=Label(lf_appliances3,text="Samsung 1.5 Ton 5 Star",font="arial 9",justify="center").grid(row=1,column=0)
    name_appliances3=Label(lf_appliances3,text="Split Inverter AC",font="arial 9",justify="center").grid(row=2,column=0)
    name_appliances4=Label(lf_appliances4,text="LG 260L Double Door Refrigerator",font="arial 9",justify="center").grid(row=1,column=0)
    name_appliances5=Label(lf_appliances5,text="IFB 20 L Convection",font="arial 9",justify="center").grid(row=1,column=0)
    name_appliances5=Label(lf_appliances5,text="Microwave Oven 20SC2",font="arial 9",justify="center").grid(row=2,column=0)
    name_appliances6=Label(lf_appliances6,text="Bajaj GX1 500W Mixer Grinder",font="arial 9",justify="center").grid(row=1,column=0,padx=12)
    name_appliances7=Label(lf_appliances7,text="Balzano OX218 Electric Kettle",font="arial 9",justify="center").grid(row=1,column=0)
    name_appliances8=Label(lf_appliances8,text="Elica WDFL 606 HAC MS NERO",font="arial 9",justify="center").grid(row=1,column=0)
    name_appliances8=Label(lf_appliances8,text="Auto Clean Wall Mounted Chimney",font="arial 9",justify="center").grid(row=2,column=0)
    name_appliances9=Label(lf_appliances9,text="Kent Ace 8 L Water Purifier",font="arial 9",justify="center").grid(row=1,column=0)
    name_appliances10=Label(lf_appliances10,text="Eureka Forbes Quick Clean DX",font="arial 9",justify="center").grid(row=1,column=0)
    name_appliances10=Label(lf_appliances10,text="Dry Vacuum Cleaner",font="arial 9",justify="center").grid(row=2,column=0)
    price_appliances1=Label(lf_appliances1,text="Price: Rs.14,990",font="arial 9 bold").grid(row=2,column=0)
    price_appliances2=Label(lf_appliances2,text="Price: Rs.23,790",font="arial 9 bold").grid(row=2,column=0)
    price_appliances3=Label(lf_appliances3,text="Price: Rs.34,999",font="arial 9 bold").grid(row=3,column=0)
    price_appliances4=Label(lf_appliances4,text="Price: Rs.25,290",font="arial 9 bold").grid(row=2,column=0)
    price_appliances5=Label(lf_appliances5,text="Price: Rs.9,690",font="arial 9 bold").grid(row=3,column=0)
    price_appliances6=Label(lf_appliances6,text="Price: Rs.1,999",font="arial 9 bold").grid(row=2,column=0)
    price_appliances7=Label(lf_appliances7,text="Price: Rs.879",font="arial 9 bold").grid(row=2,column=0)
    price_appliances8=Label(lf_appliances8,text="Price: Rs.11,999",font="arial 9 bold").grid(row=3,column=0)
    price_appliances9=Label(lf_appliances9,text="Price: Rs.12,499",font="arial 9 bold").grid(row=2,column=0)
    price_appliances10=Label(lf_appliances10,text="Price: Rs.3,249",font="arial 9 bold").grid(row=3,column=0)
    def AddA1():
        global appliances_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            appliances_list.append(["Whirlpool Top Load",14990,"14,990",Spaces(40-len("Whirlpool Top Load"))])
            messagebox.showinfo("Product Status","Whirlpool 7kg Automatic Top Load is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Whirlpool 7kg Automatic Top Load is not added to the cart.")
    def AddA2():
        global appliances_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            appliances_list.append(["IFB Front Load",23790,"23,790",Spaces(40-len("IFB Front Load"))])
            messagebox.showinfo("Product Status","IFB 6kg Fully Automatic Front Load is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","IFB 6kg Fully Automatic Front Load is not added to the cart.")
    def AddA3():
        global appliances_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            appliances_list.append(["Samsung Inverter AC",34999,"34,999",Spaces(40-len("Samsung Inverter AC"))])
            messagebox.showinfo("Product Status","Samsung 1.5 Ton 5 Star Split Inverter AC is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Samsung 1.5 Ton 5 Star Split Inverter AC is not added to the cart.")
    def AddA4():
        global appliances_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            appliances_list.append(["LG 260L Refrigerator",25290,"25,290",Spaces(40-len("LG 260L Refrigerator"))])
            messagebox.showinfo("Product Status","LG 260L Double Door Refrigerator is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","LG 260L Double Door Refrigerator is not added to the cart.")
    def AddA5():
        global appliances_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            appliances_list.append(["IFB Microwave Oven",9690,"9,690",Spaces(40-len("IFB Microwave Oven"))])
            messagebox.showinfo("Product Status","IFB 20 L Convection Microwave Oven 20SC2 is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","IFB 20 L Convection Microwave Oven 20SC2 is not added to the cart.")
    def AddA6():
        global appliances_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            appliances_list.append(["Bajaj Mixer Grinder",1999,"1,999",Spaces(40-len("Bajaj Mixer Grinder"))])
            messagebox.showinfo("Product Status","Bajaj GX1 500W Mixer Grinder is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Bajaj GX1 500W Mixer Grinder is not added to the cart.")
    def AddA7():
        global appliances_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            appliances_list.append(["Balzano Electric Kettle",879,"879",Spaces(40-len("Balzano Electric Kettle"))])
            messagebox.showinfo("Product Status","Balzano OX218 Electric Kettle is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Balzano OX218 Electric Kettle is not added to the cart.")
    def AddA8():
        global appliances_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            appliances_list.append(["Elica Wall Mounted Chimney",11999,"11,999",Spaces(40-len("Elica Wall Mounted Chimney"))])
            messagebox.showinfo("Product Status","Elica WDFL 606 HAC MS NERO Auto Clean Wall Mounted Chimney is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Elica WDFL 606 HAC MS NERO Auto Clean Wall Mounted Chimney is not added to the cart.")
    def AddA9():
        global appliances_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            appliances_list.append(["Kent Ace Water Purifier",12499,"12,499",Spaces(40-len("Kent Ace Water Purifier"))])
            messagebox.showinfo("Product Status","Kent Ace 8 L Water Purifier is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Kent Ace 8 L Water Purifier is not added to the cart.")
    def AddA10():
        global appliances_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            appliances_list.append(["Eureka Dry Vacuum Cleaner",3249,"3,249",Spaces(40-len("Eureka Dry Vacuum Cleaner"))])
            messagebox.showinfo("Product Status","Eureka Forbes Quick Clean DX Dry Vacuum Cleaner is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Eureka Forbes Quick Clean DX Dry Vacuum Cleaner is not added to the cart.")
    add_appliances1=Button(lf_appliances1,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddA1).place(x=68,y=245)
    add_appliances2=Button(lf_appliances2,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddA2).place(x=68,y=245)
    add_appliances3=Button(lf_appliances3,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddA3).place(x=68,y=245)
    add_appliances4=Button(lf_appliances4,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddA4).place(x=68,y=245)
    add_appliances5=Button(lf_appliances5,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddA5).place(x=68,y=245)
    add_appliances6=Button(lf_appliances6,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddA6).place(x=68,y=245)
    add_appliances7=Button(lf_appliances7,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddA7).place(x=68,y=245)
    add_appliances8=Button(lf_appliances8,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddA8).place(x=68,y=245)
    add_appliances9=Button(lf_appliances9,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddA9).place(x=68,y=245)
    add_appliances10=Button(lf_appliances10,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddA10).place(x=68,y=245)
Grocery_button=Button(Button_frame,text="Grocery",font="times 20 bold",width=17,bd=6,bg="cadetblue",fg="white",activebackground="light blue",command=GroceryCall)
Grocery_button.grid(row=0,column=0,padx=5,pady=5)
Electronics_button=Button(Button_frame,text="Electronics",font="times 20 bold",width=17,bd=6,bg="cadetblue",fg="white",activebackground="light blue",command=ElectronicsCall)
Electronics_button.grid(row=1,column=0,padx=5,pady=5)
Sports_Gym_button=Button(Button_frame,text="Sports and Gym",font="times 20 bold",width=17,bd=6,bg="cadetblue",fg="white",activebackground="light blue",command=SportsGymCall)
Sports_Gym_button.grid(row=2,column=0,padx=5,pady=5)
Furniture_button=Button(Button_frame,text="Furniture",font="times 20 bold",width=17,bd=6,bg="cadetblue",fg="white",activebackground="light blue",command=FurnitureCall)
Furniture_button.grid(row=3,column=0,padx=5,pady=5)
Appliances_button=Button(Button_frame,text="Appliances",font="times 20 bold",width=17,bd=6,bg="cadetblue",fg="white",activebackground="light blue",command=AppliancesCall)
Appliances_button.grid(row=4,column=0,padx=5,pady=5)
Coupon_frame=LabelFrame(root,bd=2,relief="groove",text="MEGA SALE!!!",fg="green",font="arial 16 bold")
Coupon_frame.place(x=2,y=450,width=300,height=230)
Coupon_1=Label(Coupon_frame,text="Get 15% Off on your purchase(upto Rs.500)",font="times 12",fg="yellow",bg="brown")
Coupon_2=Label(Coupon_frame,text="Get 10% Off on your purchase(upto Rs.750)",font="times 12",fg="yellow",bg="brown")
Coupon_3=Label(Coupon_frame,text="Get 5% Off on your purchase(upto Rs.1000)",font="times 12",fg="yellow",bg="brown")
Coupon_1.grid(row=0,column=0,padx=10,pady=17)
Coupon_2.grid(row=1,column=0,padx=10,pady=17)
Coupon_3.grid(row=2,column=0,padx=10,pady=17)
def Bill():
    op=messagebox.askyesno("Bill Generation Confirmation","Products cannot be added or removed during bill generation. Are you sure that you have finished shopping?")
    if op:
        Products_frame.destroy()
        Button_frame.destroy()
        Coupon_frame.destroy()
        bill_gen_button.destroy()
        grocery_price=0
        electronics_price=0
        sportsgym_price=0
        furniture_price=0
        appliances_price=0
        for i in range(len(grocery_list)):
            grocery_price+=grocery_list[i][1]
        for i in range(len(electronics_list)):
            electronics_price+=electronics_list[i][1]
        for i in range(len(sportsgym_list)):
            sportsgym_price+=sportsgym_list[i][1]
        for i in range(len(furniture_list)):
            furniture_price+=furniture_list[i][1]
        for i in range(len(appliances_list)):
            appliances_price+=appliances_list[i][1]
        total_price=grocery_price+electronics_price+sportsgym_price+furniture_price+appliances_price
        discount=[0,0,0]
        if 0.15*total_price<500:
            discount[0]=0.15*total_price
        else:
            discount[0]=500
        if 0.1*total_price<750:
            discount[1]=0.1*total_price
        else:
            discount[1]=750
        if 0.05*total_price<1000:
            discount[2]=0.05*total_price
        else:
            discount[2]=1000
        max_discount=max(discount)
        if max_discount==discount[0]:
            suggest=Label(root,bd=1,text="Suggested : 15% Off upto Rs.500",font="times 12",fg="blue").place(x=545,y=480)
        elif max_discount==discount[1]:
            suggest=Label(root,bd=1,text="Suggested : 10% Off upto Rs.750",font="times 12",fg="blue").place(x=545,y=480)
        else:
            suggest=Label(root,bd=1,text="Suggested : 5% Off upto Rs.1000",font="times 12",fg="blue").place(x=545,y=480)
        def GenBill(d,choice):
            bill_area=LabelFrame(root,bd=2,relief="groove")
            bill_area.place(x=305,y=80,width=750,height=600)
            bill_title=Label(bill_area,text="INVOICE",font="arial 15 bold",bd=4,relief="groove").pack(fill=X)
            scroll_y=Scrollbar(bill_area,orient=VERTICAL)
            bill_txt_area=Text(bill_area,yscrollcommand=scroll_y.set)
            scroll_y.pack(side=RIGHT,fill=Y)
            scroll_y.config(command=bill_txt_area.yview)
            bill_txt_area.pack(fill=BOTH,expand=1)
            bill_txt_area.insert(END,Spaces(40)+"The Emporium\n"+Spaces(90,'*')+"\n")
            if len(grocery_list)>0:
                bill_txt_area.insert(END,"Grocery Product(s)\n\nProduct Name"+Spaces(28)+"Price"+Spaces(25)+"Quantity\n")
                for i in grocery_list:
                    bill_txt_area.insert(END,i[0]+i[3]+"Rs."+str(i[1])+Spaces(27-len(str(i[1])))+i[2]+"\n")
                bill_txt_area.insert(END,"\nTotal Grocery Price : Rs."+str(grocery_price)+"\n"+Spaces(90,'*')+"\n")
            if len(electronics_list)>0:
                bill_txt_area.insert(END,"Electronics Product(s)\n\nProduct Name"+Spaces(28)+"Price"+Spaces(25)+"Colour\n")
                for i in electronics_list:
                    bill_txt_area.insert(END,i[0]+i[4]+"Rs."+i[2]+Spaces(27-len(i[2]))+i[3]+"\n")
                bill_txt_area.insert(END,"\nTotal Electronics Price : Rs."+str(electronics_price)+"\n"+Spaces(90,'*')+"\n")
            if len(sportsgym_list)>0:
                bill_txt_area.insert(END,"Sports and Gym Equipment(s)\n\nProduct Name"+Spaces(28)+"Price\n")
                for i in sportsgym_list:
                    bill_txt_area.insert(END,i[0]+i[3]+"Rs."+i[2]+"\n")
                bill_txt_area.insert(END,"\nTotal Sports and Gym Equipment Price : Rs."+str(sportsgym_price)+"\n"+Spaces(90,'*')+"\n")
            if len(furniture_list)>0:
                bill_txt_area.insert(END,"Furniture Product(s)\n\nProduct Name"+Spaces(28)+"Price\n")
                for i in furniture_list:
                    bill_txt_area.insert(END,i[0]+i[3]+"Rs."+i[2]+"\n")
                bill_txt_area.insert(END,"\nTotal Furniture Price : Rs."+str(furniture_price)+"\n"+Spaces(90,'*')+"\n")
            if len(appliances_list)>0:
                bill_txt_area.insert(END,"Appliance(s)\n\nProduct Name"+Spaces(28)+"Price\n")
                for i in appliances_list:
                    bill_txt_area.insert(END,i[0]+i[3]+"Rs."+i[2]+"\n")
                bill_txt_area.insert(END,"\nTotal Appliances Price : Rs."+str(appliances_price)+"\n"+Spaces(90,'*'))
            bill_txt_area.insert(END,"\nTotal Price(before discount) = Rs."+str(total_price))
            if choice==1:
                bill_txt_area.insert(END,"\nCoupon Applied : 15% Off upto Rs.500")
            elif choice==2:
                bill_txt_area.insert(END,"\nCoupon Applied : 10% Off upto Rs.750")
            else:
                bill_txt_area.insert(END,"\nCoupon Applied : 5% Off upto Rs.1000")
            bill_txt_area.insert(END,"\nDiscount Offered : Rs."+str(d))
            bill_txt_area.insert(END,"\nTotal Price(after discount) = Rs."+str(total_price-d))
            save_button=Button(root,text="Save Invoice",font="times 20 bold",bd=6,bg="skyblue",width=10,fg="white",command=lambda:save_invoice(bill_txt_area.get("1.0",END)))
            save_button.place(x=1120,y=600)
        Coupon_frame_2=LabelFrame(root,bd=2,relief="groove",text="Apply a Coupon",fg="green",font="arial 16 bold").place(x=500,y=150,width=380,height=300)
        Coupon_apply1=Button(Coupon_frame_2,text="15% Off upto Rs.500",font="times 20 bold",width=17,bd=6,bg="cadetblue",fg="white",activebackground="light blue",command=lambda:GenBill(discount[0],1))
        Coupon_apply1.place(x=540,y=190)
        Coupon_apply2=Button(Coupon_frame_2,text="10% Off upto Rs.750",font="times 20 bold",width=17,bd=6,bg="cadetblue",fg="white",activebackground="light blue",command=lambda:GenBill(discount[1],2))
        Coupon_apply2.place(x=540,y=280)
        Coupon_apply3=Button(Coupon_frame_2,text="5% Off upto Rs.1000",font="times 20 bold",width=17,bd=6,bg="cadetblue",fg="white",activebackground="light blue",command=lambda:GenBill(discount[2],3))
        Coupon_apply3.place(x=540,y=370)
    else:
        messagebox.showinfo("Bill Generation Confirmation","You can continue shopping now.")
bill_gen_button=Button(Heading,bd=4,text="Proceed to Checkout",font="times 17 bold",bg="skyblue",fg="white",activebackground="purple",command=Bill)
bill_gen_button.grid(row=0,column=3)
root.mainloop()
