######### ADD title FRAME 0

import tkinter as tk
from PIL import ImageTk,Image
from tkinter import ttk
from Cancer_mode import *

###################################
###### ML based work #############
df=get_df()


def show_frame(frame):
    frame.tkraise()

def the_last_frame(a,values):
    frame4 = tk.Frame(window, bg="pink")
    frame4.grid(row=0, column=0, sticky='nsew')
    bg4 = ImageTk.PhotoImage(Image.open('bg5.jpg'))
   # bg5 = ttk.Label(frame4, image=bg5).place(x=0, y=0, relwidth=1, relheight=1)
    l1_f4 = tk.Label(frame4, text='YOUR RESULTS ARE:', font=t1, bg='pink').grid(row=0, column=0)
    #l2_f4=tk.Label(frame4,text='Diagnosis:').grid(row=1,column=0)

    pred = getpred()
    df=get_df()

    for x in range(len(a)):
        pred[a[x]] = values[x]

    df2 = df.astype(float).values.tolist()
    random.shuffle(df2)
    pred = pred.astype(float).values.tolist()
    df_set = {0.0: [], 1.0: []}
    for i in df2:
        df_set[i[-1]].append(i[:-1])
    global result
    result = k_nearest_neighbours(df_set, pred, k=3)
    if result:
        dignosis="Malignant"
    else:
        dignosis="Benign"

    print(result)
    l2_f4 = tk.Label(frame4, text='Diagnosis: {:s}'.format(dignosis),font=('verdana',14),bg='lightblue').grid(row=1,column=1)

    accuracy=Accuracy_Indicator(df2)*100
    l3_f4 = tk.Label(frame4, text='Accuracy: {:.1f}'.format(accuracy), font=('verdana',14),bg='lightblue').grid(row=2, column=1)

    button3 = tk.Button(frame4, text="Exit", command=window.quit).grid(row=8,column=1)  # pack(side='bottom',padx=10)

    show_frame(frame4)



def val_values(to_show,e,a):
    global values
    values=[0]*len(to_show)
    l2_f3 = tk.Label(frame3)
    l2_f3.grid(row=10)
    try:
        for x in range(len(to_show)):
            values[x]=float(e[x].get())
        b=False
        for x in range(len(to_show)):
            if values[x]<0 or values[x]>5000:
                b=True
        if b:
            l2_f3.configure(text="Enter an integer value between 0 and 50000")
            for x in range(len(to_show)):
                values[x] = e[x].delete(0, 1000)
        else:
            the_last_frame(a,values)

    except:
        l2_f3.configure(text="Enter an integer value between 0 and 50000")
        for x in range(len(to_show)):
            values[x] = e[x].delete(0, 1000)



def val_id():
    try:
        global id
        id=int(e1_f1.get())

        if id <100000 or id>=1000000:
            l2_f1.configure(text="Incorrect Value, the Value must have six integer Digits", bg='red')
            e1_f1.delete(0, 1000)

        else:
            show_frame(frame2)

    except ValueError:
        l2_f1.configure(text="Incorrect Value, the Value must have six integer Digits",bg='red')
        e1_f1.delete(0,1000)

# def box_value():
#     global a
#     global to_show
#     global z
#     a=[]
#     to_show=["Mean Radius","Mean Texture","Mean Perimeter","Mean smoothness","Mean Compactness","Mean Concavity","Mean Symmetry","Mean Concave Points"]
#     counter=8
#     if concavity.get()==0:
#         a.append('concavity_mean')
#         to_show.remove("Mean Concavity")
#         counter-=1
#     if Radius.get()==0:
#         a.append('radius_mean')
#         to_show.remove("Mean Radius")
#         counter -= 1
#     if Texture.get()==0:
#         a.append('texture_mean')
#         to_show.remove("Mean Texture")
#         counter -= 1
#     if Perimeter.get()==0:
#         a.append('perimeter_mean')
#         to_show.remove("Mean Perimeter")
#         counter -= 1
#     if smoothness.get()==0:
#         a.append('smoothness_mean')
#         to_show.remove("Mean smoothness")
#         counter -= 1
#     if symmetry.get()==0:
#         a.append('symmetry_mean')
#         to_show.remove("Mean Symmetry")
#         counter -= 1
#     if compactness.get()==0:
#         a.append('compactness_mean')
#         to_show.remove("Mean Compactness")
#         counter -= 1
#     if points.get()==0:
#         a.append('concave points_mean')
#         to_show.remove("Mean Concave Points")
#         counter -= 1
#
#
#     if counter==0:
#         l2_l2 = tk.Label(frame2, text="Please atleast tick one label",bg='red',font=t1).grid(row=9)
#     else:
#         df.drop(a, inplace=True, axis=1)
#         show_frame(frame3)
#         bg3 = ttk.Label(frame3, image=bg3).place(x=0, y=0, relwidth=1, relheight=1)
#         title3 = tk.Label(frame3, text="Symptom Value for Analysis via Machine Learning", bg='blue').grid(
#             row=0)  # pack(fill="both")
#
#         b1_f3 = ttk.Button(frame3, text="Enter", command=lambda: show_frame(frame4)).grid(row=8,
#                                                                                           column=0)  # pack(side='bottom')


