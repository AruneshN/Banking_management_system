#.............................................library................................................................
import tkinter
from tkinter import*
import tkinter as Tk
import pymysql
from tkinter import messagebox
import threading
import time
from PIL import ImageTk,Image
from tkinter import ttk
#...........................................database.................................................................................................
db_connection =pymysql.connect(
    host="localhost",
    user="root",
    passwd="arunesh5488",
    database="banksystem"
)
my_database=db_connection.cursor()
print("server connected")


def Acc():
    bot=tkinter.Tk()
    bot.title("ACCOUNT OPENING")
    bot.config(bg="#2A363B")
    bot.geometry("1366x768")
    Label(bot,text="ISAB BANK OF INDIA",bg="#2A363B",fg="white",font=("times new roman",50,"underline")).place(x=360,y=10)
    label_frames=LabelFrame(bot,bg="sky blue",text="Sign up",font=("times new roman",20,"bold"))
    label_frames.pack(fill="both", expand="yes", padx=190, pady=90)
#..label.....................................................................................................................
    Label(label_frames,font=("times new roman",18,"bold"),bg="sky blue",fg="black",text="Full Name").place(x=80,y=50)
    Label(label_frames,font=("times new roman",18,"bold"),bg="sky blue",fg="black",text="Account Type").place(x=80,y=130) 
    Label(label_frames,font=("times new roman",18,"bold"),bg="sky blue",fg="black",text="Aadhar Number").place(x=80,y=200)
    Label(label_frames,font=("times new roman",18,"bold"),bg="sky blue",fg="black",text="Account Number").place(x=80,y=280)
    Label(label_frames,font=("times new roman",18,"bold"),bg="sky blue",fg="black",text="Mobile Number").place(x=530,y=50)
    Label(label_frames,font=("times new roman",18,"bold"),bg="sky blue",fg="black",text="G-mail Id").place(x=530,y=130)
    Label(label_frames,font=("times new roman",18,"bold"),bg="sky blue",fg="black",text="Gender").place(x=530,y=200)
    Label(label_frames,font=("times new roman",18,"bold"),bg="sky blue",fg="black",text="Date of Birth").place(x=530,y=280)
    Label(label_frames,font=("times new roman",18,"bold"),bg="sky blue",fg="black",text="Password").place(x=80,y=360)
    Label(label_frames,font=("times new roman",18,"bold"),bg="sky blue",fg="black",text="Confirm Password").place(x=530,y=360)
    Label(label_frames,font=("times new roman",18,"bold"),bg="sky blue",fg="black",text="Initial Balance").place(x=80,y=440)
#...entry.........................................................................................................................
    
    a1=Entry(label_frames,width=30)#name
    a1.place(x=270,y=55)
    a2=Entry(label_frames,width=30)#aadhar
    a2.place(x=270,y=205)
    a3=Entry(label_frames,width=30)#phone
    a3.place(x=730,y=55)
    a4=Entry(label_frames,width=30)#gmail
    a4.place(x=730,y=135)
    a5=Entry(label_frames,width=30)#account number
    a5.place(x=270,y=285)
    a6=Entry(label_frames,width=30)#password
    a6.place(x=270,y=365)
    a7=Entry(label_frames,width=30)#d.o.b
    a7.place(x=730,y=285)
    a8=Entry(label_frames,width=30)#con pass
    a8.place(x=730,y=365)
    a9=Entry(label_frames,width=30)#balance
    a9.place(x=270,y=445)
    def Pass():
        if a6.get() == a8.get():
            messagebox.showinfo("Message","SIGN UP") and slog()
        else:
            messagebox.showinfo("Login","incorrect pin")

#..combo box.......................................................................................................
    
    cb1=ttk.Combobox(label_frames,width=28,state="readonly")
    cb1['values']=("Saving Account","Current Account")
    cb1.place(x=270,y=135)
    cb2=ttk.Combobox(label_frames,width=28,state="readonly")
    cb2['values']=("Male","Female","Other")
    cb2.place(x=730,y=205)
    def signin():
        sql_statement="INSERT INTO user_detail (Full_Name,Account_Type,Aadhar_Number,Account_Number,Mobile_Number,G_mail_Id,Gender,Date_of_Birth,Password,Confirm_Password,Initial_Balance) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        values=(a1.get(),cb1.get(),a2.get(),a5.get(),a3.get(),a4.get(),cb2.get(),a7.get(),a6.get(),a8.get(),a9.get())
        my_database.execute(sql_statement,values)
        db_connection.commit()   
