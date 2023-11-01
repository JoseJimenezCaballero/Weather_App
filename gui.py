import tkinter as tk
import customtkinter as ctk
import requests
import json
import math
from PIL import Image, ImageTk
import time

class gui():
    def __init__(self):
        self.window = ctk.CTk(fg_color='#a1a1a1')
        self.window.title("Weather")
        self.window.geometry('950x650')
        self.window._set_appearance_mode('system')
        self.window.minsize(950,650)
        self.window.maxsize(950,650)
        self.forecast_widget_bg = '#909090' #bg color of widget behind 12 hour forecast. default value
        self.animated_panel = side_panel(self.window,-0.3,-0.02,self.forecast_widget_bg)
        self.animated_panel.tkraise()
        self.animated_button = side_button(self.window, 0.01, 0.2)
        self.animated_button.configure(command=lambda:[self.animated_panel.animate(), self.animated_button.animate()])
    



#method will take condition and mode as param and change the bg color accorgdingly
    def __bg_color_selector(self,condition, mode): 
        if(mode == 'night'):
            if(condition == 'Clear'):
                return '512/night_half_moon_clear.png'
            elif(condition == 'Partly cloudy'):
                return '512/night_full_moon_partial_cloud.png'
            elif(condition == 'Cloudy'):
                return '512/cloudy.png'
            elif(condition == 'Mist'):
                return '512/mist.png'
            elif(condition == 'Overcast'):
                return '512/overcast.png'
            elif(condition == 'Rain'):
                return '512/night_half_moon_rain.png'
            elif(condition == 'Light rain'):
                return '512/night_half_moon_rain.png'
            elif(condition == 'Moderate rain'):
                return '512/rain.png'
            elif(condition == 'Patchy rain possible'):
                return '512/night_half_moon_rain.png'
            elif(condition == 'Light drizzle' or condition == 'Light rain shower'):
                return '512/night_full_moon_rain.png'
            else:
                return 'white'
        else:
            if(condition == 'Clear'):
                return '#3872ff','#054EFF', '#003DD1'
            elif(condition == 'Patchy rain possible'):
                return '#3872ff','#054EFF', '#003DD1'
            elif(condition == 'Light rain'):
                return '#3872ff','#054EFF', '#003DD1'
            elif(condition == 'Moderate rain'):
                return '#a1a1a1','#888888','#6F6F6F'
            elif(condition == 'Partly cloudy'):
                return '#3872ff','#054EFF', '#003DD1'
            elif(condition == 'Cloudy'):
                return '#a1a1a1','#888888','#6F6F6F'
            elif(condition == 'Mist'):
                return '#a1a1a1','#888888','#6F6F6F'
            elif(condition == 'Overcast'):
                return '#a1a1a1','#888888','#6F6F6F'
            elif(condition == 'Rain'):
                return '#a1a1a1','#888888','#6F6F6F'
            elif(condition == 'Sunny'):
                return '#3872ff','#054EFF', '#003DD1'
            elif(condition == 'Light drizzle' or condition == 'Light rain shower'):
                return '#3872ff','#054EFF', '#003DD1'
            else:
                return 'black','white','blue'

    def bg_setter(self,condition,mode):#changes bg color of main window and the sub window
        main_bg, forecast_bg , sidebar = self.__bg_color_selector(condition, mode)
        self.window.configure(fg_color=main_bg)
        self.forecast_widget_bg = forecast_bg
        self.animated_panel.update_fg(sidebar)
        self.animated_button.update_fg(sidebar)

    def __image_selector(self,condition, mode): #takes condition of hour and mode which is night or day
        if(mode == 'night'):
            if(condition == 'Clear'):
                return '512/night_half_moon_clear.png'
            elif(condition == 'Partly cloudy'):
                return '512/night_full_moon_partial_cloud.png'
            elif(condition == 'Cloudy'):
                return '512/cloudy.png'
            elif(condition == 'Mist'):
                return '512/mist.png'
            elif(condition == 'Overcast'):
                return '512/overcast.png'
            elif(condition == 'Rain'):
                return '512/night_half_moon_rain.png'
            elif(condition == 'Light rain'):
                return '512/night_half_moon_rain.png'
            elif(condition == 'Moderate rain'):
                return '512/rain.png'
            elif(condition == 'Patchy rain possible'):
                return '512/night_half_moon_rain.png'
            elif(condition == 'Light drizzle' or condition == 'Light rain shower'):
                return '512/night_full_moon_rain.png'
            else:
                return '512/tornado.png'
        else:
            if(condition == 'Clear'):
                return '512/day_clear.png'
            elif(condition == 'Patchy rain possible' or condition == 'Patchy light rain'):
                return '512/day_rain.png'
            elif(condition == 'Light rain'):
                return '512/day_rain.png'
            elif(condition == 'Moderate rain'):
                return '512/rain.png'
            elif(condition == 'Partly cloudy'):
                return '512/day_partial_cloud.png'
            elif(condition == 'Cloudy'):
                return '512/cloudy.png'
            elif(condition == 'Mist'):
                return '512/mist.png'
            elif(condition == 'Overcast'):
                return '512/overcast.png'
            elif(condition == 'Rain'):
                return '512/day_rain.png'
            elif(condition == 'Sunny'):
                return '512/day_clear.png'
            elif(condition == 'Light drizzle' or condition == 'Light rain shower'):
                return '512/day_rain.png'
            else:
                return '512/tornado.png'

    def set_settings_button_img(self,condition, mode):
        main, forecast, ignore = self.__bg_color_selector(condition, mode)
        im_now = ctk.CTkImage(
        light_image=Image.open('512/menu.png'),
        dark_image=Image.open('512/menu.png'),
        size=(22,22)
        )
        self.animated_button.configure(image=im_now, fg_color=main,hover_color=forecast)

        
    def set_city(self,city):
        city = ctk.CTkLabel(self.window, text=city, font=('SF Pro', 30))
        city.place(relx = 0.5, rely = 0.11, anchor = 'c') #anchor to center

    def set_temp(self,temp_):
        temp = ctk.CTkLabel(self.window, text= " " + temp_ + "°", font=('SF Pro', 63), fg_color='transparent')
        temp.place(relx = 0.5, rely = 0.196, anchor = 'c')        


    def set_condition(self,condition):
        current_w = ctk.CTkLabel(self.window, text=condition, font=('SF Pro', 18))
        current_w.place(relx = 0.5, rely = 0.275, anchor = 'c') #anchor to center

    def set_high(self,high_):
        high = ctk.CTkLabel(self.window, text= "H:"+ str(high_) + "°" ,font=('SF Pro', 18), fg_color='transparent')
        high.place(relx = 0.47, rely = 0.325, anchor = 'c')

    def set_low(self,low_):
        low = ctk.CTkLabel(self.window, text="L:" + str(low_) + "°", font=('SF Pro', 18), fg_color='transparent')
        low.place(relx = 0.53, rely = 0.325, anchor = 'c')

    def set_bg_forecast(self):
        self.bg_behind_forecast = ctk.CTkFrame(self.window, width=875, height=150, fg_color=self.forecast_widget_bg, corner_radius=15)
        self.bg_behind_forecast.place(relx=0.5,rely=0.55, anchor='c')

    def set_hr_text_now(self, temp, condition, mode):
        ccondition = self.__image_selector(condition, mode)
        im_now = ctk.CTkImage(
        light_image=Image.open(ccondition),
        dark_image=Image.open(ccondition),
        size=(30,30)
        )
        zero_text = ctk.CTkLabel(self.window, text = 'Now', font=('SF Pro', 14), fg_color=self.forecast_widget_bg)
        zero_temp = ctk.CTkLabel(self.window, text = str(temp) + '°', font=('SF Pro', 14), fg_color=self.forecast_widget_bg)
        zero_text.place(relx=0.10,rely=0.45)
        zero_temp.place(relx=0.10,rely=0.608)
        im_lab_now = ctk.CTkLabel(self.bg_behind_forecast, text='', image=im_now, fg_color=self.forecast_widget_bg)
        im_lab_now.place(relx=0.083,rely=0.5, anchor='c')

    #places hours and temp on forecast widget    
    def set_hr_text_1(self,hour, temp, condition, mode):
        ccondition = self.__image_selector(condition, mode)
        im_now = ctk.CTkImage(
        light_image=Image.open(ccondition),
        dark_image=Image.open(ccondition),
        size=(30,30)
        )
        if(hour >= 12):
            hour = hour - 12
            one_hour_text = ctk.CTkLabel(self.window, text = str(hour) + 'PM', font=('SF Pro', 13), fg_color=self.forecast_widget_bg)
            one_hour_temp = ctk.CTkLabel(self.window, text = str(temp) + '°', font=('SF Pro', 14), fg_color=self.forecast_widget_bg)
            one_hour_text.place(relx=0.17,rely=0.45)
            one_hour_temp.place(relx=0.17,rely=0.608)

        else:
            one_hour_text = ctk.CTkLabel(self.window, text = str(hour) + 'AM', font=('SF Pro', 13), fg_color=self.forecast_widget_bg)
            one_hour_temp = ctk.CTkLabel(self.window, text = str(temp) + '°', font=('SF Pro', 14), fg_color=self.forecast_widget_bg)
            one_hour_text.place(relx=0.17,rely=0.45)
            one_hour_temp.place(relx=0.17,rely=0.608)

        im_lab_one = ctk.CTkLabel(self.bg_behind_forecast, text='', image=im_now, fg_color=self.forecast_widget_bg)
        im_lab_one.place(relx=0.16,rely=0.5, anchor='c')
    
    def set_hr_text_2(self,hour, temp, condition, mode):
        ccondition = self.__image_selector(condition, mode)
        im_now = ctk.CTkImage(
        light_image=Image.open(ccondition),
        dark_image=Image.open(ccondition),
        size=(30,30)
        )
        if(hour >= 12):
            hour = hour - 12
            one_hour_text = ctk.CTkLabel(self.window, text = str(hour) + 'PM', font=('SF Pro', 13), fg_color=self.forecast_widget_bg)
            one_hour_temp = ctk.CTkLabel(self.window, text = str(temp) + '°', font=('SF Pro', 14), fg_color=self.forecast_widget_bg)
            one_hour_text.place(relx=0.24,rely=0.45)
            one_hour_temp.place(relx=0.24,rely=0.608)

        else:
            one_hour_text = ctk.CTkLabel(self.window, text = str(hour) + 'AM', font=('SF Pro', 13), fg_color=self.forecast_widget_bg)
            one_hour_temp = ctk.CTkLabel(self.window, text = str(temp) + '°', font=('SF Pro', 14), fg_color=self.forecast_widget_bg)
            one_hour_text.place(relx=0.24,rely=0.45)
            one_hour_temp.place(relx=0.24,rely=0.608)
        
        im_lab_two = ctk.CTkLabel(self.bg_behind_forecast, text='', image=im_now, fg_color=self.forecast_widget_bg)
        im_lab_two.place(relx=0.23,rely=0.5, anchor='c')

    def set_hr_text_3(self,hour, temp, condition, mode):
        ccondition = self.__image_selector(condition, mode)
        im_now = ctk.CTkImage(
        light_image=Image.open(ccondition),
        dark_image=Image.open(ccondition),
        size=(30,30)
        )
        if(hour >= 12):
            hour = hour - 12
            one_hour_text = ctk.CTkLabel(self.window, text = str(hour) + 'PM', font=('SF Pro', 13), fg_color=self.forecast_widget_bg)
            one_hour_temp = ctk.CTkLabel(self.window, text = str(temp) + '°', font=('SF Pro', 14), fg_color=self.forecast_widget_bg)
            one_hour_text.place(relx=0.31,rely=0.45)
            one_hour_temp.place(relx=0.31,rely=0.608)

        else:
            one_hour_text = ctk.CTkLabel(self.window, text = str(hour) + 'AM', font=('SF Pro', 13), fg_color=self.forecast_widget_bg)
            one_hour_temp = ctk.CTkLabel(self.window, text = str(temp) + '°', font=('SF Pro', 14), fg_color=self.forecast_widget_bg)
            one_hour_text.place(relx=0.31,rely=0.45)
            one_hour_temp.place(relx=0.31,rely=0.608)
        
        im_lab_three = ctk.CTkLabel(self.bg_behind_forecast, text='', image=im_now, fg_color=self.forecast_widget_bg)
        im_lab_three.place(relx=0.31,rely=0.5, anchor='c')

    def set_hr_text_4(self,hour, temp, condition, mode):
        ccondition = self.__image_selector(condition, mode)
        im_now = ctk.CTkImage(
        light_image=Image.open(ccondition),
        dark_image=Image.open(ccondition),
        size=(30,30)
        )
        if(hour >= 12):
            hour = hour - 12
            one_hour_text = ctk.CTkLabel(self.window, text = str(hour) + 'PM', font=('SF Pro', 13), fg_color=self.forecast_widget_bg)
            one_hour_temp = ctk.CTkLabel(self.window, text = str(temp) + '°', font=('SF Pro', 14), fg_color=self.forecast_widget_bg)
            one_hour_text.place(relx=0.38,rely=0.45)
            one_hour_temp.place(relx=0.38,rely=0.608)

        else:
            one_hour_text = ctk.CTkLabel(self.window, text = str(hour) + 'AM', font=('SF Pro', 13), fg_color=self.forecast_widget_bg)
            one_hour_temp = ctk.CTkLabel(self.window, text = str(temp) + '°', font=('SF Pro', 14), fg_color=self.forecast_widget_bg)
            one_hour_text.place(relx=0.38,rely=0.45)
            one_hour_temp.place(relx=0.38,rely=0.608)

        im_lab_four = ctk.CTkLabel(self.bg_behind_forecast, text='', image=im_now, fg_color=self.forecast_widget_bg)
        im_lab_four.place(relx=0.383,rely=0.5, anchor='c')




    
    def set_hr_text_5(self,hour, temp, condition, mode):
        ccondition = self.__image_selector(condition, mode)
        im_now = ctk.CTkImage(
        light_image=Image.open(ccondition),
        dark_image=Image.open(ccondition),
        size=(30,30)
        )
        if(hour >= 12):
            hour = hour - 12
            one_hour_text = ctk.CTkLabel(self.window, text = str(hour) + 'PM', font=('SF Pro', 13), fg_color=self.forecast_widget_bg)
            one_hour_temp = ctk.CTkLabel(self.window, text = str(temp) + '°', font=('SF Pro', 14), fg_color=self.forecast_widget_bg)
            one_hour_text.place(relx=0.45,rely=0.45)
            one_hour_temp.place(relx=0.45,rely=0.608)

        else:
            one_hour_text = ctk.CTkLabel(self.window, text = str(hour) + 'AM', font=('SF Pro', 13), fg_color=self.forecast_widget_bg)
            one_hour_temp = ctk.CTkLabel(self.window, text = str(temp) + '°', font=('SF Pro', 14), fg_color=self.forecast_widget_bg)
            one_hour_text.place(relx=0.45,rely=0.45)
            one_hour_temp.place(relx=0.45,rely=0.608)

        im_lab_five = ctk.CTkLabel(self.bg_behind_forecast, text='', image=im_now, fg_color=self.forecast_widget_bg)
        im_lab_five.place(relx=0.463,rely=0.5, anchor='c')



    def set_hr_text_6(self,hour, temp, condition, mode):
        ccondition = self.__image_selector(condition, mode)
        im_now = ctk.CTkImage(
        light_image=Image.open(ccondition),
        dark_image=Image.open(ccondition),
        size=(30,30)
        )
        if(hour >= 12):
            hour = hour - 12
            one_hour_text = ctk.CTkLabel(self.window, text = str(hour) + 'PM', font=('SF Pro', 13), fg_color=self.forecast_widget_bg)
            one_hour_temp = ctk.CTkLabel(self.window, text = str(temp) + '°', font=('SF Pro', 14), fg_color=self.forecast_widget_bg)
            one_hour_text.place(relx=0.52,rely=0.45)
            one_hour_temp.place(relx=0.52,rely=0.608)

        else:
            one_hour_text = ctk.CTkLabel(self.window, text = str(hour) + 'AM', font=('SF Pro', 13), fg_color=self.forecast_widget_bg)
            one_hour_temp = ctk.CTkLabel(self.window, text = str(temp) + '°', font=('SF Pro', 14), fg_color=self.forecast_widget_bg)
            one_hour_text.place(relx=0.52,rely=0.45)
            one_hour_temp.place(relx=0.52,rely=0.608)

        im_lab_six = ctk.CTkLabel(self.bg_behind_forecast, text='', image=im_now, fg_color=self.forecast_widget_bg)
        im_lab_six.place(relx=0.536,rely=0.5, anchor='c')



    def set_hr_text_7(self,hour, temp, condition, mode):
        ccondition = self.__image_selector(condition, mode)
        im_now = ctk.CTkImage(
        light_image=Image.open(ccondition),
        dark_image=Image.open(ccondition),
        size=(30,30)
        )
        if(hour >= 12):
            hour = hour - 12
            one_hour_text = ctk.CTkLabel(self.window, text = str(hour) + 'PM', font=('SF Pro', 13), fg_color=self.forecast_widget_bg)
            one_hour_temp = ctk.CTkLabel(self.window, text = str(temp) + '°', font=('SF Pro', 14), fg_color=self.forecast_widget_bg)
            one_hour_text.place(relx=0.59,rely=0.45)
            one_hour_temp.place(relx=0.59,rely=0.608)

        else:
            one_hour_text = ctk.CTkLabel(self.window, text = str(hour) + 'AM', font=('SF Pro', 13), fg_color=self.forecast_widget_bg)
            one_hour_temp = ctk.CTkLabel(self.window, text = str(temp) + '°', font=('SF Pro', 14), fg_color=self.forecast_widget_bg)
            one_hour_text.place(relx=0.59,rely=0.45)
            one_hour_temp.place(relx=0.59,rely=0.608)

        im_lab_seven = ctk.CTkLabel(self.bg_behind_forecast, text='', image=im_now, fg_color=self.forecast_widget_bg)
        im_lab_seven.place(relx=0.612,rely=0.5, anchor='c')


    
    def set_hr_text_8(self,hour, temp, condition, mode):
        ccondition = self.__image_selector(condition, mode)
        im_now = ctk.CTkImage(
        light_image=Image.open(ccondition),
        dark_image=Image.open(ccondition),
        size=(30,30)
        )
        if(hour >= 12):
            hour = hour - 12
            one_hour_text = ctk.CTkLabel(self.window, text = str(hour) + 'PM', font=('SF Pro', 13), fg_color=self.forecast_widget_bg)
            one_hour_temp = ctk.CTkLabel(self.window, text = str(temp) + '°', font=('SF Pro', 14), fg_color=self.forecast_widget_bg)
            one_hour_text.place(relx=0.66,rely=0.45)
            one_hour_temp.place(relx=0.66,rely=0.608)

        else:
            one_hour_text = ctk.CTkLabel(self.window, text = str(hour) + 'AM', font=('SF Pro', 13), fg_color=self.forecast_widget_bg)
            one_hour_temp = ctk.CTkLabel(self.window, text = str(temp) + '°', font=('SF Pro', 14), fg_color=self.forecast_widget_bg)
            one_hour_text.place(relx=0.66,rely=0.45)
            one_hour_temp.place(relx=0.66,rely=0.608)

        im_lab_eight = ctk.CTkLabel(self.bg_behind_forecast, text='', image=im_now, fg_color=self.forecast_widget_bg)
        im_lab_eight.place(relx=0.688,rely=0.5, anchor='c')


    def set_hr_text_9(self,hour, temp, condition, mode):
        ccondition = self.__image_selector(condition, mode)
        im_now = ctk.CTkImage(
        light_image=Image.open(ccondition),
        dark_image=Image.open(ccondition),
        size=(30,30)
        )
        if(hour >= 12):
            hour = hour - 12
            one_hour_text = ctk.CTkLabel(self.window, text = str(hour) + 'PM', font=('SF Pro', 13), fg_color=self.forecast_widget_bg)
            one_hour_temp = ctk.CTkLabel(self.window, text = str(temp) + '°', font=('SF Pro', 14), fg_color=self.forecast_widget_bg)
            one_hour_text.place(relx=0.73,rely=0.45)
            one_hour_temp.place(relx=0.73,rely=0.608)

        else:
            one_hour_text = ctk.CTkLabel(self.window, text = str(hour) + 'AM', font=('SF Pro', 13), fg_color=self.forecast_widget_bg)
            one_hour_temp = ctk.CTkLabel(self.window, text = str(temp) + '°', font=('SF Pro', 14), fg_color=self.forecast_widget_bg)
            one_hour_text.place(relx=0.73,rely=0.45)
            one_hour_temp.place(relx=0.73,rely=0.608)

        im_lab_nine = ctk.CTkLabel(self.bg_behind_forecast, text='', image=im_now, fg_color=self.forecast_widget_bg)
        im_lab_nine.place(relx=0.765,rely=0.5, anchor='c')


    def set_hr_text_10(self,hour, temp, condition, mode):
        ccondition = self.__image_selector(condition, mode)
        im_now = ctk.CTkImage(
        light_image=Image.open(ccondition),
        dark_image=Image.open(ccondition),
        size=(30,30)
        )
        if(hour >= 12):
            hour = hour - 12
            one_hour_text = ctk.CTkLabel(self.window, text = str(hour) + 'PM', font=('SF Pro', 13), fg_color=self.forecast_widget_bg)
            one_hour_temp = ctk.CTkLabel(self.window, text = str(temp) + '°', font=('SF Pro', 14), fg_color=self.forecast_widget_bg)
            one_hour_text.place(relx=0.80,rely=0.45)
            one_hour_temp.place(relx=0.80,rely=0.608)

        else:
            one_hour_text = ctk.CTkLabel(self.window, text = str(hour) + 'AM', font=('SF Pro', 13), fg_color=self.forecast_widget_bg)
            one_hour_temp = ctk.CTkLabel(self.window, text = str(temp) + '°', font=('SF Pro', 14), fg_color=self.forecast_widget_bg)
            one_hour_text.place(relx=0.80,rely=0.45)
            one_hour_temp.place(relx=0.80,rely=0.608)

        im_lab_ten = ctk.CTkLabel(self.bg_behind_forecast, text='', image=im_now, fg_color=self.forecast_widget_bg)
        im_lab_ten.place(relx=0.839,rely=0.5, anchor='c')

    
    def set_hr_text_11(self,hour, temp, condition, mode):
        ccondition = self.__image_selector(condition, mode)
        im_now = ctk.CTkImage(
        light_image=Image.open(ccondition),
        dark_image=Image.open(ccondition),
        size=(30,30)
        )
        if(hour >= 12):
            hour = hour - 12
            one_hour_text = ctk.CTkLabel(self.window, text = str(hour) + 'PM', font=('SF Pro', 13), fg_color=self.forecast_widget_bg)
            one_hour_temp = ctk.CTkLabel(self.window, text = str(temp) + '°', font=('SF Pro', 14), fg_color=self.forecast_widget_bg)
            one_hour_text.place(relx=0.87,rely=0.45)
            one_hour_temp.place(relx=0.87,rely=0.608)

        else:
            one_hour_text = ctk.CTkLabel(self.window, text = str(hour) + 'AM', font=('SF Pro', 13), fg_color=self.forecast_widget_bg)
            one_hour_temp = ctk.CTkLabel(self.window, text = str(temp) + '°', font=('SF Pro', 14), fg_color=self.forecast_widget_bg)
            one_hour_text.place(relx=0.87,rely=0.45)
            one_hour_temp.place(relx=0.87,rely=0.608)

        im_lab_eleven = ctk.CTkLabel(self.bg_behind_forecast, text='', image=im_now, fg_color=self.forecast_widget_bg)
        im_lab_eleven.place(relx=0.915,rely=0.5, anchor='c')
        

    def animate_button(self):

        print('penis')
        if self.button_in_start:
            if self.button_pos < self.button_end:
                self.button_pos+=0.008
                print(self.button_pos)
                self.button.place(relx=self.button_pos,rely=0.03)
                self.window.after(10,self.animate_button())
            self.button_in_start = False    



    def mainloop(self):
        return self.window.mainloop()    


