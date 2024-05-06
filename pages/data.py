SurveyName="New Untitled Survey"
Longitude=""
Lattitude=""
Intervals=0
Elevation=""
profile = 1
value=""
global Station
Station= 0

dataset={"Station":[],"Inphase":[],"Outphase":[],"Longitude":[],"Lattitude":[],"Elevation":[]}

def add_data(Inphase,Outphase,Longitude,Lattitude,Elevation):
	global Station
	dataset["Station"]+=[Station]
	Station = Station + Intervals
	dataset["Inphase"]+=[Inphase]
	dataset["Outphase"]+=[Outphase]
	dataset["Longitude"]+=[Longitude]
	dataset["Lattitude"]+=[Lattitude]
	dataset["Elevation"]+=[Elevation]

def config():
	dataset={"Station":[],"Inphase":[],"Outphase":[],"Longitude":[],"Lattitude":[],"Elevation":[]}