#..account opening buttons...........................................................................................
    
    button=Tk.Button(label_frames,relief=FLAT,command=signin,font=("times new roman",15,"bold"),fg="black",text="Submit",bg="sky blue",width="20").place(x=360,y=485)
    button=Tk.Button(label_frames,relief=FLAT,font=("times new roman",15,"bold"),fg="black",text="Back",bg="sky blue",width="20").place(x=100,y=485)
    button=Tk.Button(label_frames,relief=FLAT,command=Pass,font=("times new roman",15,"bold"),fg="black",state="normal",text="Next",bg="sky blue",width="20").place(x=620,y=485)
    def slog():
        ulog=tkinter.Tk()
        ulog.title("SignIn")
        ulog.config(bg="#C2571A")
        Label(ulog,text="ISAB BANK OF INDIA",bg="#C2571A",fg="white",font=("times new roman",50,"underline")).place(x=360,y=10)
        ulog.geometry("1366x768")
        log_frames=LabelFrame(ulog,bg="#FF5C5C",fg="red",highlightbackground="black",highlightthickness=4,text="ISAB",font=("times new roman",20,"bold"))
        log_frames.pack(fill="both", expand="yes", padx=280, pady=180)
        Label(log_frames,text="UserName",bg="#FF5C5C",fg="white",font=("times new roman",29,"bold")).place(x=160,y=40)
        Label(log_frames,text="PassWord",bg="#FF5C5C",fg="white",font=("times new roman",29,"bold")).place(x=160,y=140)
        
        l1=Entry(log_frames,width=35)#name
        l1.place(x=360,y=55)
        l2=Entry(log_frames,width=35)#pass
        l2.place(x=360,y=155)
        def log():
            if a1.get()==l1.get():
                if a8.get()==l2.get():
                    messagebox.showinfo("Message","SIGN UP") and mp()
            else:
                messagebox.showinfo("Message","INCORRECT") and slog()
        button=Tk.Button(log_frames,relief=FLAT,command=log,text="LOG",bg="#FF5C5C",fg="black",font=("times new roman",20,"bold")).place(x=380,y=250)
        button=Tk.Button(log_frames,text="BACK",command=Acc  ,relief=FLAT,bg="#FF5C5C",fg="black",font=("times new roman",20,"bold")).place(x=250,y=250)

#.......................................main home page..........................................................................

def mp():
    main=tkinter.Tk()
    main.title("Tkinter Bank")
    main.config(bg="#722F37")
    Label(main,text="ISAB BANK OF INDIA",bg="#722F37",fg="white",font=("times new roman",50,"underline")).place(x=360,y=10)
    main.geometry("1366x768")
#...home page frame................................................................................................
    hp_frames=LabelFrame(main,bg="white",fg="red",highlightbackground="blue",highlightthickness=4,text="Welcome",font=("times new roman",20,"bold"))
    hp_frames.pack(fill="both", expand="yes", padx=280, pady=98)
    butt=Tk.Button(hp_frames,text="Preview",command= Acc,relief=FLAT,bg="red",fg="black",font=("times new roman",18,"bold")).place(x=70,y=458)
    def fr():
        mi_frames=LabelFrame(hp_frames,highlightbackground="black",highlightthickness=2,bg="white",fg="red",font=("times new roman",20,"bold"))
        mi_frames.pack(fill="both", expand="yes", padx=200, pady=80)


