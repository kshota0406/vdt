import tkinter as tk
import tkinter.font as font
import pyautogui
import datetime

root=tk.Tk()
root.title("VDT作業監視アプリ")
root.geometry('390x80')  
root.configure(bg='#b0e0e6')

text_min=tk.StringVar()
text_min.set("60")

text_sec=tk.StringVar()
text_sec.set("0")
my_font=font.Font(size=18)

buff_min=tk.StringVar()
buff_min.set("0")

buff_sec=tk.StringVar()
buff_sec.set("0")


text_start_stop=tk.StringVar()
text_start_stop.set("START")

info=tk.StringVar()
info.set("STARTを押してください")

start=True
check=True
stop=False

def start():
    global start,check,text_min,text_sec,start,check,stop,info
    start=False
    if check==True and stop==True:
        start=True
        text_start_stop.set("STOP")
        info.set("VDT作業監視中")
        timer()
    
    elif check==False and stop==True:
        count_min=int(buff_min.get())
        count_sec=int(buff_sec.get()) 
        buff_min.set("0")
        buff_sec.set("0")
        buff_min.set(count_min)
        buff_sec.set(count_sec)
        check=True
        text_start_stop.set("START")
        info.set("停止中")
        timer()
        
    else:
        start=True
        stop=True
        text_start_stop.set("STOP")
        buff_min.set(int(text_min.get()))
        buff_sec.set(int(text_sec.get()))
        info.set("VDT作業監視中")
        timer()
    
        

def timer():
    global start,buff_min,buff_sec,text_min,text_sec,check,position1,position2
    if start==True:
        if int(buff_min.get())==0 and int(buff_sec.get())==0:
            pass
        else:
            check=False
            time_min=int(buff_min.get())
            time_sec=int(buff_sec.get())
            text_min2=int(text_min.get())
            text_sec2=int(text_sec.get())
            if time_min>=0:
                time_sec-=1
                buff_sec.set(str(time_sec))
                root.after(1000,timer)
                if time_sec==-1:
                    time_min-=1
                    buff_min.set(str(time_min))
                    buff_sec.set("59")
                if (str(time_min)[-1])=="9" and time_sec==58:
                    position1=pyautogui.position()
                    print(datetime.datetime.now())
                    print("初期値設定")
                if (str(time_min)[-1])=="0" and time_sec==0:
                    position2=pyautogui.position()
                    if position1 == position2:
                      print(datetime.datetime.now())
                      print("-------------PC作業していません---------------------")
                      print(position1)
                      print(position2)
                      print("--------------------------------------------------")
                      buff_sec.set(str(text_sec2))
                      buff_min.set(str(text_min2))
                    elif position1 != position2:
                      print(datetime.datetime.now())
                      print("-------------PC作業中-----------------------------")
                      print(position1)
                      print(position2)
                      print("--------------------------------------------------")

            if int(buff_min.get())==0 and int(buff_sec.get())==0:
                start=False
                time_min=0
                time_sec=0
                buff_sec.set(str(time_sec))
                buff_min.set(str(time_min))
                info.set("PC連続作業が1時間経過しました")
                root.geometry('1000x1500') 
                root.attributes("-topmost", True)
                root.attributes("-topmost", False)
                
                

                

            
def stop():
    global start,check,stop
    start=True
    check=True
    stop=False
    time_min=0
    time_sec=0
    buff_sec.set(str(time_sec))
    buff_min.set(str(time_min))
    info.set("STARTを押してください")

label=tk.Label(root,text="10分マウス操作がないとタイマーがリセットされます",bg='#b0e0e6')
label.grid(row=0,column=0,columnspan=14)

label=tk.Label(root,width=30,font=my_font,bg="#fffacd",fg="#ff6347",textvariable=info)
label.grid(row=1,column=0,columnspan=14)

# label=tk.Label(root,text="設定")
# label.grid(row=2,column=0,columnspan=1)
    
# entry=tk.Entry(root,width=2,font=my_font,textvariable=text_min)
# entry.grid(row=2,column=1)

# label_min=tk.Label(root,text=u"分")
# label_min.grid(row=2,column=2)

# entry1=tk.Entry(root,width=2,font=my_font,textvariable=text_sec)
# entry1.grid(row=2,column=3)

# label_sec=tk.Label(root,text=u"秒")
# label_sec.grid(row=2,column=4)

label=tk.Label(root,text="タイマー",bg='#b0e0e6')
label.grid(row=2,column=4,columnspan=1)

label=tk.Label(root,font=my_font,textvariable=buff_min,bg='#b0e0e6')
label.grid(row=2,column=5,columnspan=1)

label=tk.Label(root,text="分",bg='#b0e0e6')
label.grid(row=2,column=6,columnspan=1)

label=tk.Label(root,font=my_font,textvariable=buff_sec,bg='#b0e0e6')
label.grid(row=2,column=7,columnspan=1)

label=tk.Label(root,text="秒",bg='#b0e0e6')
label.grid(row=2,column=8,columnspan=1)

button=tk.Button(root,bg="black",fg="white",textvariable=text_start_stop,command=start)
button.grid(row=2,column=9)

button=tk.Button(root,text=u"RESET",bg="black",fg="white",command=stop)
button.grid(row=2,column=10)


root.mainloop()