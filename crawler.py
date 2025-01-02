from crawpy import starter
import tkinter as tk
from functools import partial
from PIL import Image, ImageTk
def intrnlUrl():
    global root
    root = tk.Tk()
    root.state('zoomed')
    root.title("$$$ WEB CRAWLER $$$")
    img = Image.open("ayush.png")  
    bimg = ImageTk.PhotoImage(img) 
    biml = tk.Label(root, image=bimg)
    biml.place(x=100,y=20)
    msgenter_url=tk.Label(root,text="Here u can put your URL to fetch",font=('Constania',25),fg='Black')
    msgenter_url.place(x=root.winfo_screenwidth()/2,y=100,anchor='center')
    enter_url=tk.Label(root,text="Enter URL",font=('Arial',20),fg='black')
    enter_url.place(x=root.winfo_screenwidth()/2-100,y=175,anchor='center')
    lim=tk.Label(root,text="Enter LIMIT",font=('Arial',20),fg='black')
    lim.place(x=root.winfo_screenwidth()/2+100,y=175,anchor='center')
    furl=tk.StringVar()
    limit=tk.StringVar(value='100')
    extrn=partial(extrnlenrty,furl,limit)
    UrlE=tk.Entry(root,textvariable=furl)
    UrlE.place(x=root.winfo_screenwidth()/2-100,y=225,anchor='center')
    lm=tk.Entry(root,textvariable=limit)
    lm.place(x=root.winfo_screenwidth()/2+100,y=225,anchor='center')

    start_button=tk.Button(root,text="fetch",command=extrn,font=('Arial',15))
    start_button.place(x=root.winfo_screenwidth()/2,y=275,anchor='center')

    root.mainloop()

def extrnlenrty(url,lim=100):
    u=(url.get())
    limit=(lim.get())
    ot=starter(u,int(limit))
    fetch_url(ot)
    return 

def fetch_url(ot):
    st=len("URL not Found or Connectivity Unavaiable")
    s2="Number of URL found:"+str(ot)
    s1=len(s2)
    k=st-s1
    print('*'*int(k/2)+s2+'*'*int(k/2))
    if ot!=0:
        label2=tk.Label(root,text='*'*int(k/2)+s2+'*'*int(k/2),font=('Constantia',25),fg='Black')
        label2.place(x=root.winfo_screenwidth()/2,y=350,anchor='center')
    else:
        label2 = tk.Label(root,text="URL not Found or Connectivity Unavailable",font=('Constantia',25),fg='Red')
        label2.place(x=root.winfo_screenwidth()/2,y=350,anchor='center')   
intrnlUrl()