###...................................Bank statement........................................................................

    def details():
        det_frames=LabelFrame(hp_frames,highlightbackground="black",highlightthickness=2,bg="white",fg="red",font=("times new roman",20,"bold"))
        det_frames.pack(fill="both", expand="yes", padx=100, pady=100)
        Label(det_frames,text="PROFILE",bg="white",fg="black",font=("times new roman",16,"underline")).place(x=250,y=10)
        Label(det_frames,text="Name :",bg="white",fg="black",font=("times new roman",16,"underline")).place(x=50,y=60)
        Label(det_frames,text="Account No:",bg="white",fg="black",font=("times new roman",16,"underline")).place(x=50,y=130)
        Label(det_frames,text="Mobile No:",bg="white",fg="black",font=("times new roman",16,"underline")).place(x=50,y=210)
        det_button=Tk.Button(det_frames,command=det_frames.destroy,text="Back",fg="blue",bg="white",font=("times new roman",15,"bold")).place(x=250,y=250)
        sql_statement="SELECT Full_Name,Account_Number,Mobile_Number FROM user_detail"
        my_database.execute(sql_statement)
        output=my_database.fetchall()
        print(output[0])
        a=output[0]
        b=a[0]
        print(output[0])
        c=output[0]
        d=c[1]
        print(output[0])
        e=output[0]
        f=e[2]

        Label(det_frames,text=b,bg="white",fg="red",font=("times new roman",15,"bold")).place(x=200,y=60)
        Label(det_frames,text=d,bg="white",fg="red",font=("times new roman",15,"bold")).place(x=200,y=130)
        Label(det_frames,text=f,bg="white",fg="red",font=("times new roman",15,"bold")).place(x=200,y=210)
#.......................................Account Holder Deails..............................................................
    def hold():
        hold_frames=LabelFrame(hp_frames,highlightbackground="black",highlightthickness=2,bg="white",fg="red",font=("times new roman",20,"bold"))
        hold_frames.pack(fill="both", expand="yes", padx=30, pady=50)
        Label(hold_frames,text="DETAILS",bg="white",fg="black",font=("times new roman",16,"underline")).place(x=290,y=10)
        Label(hold_frames,text="Name :",bg="white",fg="black",font=("times new roman",16,"underline")).place(x=30,y=60)
        Label(hold_frames,text="Account No:",bg="white",fg="black",font=("times new roman",16,"underline")).place(x=30,y=130)
        Label(hold_frames,text="Mobile No:",bg="white",fg="black",font=("times new roman",16,"underline")).place(x=30,y=200)
        Label(hold_frames,text="G-mail Id:",bg="white",fg="black",font=("times new roman",16,"underline")).place(x=30,y=270)
        Label(hold_frames,text="Account Type:",bg="white",fg="black",font=("times new roman",16,"underline")).place(x=400,y=60)
        Label(hold_frames,text="Date Of Birth:",bg="white",fg="black",font=("times new roman",16,"underline")).place(x=400,y=130)
        Label(hold_frames,text="Gender:",bg="white",fg="black",font=("times new roman",16,"underline")).place(x=400,y=200)
        hold_button=Tk.Button(hold_frames,command=hold_frames.destroy,text="Back",fg="blue",bg="white",font=("times new roman",15,"bold")).place(x=290,y=350)
        sql_statement="SELECT Full_Name,Account_Number,Mobile_Number,G_mail_Id,Account_Type,Date_of_Birth,Gender FROM user_detail"
        my_database.execute(sql_statement)
        output=my_database.fetchall()
        print(output[0])
        a=output[0]
        b=a[0]
        print(output[0])
        c=output[0]
        d=c[1]
        print(output[0])
        e=output[0]
        f=e[2]
        print(output[0])
        g=output[0]
        h=a[3]
        print(output[0])
        i=output[0]
        j=c[4]
        print(output[0])
        k=output[0]
        l=e[5]
        print(output[0])
        m=output[0]
        n=e[6]

        Label(hold_frames,text=b,bg="white",fg="red",font=("times new roman",15,"bold")).place(x=150,y=60)
        Label(hold_frames,text=d,bg="white",fg="red",font=("times new roman",15,"bold")).place(x=150,y=130)
        Label(hold_frames,text=f,bg="white",fg="red",font=("times new roman",15,"bold")).place(x=150,y=200)
        Label(hold_frames,text=h,bg="white",fg="red",font=("times new roman",15,"bold")).place(x=150,y=270)
        Label(hold_frames,text=j,bg="white",fg="red",font=("times new roman",15,"bold")).place(x=530,y=60)
        Label(hold_frames,text=l,bg="white",fg="red",font=("times new roman",15,"bold")).place(x=530,y=130)
        Label(hold_frames,text=n,bg="white",fg="red",font=("times new roman",15,"bold")).place(x=530,y=200)      
