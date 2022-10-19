import csv 

class ELM_MeasurementAnalyzer:

    def __init__(self, csv_filename: str):

        measurement_dictionary = {} 

        with open(csv_filename, newline='', encoding="utf-8") as csvfile:
            trip_reader = list(csv.reader(csvfile, delimiter=';', quotechar='|'))

            # TODO - refactor this 

            measurement_list_first = [] 
            measurement_list_second = []
            measurement_list_third = [] 
            measurement_list_fourth = [] 

            for record in trip_reader[1:]:
                measurement_list_first.append(record[0])
                measurement_list_second.append(record[1])
                measurement_list_third.append(record[2])
                measurement_list_fourth.append(record[3])
                
            measurement_dictionary['SECONDS'] = measurement_list_first
            measurement_dictionary['PID'] = measurement_list_second
            measurement_dictionary['VALUE'] = measurement_list_third
            measurement_dictionary['UNITS'] = measurement_list_fourth

        # Get unique measurement types from whole measurement 
        measurement_types = list(set(measurement_dictionary['PID']))


        list_of_measurement_types = [[el] for el in measurement_types]

        for meas_number, meas_name in enumerate(measurement_dictionary['PID']):
            for pid_number, pid_meas_name in enumerate(measurement_types):
                if pid_meas_name == meas_name:
                    # extract time value and unit parameters from measurement 
                    time =  round (float(measurement_dictionary['SECONDS'][meas_number].split('"')[1]) - float(measurement_dictionary['SECONDS'][0].split('"')[1]))
                    value = float(measurement_dictionary['VALUE'][meas_number].split('"')[1])
                    unit = measurement_dictionary['UNITS'][meas_number].split('"')[1]

                    list_of_measurement_types[pid_number].append((time, value, unit))

        for pid_measurement in list_of_measurement_types:
            measurement_dictionary[pid_measurement[0]] = pid_measurement[1:]
            
        self.measurement =  dict( sorted(measurement_dictionary.items(), key=lambda x: x[0].lower()) ) 

    
    def get_measurement(self) -> dict:
        return self.measurement