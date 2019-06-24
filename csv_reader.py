import csv

class Main():
    def __init__(self, filename):
        with open(filename, "r") as f_input:
            csv_input = csv.reader(f_input)
            self.details = list(csv_input)

    def get_col_row(self, col, row):
        return self.details[row-1][col-1]

data = Main("vehicle.csv")

i=0
j=0
check = 'true'
while  check == 'true':
	vehicle_id = data.get_col_row(i, j)
	print(vehicle_id)
	id, latitude, longitude = [(n) for n in vehicle_id.split(",")]
	if (latitude == '42.743301' and longitude == '-78.425315'):
		print(id)
		check = 'false'
	else:
		i=i+1;
		j=j+1;