class side_panel(ctk.CTkFrame):#trying side panel as its own class
    def __init__(self,parent,start_pos,end_pos,fgcolor):
        super().__init__(master=parent, fg_color=fgcolor)

        self.width = abs(start_pos - end_pos)
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.pos = start_pos
        self.in_start = True


        self.place(relx = self.start_pos, rely = 0, relheight=1)

    def animate(self):
        if self.in_start:
            self.animate_forwards()

        else:
            self.animate_backwards()


    def animate_forwards(self):

        if self.pos < self.end_pos:
            self.pos += 0.008
            self.place(relx = self.pos, rely = 0, relheight=1)
            self.tkraise()

            self.after(10,self.animate_forwards())

    def animate_backwards(self):

        if self.pos > self.end_pos:
            self.pos -= 0.008
            self.place(relx = self.pos, rely = 0, relheight=1)
            self.tkraise()

            self.after(10,self.animate_backwards())

    def update_fg(self,fgcolor):
        self.configure(fg_color=fgcolor)




#make a class for button to animate bc its not working rn :<

class side_button(ctk.CTkButton):
    def __init__(self, parent, starting_pos, ending_pos):
        super().__init__(master=parent)

        self.start_pos = starting_pos
        self.end_pos = ending_pos
        self.pos = starting_pos
        self.in_start = True

        #relx = 0.01, rely = 0.03,
        self.place(relx = self.start_pos, rely = 0.03)

    def animate(self):
        if self.in_start:
            self.animate_forwards()

        else:
            self.animate_backwards()


    def animate_forwards(self):

        if self.pos < self.end_pos:
            self.pos += 0.008
            self.place(relx = self.pos, rely = 0.03)

            self.after(10,self.animate_forwards())

    def update_fg(self,fgcolor):
        self.configure(text='',fg_color=fgcolor, width=20, height=20)

#(self.window,text='',width=20,height=20, command=lambda:[self.animate_button(), self.animated_panel.animate()])