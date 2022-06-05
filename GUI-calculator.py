from struct import pack
from tkinter import *
from tkinter import ttk, messagebox

GUI = Tk() 
GUI.title('โปรแกรมคำนวณปลา รถพุ่มพวง ')
GUI.geometry('700x600')

#bg = PhotoImage(file='car.png')
bg = PhotoImage(file= r'C:\Users\supachai.o\Desktop\UncleEngineer\car.png')   #การใส่ path ยาว ต้องใส่ตัว r  นำหน้าด้วย

BG = Label(GUI, image=bg)
BG.pack()


L = Label(GUI,text='กรุณากรอกจำนวนปลา (กิโลกรัม)',font=(None,20))
L.pack()


 
v_quantity = StringVar()                                                           #เป็นตัวแปรที่ใช้เก็บข้อความเมื่อพิมพ์เสร็จแล้ว
E1 = ttk.Entry(GUI, textvariable=v_quantity, font=(None,20))
E1.pack()                                                                         # .pack คือคำสั่งแปะใน GUI



def Cal():
    try:
        quan = float(v_quantity.get())
        calc = quan * 39                                                           #39 บาทต่อกิโล * จำนวนปลา                                           
        messagebox.showinfo('ราคาทั้งหมด' , 'ราคาปลาทั้งหมด {} บาท'.format(calc))
        v_quantity.set('')
        E1.focus()                                                              #เมือแสดงผลเสร็จ ให้ cursor ไปจ่อที่กล่องป้อนตัวเลขต่อ
    except:
        messagebox.showwarning('กรอกผิด','กรุณากรอกเฉพาะตัวเลขเท่านั้น')
        v_quantity.set('1')  
        E1.focus()                                                      #การ clear ข้อความที่กรอกผิด




B = ttk.Button(GUI, text='คำนวณ' , command=Cal)
B.pack(ipadx=30,ipady=20,pady=20)                                                  #ipadx    ขยายความกว้าง x,y


GUI.mainloop()  #เพื่อให้โปรแกรมรันตลอดเวลา