t1=('arial',12)


window=tk.Tk()
window.grid_columnconfigure(0,weight=1) # weight is basically if there is extra space it should be occupied
window.grid_rowconfigure(0, weight=1)
window.geometry("500x300")
window.title("ML for Breast Cancer Analysis")


frame1=tk.Frame(window,bg='pink')
frame2=tk.Frame(window,bg='lightblue')
frame3=tk.Frame(window,bg='red')

for frame in (frame1,frame2,frame3):
    frame.grid(row=0,column=0,sticky="nsew")


### IMAGES IMPORTED HERE
bg=ImageTk.PhotoImage(Image.open('logo.jpg'))
bg2=ImageTk.PhotoImage(Image.open('bg3.jpg'))


################################################
###### Our first page###########################
show_frame(frame1)
bg1=ttk.Label(frame1,image=bg).place(x=0,y=0,relwidth=1,relheight=1)
l1_f1=tk.Label(frame1,text='Medical ID:',font=t1,bg='pink').grid(row=0,column=0)
e1_f1=tk.Entry(frame1,bg='pink',font=t1)
e1_f1.grid(row=0,column=1)
l2_f1=tk.Label(frame1,bg='pink',text="ID must be six integer digits")
l2_f1.grid(row=3,column=1)
b1_f1=tk.Button(frame1,bg='pink',text='Enter',font=t1,command=lambda:val_id()).grid(row=2,column=1)
#l2_f1=tk.Label(frame1,text="Please tick available symptoms:")

#l3_f1=tk.Label(frame1,text=var.get()).pack()
#b1_f1=tk.Button(frame1,text="Enter Data",command=lambda:show_frame(frame2))

#b1.grid(row=2,column=2,rowspan=20)
# l1.pack(side='top'   ,fill='both')
# e1.pack(side='left')
# l2_f1.pack(side="top")
# c1_f1.pack()
#b1_f1.pack()
#############################################################################
#############################################################################
def box_value():
    global a
    global to_show
    global z
    a=['concavity_mean','radius_mean','texture_mean','perimeter_mean','smoothness_mean','symmetry_mean','compactness_mean','concave points_mean']
    to_show=["Mean Radius","Mean Texture","Mean Perimeter","Mean smoothness","Mean Compactness","Mean Concavity","Mean Symmetry","Mean Concave Points"]
    counter=8
    if concavity.get()==0:
        a.remove('concavity_mean')
        to_show.remove("Mean Concavity")
        counter-=1
    if Radius.get()==0:
        a.remove('radius_mean')
        to_show.remove("Mean Radius")
        counter -= 1
    if Texture.get()==0:
        a.remove('texture_mean')
        to_show.remove("Mean Texture")
        counter -= 1
    if Perimeter.get()==0:
        a.remove('perimeter_mean')
        to_show.remove("Mean Perimeter")
        counter -= 1
    if smoothness.get()==0:
        a.remove('smoothness_mean')
        to_show.remove("Mean smoothness")
        counter -= 1
    if symmetry.get()==0:
        a.remove('symmetry_mean')
        to_show.remove("Mean Symmetry")
        counter -= 1
    if compactness.get()==0:
        a.remove('compactness_mean')
        to_show.remove("Mean Compactness")
        counter -= 1
    if points.get()==0:
        a.remove('concave points_mean')
        to_show.remove("Mean Concave Points")
        counter -= 1


    if counter==0:
        l2_l2 = tk.Label(frame2, text="Please atleast tick one label",bg='red',font=t1).grid(row=9)
    else:
        df.drop(a, inplace=True, axis=1)
        show_frame(frame3)
        bg3 = ImageTk.PhotoImage(Image.open('bg4.jpg'))
        bg3 = ttk.Label(frame3, image=bg3).place(x=0, y=0, relwidth=1, relheight=1)
        title3 = tk.Label(frame3, text="Symptom Value for Analysis via Machine Learning", bg='lightblue',font=t1).grid(
            row=0,sticky='ew')  # pack(fill="both")
        l=[0]*len(to_show)
        e=[0]*len(to_show)
        for x in range(len(to_show)):
            l[x]=tk.Label(frame3,text=to_show[x])
            e[x]=tk.Entry(frame3)

            l[x].grid(row=x+1,column=0)
            e[x].grid(row=x+1,column=1)

        b1_f3 = ttk.Button(frame3, text="Enter", command=lambda: val_values(to_show,e,a)).grid(row=9,
                                                                                          column=0)



