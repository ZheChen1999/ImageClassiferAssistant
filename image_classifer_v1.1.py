from tkinter import *
import cv2 as cv
from PIL import Image, ImageTk
import os
from PIL import ImageTk
import PIL
from tkinter import *
import time
from sys import platform
from tkinter import *
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from PIL.ImageTk import PhotoImage

def pos_or_neg_or_unknow():
    num = var.get()
    #print(var.get())
    if num == 'A':
        l.config(text='This is positive sample')
    elif num  == 'B':
        l.config(text='This is negative sample' )
    elif num  == 'C':
        l.config(text='This is Unknow sample' )

    return var.get()

global dataset_image_filename
global img_path1
global img_path2
global img_path3
global total_image_num
def get_dataset_dir():
    global dataset_image_filename
    global dataset_dir
    global img_path1
    global img_path2
    global img_path3
    global number_image
    global dataset_image_filename
    global dataset_dir
    global flag_get_dir
    global total_image_num
    which_class = pos_or_neg_or_unknow()
    var = e.get()
    #print(var)
    dataset_dir = var
    dataset_image_filename = [x for x in os.listdir(dataset_dir) if x.endswith(".jpg")]  #
    img_path1 = dataset_dir + dataset_image_filename[number_image-1]
    img_path2 = dataset_dir + dataset_image_filename[number_image]
    img_path3 = dataset_dir + dataset_image_filename[number_image+1]
    flag_get_dir = 1
    total_image_num = len(dataset_image_filename)
    label1_text = "Total: " + str(total_image_num) + " images"
    l1.config(text=label1_text)
    # print(exists(img_path1))
    #print(dataset_image_filename)

global flag_get_dir

def button1():
    global img_path1
    global img_path2
    global img_path3
    global number_image
    global dataset_image_filename
    global dataset_dir
    global flag_get_dir
    which_class = pos_or_neg_or_unknow()
    image = PIL.Image.open(img_path2)
    print(img_path2.split('/')[-1])
    if img_path2.split('/')[-1]  in dataset_image_filename:
        if True:
            if which_class == "A":
                img_save_path2 = "Pos_sample/" + dataset_image_filename[number_image]
            elif which_class == "B":
                img_save_path2 = "Neg_sample/" + dataset_image_filename[number_image]
            elif which_class == "C":
                img_save_path2 = "Unknow_sample/" + dataset_image_filename[number_image]
            else:
                img_save_path2 = "Unknow_sample/" + dataset_image_filename[number_image]


        image.save(img_save_path2)
        dataset_image_filename.pop(number_image)
        print(which_class)
    flag_get_dir = 1

    process_image_num = total_image_num - len(dataset_image_filename)
    label1_text = "Total: " + str(total_image_num) + " images; " + '\n' + "Processed: " + str(process_image_num) + " images;" + '\n' + "Remain: " + str(len(dataset_image_filename)) + " images;"
    l1.config(text=label1_text)

def button2():
    global img_path1
    global img_path2
    global img_path3
    global number_image
    global dataset_image_filename
    global dataset_dir
    if number_image < len(dataset_image_filename)-2:
        number_image = number_image + 1
    else:
        number_image = 0
    if len(dataset_image_filename) == 2 or len(dataset_image_filename) == 1:
        img_path1 = dataset_dir + dataset_image_filename[number_image]
        img_path2 = dataset_dir + dataset_image_filename[number_image]
        img_path3 = dataset_dir + dataset_image_filename[number_image]
    elif len(dataset_image_filename) > 2:
        img_path1 = dataset_dir + dataset_image_filename[number_image-1]
        img_path2 = dataset_dir + dataset_image_filename[number_image]
        img_path3 = dataset_dir + dataset_image_filename[number_image+1]
    elif len(dataset_image_filename) == 0:
        img_path1 = "APM.JPG"
        img_path2 = "APM.JPG"
        img_path3 = "APM.JPG"

def button3():
    global img_path1
    global img_path2
    global img_path3
    global number_image
    global dataset_image_filename
    global dataset_dir
    if number_image > 2:
        number_image = number_image - 1
    else:
        number_image = len(dataset_image_filename) - 2
    if len(dataset_image_filename) == 2 or len(dataset_image_filename) == 1:
        img_path1 = dataset_dir + dataset_image_filename[number_image]
        img_path2 = dataset_dir + dataset_image_filename[number_image]
        img_path3 = dataset_dir + dataset_image_filename[number_image]
    elif len(dataset_image_filename) > 2:
        img_path1 = dataset_dir + dataset_image_filename[number_image-1]
        img_path2 = dataset_dir + dataset_image_filename[number_image]
        img_path3 = dataset_dir + dataset_image_filename[number_image+1]
    elif len(dataset_image_filename) == 0:
        img_path1 = "APM.JPG"
        img_path2 = "APM.JPG"
        img_path3 = "APM.JPG"

