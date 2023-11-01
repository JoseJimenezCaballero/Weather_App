from Weather_class import weather_api
from gui import gui
import requests
import json
import math

weather = weather_api('Tampa')
gui_ = gui()
gui_.bg_setter(weather.get_current_condition(),weather.get_mode())
gui_.set_settings_button_img(weather.get_current_condition(), weather.get_mode())
gui_.set_city(weather.get_city())
gui_.set_high(weather.get_current_max_temp())
gui_.set_low(weather.get_current_low_temp())
gui_.set_condition(weather.get_current_condition())
gui_.set_bg_forecast()
gui_.set_temp(weather.get_current_temp_f())
gui_.set_hr_text_now(weather.get_current_temp_f(), weather.get_current_condition(), weather.get_mode())
gui_.set_hr_text_1(weather.get_hour(1), weather.get_hour_temp_f(1), weather.get_hour_condition(1), weather.get_mode())
gui_.set_hr_text_2(weather.get_hour(2), weather.get_hour_temp_f(2), weather.get_hour_condition(2), weather.get_mode())
gui_.set_hr_text_3(weather.get_hour(3), weather.get_hour_temp_f(3), weather.get_hour_condition(3), weather.get_mode())
gui_.set_hr_text_4(weather.get_hour(4), weather.get_hour_temp_f(4), weather.get_hour_condition(4), weather.get_mode())
gui_.set_hr_text_5(weather.get_hour(5), weather.get_hour_temp_f(5), weather.get_hour_condition(5), weather.get_mode())
gui_.set_hr_text_6(weather.get_hour(6), weather.get_hour_temp_f(6), weather.get_hour_condition(6), weather.get_mode())
gui_.set_hr_text_7(weather.get_hour(7), weather.get_hour_temp_f(7), weather.get_hour_condition(7), weather.get_mode())
gui_.set_hr_text_8(weather.get_hour(8), weather.get_hour_temp_f(8), weather.get_hour_condition(8), weather.get_mode())
gui_.set_hr_text_9(weather.get_hour(9), weather.get_hour_temp_f(9), weather.get_hour_condition(9), weather.get_mode())
gui_.set_hr_text_10(weather.get_hour(10), weather.get_hour_temp_f(10), weather.get_hour_condition(10), weather.get_mode())
gui_.set_hr_text_11(weather.get_hour(11), weather.get_hour_temp_f(11), weather.get_hour_condition(11), weather.get_mode())
#fix the mode being set at once and not changing depending on the time, basically create an hourly fucntion that gets the mode 
#based on the is day value of the api. -.- 

#was woeking on implementing the color bg for the settings background to then do the animation



gui_.mainloop()