#########################################################
#########################################################
############## THE SECOND PAGE ##########################

bg22=ttk.Label(frame2,image=bg2).place(x=0,y=0,relwidth=1,relheight=1)
title2=tk.Label(frame2,text="CHECK AVAILABLE SYMPTOMS",bg='lightblue',font=('Verdana',14)).grid(row=0,column=0,padx=5,pady=10)
#pack(fill="both")

# available symptoms and their analysis

Radius = tk.IntVar()
Texture=tk.IntVar()
Perimeter=tk.IntVar()
smoothness=tk.IntVar()
compactness=tk.IntVar()
concavity=tk.IntVar()
symmetry=tk.IntVar()
points=tk.IntVar()

c1_f2=tk.Checkbutton(frame2,text="Mean Radius",bg='lightblue',variable=Radius)
c2_f2=tk.Checkbutton(frame2,text="Mean Texture",bg='lightblue',variable=Texture)
c3_f2=tk.Checkbutton(frame2,text="Mean Perimeter",bg='lightblue',variable=Perimeter)
c4_f2=tk.Checkbutton(frame2,text="Mean smoothness",bg='lightblue',variable=smoothness)
c5_f2=tk.Checkbutton(frame2,text="Mean Compactness",bg='lightblue',variable=compactness)
c6_f2=tk.Checkbutton(frame2,text="Mean Concavity",bg='lightblue',variable=concavity)
c7_f2=tk.Checkbutton(frame2,text="Mean Symmetry",bg='lightblue',variable=symmetry)
c8_f2=tk.Checkbutton(frame2,text="Mean Concave Points",bg='lightblue',variable=points)

c1_f2.grid(row=1)
c2_f2.grid(row=1,column=3)#row=1,column=1,rowspan=2)
c3_f2.grid(row=3)#row=1,column=2,rowspan=2)
c4_f2.grid(row=3,column=3)#row=2,column=0,rowspan=2)
c5_f2.grid(row=5)#row=2,column=1,rowspan=2)
c6_f2.grid(row=5,column=3)#row=2,column=2,rowspan=2)
c7_f2.grid(row=7)#row=3,column=0,rowspan=2)
c8_f2.grid(row=7,column=3)#row=3,column=0,rowspan=2)
c=[]
button2=ttk.Button(frame2,text="Enter",command=lambda:c==box_value()).grid(row=8,column=0) #pack(side='bottom')


######################################################
######################################################
#### Our third page




#######################################################
########## LAST PAGE EEEEEE YOOOOOOOOOOOOOOOOOO


window.mainloop()
#

# class Cancer_app(tk.Tk): # our class is inheriting the window functionality
#       def __init__(self,*args,**kwargs):  # this will always run with our class,self is just convention
##### our second page###################################
#           tk.Tk.__init__(self,*args,**kwargs)
#           # This is the 1st of 3rd
#           f1 = tk.Frame(self)
#           l1 = tk.Label(f1,text="Page0",font=('arial',12))
#           #l1.grid()
#           l1.pack()
#           f1.pack(side='top',fill='both',expand=True)
#
#           # ekkk
#           #f1.grid_columnconfigure(0,weight=1) # weight is basically if there is extra space it should be occupied
#           #f1.grid_rowconfigure(0, weight=1)
#           #Now We Define a dictionary of possible frames for kinter
#           self.frames={}
#           for F in (StartPage,PageOne):
#               frame=F(f1,self)
#               self.frames[F]=frame
#               #frame.grid(row=0,column=0,sticky="nsew"
#               frame.pack(side='top', fill='both', expand=True)
#           self.show_frame(StartPage)
#
#
#       def show_frame(self,cont):
#           frame=self.frames[cont]
#           frame.tkraise()
# # The first page
# class StartPage(tk.Frame):
#     def __init__(self,parent,controller):
#         tk.Frame.__init__(self,parent)
#         label=tk.Label(text="Enter your ID", font=('arial',12))
#         label.pack(padx=10,pady=10)
#         e1=tk.Entry().pack(padx=5,pady=5)
#         b1=tk.Button(text="use me!!",command=lambda: controller.show_frame(PageOne))
#         b1.pack()
#
# class PageOne(tk.Frame):
#     def __init__(self,parent,controller):
#         tk.Frame.__init__(self,parent)
#     label = tk.Label(text="Enter Your Symptoms", font=('arial', 12))
#     label.pack(padx=10, pady=10)
#     b1 = tk.Button(text="GO BACK", command=lambda: controller.show_frame(StartPage))
#     b1.pack()
#
#
#
#
#
#
#
# app=Cancer_app()
# app.mainloop()





