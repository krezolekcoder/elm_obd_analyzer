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
    
    meas_analyzer = ELM_MeasurementAnalyzer(filepaths[0])

    measurement_dictionary = meas_analyzer.get_measurement()
    
    meas_list =  measurement_dictionary['"[DASH] Poziom paliwa"']

    time_measurement = np.asarray([el[0] for el in meas_list]) / 60.0
    value_measurement = [el[1] for el in meas_list]
    unit_type = [el[2] for el in meas_list]

    plt.figure(1)
    plt.title('Analiza spalania')
    plt.plot(time_measurement, value_measurement)
    plt.xlabel('Czas [m]')
    plt.ylabel(f'Poziom paliwa {unit_type[0]}')
    plt.legend()
    plt.show() 