#..............debit...........................................................................................
    def debit():
        deb_frames=LabelFrame(hp_frames,highlightbackground="black",highlightthickness=2,bg="white",fg="red",font=("times new roman",20,"bold"))
        deb_frames.pack(fill="both", expand="yes", padx=150, pady=70)
        Label(deb_frames,text="WITHDRAW",bg="white",fg="black",fon=("times new roman",14,"underline")).place(x=170,y=10)
        Label(deb_frames,text="Account Number",bg="white",fg="black",font=("times new roman",14,"bold")).place(x=50,y=50)
        Label(deb_frames,text="Pin Number",bg="white",fg="black",font=("times new roman",14,"bold")).place(x=50,y=130)
        Label(deb_frames,text="Amount",bg="white",fg="black",font=("times new roman",14,"bold")).place(x=50,y=200)
        Label(deb_frames,text="Total Balance",bg="white",fg="black",font=("times new roman",14,"bold")).place(x=50,y=260)
        f1=Entry(deb_frames,font=("times new roman",14,"bold"))#acc num
        f1.place(x=250,y=55)
        f2=Entry(deb_frames,font=("times new roman",14,"bold"))#pin
        f2.place(x=250,y=135)
        f3=Entry(deb_frames,font=("times new roman",14,"bold"))#amt
        f3.place(x=250,y=205)

        def deb_amt():
            debit_amt=f3.get()
            debit_amt= int(debit_amt)
            sql_statement="SELECT Initial_Balance FROM user_detail"
            my_database.execute(sql_statement)
            output=my_database.fetchall()
            print(output[0])
            a=output[0]
            b=a[0]
            b= int(b)


        
            Label(deb_frames,text=b-debit_amt,bg="white",fg="red",font=("times new roman",15,"bold")).place(x=250,y=260)
        de=Tk.Button(deb_frames,command=deb_amt ,text="Send",relief=FLAT,fg="white",bg="blue",font=("times new roman",16,"bold")).place(x=200,y=310)
        button=Tk.Button(deb_frames,command=deb_frames.destroy,text="close",relief=FLAT,fg="white",bg="blue",font=("times new roman",16,"bold")).place(x=350,y=310)       
#.................................................pay.....................................................................................            
    def credit():    
        cre_frames=LabelFrame(hp_frames,highlightbackground="black",highlightthickness=2,bg="white",fg="red",font=("times new roman",20,"bold"))
        cre_frames.pack(fill="both", expand="yes", padx=150, pady=70)
        Label(cre_frames,text="PAY",bg="white",fg="black",fon=("times new roman",14,"underline")).place(x=170,y=10)
        Label(cre_frames,text="Account Number",bg="white",fg="black",font=("times new roman",14,"bold")).place(x=50,y=60)
        Label(cre_frames,text="To Account Number",bg="white",fg="black",font=("times new roman",14,"bold")).place(x=50,y=140)
        Label(cre_frames,text="Amount",bg="white",fg="black",font=("times new roman",14,"bold")).place(x=50,y=210)
        Label(cre_frames,text="Total Balance",bg="white",fg="black",font=("times new roman",14,"bold")).place(x=50,y=260)
        c1=Entry(cre_frames,font=("times new roman",14,"bold"))
        c1.place(x=250,y=65)
        c2=Entry(cre_frames,font=("times new roman",14,"bold"))
        c2.place(x=250,y=145)
        c3=Entry(cre_frames,font=("times new roman",14,"bold"))#amt
        c3.place(x=250,y=215)

        def cre_amt():
            crt_amt=c3.get()
            crt_amt= int(crt_amt)
            sql_statement="SELECT Initial_Balance FROM user_detail"
            my_database.execute(sql_statement)
            output=my_database.fetchall()
            print(output[0])
            a=output[0]
            b=a[0]
            b= int(b)
            
            Label(cre_frames,text=b-crt_amt,bg="white",fg="red",font=("times new roman",15,"bold")).place(x=250,y=260)      
        button=Tk.Button(cre_frames,command=cre_amt,text="Send",relief=FLAT,fg="white",bg="blue",font=("times new roman",18,"bold")).place(x=200,y=310)
        button=Tk.Button(cre_frames,command=cre_frames.destroy,text="close",relief=FLAT,fg="white",bg="blue",font=("times new roman",16,"bold")).place(x=350,y=310)           
        credit_amt=c3.get()
