import tkinter as tk
import os
window = tk.Tk()
window.geometry('900x500')
window.title("คำนวณเกรด")

Choose = tk.Label(window,text=" เกรดเฉลี่ย GPA",fg="blue",font=("Arial ",12))
Choose.grid(column=0,row=1)

credit = tk.Label(window,text="หน่วยกิต")
credit.grid(column=1,row=2)
grede = tk.Label(window,text="เกรดที่ได้")
grede.grid(column=2,row=2)

b1 = tk.Label(window,text="วิชาที่ 1 : ",font=("Arial ",12))
b1.grid(column=0,row=3)
c1 = tk.Entry(window,width=15)
c1.grid(column=1,row=3)
c1.insert(0,"0")
g1 = tk.Entry(window,width=15)
g1.grid(column=2,row=3)
g1.insert(0,"0")

b2 = tk.Label(window,text="วิชาที่ 2 : ",font=("Arial ",12))
b2.grid(column=0,row=4)
c2 = tk.Entry(window,width=15)
c2.grid(column=1,row=4)
c2.insert(0,"0")
g2 = tk.Entry(window,width=15)
g2.grid(column=2,row=4)
g2.insert(0,"0")

b3 = tk.Label(window,text="วิชาที่ 3 : ",font=("Arial ",12))
b3.grid(column=0,row=5)
c3 = tk.Entry(window,width=15)
c3.grid(column=1,row=5)
c3.insert(0,"0")
g3 = tk.Entry(window,width=15)
g3.grid(column=2,row=5)
g3.insert(0,"0")

b4 = tk.Label(window,text="วิชาที่ 4 : ",font=("Arial ",12))
b4.grid(column=0,row=6)
c4 = tk.Entry(window,width=15)
c4.grid(column=1,row=6)
c4.insert(0,"0")
g4 = tk.Entry(window,width=15)
g4.grid(column=2,row=6)
g4.insert(0,"0")

b5 = tk.Label(window,text="วิชาที่ 5 : ",font=("Arial ",12))
b5.grid(column=0,row=7)
c5 = tk.Entry(window,width=15)
c5.grid(column=1,row=7)
c5.insert(0,"0")
g5 = tk.Entry(window,width=15)
g5.grid(column=2,row=7)
g5.insert(0,"0")

b6 = tk.Label(window,text="วิชาที่ 6 : ",font=("Arial ",12))
b6.grid(column=0,row=8)
c6 = tk.Entry(window,width=15)
c6.grid(column=1,row=8)
c6.insert(0,"0")
g6 = tk.Entry(window,width=15)
g6.grid(column=2,row=8)
g6.insert(0,"0")

b7 = tk.Label(window,text="วิชาที่ 7 : ",font=("Arial ",12))
b7.grid(column=0,row=9)
c7 = tk.Entry(window,width=15)
c7.grid(column=1,row=9)
c7.insert(0,"0")
g7 = tk.Entry(window,width=15)
g7.grid(column=2,row=9)
g7.insert(0,"0")

b8 = tk.Label(window,text="วิชาที่ 8 : ",font=("Arial ",12))
b8.grid(column=0,row=10)
c8 = tk.Entry(window,width=15)
c8.grid(column=1,row=10)
c8.insert(0,"0")
g8 = tk.Entry(window,width=15)
g8.grid(column=2,row=10)
g8.insert(0,"0")

b9 = tk.Label(window,text="วิชาที่ 9 : ",font=("Arial ",12))
b9.grid(column=0,row=11)
c9 = tk.Entry(window,width=15)
c9.grid(column=1,row=11)
c9.insert(0,"0")
g9 = tk.Entry(window,width=15)
g9.grid(column=2,row=11)
g9.insert(0,"0")

b10 = tk.Label(window,text="วิชาที่ 10 : ",font=("Arial ",12))
b10.grid(column=0,row=12)
c10 = tk.Entry(window,width=15)
c10.grid(column=1,row=12)
c10.insert(0,"0")
g10 = tk.Entry(window,width=15)
g10.grid(column=2,row=12)
g10.insert(0,"0")

b11 = tk.Label(window,text="วิชาที่ 11 : ",font=("Arial ",12))
b11.grid(column=0,row=13)
c11 = tk.Entry(window,width=15)
c11.grid(column=1,row=13)
c11.insert(0,"0")
g11 = tk.Entry(window,width=15)
g11.grid(column=2,row=13)
g11.insert(0,"0")

b12 = tk.Label(window,text="วิชาที่ 12 : ",font=("Arial ",12))
b12.grid(column=0,row=14)
c12 = tk.Entry(window,width=15)
c12.grid(column=1,row=14)
c12.insert(0,"0")
g12 = tk.Entry(window,width=15)
g12.grid(column=2,row=14)
g12.insert(0,"0")



