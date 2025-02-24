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
        # App.frames["frame2"].pack_forget()
        # App.frames["frame3"].pack_forget()
        # App.frames["frame4"].pack_forget()
        # App.frames["frame5"].pack_forget()
        # App.frames["frame6"].pack_forget()
        # App.frames["frame7"].pack_forget()
        # App.frames["frame8"].pack_forget()
        # App.frames["frame9"].pack_forget()
        App.frames["frame0"].pack(in_=App.main_container,side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=0, pady=0)

    def frame1_selector(self):
        App.frames["frame0"].pack_forget()
        # App.frames["frame2"].pack_forget()
        # App.frames["frame4"].pack_forget()
        # App.frames["frame3"].pack_forget()
        # App.frames["frame8"].pack_forget()
        # App.frames["frame5"].pack_forget()
        # App.frames["frame6"].pack_forget()
        # App.frames["frame7"].pack_forget()
        # App.frames["frame9"].pack_forget()
        App.frames["frame1"].pack(in_=App.main_container,side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=0, pady=0)

    def frame2_selector(self):
        App.frames["frame0"].pack_forget()
        App.frames["frame1"].pack_forget()
        App.frames["frame4"].pack_forget()
        App.frames["frame3"].pack_forget()
        App.frames["frame5"].pack_forget()
        App.frames["frame6"].pack_forget()
        App.frames["frame8"].pack_forget()
        App.frames["frame9"].pack_forget()
        App.frames["frame2"].pack(in_=App.main_container,side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=0, pady=0)

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
        App.frames["frame3"].pack(in_=App.main_container,side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=0, pady=0)

    def mode(self, val):
        if val == "background":
            color = "#3B707D"
            return color    
        if val == "text_color":
            color = "black"
            return color  
        if val == "hover_color":
            color = "#ADC2D3"
            return color
        if val == "frame_background":
            color = "#C3CEDA"
            return color
        if val == "topframe_background":
            color = "#EAEFF2"
            return color
        if val == "infoframe_background":
            color = "#EAEFF2"
            return color
    def on_enter(self,event,objectname):
        objectname.configure(text_color="darkorange")

    
    def on_leave(self,event,objectname):
        objectname.configure(text_color=self.mode("text_color"))
    
    def __init__(self):
        super().__init__()
        customtkinter.set_appearance_mode("light")
        self.title("Personel Takip")
        if self.winfo_screenwidth() > 1480 :
            customtkinter.set_widget_scaling(0.8)
            print(self.winfo_screenwidth())
            self.minsize(1400,850)
        else:
            customtkinter.set_widget_scaling(0.60)
            self.minsize(1000,750)
            print(self.winfo_screenwidth())
            print(self.mode())

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
        self.wm_iconbitmap(f"{image_path}/logo.ico")

        self.geometry("{}x{}+0+0".format(self.winfo_screenwidth()-100, self.winfo_screenheight()-100))

        #image
        self.Homepage_icon = customtkinter.CTkImage(Image.open(os.path.join(image_path, "home.png")), size=(40, 40))
        self.Settings_icon = customtkinter.CTkImage(Image.open(os.path.join(image_path, "settings.png")), size=(40, 40))
        self.Log_icon = customtkinter.CTkImage(Image.open(os.path.join(image_path, "log.png")), size=(40, 40))
        self.Reports_icon = customtkinter.CTkImage(Image.open(os.path.join(image_path, "report.png")), size=(40, 40))
        self.Prsonel_icon = customtkinter.CTkImage(Image.open(os.path.join(image_path, "user.png")), size=(40, 40))
        self.logo = customtkinter.CTkImage(Image.open(os.path.join(image_path, "logo.png")), size=(180, 55))
        self.profilesetting = customtkinter.CTkImage(Image.open(os.path.join(image_path, "boy.png")), size=(55, 55)) 
        self.info = customtkinter.CTkImage(Image.open(os.path.join(image_path, "info.png")), size=(45, 45)) 
        self.profile_img = customtkinter.CTkImage(Image.open(os.path.join(image_path, "profile.png")), size=(200, 200)) 
        self.permission_icon = customtkinter.CTkImage(Image.open(os.path.join(image_path, "day-off.png")), size=(25, 25)) 
        #main_container
        App.main_container = customtkinter.CTkFrame(self)
        App.main_container.pack(fill=tkinter.BOTH, expand=True, padx=0, pady=0)

        #Menu Design
        self.menu_frame = customtkinter.CTkFrame(App.main_container, fg_color=self.mode("topframe_background"), width=200, border_color="black", corner_radius=0)
        self.menu_frame.pack(side=tkinter.LEFT, fill=tkinter.Y, expand=False, padx=0, pady=0)

        menu_logo = customtkinter.CTkLabel(self.menu_frame ,text="", image=self.logo)
        menu_logo.grid(row=0, column=0, padx=0, pady=15) 

        self.homepage_icon = customtkinter.CTkButton(self.menu_frame, text="Ana sayfa", font=("Century Gothic",18.0,"bold"), fg_color="transparent", command=self.frame0_selector, image=self.Homepage_icon, hover=True, anchor="w", height=70, width=200, text_color=self.mode("text_color"), hover_color=self.mode("hover_color"))
        self.homepage_icon.grid(row=1, column=0, padx=5, pady=5) 

        self.homepage_icon.bind("<Enter>", lambda event, btn=self.homepage_icon: self.on_enter(event, btn))
        self.homepage_icon.bind("<Leave>", lambda event, btn=self.homepage_icon: self.on_leave(event, btn))

        self.Prsonel_icn = customtkinter.CTkButton(self.menu_frame, text="Personel", font=("Century Gothic",18.0,"bold"), fg_color="transparent", command=self.frame1_selector, image=self.Prsonel_icon, hover=True, anchor="w", height=70, width=200, text_color=self.mode("text_color"), hover_color=self.mode("hover_color"))
        self.Prsonel_icn.grid(row=2, column=0, padx=5, pady=5) 

        self.Prsonel_icn.bind("<Enter>", lambda event, btn=self.Prsonel_icn: self.on_enter(event, btn))
        self.Prsonel_icn.bind("<Leave>", lambda event, btn=self.Prsonel_icn: self.on_leave(event, btn))

        self.product_control = customtkinter.CTkButton(self.menu_frame, text="Raporlar", font=("Century Gothic",18.0,"bold"), fg_color="transparent", command=self.frame2_selector, image=self.Reports_icon, hover=True, anchor="w", height=70, width=200, text_color=self.mode("text_color"), hover_color=self.mode("hover_color"))
        self.product_control.grid(row=3, column=0, padx=5, pady=5) 

        self.product_control.bind("<Enter>", lambda event, btn=self.product_control: self.on_enter(event, btn))
        self.product_control.bind("<Leave>", lambda event, btn=self.product_control: self.on_leave(event, btn))

        self.profile_icon = customtkinter.CTkButton(self.menu_frame, text="Loglar", font=("Century Gothic",18.0,"bold"), fg_color="transparent", command=self.frame3_selector, image=self.Log_icon, hover=True, anchor="w", height=70, width=200, text_color=self.mode("text_color"), hover_color=self.mode("hover_color"))
        self.profile_icon.grid(row=4, column=0, padx=5, pady=5) 

        self.profile_icon.bind("<Enter>", lambda event, btn=self.profile_icon: self.on_enter(event, btn))
        self.profile_icon.bind("<Leave>", lambda event, btn=self.profile_icon: self.on_leave(event, btn))

        self.setting_icon = customtkinter.CTkButton(self.menu_frame, text="Ayarlar", font=("Century Gothic",18.0,"bold"), fg_color="transparent", command=self.frame3_selector, image=self.Settings_icon, hover=True, anchor="w", height=70, width=200, text_color=self.mode("text_color"), hover_color=self.mode("hover_color"))
        self.setting_icon.grid(row=5, column=0, padx=5, pady=5) 

        self.setting_icon.bind("<Enter>", lambda event, btn=self.setting_icon: self.on_enter(event, btn))
        self.setting_icon.bind("<Leave>", lambda event, btn=self.setting_icon: self.on_leave(event, btn))

        # Homwpage Design
        App.frames["frame0"] = customtkinter.CTkFrame(App.main_container, fg_color=self.mode("frame_background"))
    
        self.Homepage_top_frame = customtkinter.CTkFrame(App.frames["frame0"], fg_color=self.mode("topframe_background"), height=80, corner_radius=0)
        self.Homepage_top_frame.pack(side=tkinter.TOP, fill=tkinter.X, expand=False, padx=0, pady=0)

        self.User_name = customtkinter.CTkLabel(self.Homepage_top_frame, text="Merhaba Murat Kargün !", font=("Century Gothic",20,"bold"),height=50 ,width= 300)
        self.User_name.place(relx=0.1, rely=0.5, anchor=tkinter.CENTER)

        self.User_profile = customtkinter.CTkButton(self.Homepage_top_frame, font=("Century Gothic",18.0,"bold"), fg_color="transparent", text="Murat Kargün", command=self.frame3_selector, image=self.profilesetting, hover=True, anchor="w", height=70, width=200, text_color=self.mode("text_color"))
        self.User_profile.place(relx=0.85, rely=0.5, anchor=tkinter.CENTER)

        self.User_profile.bind("<Enter>", lambda event, btn=self.User_profile: self.on_enter(event, btn))
        self.User_profile.bind("<Leave>", lambda event, btn=self.User_profile: self.on_leave(event, btn))

        self.info_icon = customtkinter.CTkButton(self.Homepage_top_frame, font=("Century Gothic",18.0), fg_color="transparent", text=None, command=self.frame3_selector, image=self.info, hover=True, anchor="w", height=50, width=50, text_color=self.mode("text_color"), hover_color=self.mode("hover_color"))
        self.info_icon.place(relx=0.95, rely=0.5, anchor=tkinter.CENTER)

        self.Homepage_bottom_frame = customtkinter.CTkFrame(App.frames["frame0"], fg_color="transparent")
        self.Homepage_bottom_frame.pack(side=tkinter.TOP, fill=tkinter.Y, expand=True, padx=0, pady=0)

        self.homepage_info_frame_1 = customtkinter.CTkFrame(self.Homepage_bottom_frame, width=600, height=500, fg_color=self.mode("infoframe_background"))
        self.homepage_info_frame_1.grid(row=0, column=0,columnspan= 3, rowspan=2, padx=20, pady=20)

        self.homepage_info_frame_2 = customtkinter.CTkScrollableFrame(self.Homepage_bottom_frame, width=830, height=450,label_text="Bekleyen İşlemler", label_font=("Century Gothic",17,"bold"), fg_color=self.mode("infoframe_background"))
        self.homepage_info_frame_2.grid(row=0, column=4,columnspan= 3, rowspan=2, padx=20, pady=20)

        self.homepage_info_frame_3 = customtkinter.CTkFrame(self.Homepage_bottom_frame, width=600, height=350, fg_color=self.mode("infoframe_background"))
        self.homepage_info_frame_3.grid(row=3, column=0, padx=20, pady=15)

        self.homepage_info_frame_4 = customtkinter.CTkFrame(self.Homepage_bottom_frame, width=400, height=350, fg_color=self.mode("infoframe_background"))
        self.homepage_info_frame_4.grid(row=3, column=4,  padx=20, pady=10)

        self.homepage_info_frame_5 = customtkinter.CTkFrame(self.Homepage_bottom_frame, width=400, height=350, fg_color=self.mode("infoframe_background"))
        self.homepage_info_frame_5.grid(row=3, column=6, padx=20, pady=10)

        self.homepage_profil_image = customtkinter.CTkLabel(self.homepage_info_frame_1, font=("Century Gothic",18.0,"bold"), fg_color="transparent", text=None, image=self.profile_img, anchor="w", height=100, width=100, text_color=self.mode("text_color"))
        self.homepage_profil_image.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

        self.homepage_profil_name = customtkinter.CTkLabel(self.homepage_info_frame_1, text="Murat Kargün", font=("Century Gothic",20,"bold"),height=50 ,width= 300)
        self.homepage_profil_name.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

        self.homepage_profil_sts = customtkinter.CTkLabel(self.homepage_info_frame_1, text="Yönetici", font=("Century Gothic",17),height=50 ,width= 300)
        self.homepage_profil_sts.place(relx=0.5, rely=0.68, anchor=tkinter.CENTER)

        profile_permission_btn = customtkinter.CTkButton(self.homepage_info_frame_1, text="İzin Ekle", font=("Century Gothic",17), fg_color="green", text_color="white", image=self.permission_icon, width=250, height=50)
        profile_permission_btn.place(relx=0.75, rely=0.9, anchor=tkinter.CENTER)

        profile_notif_btn = customtkinter.CTkButton(self.homepage_info_frame_1, text="Bildirim Ekle", font=("Century Gothic",17), fg_color="#E66912", text_color="white", image=self.permission_icon, width=250, height=50)
        profile_notif_btn.place(relx=0.25, rely=0.9, anchor=tkinter.CENTER)

        profile_history_lable = customtkinter.CTkLabel(self.homepage_info_frame_3, text="Geçmiş İzinlerim", font=("Century Gothic",17,"bold"))
        profile_history_lable.place(relx=0.15, rely=0.07, anchor=tkinter.CENTER)

        profile_permission_lable = customtkinter.CTkLabel(self.homepage_info_frame_4, text="Kalan İzinlerim", font=("Century Gothic",17,"bold"))
        profile_permission_lable.place(relx=0.2, rely=0.07, anchor=tkinter.CENTER)

        profile_notif_lable = customtkinter.CTkLabel(self.homepage_info_frame_5, text="Duyurular", font=("Century Gothic",17,"bold"))
        profile_notif_lable.place(relx=0.15, rely=0.07, anchor=tkinter.CENTER)


        # Personel Design
        App.frames["frame1"] = customtkinter.CTkFrame(App.main_container, fg_color=self.mode("infoframe_background"))

        # self.Personel_frame = customtkinter.CTkFrame(App.frames["frame1"], fg_color="transparent")
        # self.Personel_frame.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=0, pady=0)

        self.tabview_page1 = customtkinter.CTkTabview(master=App.frames['frame1'],text_color="white",segmented_button_unselected_color=self.mode("hover_color"), fg_color=self.mode("frame_background"), width=1200)
        self.tabview_page1.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=10, pady=10)
        self.tabview_page1._segmented_button.configure(font=('', 17,"bold"), text_color=self.mode("text_color"))
        self.tabview_page1.add("Personel Listesi")  
        self.tabview_page1.add("Personel İşlemleri")  
        self.tabview_page1.set("Personel Listesi") 

        self.personel_show_frame = customtkinter.CTkScrollableFrame(self.tabview_page1.tab("Personel Listesi"), width=1200, height=900,label_text="Personel Listesi", label_font=("Century Gothic",17,"bold"), fg_color=self.mode("infoframe_background"))
        self.personel_show_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.frame0_selector()

if __name__ == "__main__":
    app = App()
    app.mainloop()