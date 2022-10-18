import csv 
import os
import matplotlib.pyplot as plt 
import numpy as np 
from elm_measurement_analyzer import ELM_MeasurementAnalyzer

def find_csv_filenames( path_to_dir, suffix=".csv" ):
    filenames = os.listdir(path_to_dir)
    return [ filename for filename in filenames if filename.endswith( suffix ) ]

if __name__ == "__main__":
    print ("Hello world ! "); 

    csv_filenames = find_csv_filenames('vw_golf_worktrips')
    
    filepaths = [] 

    for file in csv_filenames:
        filepaths.append(f'vw_golf_worktrips/{file}')
    
    measurement_dictionary = {} 

    with open(filepaths[0], newline='', encoding="utf-8") as csvfile:
        trip_reader = list(csv.reader(csvfile, delimiter=';', quotechar='|'))
    
        # for dict_key in trip_reader[0]:
        #     if(len(dict_key) > 0):
        #         key = dict_key.split('"')[1]
        #         measurement_dictionary[dict_key] = None

        measurement_list_first = [] 
        measurement_list_second = []
        measurement_list_third = [] 
        measurement_list_fourth = [] 

        measurements_list_of_lists = [] 


        for record in trip_reader[1:]:
            measurement_list_first.append(record[0])
            measurement_list_second.append(record[1])
            measurement_list_third.append(record[2])
            measurement_list_fourth.append(record[3])
            
        measurement_dictionary['SECONDS'] = measurement_list_first
        measurement_dictionary['PID'] = measurement_list_second
        measurement_dictionary['VALUE'] = measurement_list_third
        measurement_dictionary['UNITS'] = measurement_list_fourth

    measurement_types = list(set(measurement_dictionary['PID']))

    list_of_measurement_types = [[el] for el in measurement_types]

    for meas_number, value in enumerate(measurement_dictionary['PID']):
        for pid_no, elem in enumerate(measurement_types):
            if elem == value:
                list_of_measurement_types[pid_no].append(measurement_dictionary['VALUE'][meas_number].split('"')[1])
    

    measurement_dictionary = {}

    for pid_measurement in list_of_measurement_types:
        measurement_dictionary[pid_measurement[0]] = np.asarray([float(x) for x in pid_measurement[1:]])
    

    for key, value in measurement_dictionary.items():
        print(f'{key}')
    

    meas_list =  measurement_dictionary['"[DASH] Poziom paliwa"']
    distance_km =  measurement_dictionary['"Pokonany dystans"']
    obroty =  measurement_dictionary['"Oil max level"']

    injection_deviation1 = measurement_dictionary['"Injection amount deviation cylinder 1"']
    injection_deviation2 = measurement_dictionary['"Injection amount deviation cylinder 2"']
    injection_deviation3 = measurement_dictionary['"Injection amount deviation cylinder 3"']
    injection_deviation4 = measurement_dictionary['"Injection amount deviation cylinder 4"']

    plt.figure(1)
    plt.title('Analiza przejazdu')
    plt.plot(meas_list, label= 'Poziom paliwa[L]')
    plt.plot(distance_km, label = 'Przebyty dystans [km]')
    plt.legend()

    plt.figure(2)
    plt.title('Obroty silnika')
    plt.plot(obroty)
    

    plt.figure(3)
    plt.title('Odchyłki wtrysków ')
    plt.plot(injection_deviation1, label = 'Cylinder 1')
    plt.plot(injection_deviation2, label = 'Cylinder 2')
    plt.plot(injection_deviation3, label = 'Cylinder 3')
    plt.plot(injection_deviation4, label = 'Cylinder 4')
    plt.legend()
    plt.show()