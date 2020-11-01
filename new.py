from tkinter import *
import os.path
import os
from tkinter.filedialog import *
from tkinter.messagebox import showerror, showinfo
from tkinter.simpledialog import askstring
import tkinter
from tkinter import ttk
from PIL import ImageTk, Image, ImageFilter
r = tkinter.Tk()
import sys
import time
from threading import Thread
class ed:
    def __init__(self, r,fuck=None):
        self.tr = False
        self.for_list = ("*.mpeg","*.hdf5","*.grib","*.fits","*.bufr","*.xv","*.pdf","*.palm","*.xpm","*.wmf","*.wal","*.psd","*.pixar","*.pcd","*.mpo","*.mic","*.mcidas","*.naa","*.iptc","*.imt","*.gd","*.gbr","*.ftex","*.fpx","*.flc","*.fli","*.dds","*.dcx","*.cur","*.blp","*.xbm","*.webp","*.tiff","*.tga","*.spi","*.sgi","*.ppm","*.png","*.pcx","*.msp","*.jpeg","*.im","*.ico","*.icns","*.gif","*.eps","*.dib","*.bmp","*.MPEG","*.HDF5","*.GRIB","*.FITS","*.BUFR","*.XV","*.PDF","*.PALM","*.XPM","*.WMF","*.WAL","*.PSD","*.PIXAR","*.PCD","*.MPO","*.MIC","*.MCIDAS","*.NAA","*.IPTC","*.IMT","*.GD","*.GBR","*.FTEX","*.FPX","*.FLC","*.FLI","*.DDS","*.DCX","*.CUR","*.BLP","*.XBM","*.WEBP","*.TIFF","*.TGA","*.SPI","*.SGI","*.PPM","*.PNG","*.PCX","*.MSP","*.JPEG","*.IM","*.ICO","*.ICNS","*.GIF","*.EPS","*.DIB","*.BMP")
        try:
            d = os.getcwd()
            d = "/".join(d.split("\\"))
            os.mkdir(d+"/Mydir/")
        except:
            pass
        try:
            self.list.clear()
            self.n=0
        except:
            pass
        self.n=0
        r.wm_iconbitmap("C:/Users/Fedinho/Desktop/filmes/Assistidos/Deep.blue.sea.2.2018.1080p-dual-por-cinemaqualidade.to/python/BLUDV/icons/Junior Icon 28.ico")
        r.title("Image opener")
        r.configure(bg='#123058',cursor="hand2")
        if fuck == None:
             try:
                 self.fil=askopenfilenames(parent=r, initialdir='C:/Programs Files', filetypes=[("All Images",("*.MPEG","*.HDF5","*.GRIB","*.FITS","*.BUFR","*.XV","*.PDF","*.PALM","*.XPM","*.WMF","*.WAL","*.PSD","*.PIXAR","*.PCD","*.MPO","*.MIC","*.mpeg","*.hdf5","*.grib","*.fits","*.bufr","*.xv","*.pdf","*.palm","*.xpm","*.wmf","*.wal","*.psd","*.pixar","*.pcd","*.mpo","*.mic","*.mcidas","*.naa","*.iptc","*.imt","*.gd","*.gbr","*.ftex","*.fpx","*.flc","*.fli","*.dds","*.dcx","*.cur","*.blp","*.xbm","*.webp","*.tiff","*.tga","*.spi","*.sgi","*.ppm","*.png","*.pcx","*.msp","*.jpeg","*.im","*.ico","*.icns","*.gif","*.eps","*.dib","*.bmp","*.MCIDAS","*.NAA","*.IPTC","*.IMT","*.GD","*.GBR","*.FTEX","*.FPX","*.FLC","*.FLI","*.DDS","*.DCX","*.CUR","*.BLP","*.XBM","*.WEBP","*.TIFF","*.TGA","*.SPI","*.SGI","*.PPM","*.PNG","*.PCX","*.MSP","*.JPEG","*.IM","*.ICO","*.ICNS","*.GIF","*.EPS","*.DIB","*.BMP","*.psd","*.hdf","*.sgi","*.mpg","*.pcx","*.pix","*.mci","*.msp","*.cur","*.sip","*.ftx","*.fpx","*.gbr","*..iptc","*..ipt","*.imt","*.tif","*.blp","*.tiff","*.tga","*.xpm","*.sun","*.xvt","*.webp","*.png","*.ico","*.bmp","*.gif","*.jpg","*.xbm","*.thm","*.icns","*.ppm")),("All files","*")])
             except:
                 showerror("File error","This folder can't be found\nMay was delected or come from another device")
             r.bind("<b>",self.pt)
             if len(self.fil)>=1:
                 self.fil=self.fil[0]
                 try:
                     self.fl=os.path.dirname(self.fil)
                     self.list=[]
                 except:
                     pass
                 self.cho(filr=self.fil)
             else:
                 showerror("Error" ,"Choose an image to be open\nOtherwise press 'b' to choose another one")
                 try:
                     self.fil = self.ba
                     self.cho(filr=self.fil)
                 except:
                     pass
        else:
               try:
                    self.fl=os.path.dirname(fuck)     
               except:
                    pass
               r.bind("<b>",self.pt)
               self.list=[]
               self.cho(fuck)
    def resizing(self, event=None):
        try:
            self.ipr =  Image.open(self.cur_file)
            self.ip = self.ipr.transpose(Image.ROTATE_90)
            s = self.ip.size
            self.ip = self.ip.resize((s[0], s[1]))
            d = os.getcwd()
            d = "/".join(d.split("\\"))
            f = d+str("/Mydir/")
            try:
                formato = self.cur_file.split("/")[-1]
                formato = formato.split(".")[-1]
            except:
                formato = "png"
            
            file = f+str(len(os.listdir(f))+1)+"."+formato
            self.ip.save(file)
            self.cho(file)
        except:
            showerror("Error","This file was moved or you system is not giving acess to your files")
    def lefttoright(self):
        try:
            self.ipr =  Image.open(self.cur_file)
            self.ip = self.ipr.transpose(Image.FLIP_LEFT_RIGHT)
            s = self.ip.size
            self.ip = self.ip.resize((s[0], s[1]))
            d = os.getcwd()
            d = "/".join(d.split("\\"))
            f = d+str("/Mydir/")
            try:
                formato = self.cur_file.split("/")[-1]
                formato = formato.split(".")[-1]
            except:
                formato = "png"
            
            file = f+str(len(os.listdir(f))+1)+"."+formato
            self.ip.save(file)
            self.cho(file)
        except:
            showerror("Error","This file was moved or you system is not giving acess to your files")
    def uptodown(self):
        try:
            self.ipr =  Image.open(self.cur_file)
            self.ip = self.ipr.transpose(Image.FLIP_TOP_BOTTOM)
            s = self.ip.size
            self.ip = self.ip.resize((s[0], s[1]))
            d = os.getcwd()
            d = "/".join(d.split("\\"))
            f = d+str("/Mydir/")
            try:
                formato = self.cur_file.split("/")[-1]
                formato = formato.split(".")[-1]
            except:
                formato = "png"
            
            file = f+str(len(os.listdir(f))+1)+"."+formato
            self.ip.save(file)
            self.cho(file)
        except:
            showerror("Error","This file was moved or you system is not giving acess to your files")
    def clickado(self, event):
         r.title(str(event.x)+" "+str( event.y))
    def filtering(self):
          e = self.comm.get()
          #("Mini filter","Multi band filter","BLUR","ENHANCED","CONTOUR","EMBOSS","EDGE ENHANCE MORE","DETAIL","FIND EDGES","SMOOTH MORE","SMOOTH","SHARPEN")
          if e == "BLUR":
               self.im_cur = self.im_cur.filter(ImageFilter.BLUR)
               self.im = ImageTk.PhotoImage(self.im_cur)
               self.bt["image"] = self.im
          elif e == "SMOOOTH MORE":
               self.im_cur = self.im_cur.filter(ImageFilter.SMOOTH_MORE)
               self.im = ImageTk.PhotoImage(self.im_cur)
               self.bt["image"] = self.im
          elif e == "SHARPEN":
               self.im_cur = self.im_cur.filter(ImageFilter.SHARPEN)
               self.im = ImageTk.PhotoImage(self.im_cur)
               self.bt["image"] = self.im
          elif e == "SMOOTH":
               self.im_cur = self.im_cur.filter(ImageFilter.SMOOTH)
               self.im = ImageTk.PhotoImage(self.im_cur)
               self.bt["image"] = self.im
          elif e == "FIND EDGES":
               self.im_cur = self.im_cur.filter(ImageFilter.FIND_EDGES)
               self.im = ImageTk.PhotoImage(self.im_cur)
               self.bt["image"] = self.im
          elif e == "DETAIL":
               self.im_cur = self.im_cur.filter(ImageFilter.DETAIL)
               self.im = ImageTk.PhotoImage(self.im_cur)
               self.bt["image"] = self.im
          elif e == "EDGE ENHANCE MORE":
               self.im_cur = self.im_cur.filter(ImageFilter.EDGE_ENHANCE_MORE)
               self.im = ImageTk.PhotoImage(self.im_cur)
               self.bt["image"] = self.im
          elif e == "EMBOSS":
               self.im_cur = self.im_cur.filter(ImageFilter.EMBOSS)
               self.im = ImageTk.PhotoImage(self.im_cur)
               self.bt["image"] = self.im
          elif e == "CONTOUR":
               self.im_cur = self.im_cur.filter(ImageFilter.CONTOUR)
               self.im = ImageTk.PhotoImage(self.im_cur)
               self.bt["image"] = self.im
          elif e == "Mini filter":
               self.im_cur = self.im_cur.filter(ImageFilter.MinFilter)
               self.im = ImageTk.PhotoImage(self.im_cur)
               self.bt["image"] = self.im
          elif e == "EDGE ENHACED":
               self.im_cur = self.im_cur.filter(ImageFilter.EDGE_ENHANCED)
               self.im = ImageTk.PhotoImage(self.im_cur)
               self.bt["image"] = self.im
          elif e == "GaussianBlur":
               self.im_cur = self.im_cur.filter(ImageFilter.GaussianBlur(3))
               self.im = ImageTk.PhotoImage(self.im_cur)
               self.bt["image"] = self.im
          elif e == "BoxBlur":
               self.im_cur = self.im_cur.filter(ImageFilter.BoxBlur(4))
               self.im = ImageTk.PhotoImage(self.im_cur)
               self.bt["image"] = self.im
          elif e == "UnsharpMask":
               self.im_cur = self.im_cur.filter(ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3))
               self.im = ImageTk.PhotoImage(self.im_cur)
               self.bt["image"] = self.im
          else:
               self.im_cur = Image.open(self.cur_file)
               self.im = ImageTk.PhotoImage(self.im_cur)
               self.bt["image"] = self.im
    def cho(self, filr):
        self.errr = False
        try:
            self.fr.pack_forget()
            self.r.pack_forget()
            self.r2.pack_forget()
        except:
            pass
        self.fr=tkinter.Frame(r, bg='#101010', relief='sunken')
        self.fr.pack()
        self.au = tkinter.Button(self.fr, bg='#00ffff',text="Creator: Francisco Ernesto Uqueio\n+258874437105",command=self.author, fg="green")
        self.au.pack(side="top")
        try:
            try:
                sizex = int(r.winfo_screenwidth())
                sizey = int(r.winfo_screenheight()) - 100
            except:
                sizex = 1500
                sizey = 800
            self.cur_file = filr
            self.ba = filr
            self.im_cur = Image.open(filr)
            self.im_cur.thumbnail((sizex, sizey))
            self.im_cur.resize((sizex, sizey))
            self.im=ImageTk.PhotoImage(self.im_cur)
            self.bt=tkinter.Button(self.fr, image=self.im,bg="#101010",highlightbackground="darkcyan")
            self.bt.pack()
            self.bt.bind("<Button-1>",self.clickado)
            self.r=tkinter.Frame(r, bg='#101010', relief='sunken')
            self.r.pack(side="bottom")
            self.bta=Button(self.r, text="<<Previous",bg='#00ffff')
            self.bta.pack(side="left")
            self.btb=Button(self.r, text="Open",bg='#00ffff')
            self.btb.pack(side="left")
            self.btn=Button(self.r, text="Next>>>>",bg='#00ffff')
            self.btn.pack(side="right")
            self.btb.bind("<Button-1>",self.pt)
            r.bind("<b>",self.pt)
            r.bind("<n>", self.nex)
            self.btn.bind("<Button-1>", self.nex)
            r.bind("<Up>", self.nex)
            r.bind("<Down>", self.pre)
            r.bind("<Right>", self.nex)
            r.bind("<Left>", self.pre)
            r.bind("<p>", self.pre)
            self.bta.bind("<Button-1>", self.pre)
            self.ll = Button(self.r,bg="#00ffff", text="Rotate 90")
            self.ll.pack(side="right")
            self.ll["command"] = self.resizing
            self.ll = Button(self.r,bg="#00ffff", text="Left-Right")
            self.ll.pack(side="right")
            self.ll["command"] = self.lefttoright
            self.ll = Button(self.r,bg="#00ffff", text="Up-Down")
            self.ll.pack(side="right")
            self.ll["command"] = self.uptodown
            self.ll = Button(self.r,bg="#00ffff", text="Join 2 Images")
            self.ll.pack(side="right")
            self.ll["command"] = self.twoimages
            self.ll = Button(self.r,bg="#00ffff", text="Save as")
            self.ll.pack(side="right")
            self.ll["command"] = self.changeformat
            self.r2 = tkinter.Frame(r, bg='#101010', relief='sunken')
            self.r2.pack()
            self.lll = Label(self.r2,text="Choose an image effect:",fg="#101010",bg="#00ffff")
            self.lll.pack(side="left")
            self.comm = ttk.Combobox(self.r2,values=("None","UnsharpMask","BoxBlur","GaussianBlur","Mini filter","Multi band filter","BLUR","EGDE ENHACED","CONTOUR","EMBOSS","EDGE ENHANCE MORE","DETAIL","FIND EDGES","SMOOTH MORE","SMOOTH","SHARPEN"))
            self.comm.current(0)
            self.comm.pack(side="left")
            self.tre = Button(self.r2,text="See effect",bg="darkcyan", command=self.filtering)
            self.tre.pack(side="right")
            #Thread(target=self.filtering,args=[])
            #self.tre.start()
            try:
                 self.tread = Thread(target=self.rrrrr,args=[])
                 self.tread.start()
            except:
                 pass
            try:
                r.title(str(filr.split("/")[-1]))
            except:
                pass
        except Exception as e:
            print(e)
            showerror("Error","The file '"+str(filr)+"' can not be opened\nPress 'b' to open another image")
        try:
            for i in os.listdir(self.fl):
                if i.endswith(".png") or i.endswith(".PNG") or i.endswith(".spi") or i.endswith(".SPI"):
                    self.list.append(i)
                elif i.endswith(".gif") or i.endswith(".GIF") or i.endswith(".dib") or i.endswith(".DIB"):
                    self.list.append(i)
                elif i.endswith(".jpg") or i.endswith(".JPG") or i.endswith(".GD") or i.endswith(".gd"):
                    self.list.append(i)
                elif i.endswith(".ico".upper()) or i.endswith(".ico") or i.endswith(".im") or i.endswith(".IM") or i.endswith(".dcx") or i.endswith(".DCX"):
                    self.list.append(i)
                elif i.endswith(".xbm") or i.endswith(".XBM") or i.endswith(".mic") or i.endswith(".MIC"):
                    self.list.append(i)
                elif i.endswith(".icns") or i.endswith(".ICNS") or i.endswith(".PCD") or i.endswith(".pcd"):
                    self.list.append(i)
                elif i.endswith(".ppm") or i.endswith(".PPM") or i.endswith(".xvt") or i.endswith(".XVT"):
                    self.list.append(i)
                elif i.endswith(".thm") or i.endswith(".THM") or i.endswith(".sun") or i.endswith(".SUN"):
                    self.list.append(i)
                elif i.endswith(".bmp") or i.endswith(".xpm") or i.endswith(".BMP") or i.endswith(".XPM") or i.endswith(".eps") or i.endswith(".EPS"):
                    self.list.append(i)
                elif i.endswith(".webp") or i.endswith(".tga") or i.endswith(".WEBP") or i.endswith(".TGA") or i.endswith(".mpo") or i.endswith(".MPO"):
                    self.list.append(i)
                elif i.endswith(".blp") or i.endswith(".tiff") or i.endswith(".BLP") or i.endswith(".TIFF"):
                    self.list.append(i)
                elif i.endswith(".imt") or i.endswith(".tif") or i.endswith(".IMT") or i.endswith(".TIF") or i.endswith(".wal") or i.endswith(".WAL"):
                    self.list.append(i)
                elif i.endswith(".iptc") or i.endswith(".ipt") or i.endswith(".IPTC") or i.endswith(".IPT") or i.endswith(".wmf") or i.endswith(".WMF"):
                    self.list.append(i)
                elif i.endswith(".ftx") or i.endswith(".ftex") or i.endswith(".FTEX") or i.endswith(".fpx") or i.endswith(".gbr") or i.endswith(".FTX") or i.endswith(".FPX") or i.endswith(".GBR"):
                    self.list.append(i)
                elif i.endswith(".cur") or i.endswith(".sip") or i.endswith(".CUR") or i.endswith(".SIP"):
                    self.list.append(i)
                elif i.endswith(".mci") or i.endswith(".msp") or i.endswith(".MCI") or i.endswith(".MSP"):
                    self.list.append(i)
                elif i.endswith(".mpg") or i.endswith(".pcx") or i.endswith(".pix") or i.endswith(".MPG") or i.endswith(".PCX") or i.endswith(".PIX"):
                    self.list.append(i)
                elif i.endswith(".hdf") or i.endswith(".sgi") or i.endswith(".psd") or i.endswith(".HDF") or i.endswith(".SGI") or i.endswith(".PSD"):
                    self.list.append(i)
                elif i.endswith('.dib') or i.endswith('.DIB'):
                   self.list.append(i)
                elif i.endswith('.eps') or i.endswith('.EPS'):
                   self.list.append(i)
                elif i.endswith('.gif') or i.endswith('.GIF'):
                   self.list.append(i)
                elif i.endswith('.icns') or i.endswith('.ICNS'):
                   self.list.append(i)
                elif i.endswith('.ico') or i.endswith('.ICO'):
                   self.list.append(i)
                elif i.endswith('.im') or i.endswith('.IM'):
                   self.list.append(i)
                elif i.endswith('.jpeg') or i.endswith('.JPEG'):
                   self.list.append(i)
                elif i.endswith('.msp') or i.endswith('.MSP'):
                   self.list.append(i)
                elif i.endswith('.pcx') or i.endswith('.PCX'):
                   self.list.append(i)
                elif i.endswith('.png') or i.endswith('.PNG'):
                   self.list.append(i)
                elif i.endswith('.ppm') or i.endswith('.PPM'):
                   self.list.append(i)
                elif i.endswith('.sgi') or i.endswith('.SGI'):
                   self.list.append(i)
                elif i.endswith('.spi') or i.endswith('.SPI'):
                   self.list.append(i)
                elif i.endswith('.tga') or i.endswith('.TGA'):
                   self.list.append(i)
                elif i.endswith('.tiff') or i.endswith('.TIFF'):
                   self.list.append(i)
                elif i.endswith('.webp') or i.endswith('.WEBP'):
                   self.list.append(i)
                elif i.endswith('.xbm') or i.endswith('.XBM'):
                   self.list.append(i)
                elif i.endswith('.blp') or i.endswith('.BLP'):
                   self.list.append(i)
                elif i.endswith('.cur') or i.endswith('.CUR'):
                   self.list.append(i)
                elif i.endswith('.dcx') or i.endswith('.DCX'):
                   self.list.append(i)
                elif i.endswith('.dds') or i.endswith('.DDS'):
                   self.list.append(i)
                elif i.endswith('.fli') or i.endswith('.FLI'):
                   self.list.append(i)
                elif i.endswith('.flc') or i.endswith('.FLC'):
                   self.list.append(i)
                elif i.endswith('.fpx') or i.endswith('.FPX'):
                   self.list.append(i)
                elif i.endswith('.ftex') or i.endswith('.FTEX'):
                   self.list.append(i)
                elif i.endswith('.gbr') or i.endswith('.GBR'):
                   self.list.append(i)
                elif i.endswith('.gd') or i.endswith('.GD'):
                   self.list.append(i)
                elif i.endswith('.imt') or i.endswith('.IMT'):
                   self.list.append(i)
                elif i.endswith('.iptc') or i.endswith('.IPTC'):
                   self.list.append(i)
                elif i.endswith('.naa') or i.endswith('.NAA'):
                   self.list.append(i)
                elif i.endswith('.mcidas') or i.endswith('.MCIDAS'):
                   self.list.append(i)
                elif i.endswith('.mic') or i.endswith('.MIC'):
                   self.list.append(i)
                elif i.endswith('.mpo') or i.endswith('.MPO'):
                   self.list.append(i)
                elif i.endswith('.pcd') or i.endswith('.PCD'):
                   self.list.append(i)
                elif i.endswith('.pixar') or i.endswith('.PIXAR'):
                   self.list.append(i)
                elif i.endswith('.psd') or i.endswith('.PSD'):
                   self.list.append(i)
                elif i.endswith('.wal') or i.endswith('.WAL'):
                   self.list.append(i)
                elif i.endswith('.wmf') or i.endswith('.WMF'):
                   self.list.append(i)
                elif i.endswith('.xpm') or i.endswith('.XPM'):
                   self.list.append(i)
                elif i.endswith('.palm') or i.endswith('.PALM'):
                   self.list.append(i)
                elif i.endswith('.pdf') or i.endswith('.PDF'):
                   self.list.append(i)
                elif i.endswith('.xv') or i.endswith('.XV'):
                   self.list.append(i)
                elif i.endswith('.bufr') or i.endswith('.BUFR'):
                   self.list.append(i)
                elif i.endswith('.fits') or i.endswith('.FITS'):
                   self.list.append(i)
                elif i.endswith('.grib') or i.endswith('.GRIB'):
                   self.list.append(i)
                elif i.endswith('.hdf5') or i.endswith('.HDF5'):
                   self.list.append(i)
                elif i.endswith('.mpeg') or i.endswith('.MPEG'):
                   self.list.append(i)
        except:
            pass

    def rrrrr(self):
        try:
             if self.im_cur.is_animated:
               for x in range(self.im_cur.n_frames):
                    try:
                         time.sleep(0.030)
                         self.im_cur.seek(x)
                         self.im=ImageTk.PhotoImage(self.im_cur)
                         self.bt["image"] = self.im
                    except:
                         break
                         self.tread.stop()
        except:
             pass
    def changeformat(self):
         try:
              tr = self.cur_file.split("/")
              t = "/".join(tr[0:-1])
              loc = asksaveasfilename(parent=r, initialdir = t)
              formato = askstring("Choose format","Which format:")
              self.im_cur.save(loc+"."+formato)
         except Exception as e:
             tr = self.cur_file.split("/")
             t = "/".join(tr[0:-1])
             loc = asksaveasfilename(parent=r, initialdir = t)
             try:
                 im = Image.open(self.cur_file)
                 formato = askstring("Choose format","Which format:")
                 try:
                     im.save(loc+"."+formato)
                     self.cho(loc+"."+formato)
                 except:
                     showerror("Error","Invalid format, please choose a valid format")
             except:
                 showerror("Error","'"+str(self.cur_file)+"' is not an valid image") 
    def twoimages(self):
        try:
            tr = self.cur_file.split("/")
            t = "/".join(tr[0:-1])
            fi = askopenfilenames(parent=r, initialdir=t, filetypes=[("All Images",("*.psd","*.hdf","*.sgi","*.mpg","*.pcx","*.pix","*.mci","*.msp","*.cur","*.sip","*.ftx","*.fpx","*.gbr","*..iptc","*..ipt","*.imt","*.tif","*.blp","*.tiff","*.tga","*.xpm","*.sun","*.xvt","*.webp","*.png","*.ico","*.bmp","*.gif","*.jpg","*.xbm","*.thm","*.icns","*.ppm")),("All files","*")])
            fi2 = askopenfilenames(parent=r, initialdir=t, filetypes=[("All Images",("*.psd","*.hdf","*.sgi","*.mpg","*.pcx","*.pix","*.mci","*.msp","*.cur","*.sip","*.ftx","*.fpx","*.gbr","*..iptc","*..ipt","*.imt","*.tif","*.blp","*.tiff","*.tga","*.xpm","*.sun","*.xvt","*.webp","*.png","*.ico","*.bmp","*.gif","*.jpg","*.xbm","*.thm","*.icns","*.ppm")),("All files","*")])
            try:
                image1 = Image.open(fi[0])
                image2 = Image.open(fi2[0])
                image1 = image1.resize((500, 500))
                image2 = image2.resize((500, 500))
                image1_size = image1.size
                image2_size = image2.size
                new_image = Image.new('RGB',(2*image1_size[0], image1_size[1]), (250,250,250))
                new_image.paste(image1,(0,0))
                new_image.paste(image2,(image1_size[0],0))
                loc = asksaveasfilename(parent=r, initialdir = t)
                try:
                    new_image.save(str(loc)+".jpg","JPEG")
                    self.cho(str(loc)+".jpg")
                except:
                    showerror("Error","Choose another name, that can't be set to that file")
            except:
                showerror("Error","The selected images can't be joined, verify the respective location")
        except:
            pass
    def author(self):
        showinfo("Information about Author","Created by: Francisco Ernesto Uqueio\nCountry: Mozambique\nYear: 2020\nAge: 17\nNumber: +258874473105\nEmail: franciscoernesto287@gmail.com")
    def pt(self, event):
        self.__init__(r)
        self.n=0
    def nex(self, event=None):
        try:
            self.n=self.n+1
            self.arq=str(self.fl)+str('/')+str(self.list[self.n])
            self.cho(self.arq)
            self.errr = False
            try:
                r.title(str(self.arq.split("/")[-1]))
            except:
                pass
        except:
            if self.errr == True:
                pass
            else:
                self.pre
                self.errr = True
    def pre(self, event=None):
        try:
            self.n=self.n-1
            self.arq=str(self.fl)+str('/')+str(self.list[self.n])
            self.cho(self.arq)
            self.errr = False
            try:
                r.title(str(self.arq.split("/")[-1]))
            except:
                pass
        except:
            if self.errr == True:
                pass
            else:
                self.nex
                self.errr = True
e = sys.argv
if len(e) >= 2:
     if len(e[1]) > 2:
          ed(r,fuck=e[1])
          r.mainloop()
else:
     ed(r)
     r.mainloop()
try:
     d = os.getcwd()
     d = "/".join(d.split("\\"))
     f = d+str("/Mydir/")
     for x in os.listdir(f):
         os.remove(f+x)
except:
     pass
    
