from models.weather import Weather
import statistics 

# Build weather response dict
def construct_weather(city, weather_list):
    # Init empty lists for data processing
    weather_data = []
    weather_temp_data_points = []
    min_temp_list = []
    max_temp_list = []
    humidity_list = []
    time_list = []

    # Process raw weather data to construct required data points
    for x in weather_list:
        weather_obj = Weather(x['dt_txt'], x['main']['temp_min'], x['main']['temp_max'], x['main']['humidity'])
        weather_data.append(weather_obj.__dict__)
        weather_temp_data_points.append(x['main']['temp_min'])
        weather_temp_data_points.append(x['main']['temp_max'])
        min_temp_list.append(x['main']['temp_min'])
        max_temp_list.append(x['main']['temp_max'])
        humidity_list.append(x['main']['humidity'])
        time_list.append(x['dt_txt'])
    
    # Calculate average temp for periods
    pre_avg = 0
    for x in weather_temp_data_points:
        pre_avg += x
    weather_avg = pre_avg / len(weather_temp_data_points)

    # Calculate median temp for periods
    weather_median = statistics.median(weather_temp_data_points)
    
    # Create graph min temp values as string
    min_temp_list_string = ""
    for x in min_temp_list:
        min_temp_list_string = min_temp_list_string + str(x) + ","
    min_temp_list_string = min_temp_list_string[:-1]

    # Create graph max temp values as string
    max_temp_list_string = ""
    for x in max_temp_list:
        max_temp_list_string = max_temp_list_string + str(x) + ","
    max_temp_list_string = max_temp_list_string[:-1]

    # Create graph humidity values as string
    humidity_list_string = ""
    for x in humidity_list:
        humidity_list_string = humidity_list_string + str(x) + ","
    humidity_list_string = humidity_list_string[:-1]

    # Create x axis labels where 03 = 03:00
    x_axis_labels = ""
    for x in time_list:
        x_axis_labels = x_axis_labels + "|" + x[11] + x[12]    

    # Generate humidty graph with strings using Google Chart Image API
    weather_list_len = len(weather_list)    
    chart_width = str(int(weather_list_len * 20.5 + 20))
    graph_url = ("https://chart.googleapis.com/chart?chs=" 
        # + chart_width
        + "820x300&cht=bvo&chd=t:" 
        + min_temp_list_string 
        + "|" 
        + max_temp_list_string 
        + "|" 
        + humidity_list_string 
        + "&chxl=0:"
        + x_axis_labels
        + "&chbh=a&chco=ebbd34,eb4034,80f4ff&chxt=x,y&chxs=0,393939,12,0,lt|1,393939,10,1,lt")

    # Response dict
    data = {
        'status': 200,
        'msg': 'Success',
        'city': city,
        'weather_data_points': weather_data,
        'temp_average': round(weather_avg, 2),
        'temp_mean': round(weather_median, 2),
        'graph_url': graph_url
    }    
    return data