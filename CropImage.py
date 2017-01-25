import os

import tkinter as tk # this is in python 3.4. For python 2.x import Tkinter
from PIL import Image, ImageTk
import glob
from PIL.Image import ANTIALIAS


class CropApp(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.image_list = []
        self.image_filename = []
        self.import_directory()
        self.index_image = 914
        self.index_file = 0

        self.find_index()

        #maximize window-----------------------
        toplevel = self.winfo_toplevel()
        toplevel.wm_state('zoomed')


        #-------------------------------------

        #open image---------------------------
        self.x = self.y = 0
        self.im = self.image_list[self.index_image]
        self.tk_im = ImageTk.PhotoImage(self.im)

        #------------------------------------


        #self.im = self.im.resize((100,100),ANTIALIAS)


        imgWidth , imgHeight = self.im.size


        self.canvas = tk.Canvas(self, width=imgWidth, height=imgHeight, cursor="cross")
        self.canvas.pack(side="top", fill="both", expand=True)
        self.bindKey()




        self.rect = None

        self.start_x = None
        self.start_y = None


        self._draw_image()



    def find_index(self):

        global line
        line = None

        with open('log.txt') as fp:
            for line in fp:
               pass

            if line is not None:
                last = line
                last_line_list = last.split()
                self.index_file = int(last_line_list[1])
                print(str(self.index_file))



    def bindKey(self):
        # bind button and mouse----------------
        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_move_press)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)
        self.bind("<Return>", self.on_enter)
        self.bind("<Right>", self.on_right)
        self.bind("<Left>", self.on_left)
        # --------------------------------------

    def _draw_image(self):



         self.canvas.create_image(0,0,anchor="nw",image=self.tk_im)
         self.canvas.place(relx=0.5, rely=0.5, anchor="center")


    def import_directory(self):

        for filename in glob.glob('./image/CAT_00/*.jpg'):  # assuming gif
            im = Image.open(filename)
            self.image_filename.append(filename)
            self.image_list.append(im)



    def on_button_press(self, event):
        # save mouse drag start position
        self.start_x = event.x
        self.start_y = event.y

        # create rectangle if not yet exist
        #if not self.rect:

        self.rect = self.canvas.create_rectangle(self.x, self.y, 1, 1, outline='green')


    def on_move_press(self, event):
        curX, curY = (event.x, event.y)

        # expand rectangle as you drag the mouse
        self.canvas.coords(self.rect, self.start_x, self.start_y, curX, curY)
        self.curX = curX
        self.curY = curY
        print(str(self.start_x)+" "+str(self.start_y))
        print(str(curX)+" "+str(curY))
        print(abs(self.start_x-curX))
        print(abs(self.start_y-curY))





    def on_button_release(self, event):
        print("release")



    def on_enter(self, event):
        self.write_file(self.image_filename[self.index_image],self.start_x,self.start_y,abs(self.start_x-self.curX),abs(self.start_y-self.curY))
        print("enter")
        #filenames = next(os.walk('./image/CAT_00/'))[2]
        #print(filenames[0])


    def on_left(self, event):
        if self.index_image != 0 :
            self.index_image = self.index_image-1
            self.im = self.image_list[self.index_image]
            self.tk_im = ImageTk.PhotoImage(self.im)
            self.rect = None
            self.start_x = None
            self.start_y = None
            imgWidth, imgHeight = self.im.size

            self.canvas = tk.Canvas(self, width=imgWidth, height=imgHeight, cursor="cross")
            self.canvas.pack(side="top", fill="both", expand=True)

            self._draw_image()

        print('left')


    def on_right(self, event):
        self.index_image = self.index_image +1
        self.im = self.image_list[self.index_image]
        self.tk_im = ImageTk.PhotoImage(self.im)
        self.start_x = None
        self.start_y = None
        imgWidth, imgHeight = self.im.size

        self.canvas.delete(self.rect)
       # self.canvas = tk.Canvas(self, width=imgWidth, height=imgHeight, cursor="cross")
        self.canvas.config(width = imgWidth,height = imgHeight)


        self._draw_image()

        print('right')


    def write_file(self,path,x,y,width,height):
        self.text_file = open("log.txt", "a")
        self.index_file = self.index_file + 1
        self.text_file.write(path+"  "+str(self.index_file)+"  "+str(x)+" "+str(y)+" "+str(x+width)+" "+str(y+height)+'\n')
        #text_file.write("Purchase Amount: %s" % TotalAmount)
        self.text_file.close()






if __name__ == "__main__":
    app = CropApp()
    app.mainloop()