#................debosit.........................................................................................................
    def Credits():
    
        Cre_frames=LabelFrame(hp_frames,highlightbackground="black",highlightthickness=2,bg="white",fg="red",font=("times new roman",20,"bold"))
        Cre_frames.pack(fill="both", expand="yes", padx=150, pady=70)
        Label(Cre_frames,text="DEPOSIT",bg="white",fg="black",fon=("times new roman",14,"underline")).place(x=170,y=10)
        Label(Cre_frames,text="Account Number",bg="white",fg="black",font=("times new roman",14,"bold")).place(x=50,y=60)
        Label(Cre_frames,text="To Account Number",bg="white",fg="black",font=("times new roman",14,"bold")).place(x=50,y=140)
        Label(Cre_frames,text="Amount",bg="white",fg="black",font=("times new roman",14,"bold")).place(x=50,y=210)
        Label(Cre_frames,text="Total Balance",bg="white",fg="black",font=("times new roman",14,"bold")).place(x=50,y=260)
        C1=Entry(Cre_frames,font=("times new roman",14,"bold"))
        C1.place(x=250,y=65)
        C2=Entry(Cre_frames,font=("times new roman",14,"bold"))
        C2.place(x=250,y=145)
        C3=Entry(Cre_frames,font=("times new roman",14,"bold"))#amt
        C3.place(x=250,y=215)

        def toacc():                
            sql_statement="INSERT INTO user_detail (dTo_Account) values (%s)"
            values=(C2.get())
            my_database.execute(sql_statement,values)
            db_connection.commit()
       
        def Cre_amt():
            Crt_amt=C3.get()
            Crt_amt= int(Crt_amt)
            sql_statement="SELECT Initial_Balance FROM user_detail"
            my_database.execute(sql_statement)
            output=my_database.fetchall()
            print(output[0])
            a=output[0]
            b=a[0]
            b= int(b)
            

            Label(Cre_frames,text=b+Crt_amt,bg="white",fg="red",font=("times new roman",15,"bold")).place(x=250,y=260)      
        button=Tk.Button(Cre_frames,command=Cre_amt,relief=FLAT,text="Send",fg="white",bg="blue",font=("times new roman",18,"bold")).place(x=200,y=310)
        button=Tk.Button(Cre_frames,command=toacc and Cre_frames.destroy,relief=FLAT,text="close",fg="white",bg="blue",font=("times new roman",16,"bold")).place(x=350,y=310)           
      
#....pay number...............................................................................................................
    def Num(): 
    
        Nu_frames=LabelFrame(hp_frames,highlightbackground="black",highlightthickness=2,bg="white",fg="red",font=("times new roman",20,"bold"))
        Nu_frames.pack(fill="both", expand="yes", padx=150, pady=70)
        Label(Nu_frames,text="PAY ON NUMBER",bg="white",fg="black",fon=("times new roman",14,"underline")).place(x=170,y=10)
        Label(Nu_frames,text="Receiver Mobile Number",bg="white",fg="black",font=("times new roman",14,"bold")).place(x=30,y=60)
        Label(Nu_frames,text="Amount",bg="white",fg="black",font=("times new roman",14,"bold")).place(x=30,y=110)
        Label(Nu_frames,text="Total Balance",bg="white",fg="black",font=("times new roman",14,"bold")).place(x=30,y=170)
        n1=Entry(Nu_frames,font=("times new roman",14,"bold"))
        n1.place(x=250,y=65)
        n2=Entry(Nu_frames,font=("times new roman",14,"bold"))
        n2.place(x=250,y=115)

        def pnum():
            nu_amt=n2.get()
            nu_amt= int(nu_amt)
            sql_statement="SELECT Initial_Balance FROM user_detail"
            my_database.execute(sql_statement)
            output=my_database.fetchall()
            print(output[0])
            a=output[0]
            b=a[0]
            b= int(b)
            
            Label(Nu_frames,text=b-nu_amt,bg="white",fg="red",font=("times new roman",15,"bold")).place(x=250,y=170)      
        button=Tk.Button(Nu_frames,command=pnum,text="Send",relief=FLAT,fg="white",bg="blue",font=("times new roman",18,"bold")).place(x=200,y=310)
        button=Tk.Button(Nu_frames,command=Nu_frames.destroy,text="close",relief=FLAT,fg="white",bg="blue",font=("times new roman",16,"bold")).place(x=400,y=310)           
    
