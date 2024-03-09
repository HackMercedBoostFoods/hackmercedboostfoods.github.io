import crops
class map():
#location: geographic region of crop
#Rows, cols: dimensions of the crop field, each measured in mi
    
#possibly change average_rain and average_temp to use a season object
#season object stores weather for that particular season

#possibly use soil quality
    def __init__(self, location, rows, cols, average_rain, average_temp):
        self.location = location
        self.crop_plot = [[0] *cols][rows]
        self.average_rain = average_rain
        self.average_temp = average_temp
    
    

    