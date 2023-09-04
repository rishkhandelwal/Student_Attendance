from login import *
def window2():
    def destroy():
        win1.destroy()
    def printing():
        #reading from csv and writing it in txt
        with open("CSV_files//newfile.txt", "w") as my_output_file:
            cs = pd.read_csv("CSV_files\\attendance.csv",header=None,index_col=None)
            with open("CSV_files//attendance.csv", "r") as my_input_file:
                [ my_output_file.write(" | ".join(row)+'\n') for row in csv.reader(my_input_file)]
        my_output_file.close()

        #reading from file and storing into reader and converting into string as .write() takes string
        strnew = ""
        with open('CSV_files//newfile.txt',"r") as f:
            reader = f.read()
            strnew = reader
        #for checking
        with open('CSV_files//print.txt',"w") as f:
            f.write(strnew)

        #printing
        filename = tempfile.mktemp("attendance.txt")#creating a temp file

        open (filename , "w").write(strnew)

        os.startfile(filename, "print")
        messagebox.showinfo("Print","Printing Request sent successfully!")

    def view_passwords():
        # open file
        w3 = Tk()
        w3.title("Teachers Record")
        w3.geometry('430x390')
        with open("CSV_files//users_passwords.csv", newline = "") as file:
            reader = csv.reader(file)
            # r and c tell us where to grid the labels
            r = 20
            for col in reader:
                c = 20
                for row in col:
                    label = Label(w3, width = 30, height = 2, \
                                       text = row, relief = RIDGE)
                    label.grid(row = r, column = c)

                    c += 1
                r += 1
        w3.mainloop()

    def view_attendance():
        w4 =Tk()
        w4.title("Attendance Sheet")
        w4.geometry('1000x700')

        with open("CSV_files//attendance.csv", newline = "") as file:
            reader = csv.reader(file)
            # r and c tell us where to grid the labels
            r = 20
            for col in reader:
                c = 20
                for row in col:
                    # i've added some styling
                    label = Label(w4, width = 30, height = 2, \
                                       text = row, relief = RIDGE)
                    label.grid(row = r, column = c)

                    c += 1
                r += 1
        w4.mainloop()

    def email_sent():
        with open("CSV_files//attendance.csv",newline="") as f:
            reader = csv.reader(f)
            emailid = {}
            absent = []
            for col in reader:
                if col[3] == "" or col[3]=='EMAIL':
                    pass
                else:
                    emailid.update({col[3]:col[2]})
        print(emailid)

        for e_id,atte in emailid.items():
            if atte=="0":
                absent.append(e_id)
        print(absent)

        for absent_email in absent:
            receiver = absent_email
            try:
                content = """Subject: Class Attendance
                Dear Student,You are absent today"""
                mail = smtplib.SMTP('smtp.gmail.com',587) #server,port->465 or 587
                mail.ehlo() #identify yourself to the server ehlo for extended smtp
                mail.starttls() #encrypted
                #first make your email less secure from this link https://myaccount.google.com/u/2/lesssecureapps
                mail.login('premkumar609461@gmail.com','vafhcbvstwcgglnx')  #enter your email address and password here
                mail.sendmail('premkumar609461@gmail.com',receiver,content) #send mail #from,to,content
                mail.close() #closing the connection
                print("Email Sent successfully")
                # email.mime.text to include subject line
            except:
                print("Email failed to send")
        messagebox.showinfo("Email Info","Email Sent Successfully!")

    def enter_new_record(a,b):
        with open('CSV_files//users_passwords.csv', 'r') as f:
            reader = csv.reader(f)
            list1 = list(reader)

        flag1 = 1
        flag2 = 1
        flag3 = 1
        flag4 = 1

        if a=="" or b=="":
                messagebox.showinfo("message",' Fill Complete form')
                flag1 = 0
        else:
            for i in list1:
                if(a!=i[0]):
                    pass
                else:
                    messagebox.showinfo("message",'Username is already in use!')
                    flag3=0

            for j in list1:
                if(b!=j[1]):
                    pass
                else:
                    messagebox.showinfo("message",'Use another password!')
                    flag4=0

            if ((a>='A' and a<="Z") or (a>="a" and a<="z")):
                pass
            else:
                messagebox.showinfo("message",'Type undefined!')
                flag2 = 0


        if (flag1==1 and flag2==1 and flag3 == 1 and flag4 ==1):
            with open('CSV_files//users_passwords.csv','a', newline = '') as f:
                data_handler1 = csv.writer(f,delimiter = ',')
                data_handler1.writerow([a,b])
                messagebox.showinfo("message",'New record entered')

                # framea.destroy()
            for widget in framea.winfo_children():
                  widget.destroy()

        img = Image.open('Images_Used//7.jpeg')
        img = img.resize((1050,700), PIL.Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        label_ = Label(image = img)
        label_.place(x=300,y=1)
        w = Tk()
        w.overrideredirect(1)
        w.withdraw()
        w.mainloop()
        w.destroy()

    def new_record():
        global framea
        framea=Frame(win1,width=1050,height=700)
        framea.place(x=300,y=1)
        framea.tkraise()
        label0.destroy()
        global entry_1,entry_2
        font_1 = font.Font(family = 'helvetica',size = 12,weight = "bold")
        label_1 = Label(framea,text='Enter Teacher Name',bg = "RoyalBlue4",fg = "white",width = 20,height = 2)
        label_1['font']= font_1
        label_2 = Label(framea,text="Enter Password",bg = "RoyalBlue4",fg = "white",width = 20,height = 2)
        label_2['font'] = font_1
        button_2 = Button(framea,text = " CLICK HERE TO ENTER", bg = 'RoyalBlue4', fg = 'white' , width = 25, height = 1,cursor = 'hand2',command=lambda:enter_new_record(entry_1.get(),entry_2.get()))
        font_2 = font.Font(family = "helvetica",size = 14,weight = "bold")
        font_2.configure(underline = True)
        button_2['font'] = font_2
        entry_1 = Entry(framea)
        entry_2 = Entry(framea,show="*")

        label_head = Label(framea,text="TEACHER'S ENTRY",fg = "RoyalBlue4",width = 50,height = 5)
        label_head['font'] = font_2

        label_head.place(x=190,y=100)

        label_1.place(x=300,y=250)
        entry_1.place(x=550,y=260)

        label_2.place(x=300,y=350)
        entry_2.place(x=550,y=360)

        button_2.place(x=350,y=460)

    global win1
    win1=Tk()
    win1.title('Smart_Attendance')
    win1.geometry('1350x700+0+0')
    dashboard_frame=Frame(win1,width=300,height=800,bg='#1C2739')
    dashboard_frame.place(x=0,y=0)
    dashboard_frame.tkraise()

    image00 = PIL.Image.open('Images_Used//7.jpeg')
    image00 = image00.resize((1050,700), PIL.Image.ANTIALIAS) # (height, width)
    back_image00 = ImageTk.PhotoImage(image00)

    frame2=Frame(win1,width=1050,height=700)
    frame2.place(x=300,y=1)
    frame2.tkraise()

    label0=Label(image=back_image00)
    label0.place(x=300,y=1)


    img1=PhotoImage(file='Images_Used//divider-logo.png')
    img0=PhotoImage(file='Images_Used//dashboard-logo.png')



    dashboard_label = Label(image=img0, bg='#1C2739')
    dashboard_label.place(x=5, y=3)
    divider_logo = Label(image=img1, bg='#1C2739')
    divider_logo.place(x=5, y=50)

    font_1 = font.Font(family = 'helvetica',size = 12,weight = "bold")


    image = PIL.Image.open('Images_Used//2.jpeg')
    image = image.resize((290, 80), PIL.Image.ANTIALIAS)
    back_image = ImageTk.PhotoImage(image)

    b1 = Button(image=back_image,command = view_attendance)
    b1.place(x=5,y=100)

    image1 = PIL.Image.open('Images_Used//3.jpeg')
    image1 = image1.resize((290, 80), PIL.Image.ANTIALIAS)
    back_image1 = ImageTk.PhotoImage(image1)

    b2 = Button(image=back_image1,command=view_passwords)
    b2.place(x=5,y=200)

    image2 = PIL.Image.open('Images_Used//4.jpeg')
    image2 = image2.resize((290, 80), PIL.Image.ANTIALIAS)
    back_image2 = ImageTk.PhotoImage(image2)

    b3 = Button(image=back_image2,command=new_record)
    b3.place(x=5,y=300)


    image3 = PIL.Image.open('Images_Used//5.jpeg')
    image3 = image3.resize((290, 80), PIL.Image.ANTIALIAS)
    back_image3 = ImageTk.PhotoImage(image3)

    b4 = Button(image=back_image3,command=email_sent)
    b4.place(x=5,y=400)


    image4 = PIL.Image.open('Images_Used//6.jpeg')
    image4 = image4.resize((290, 80), PIL.Image.ANTIALIAS)
    back_image4 = ImageTk.PhotoImage(image4)

    b5 = Button(image=back_image4,command=printing)
    b5.place(x=5,y=500)

    image5 = PIL.Image.open('Images_Used//exit.png')
    image5 = image5.resize((290, 80), PIL.Image.ANTIALIAS)
    back_image5 = ImageTk.PhotoImage(image5)

    b6 = Button(image=back_image5,command=destroy)
    b6.place(x=5,y=600)
    win1.mainloop()