import pyimage
from os.path import exists
from shutil import copy, rmtree
flag_get_dir = 0
if __name__=="__main__":

    dataset_dir = ''
    dataset_image_filename = [ ]
    # ????????????
    window_width = 1000
    window_height = 1000

    image_width = int(window_width * 0.3)
    image_height = int(window_height * 0.3)
    imagepos_x = int(window_width * 0.05)
    imagepos_y = int(window_height * 0.5)

    image1_width = int(window_width * 0.5)
    image1_height = int(window_height * 0.5)
    imagepos1_x = int(window_width * 0.4)
    imagepos1_y = int(window_height * 0.4)

    image2_width = int(window_width * 0.3)
    image2_height = int(window_height * 0.3)
    imagepos2_x = int(window_width * 0.95)
    imagepos2_y = int(window_height * 0.5)

    butpos1_x = 1500
    butpos1_y = 500

    butpos2_x = 1500
    butpos2_y = 600

    butpos3_x = 1500
    butpos3_y = 700

    top = Tk()
    top.wm_title("Image Classifer @APM")
    top.geometry(str(window_width) + 'x' + str(window_height))

    # image2 =Image.open('APM.jpg')
    # background_image = ImageTk.PhotoImage(image2)
    icon = PhotoImage(file="APM.jpg")
    top.call('wm', 'iconphoto', top._w, icon)
    # ????????????
    window_width = 1000
    window_height = 1000
    top.geometry(str(window_width) + 'x' + str(window_height))

    var = StringVar()
    l = Label(top, bg='yellow', width=40, text='Which is class')
    l.pack()

    # text????????????????????????????????????Option A, ?????????Option A???????????????var?????????value??????A???
    r1 = Radiobutton(top, text='Positive sample', variable=var, value='A', command=pos_or_neg_or_unknow)
    r1.place(x=1000, y=700)
    r1.pack()

    r2 = Radiobutton(top, text='Negative sample', variable=var, value='B', command=pos_or_neg_or_unknow)
    r2.place(x=1000, y=800)
    r2.pack()

    r3 = Radiobutton(top, text='Unknow sample', variable=var, value='C', command=pos_or_neg_or_unknow)
    r3.place(x=1000, y=900)
    r3.pack()

    # Entry(??????)
    # ???1???
    # ??????????????????????????????show='*'
    # ???2?????????Entry??????window??????
    dataset_image_filename = []
    # ???3????????????button
    b = Button(top, text="get dataset directory", width=20, height=1, command=get_dataset_dir)
    b.place(x=1000, y=1000)
    b.pack()  # ???button??????label???????????????
    e = Entry(top, show=None)
    e.pack()

    # ???????????? ??????  ?????????
    canvas = Canvas(top, bg='white', width=image_width, height=image_height)  # ????????????
    canvas.place(x=imagepos_x, y=imagepos_y)

    canvas1 = Canvas(top, bg='white', width=image1_width, height=image1_height)  # ????????????
    canvas1.place(x=imagepos1_x, y=imagepos1_y)

    canvas2 = Canvas(top, bg='white', width=image2_width, height=image2_height)  # ????????????
    canvas2.place(x=imagepos2_x, y=imagepos2_y)

    l1 = Label(top, bg='yellow', anchor= 's' , width=40, text='total:')
    #l1.place(x = imagepos1_x , y = imagepos1_y * 2)
    l1.pack()

    # ????????????
    b1 = Button(top, text='Save picture', width=15, height=2, command=button1)
    b1.place(x=butpos1_x, y=butpos1_y)

    b2 = Button(top, text='Next Picture', width=15, height=2, command=button2)
    b2.place(x=butpos2_x, y=butpos2_y)

    b3 = Button(top, text='Preview Picture', width=15, height=2, command=button3)
    b3.place(x=butpos3_x, y=butpos3_y)

    if os.path.exists("Pos_sample"):
        # ???????????????????????????????????????????????????????????????
        rmtree("Pos_sample")
    os.makedirs("Pos_sample")
    if os.path.exists("Neg_sample"):
        # ???????????????????????????????????????????????????????????????
        rmtree("Neg_sample")
    os.makedirs("Neg_sample")
    if  os.path.exists("Unknow_sample"):
        # ???????????????????????????????????????????????????????????????
        rmtree("Unknow_sample")
    os.makedirs("Unknow_sample")

    number_image = 0
    #dataset_dir = "posSamples/"
    #dataset_image_filename = [x for x in os.listdir(dataset_dir) if x.endswith(".jpg")]  # ?????????????????????jpg??????????????????
    #global flag_get_dir
    #flag_get_dir = 0

    #print("out " + str(flag_get_dir))
    while  True:
        #print(flag_get_dir)
        if flag_get_dir == 1:
            if  len(dataset_image_filename) == 2 or len(dataset_image_filename) == 1:
                img_path1 = dataset_dir + dataset_image_filename[number_image]
                img_path2 = dataset_dir + dataset_image_filename[number_image]
                img_path3 = dataset_dir + dataset_image_filename[number_image]
            elif len(dataset_image_filename) >= 3:
                img_path1 = dataset_dir + dataset_image_filename[number_image-1]
                img_path2 = dataset_dir + dataset_image_filename[number_image]
                img_path3 = dataset_dir + dataset_image_filename[number_image+1]
            elif len(dataset_image_filename) == 0:
                img_path1 = "APM.JPG"
                img_path2 = "APM.JPG"
                img_path3 = "APM.JPG"
            #print(flag_get_dir)
            tkImage1 = ImageTk.PhotoImage(file=img_path1)
            canvas.create_image(0, 0, anchor='nw', image=tkImage1)

            tkImage2 = ImageTk.PhotoImage(file=img_path2)
            canvas1.create_image(0, 0, anchor='nw', image=tkImage2)

            tkImage3 = ImageTk.PhotoImage(file=img_path3)
            canvas2.create_image(0, 0, anchor='nw', image=tkImage3)

        top.update()

    top.update()

    top.mainloop()