#....My account .........................................................................................................
    def feed():
        feed_frames=LabelFrame(hp_frames,highlightbackground="black",highlightthickness=2,bg="white",fg="red",font=("times new roman",20,"bold"))
        feed_frames.pack(fill="both", expand="yes", padx=260, pady=180)
        Label(feed_frames,text="Feed Back",fg="Green",bg="white",font=("times new roman",15,"underline")).place(x=90,y=10)
        fb1=ttk.Combobox(feed_frames,width=28,state="readonly")
        fb1['values']=("Very Good","Good","Improve","Bad")
        fb1.place(x=50,y=40)
        fbutton=Tk.Button(feed_frames,command=feed_frames.destroy,text="send",relief=FLAT,bg="red",fg="black",font=("times new roman",15,"bold")).place(x=100,y=100)
    def contact():
        c_frames=LabelFrame(hp_frames,highlightbackground="black",highlightthickness=2,bg="white",fg="red",font=("times new roman",20,"bold"))
        c_frames.pack(fill="both", expand="yes", padx=260, pady=180)
        Label(c_frames,text="Contact us",fg="Blue",bg="white",font=("times new roman",15,"underline")).place(x=80,y=20)
        Label(c_frames,text="Toll Free -- 9361413159",fg="green",bg="white",font=("times new roman",15,"underline")).place(x=20,y=60)
        cbutton=Tk.Button(c_frames,command=c_frames.destroy,bg="red",fg="black",relief=FLAT,text="back",font=("times new roman",15,"bold")).place(x=80,y=90)
#--------------------------------account statement-----------------------------------------------------------------------------

    def state():
        s_frames=LabelFrame(hp_frames,highlightbackground="black",highlightthickness=2,bg="white",fg="red",font=("times new roman",20,"bold"))
        s_frames.pack(fill="both", expand="yes", padx=20, pady=70)
        Label(s_frames,text="ACCOUNT STATEMENT",bg="white",fg="black",fon=("times new roman",14,"underline")).place(x=250,y=0)
        Label(s_frames,text="Account Number",bg="white",fg="black",font=("times new roman",14,"bold")).place(x=10,y=50)
        Label(s_frames,text="To Account Number",bg="white",fg="black",font=("times new roman",14,"bold")).place(x=200,y=50)
        Label(s_frames,text="Debit",bg="white",fg="black",font=("times new roman",14,"bold")).place(x=400,y=50)
        Label(s_frames,text="Credit",bg="white",fg="black",font=("times new roman",14,"bold")).place(x=500,y=50)
        Label(s_frames,text="Total Balance",bg="white",fg="black",font=("times new roman",14,"bold")).place(x=585,y=50)
        button=Tk.Button(s_frames,command=s_frames.destroy,text="close",relief=FLAT,fg="white",bg="blue",font=("times new roman",16,"bold")).place(x=300,y=310) 
        def anum():
            sql_statement="SELECT Account_number,Initial_Balance FROM user_detail"
            my_database.execute(sql_statement)
            output=my_database.fetchall()
            print(output[0])
            a=output[0]
            b=a[0]
            print(output[0])
            c=output[0]
            d=c[1]        
            Label(s_frames,text=b,bg="white",fg="red",font=("times new roman",15,"bold")).place(x=10,y=100)
            Label(s_frames,text=6384111238,bg="white",fg="red",font=("times new roman",15,"bold")).place(x=200,y=100)
            Label(s_frames,text=d,bg="white",fg="red",font=("times new roman",15,"bold")).place(x=585,y=100)
        button=Tk.Button(s_frames,command=anum ,text="Send",fg="white",bg="blue",relief=FLAT,font=("times new roman",18,"bold")).place(x=200,y=310)
        button=Tk.Button(s_frames,command=s_frames.destroy,text="close",fg="white",bg="blue",relief=FLAT,font=("times new roman",16,"bold")).place(x=400,y=310)               
