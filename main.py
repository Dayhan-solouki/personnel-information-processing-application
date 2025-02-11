from tkinter import *
import tkinter
import customtkinter  
from CTkTable import *
from PIL import ImageTk, Image
from CTkMessagebox import CTkMessagebox
from mysql.connector.locales.eng import client_error
import os

class App(customtkinter.CTk):

    frames = {"frame0": None, "frame1": None, "frame2": None, "frame3": None, "frame4": None, "frame5": None, "frame6": None, "frame7": None, "frame8": None, "frame9": None}

    def frame0_selector(self):
        App.frames["frame1"].pack_forget()
        App.frames["frame2"].pack_forget()
        App.frames["frame3"].pack_forget()
        App.frames["frame4"].pack_forget()
        App.frames["frame5"].pack_forget()
        App.frames["frame6"].pack_forget()
        App.frames["frame7"].pack_forget()
        App.frames["frame8"].pack_forget()
        App.frames["frame9"].pack_forget()
        App.frames["frame0"].pack(in_=self.right_side_container,side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=0, pady=0)

    def frame1_selector(self):
        App.frames["frame0"].pack_forget()
        App.frames["frame2"].pack_forget()
        App.frames["frame4"].pack_forget()
        App.frames["frame3"].pack_forget()
        App.frames["frame8"].pack_forget()
        App.frames["frame5"].pack_forget()
        App.frames["frame6"].pack_forget()
        App.frames["frame7"].pack_forget()
        App.frames["frame9"].pack_forget()
        App.frames["frame1"].pack(in_=self.right_side_container,side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=0, pady=0)

    def frame2_selector(self):
        App.frames["frame0"].pack_forget()
        App.frames["frame1"].pack_forget()
        App.frames["frame4"].pack_forget()
        App.frames["frame3"].pack_forget()
        App.frames["frame5"].pack_forget()
        App.frames["frame6"].pack_forget()
        App.frames["frame8"].pack_forget()
        App.frames["frame9"].pack_forget()
        App.frames["frame2"].pack(in_=self.right_side_container,side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=0, pady=0)

    def frame3_selector(self):
        App.frames["frame0"].pack_forget()
        App.frames["frame1"].pack_forget()
        App.frames["frame4"].pack_forget()
        App.frames["frame2"].pack_forget()
        App.frames["frame5"].pack_forget()
        App.frames["frame6"].pack_forget()
        App.frames["frame7"].pack_forget()
        App.frames["frame8"].pack_forget()
        App.frames["frame9"].pack_forget()
        App.frames["frame3"].pack(in_=self.right_side_container,side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=0, pady=0)

    def mode(self, val):
        if val == "background":
            color = "#8D9797"
            return color    
        if val == "text_color":
            color = "black"
            return color  
    
    def __init__(self):
        super().__init__()
        customtkinter.set_appearance_mode("light")
        self.title("Personel Takip")
        if self.winfo_screenwidth() > 1480 :
            customtkinter.set_widget_scaling(0.8)
            print(self.winfo_screenwidth())
            self.minsize(1400,800)
        else:
            customtkinter.set_widget_scaling(0.60)
            self.minsize(1000,700)
            print(self.winfo_screenwidth())
            print(self.mode())

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
        self.wm_iconbitmap(f"{image_path}/logo.ico")

        self.geometry("{}x{}+0+0".format(self.winfo_screenwidth()-100, self.winfo_screenheight()-100))

        #image
        self.Homepage_icon = customtkinter.CTkImage(Image.open(os.path.join(image_path, "home.png")), size=(50, 50))
        self.Settings_icon = customtkinter.CTkImage(Image.open(os.path.join(image_path, "settings.png")), size=(50, 50))
        self.Log_icon = customtkinter.CTkImage(Image.open(os.path.join(image_path, "log.png")), size=(50, 50))
        self.Reports_icon = customtkinter.CTkImage(Image.open(os.path.join(image_path, "deadline.png")), size=(50, 50))
        self.Prsonel_icon = customtkinter.CTkImage(Image.open(os.path.join(image_path, "personel.png")), size=(50, 50))
        #main_container
        App.main_container = customtkinter.CTkFrame(self)
        App.main_container.pack(fill=tkinter.BOTH, expand=True, padx=10, pady=10)

        # right side panel -> to show the frames
        self.right_side_panel = customtkinter.CTkFrame(App.main_container, width=1200, fg_color="transparent")
        self.right_side_panel.pack(side=tkinter.RIGHT, fill=tkinter.Y, expand=True, padx=10, pady=10)

        self.right_side_container = customtkinter.CTkFrame(self.right_side_panel, width=1200, fg_color="transparent")
        self.right_side_container.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True, padx=0, pady=0)

        #Menu Design
        self.menu_frame = customtkinter.CTkFrame(App.main_container, fg_color=self.mode("background"), width=200)
        self.menu_frame.pack(side=tkinter.LEFT, fill=tkinter.Y, expand=False, padx=5, pady=5)

        self.homepage_icon = customtkinter.CTkButton(self.menu_frame, text="Ana sayfa", font=("Century Gothic",18.0,"bold"), fg_color="transparent", command=self.frame0_selector, image=self.Homepage_icon, hover=True, anchor="w", height=50, width=200, text_color=self.mode("text_color"))
        self.homepage_icon.grid(row=0, column=0, padx=5, pady=10) 

        self.order_icon = customtkinter.CTkButton(self.menu_frame, text="Personel Bilgileri", font=("Century Gothic",18.0,"bold"), fg_color="transparent", command=self.frame1_selector, image=self.Prsonel_icon, hover=True, anchor="w", height=50, width=200, text_color=self.mode("text_color"))
        self.order_icon.grid(row=1, column=0, padx=5, pady=10) 

        self.product_control = customtkinter.CTkButton(self.menu_frame, text="Raporlar", font=("Century Gothic",18.0,"bold"), fg_color="transparent", command=self.frame2_selector, image=self.Reports_icon, hover=True, anchor="w", height=50, width=200, text_color=self.mode("text_color"))
        self.product_control.grid(row=2, column=0, padx=5, pady=10) 

        self.profile_icon = customtkinter.CTkButton(self.menu_frame, text="Loglar", font=("Century Gothic",18.0,"bold"), fg_color="transparent", command=self.frame3_selector, image=self.Log_icon, hover=True, anchor="w", height=50, width=200, text_color=self.mode("text_color"))
        self.profile_icon.grid(row=3, column=0, padx=5, pady=10) 

        self.setting_icon = customtkinter.CTkButton(self.menu_frame, text="Ayarlar", font=("Century Gothic",18.0,"bold"), fg_color="transparent", command=self.frame3_selector, image=self.Settings_icon, hover=True, anchor="w", height=50, width=200, text_color=self.mode("text_color"))
        self.setting_icon.grid(row=4, column=0, padx=5, pady=10) 

if __name__ == "__main__":
    app = App()
    app.mainloop()