lblgpa = tk.Label(window,text="หน่วยกิตรวม = ",font=("Arial ",10))
lblgpa.grid(column=1,row=15)
lblgpa = tk.Label(window,text="เกรดรวม = ",font=("Arial ",10))
lblgpa.grid(column=1,row=16)
lblgpa = tk.Label(window,text="ค่าคะแนนที่ได้ = ",font=("Arial ",10))
lblgpa.grid(column=1,row=17)
lblgpa = tk.Label(window,text="เกรดเฉลี่ย GPA = ",font=("Arial ",10))
lblgpa.grid(column=1,row=18)

CResult= tk.Label(window,fg="green")
CResult.grid(column=2,row=15)

GResult= tk.Label(window,fg="green")
GResult.grid(column=2,row=16)

GCResult= tk.Label(window,fg="green")
GCResult.grid(column=2,row=17)

GPAResult= tk.Label(window,fg="green")
GPAResult.grid(column=2,row=18)
def C_clicked():
    n1 = float(c1.get())
    n2 = float(c2.get())
    n3 = float(c3.get())
    n4 = float(c4.get())
    n5 = float(c5.get())
    n6 = float(c6.get())
    n7 = float(c7.get())
    n8 = float(c8.get())
    n9 = float(c9.get())
    n10 = float(c10.get())
    n11 = float(c11.get())
    n12 = float(c12.get())
    resultC = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10 + n11 + n12 
    CResult.configure(text=float('%.2f' %resultC))
    print(resultC)
    
    x1 = float(g1.get())
    x2 = float(g2.get())
    x3 = float(g3.get())
    x4 = float(g4.get())
    x5 = float(g5.get())
    x6 = float(g6.get())
    x7 = float(g7.get())
    x8 = float(g8.get())
    x9 = float(g9.get())
    x10 = float(g10.get())
    x11 = float(g11.get())
    x12 = float(g12.get())
    resultG = x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9 + x10 + x11 + x12 
    GResult.configure(text=float('%.2f' % resultG))
    print(resultG)
    
    resultGC = (n1*x1) + (n2*x2) ++ (n3*x3) + (n4*x4) + (n5*x5) + (n6*x6) + (n7*x7) + (n8*x8) + (n9*x9) + (n10*x10) + (n11*x11) + (n12*x12)
    GCResult.configure(text=float('%.2f' % resultGC))
    print(resultGC)
    
    resultGPA = resultGC/resultC
    GPAResult.configure(text=float('%.2f'% resultGPA))
    print(resultGPA)


btn = tk.Button(window,text="GPA",fg="black",width=12,command=C_clicked)
btn.grid(column=3,row=14)

Choose2 = tk.Label(window,text=" เกรดเฉลี่ยสะสม GPAX",fg="blue",font=("Arial ",12))
Choose2.grid(column=4,row=1)
credit2 = tk.Label(window,text="หน่วยกิตทั้งหมด")
credit2.grid(column=5,row=2)
grede2 = tk.Label(window,text="ค่าคะแนนที่ได้")
grede2.grid(column=6,row=2)

bx1 = tk.Label(window,text="ภาคการเรียนที่ 1 : ",font=("Arial ",12))
bx1.grid(column=4,row=3)
cx1 = tk.Entry(window,width=15)
cx1.grid(column=5,row=3)
cx1.insert(0,"0")
gx1 = tk.Entry(window,width=15)
gx1.grid(column=6,row=3)
gx1.insert(0,"0")

bx2 = tk.Label(window,text="ภาคการเรียนที่ 2 : ",font=("Arial ",12))
bx2.grid(column=4,row=5)
cx2 = tk.Entry(window,width=15)
cx2.grid(column=5,row=5)
cx2.insert(0,"0")
gx2 = tk.Entry(window,width=15)
gx2.grid(column=6,row=5)
gx2.insert(0,"0")

bx3 = tk.Label(window,text="ภาคการเรียนที่ี่ 3 : ",font=("Arial ",12))
bx3.grid(column=4,row=7)
cx3 = tk.Entry(window,width=15)
cx3.grid(column=5,row=7)
cx3.insert(0,"0")
gx3 = tk.Entry(window,width=15)
gx3.grid(column=6,row=7)
gx3.insert(0,"0")

bx4 = tk.Label(window,text="ภาคการเรียนที่ 4 : ",font=("Arial ",12))
bx4.grid(column=4,row=9)
cx4 = tk.Entry(window,width=15)
cx4.grid(column=5,row=9)
cx4.insert(0,"0")
gx4 = tk.Entry(window,width=15)
gx4.grid(column=6,row=9)
gx4.insert(0,"0")

bx5 = tk.Label(window,text="ภาคการเรียนที่ 5 : ",font=("Arial ",12))
bx5.grid(column=4,row=11)
cx5 = tk.Entry(window,width=15)
cx5.grid(column=5,row=11)
cx5.insert(0,"0")
gx5 = tk.Entry(window,width=15)
gx5.grid(column=6,row=11)
gx5.insert(0,"0")

bx6 = tk.Label(window,text="ภาคการเรียนที่ 6 : ",font=("Arial ",12))
bx6.grid(column=4,row=13)
cx6 = tk.Entry(window,width=15)
cx6.grid(column=5,row=13)
cx6.insert(0,"0")
gx6 = tk.Entry(window,width=15)
gx6.grid(column=6,row=13)
gx6.insert(0,"0")