#..mb.ft..............................................................................................................
    ft=Menubutton(hp_frames,text="Fund Transfer",bg="#3C6478",fg="white",font=('times new roman',20,'bold'))
    ft.menu=Menu(ft,tearoff=0)
    ft['menu']=ft.menu
    PVar=IntVar()
    wVar=IntVar()
    cVar=IntVar()
    DVar=IntVar()
    ft.menu.add_checkbutton(label='Pay ',command=credit,variable=PVar)
    ft.menu.add_separator()
    ft.menu.add_checkbutton(label='Deposit ',command=Credits,variable=DVar)
    ft.menu.add_separator()
    ft.menu.add_checkbutton(label='Withdraw',command=debit,variable=wVar)
    ft.menu.add_separator()
    ft.menu.add_checkbutton(label='Pay Phone Number',command=Num,variable=cVar)
    ft.place(x=185,y=0)
#..mb.MY ACCOUNT.......................................................................................................
    ma=Menubutton(hp_frames,text="My Account",bg="#3C6478",fg="white",font=('times new roman',20,'bold'))
    ma.menu=Menu(ma,tearoff=0)
    ma['menu']=ma.menu
    pVar=IntVar()
    fVar=IntVar()
    cVar=IntVar()
    ma.menu.add_checkbutton(label='PROFILE',command=details,variable=pVar)
    ma.menu.add_separator()
    ma.menu.add_checkbutton(label='Feedback',command=feed,variable=fVar)
    ma.menu.add_separator()
    ma.menu.add_checkbutton(label='Contact us',command=contact,variable=cVar)
    ma.place(x=20,y=0)
#..acc state.............................................................................................
    acs=Menubutton(hp_frames,text="Bank Statement",bg="#3C6478",fg="white",font=('times new roman',20,'bold'))
    acs.menu=Menu(acs,tearoff=0)
    acs['menu']=acs.menu
    pVar=IntVar()
    fVar=IntVar()
    acs.menu.add_checkbutton(label='Account Holder Details',command=hold,variable=pVar)
    acs.menu.add_separator()
    acs.menu.add_checkbutton(label='Account Statement',command=state,variable=fVar)
    acs.menu.add_separator()
    acs.place(x=380,y=0)        
#............................................logpage.......................................................................
root=tkinter.Tk()
root.title("LOG IN")
imggs = Image.open("fg.webp")
imgs= ImageTk.PhotoImage(imggs)

img2=Label(root,image = imgs)
img2.place(x=0,y=0)
Label(root,text="ISAB BANK OF INDIA",bg="sky blue",fg="black",font=("Garamond",36,"underline")).place(x=250,y=30)
root.geometry("1366x768")

label_frame=LabelFrame(root,font=("times new roman",20,"bold")).place(x=200,y=200)
imgg = Image.open("logs.png")
img= ImageTk.PhotoImage(imgg)
img2=Label(root,image = img)
img2.place(x=250,y=100)

#......entry box..............................................................................................................
u1=Entry(root,width="16",font=("times new roman",19,"bold"))
u1.place(x=425,y=290)
u2=Entry(root,width="16",font=("times new roman",19,"bold"))
u2.place(x=425,y=340)
user=u1
passs=u2

def log():
    if u1.get()=="a" and u2.get()=="5":
         messagebox.showinfo("Login","Login Succesfully") and mp()
    else:
        messagebox.showinfo("login","check details")
#................................................account opening ..........................................................................................................            
button=Tk.Button(root,command=log ,font=("times new roman",15,"bold"),fg="black",text="LOGIN",bg="pink",width="20").place(x=385,y=390)
button=Tk.Button(root,command=Acc,font=("times new roman",15,"bold"),text="CREATE ACCOUNT",bg="#16558F",fg="black",width="20").place(x=385,y=445)
root.mainloop()
