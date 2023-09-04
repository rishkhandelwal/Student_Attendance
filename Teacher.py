from login import *
def window3():
    
    def marking():
        df = pd.read_csv("CSV_files//attendance.csv")
        df.loc[:,"ATTENDANCE"] = 0 # default attendance value (absent)
        df.to_csv("CSV_files//attendance.csv",mode = 'w', index=False)

        def assure_path_exists(path): #if path not exists create path
            dir = os.path.dirname(path)
            if not os.path.exists(dir):
                os.makedirs(dir)

        
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        assure_path_exists("trainer/")
        recognizer.read('trainer/trainer.yml')
        cascadePath = "haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(cascadePath)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cam = cv2.VideoCapture(0)

        while True:
            # Read the video frame
            ret, im =cam.read()

            # Convert the captured frame into grayscale
            gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

            # Get all face from the video frame
            faces = faceCascade.detectMultiScale(gray, 1.2,5)

            # For each face in faces
            for(x,y,w,h) in faces:

                # Create rectangle around the face
                cv2.rectangle(im, (x-20,y-20), (x+w+20,y+h+20), (0,255,0), 4)

                # Recognize the face belongs to which ID
                Id, confidence = recognizer.predict(gray[y:y+h,x:x+w])

                if confidence>80: 
                    continue
                else:
                    imgdict = dict()
                    df = pd.read_csv("CSV_files//attendance.csv")
                    #Names and Ids as imgdict
                    diction = dict(df.loc[:,'NAME']) #making dict from ID and NAME columns
                    imgdict = {}
                    for key,vals in diction.items():
                        imgdict[key+1] = vals

                    # Check the ID if exist 
                    for k,v in imgdict.items(): #looping through all keys
                        # print(k, type(k), v)
                        if (k==Id): 
                            Id = v #if key is matched with recognizer Id , then assign Id=valueofimgdict
                            df.loc[k-1,"ATTENDANCE"]= 1  #student is present
                            df.to_csv("CSV_files//attendance.csv",mode = 'w', index=False)

                    # Put text describe who is in the picture
                    cv2.rectangle(im, (x-22,y-90), (x+w+22, y-22), (0,255,0), -1) #-1-->filled rectangle
                    cv2.putText(im, str(Id), (x,y-40), font, 1, (255,255,255), 3) #1 is size , 3 is thickness

            # Display the video frame with the bounded rectangle
            cv2.imshow('im',im) 

            # If 'q' is pressed, close program
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

        # Stop the camera
        cam.release()

        # Close all windows

        cv2.destroyAllWindows()


    
    def enter_new_student():
        def training():
            def assure_path_exists(path):
                dir = os.path.dirname(path)
                if not os.path.exists(dir):
                    os.makedirs(dir)

            # Create Local Binary Patterns Histograms for face recognization
            recognizer = cv2.face.LBPHFaceRecognizer_create()

            # Using prebuilt frontal face training model, for face detection
            detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml");

            # Create method to get the images and label data
            def getImagesAndLabels(path):

                # Get all file path
                imagePaths = [os.path.join(path,f) for f in os.listdir(path)] 
                #Python method listdir() returns a list containing the names of the entries in the directory given by path.Here path="dataSet"
                #print(os.listdir(path)) #['User1.1.jpg', 'User1.10.jpg', 'User1.11.jpg', 'User1.12.jpg',...]
                #print(imagePaths) #['dataSet\\User1.1.jpg', 'dataSet\\User1.10.jpg', 'dataSet\\User1.11.jpg',...]

                # Initialize empty face sample
                faceSamples=[]

                # Initialize empty id
                ids = []

                # Loop all the file path
                for imagePath in imagePaths:

                    # Get the image and convert it to grayscale
                    PIL_img = Image.open(imagePath).convert('L')

                    # PIL image to numpy array
                    img_numpy = np.array(PIL_img,'uint8')

                    # Get the image id
                    id = int(os.path.split(imagePath)[-1].split(".")[1])
                    # print(os.path.split(imagePath)[-1])
                    #OUTPUT
                    # User1.1.jpg
                    # User1.10.jpg
                    # User1.11.jpg
                    # User1.12.jpg
                    # User1.13.jpg

                    # Get the face from the training images
                    faces = detector.detectMultiScale(img_numpy)

                    # Loop for each face, append to their respective ID
                    for (x,y,w,h) in faces:

                        # Add the image to face samples
                        faceSamples.append(img_numpy[y:y+h,x:x+w])

                        # Add the ID to IDs
                        ids.append(id)

                # Pass the face array and IDs array
                return faceSamples,ids

            # Get the faces and IDs
            faces,ids = getImagesAndLabels('dataset')

            # Train the model using the faces and IDs
            recognizer.train(faces, np.array(ids))

            # Save the model into trainer.yml
            assure_path_exists('trainer/')
            recognizer.save('trainer/trainer.yml')
            messagebox.showinfo("Message","Training Done!")
            
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
        
        def insert_student(a,b,c):
            
            with open('CSV_files//attendance.csv', 'r') as f:
                reader = csv.reader(f)
                list2 = list(reader)
            f.close()
            flag1 = 1
            flag2 = 1
            flag3 = 1
            flag4 = 1
            flag5 = 1
            flag6 = 1
            inflag = 0
            if a=="" or b=="" or c=="":
                messagebox.showinfo("message",'Fill Complete form')
                flag1 = 0
            else:
                for i in list2:
                    if(a!=i[0]):
                        pass
                    else:
                        messagebox.showinfo("message",'Id is already in use!')
                        flag4=0

                for j in list2:
                    if(b!=j[1]):
                        pass
                    else:
                        messagebox.showinfo("message",'Student name is already in use!')
                        flag5=0
                        
                for k in list2:
                    if(c!=k[2]):
                        pass
                    else:
                        messagebox.showinfo("message",'Email address already in use!')
                        flag6=0
                        
                if(a.isdigit() and ((b>='A' and b<="Z") or (b>="a" and b<="z"))):
                    pass

                else:
                    messagebox.showinfo("message",'Type undefined!')
                    flag2 = 0


                regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

                if(re.search(regex,c)):    
                    pass

                else:  
                    messagebox.showinfo("Error",'Incorrect email format, Enter again')
                    flag3 = 0

            if (flag1==1 and flag2==1 and flag3==1 and flag4==1 and flag5==1 and flag6==1):
                with open('CSV_files//attendance.csv','a', newline = '') as f:
                    data_handler1 = csv.writer(f,delimiter = ',') 
                    data_handler1.writerow([a,b,0,c])
                    messagebox.showinfo("message","Record Entered!")
                
        def open_cam(a,b,c):
            if a=="" and b=="" and c=="":
                messagebox.showinfo("message","Fill Above Form")
            else:
                
                def assure_path_exists(path):
                    dir = os.path.dirname(path) 
                    if not os.path.exists(dir): 
                        os.makedirs(dir)
                vid_cam = cv2.VideoCapture(0)
                face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
                face_id = a
                count = 0

                assure_path_exists("dataset/")

                while(True):
                    _, image_frame = vid_cam.read()
                    '''"image_frame" will get the next frame in the camera (via "cam"). 
                    "_" will obtain return value from getting the camera frame, either true of false.'''

                    gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY) 
                    faces = face_detector.detectMultiScale(gray, 1.3, 5) #grayimage,scalefactor,minNeighbors
                    ''' scalefactor: Parameter specifying how much the image size is reduced at each image scale.'''
                    '''minNeighbors: This parameter will affect the quality of the detected faces
                    higher value results in less detections but with higher quality. We're using 5 in the code'''

                    for (x,y,w,h) in faces:
                        cv2.rectangle(image_frame, (x,y), (x+w,y+h), (255,0,0), 2)
                        count += 1
                        cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".png", gray[y:y+h,x:x+w])
                        cv2.imshow('frame', image_frame)
                    if cv2.waitKey(100) & 0xFF == ord('q'):
                        break
                    elif count>50:
                        break
                vid_cam.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Message","Dataset Collected!")



        frame0=Frame(win2,width=1050,height=700)
        frame0.place(x=300,y=1)
        frame0.tkraise()
        label0.destroy()
        font_1 = font.Font(family = 'helvetica',size = 12,weight = "bold")
        label_1 = Label(frame0,text='Enter Student ID',bg = "RoyalBlue4",fg = "white",width = 20,height = 2)
        label_1['font']= font_1
        label_2 = Label(frame0,text="Enter Student Name",bg = "RoyalBlue4",fg = "white",width = 20,height = 2)
        label_2['font'] = font_1
        label_3 = Label(frame0,text="Enter Student Email ",bg = "RoyalBlue4",fg = "white",width = 20,height = 2)
        label_3['font'] = font_1
        
        button_2 = Button(frame0,text = " CLICK HERE TO ENTER", bg = 'white', fg = 'RoyalBlue4' , width = 25, height = 1,cursor = 'hand2',command=lambda:insert_student(entry_a.get(),entry_b.get(),entry_c.get()))
        button_3 = Button(frame0,text = " TAKE STUDENT DATA ", bg = 'white', fg = 'RoyalBlue4' , width = 25, height = 1,cursor = 'hand2',command=lambda:open_cam(entry_a.get(),entry_b.get(),entry_c.get()))
        button_4 = Button(frame0,text = " TRAIN STUDENT DATA ", bg = 'white', fg = 'RoyalBlue4' , width = 25, height = 1,cursor = 'hand2',command=training)
        
        font_2 = font.Font(family = "helvetica",size = 14,weight = "bold")
        font_2.configure(underline = True)
        button_2['font'] = font_2
        button_3['font'] = font_2
        button_4['font'] = font_2
        
        entry_a = Entry(frame0)
        entry_b = Entry(frame0)
        entry_c = Entry(frame0)
        
        
        label_head = Label(frame0,text="STUDENT FORM",fg = "RoyalBlue4",width = 25,height = 2)
        label_head['font'] = font_2
        label_head.place(x=350,y=30)

        label_1.place(x=300,y=100)
        entry_a.place(x=550,y=110)

        label_2.place(x=300,y=200)
        entry_b.place(x=550,y=210)

        label_3.place(x=300,y=300)
        entry_c.place(x=550,y=310)

        button_2.place(x=350,y=400)
        button_3.place(x=350,y=500)
        button_4.place(x=350,y=600)


    def view_attendance():
        w4 =Tk()
        w4.title("Attendance Sheet")
        w4.geometry('1000x700')
        with open("CSV_files\\attendance.csv", newline = "") as file:
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
    def exit():
        win2.destroy()
    
    global label0,frame2
    win2=Tk()
    win2.title('Smart_Attendance')
    win2.geometry('1350x700+0+0')
    dashboard_frame=Frame(win2,width=300,height=800,bg='#1C2739')
    dashboard_frame.place(x=0,y=0)
    dashboard_frame.tkraise()

    image00 = PIL.Image.open('Images_Used//7.jpeg')
    image00 = image00.resize((1050,700), PIL.Image.ANTIALIAS) # (height, width)
    back_image00 = ImageTk.PhotoImage(image00)

    frame2=Frame(win2,width=1050,height=700)
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


    image = PIL.Image.open('Images_Used//T1.png')
    image = image.resize((290, 80), PIL.Image.ANTIALIAS) 
    back_image = ImageTk.PhotoImage(image)

    b1 = Button(image=back_image,command=view_attendance)
    b1.place(x=5,y=150)

    image1 = PIL.Image.open('Images_Used//T2.png')
    image1 = image1.resize((290, 80), PIL.Image.ANTIALIAS)
    back_image1 = ImageTk.PhotoImage(image1)

    b2 = Button(image=back_image1,command=enter_new_student)
    b2.place(x=5,y=250)

    image0 = PIL.Image.open('Images_Used//c3.png')
    image0 = image0.resize((290, 80), PIL.Image.ANTIALIAS)
    back_image0 = ImageTk.PhotoImage(image0)

    b4 = Button(image=back_image0,command=marking)
    b4.place(x=5,y=350)

    image2 = PIL.Image.open('Images_Used//exit.png')
    image2 = image2.resize((290, 80), PIL.Image.ANTIALIAS) 
    back_image2 = ImageTk.PhotoImage(image2)

    b3 = Button(image=back_image2,command=exit)
    b3.place(x=5,y=450)
    win2.mainloop()