lblgpa = tk.Label(window,text="หน่วยกิตรวม = ",font=("Arial ",10))
lblgpa.grid(column=5,row=16)
lblGC = tk.Label(window,text="ค่าคะแนนที่ได้ = ",font=("Arial ",10))
lblGC.grid(column=5,row=17)
lblgpa = tk.Label(window,text="เกรดเฉลี่ย GPAX = ",font=("Arial ",10))
lblgpa.grid(column=5,row=18)

CXResult= tk.Label(window,fg="green")
CXResult.grid(column=6,row=16)

GXResult= tk.Label(window,fg="green")
GXResult.grid(column=6,row=17)

GPAXResult= tk.Label(window,fg="green")
GPAXResult.grid(column=6,row=18)

def X_clicked():
    n1 = float(cx1.get())
    n2 = float(cx2.get())
    n3 = float(cx3.get())
    n4 = float(cx4.get())
    n5 = float(cx5.get())
    n6 = float(cx6.get())
    resultCX = n1 + n2 + n3 + n4 + n5 + n6 
    CXResult.configure(text=float('%.2f' %resultCX))
    print(resultCX)

    x1 = float(gx1.get())
    x2 = float(gx2.get())
    x3 = float(gx3.get())
    x4 = float(gx4.get())
    x5 = float(gx5.get())
    x6 = float(gx6.get())
    resultGX = x1 + x2 + x3 + x4 + x5 + x6 
    GXResult.configure(text=float('%.2f' %resultGX))
    print(resultGX)

    resultGPAX = resultGX/resultCX
    GPAXResult.configure(text=float('%.2f' %resultGPAX))
    print(resultGPAX)

btn2 = tk.Button(window,text="GPAX",fg="black",width=12,command=X_clicked)
btn2.grid(column=8,row=14)


def Gradedelete1():
    c1.delete(0,10)
    c1.insert(0,"0")
    c2.delete(0,10)
    c2.insert(0,"0")
    c3.delete(0,10)
    c3.insert(0,"0")
    c4.delete(0,10)
    c4.insert(0,"0")
    c5.delete(0,10)
    c5.insert(0,"0")
    c6.delete(0,10)
    c6.insert(0,"0")
    c7.delete(0,10)
    c7.insert(0,"0")
    c8.delete(0,10)
    c8.insert(0,"0")
    c9.delete(0,10)
    c9.insert(0,"0")
    c10.delete(0,10)
    c10.insert(0,"0")
    c11.delete(0,10)
    c11.insert(0,"0")
    c12.delete(0,10)
    c12.insert(0,"0")

    
    g1.delete(0,10)
    g1.insert(0,"0")
    g2.delete(0,10)
    g2.insert(0,"0")
    g3.delete(0,10)
    g3.insert(0,"0")
    g4.delete(0,10)
    g4.insert(0,"0")
    g5.delete(0,10)
    g5.insert(0,"0")
    g6.delete(0,10)
    g6.insert(0,"0")
    g7.delete(0,10)
    g7.insert(0,"0")
    g8.delete(0,10)
    g8.insert(0,"0")
    g9.delete(0,10)
    g9.insert(0,"0")
    g10.delete(0,10)
    g10.insert(0,"0")
    g11.delete(0,10)
    g11.insert(0,"0")
    g12.delete(0,10)
    g12.insert(0,"0")

btnback = tk.Button(window,text="Delete",fg="black",width=12,command=Gradedelete1)
btnback.grid(column=3,row=15)

def Gradedelete():
 
    cx1.delete(0,10)
    cx1.insert(0,"0")
    cx2.delete(0,10)
    cx2.insert(0,"0")
    cx3.delete(0,10)
    cx3.insert(0,"0")
    cx4.delete(0,10)
    cx4.insert(0,"0")
    cx5.delete(0,10)
    cx5.insert(0,"0")
    cx6.delete(0,10)
    cx6.insert(0,"0")

    gx1.delete(0,10)
    gx1.insert(0,"0")
    gx2.delete(0,10)
    gx2.insert(0,"0")
    gx3.delete(0,10)
    gx3.insert(0,"0")
    gx4.delete(0,10)
    gx4.insert(0,"0")
    gx5.delete(0,10)
    gx5.insert(0,"0")
    gx6.delete(0,10)
    gx6.insert(0,"0")
    
   

btnback = tk.Button(window,text="Delete",fg="black",width=12,command=Gradedelete)
btnback.grid(column=8,row=15)



def Gradeback():
    window.destroy()
    filename = 'grade1.py'
    os.system(filename)

btnback = tk.Button(window,text="<Back",fg="black",width=12,command=Gradeback)
btnback.grid(column=8,row=16)




lblv1 = tk.Label(window,text="  ",font=("Arial ",10),fg="red")
lblv1.grid(column=0,row=21)
lblv = tk.Label(window,text="*** หากไม่มีข้อมูลให้ใส่ 0 *** ",font=("Arial ",10),fg="red")
lblv.grid(column=0,row=22)

window.mainloop() 
