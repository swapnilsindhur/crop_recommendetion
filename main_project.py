import pandas as pd
from sklearn import preprocessing
import numpy as np
from sklearn.neighbors import KNeighborsClassifier


excel = pd.read_csv("Crop_recommendation.csv",header=0) 
print(excel)                                                             
print(excel.shape)


le=preprocessing.LabelEncoder()
label=le.fit_transform(list(excel["label"]))
N = list(excel["N"])                                  
P = list(excel["P"])                                  
K = list(excel["K"])                                  
temperature = list(excel["temperature"])                                 
humidity = list(excel["humidity"])                                 
ph = list(excel["ph"])                                 
rainfall = list(excel["rainfall"])  


features = list(zip(N,P,K,temperature,humidity,ph,rainfall))
features=np.array([N,P,K,temperature,humidity,ph,rainfall])
features=features.transpose()
print(features.shape) 
print(label.shape)  


model = KNeighborsClassifier(n_neighbors=3)  
model.fit(features,label) 



import PySimpleGUI as sg  

layout = [[sg.Text('                      Crop Recommendation software', font=("Helvetica", 30), text_color = 'white')],                                                                                                         
         [sg.Text('Required details :-', font=("Helvetica", 20))],                                                                                         
         [sg.Text('Enter Nitrogen content in the soil                                  :', font=("Helvetica", 20)), sg.Input(font=("Helvetica",20), size = (20,1) )],
         [sg.Text('Enter Phosphorous content in the soil                           :', font=("Helvetica", 20)), sg.Input(font=("Helvetica", 20),size = (20,1))],
         [sg.Text('Enter Potassium content in the soil                               :', font=("Helvetica", 20)), sg.Input(font=("Helvetica", 20),size = (20,1))],
         [sg.Text('Enter average Temperature in the field                          :', font=("Helvetica", 20)), sg.Input(font=("Helvetica", 20),size = (20,1)), sg.Text('*C', font=("Helvetica", 20))], 
         [sg.Text('Enter average Humidity around the field(percentage)     :', font=("Helvetica", 20)), sg.Input(font=("Helvetica", 20),size = (20,1)), sg.Text('%', font=("Helvetica", 20))], 
         [sg.Text('Enter PH value of the soil                                              :', font=("Helvetica", 20)), sg.Input(font=("Helvetica", 20),size = (20,1))], 
         [sg.Text('Enter average Rainfall around the field                          :', font=("Helvetica", 20) ), sg.Input(font=("Helvetica", 20),size = (20,1)),sg.Text('mm', font=("Helvetica", 20))],
         [sg.Text(size=(50,1),font=("Helvetica",20) , text_color = 'yellow', key='-OUTPUT1-' )],
         [sg.Button('Submit', font=("Helvetica", 20)),sg.Button('Next', font=("Helvetica", 20))] ]
window = sg.Window('Crop Recommendation software', layout) 



while True: 
	event, values = window.read()
	if event == sg.WINDOW_CLOSED or event == 'Next':                                                                                            
		break
	print(values[0])
	nitrogen_content =         values[0]                                                                                                        
	phosphorus_content =       values[1]                                                                                                        
	potassium_content =        values[2]                                                                                                        
	temperature_content =      values[3]                                                                                                        
	humidity_content =         values[4]                                                                                                       
	ph_content =               values[5]                                                                                                        
	rainfall =                 values[6]                                                                                                        
	predict1 = np.array([nitrogen_content,phosphorus_content, potassium_content, temperature_content, humidity_content, ph_content, rainfall])  
	print(predict1)                                                                                                                            
	predict1 = predict1.reshape(1,-1)                                                                             
	print(predict1)                                                                                                
	predict1 = model.predict(predict1)                                                                             
	print(predict1)                                                                                                
	crop_name = str()
	if predict1 == 0:                                                                                               
		crop_name = 'Apple'
	elif predict1 == 1:
		crop_name = 'Banana'
	elif predict1 == 2:
		crop_name = 'Blackgram'
	elif predict1 == 3:
		crop_name = 'Chickpea'
	elif predict1 == 4:
		crop_name = 'Coconut'
	elif predict1 == 5:
		crop_name = 'Coffee'
	elif predict1 == 6:
		crop_name = 'Cotton'
	elif predict1 == 7:
		crop_name = 'Grapes'
	elif predict1 == 8:
		crop_name = 'Jute'
	elif predict1 == 9:
		crop_name = 'Kidneybeans'
	elif predict1 == 10:
		crop_name = 'Lentil'
	elif predict1 == 11:
		crop_name = 'Maize'
	elif predict1 == 12:
		crop_name = 'Mango'
	elif predict1 == 13:
		crop_name = 'Mothbeans'
	elif predict1 == 14:
		crop_name = 'Mungbeans'
	elif predict1 == 15:
		crop_name = 'Muskmelon'
	elif predict1 == 16:
		crop_name = 'Orange'
	elif predict1 == 17:
		crop_name = 'Papaya'
	elif predict1 == 18:
		crop_name = 'Pigeonpeas'
	elif predict1 == 19:
		crop_name = 'Pomegranate'
	elif predict1 == 20:
		crop_name = 'Rice'
	elif predict1 == 21:
		crop_name = 'Watermelon'

	if int(humidity_content) >=1 and int(humidity_content)<= 33 :                                                
		humidity_level = 'low'
	elif int(humidity_content) >=34 and int(humidity_content) <= 66:
		humidity_level = 'medium'
	else:
		humidity_level = 'high'

	if int(temperature_content) >= 0 and int(temperature_content)<= 6:                                           
		temperature_level = 'cool'
	elif int(temperature_content) >=7 and int(temperature_content) <= 25:
		temperature_level = 'warm'
	else:
		temperature_level= 'hot' 

	if int(rainfall) >=1 and int(rainfall) <= 100:                                                             
		rainfall_level = 'less'
	elif int(rainfall) >= 101 and int(rainfall) <=200:
		rainfall_level = 'moderate'
	elif int(rainfall) >=201:
		rainfall_level = 'heavy'

	if int(nitrogen_content) >= 1 and int(nitrogen_content) <= 50:                                            
		nitrogen_level = 'less'
	elif int(nitrogen_content) >=51 and int(nitrogen_content) <=100:
		nitrogen_level = 'medium'
	elif int(nitrogen_content) >=101:
		nitrogen_level = 'high'

	if int(phosphorus_content) >= 1 and int(phosphorus_content) <= 50:                                        
		phosphorus_level = 'less'
	elif int(phosphorus_content) >= 51 and int(phosphorus_content) <=100:
		phosphorus_level = 'medium'
	elif int(phosphorus_content) >=101:
		phosphorus_level = 'high'

	if int(potassium_content) >= 1 and int(potassium_content) <=50:                                           
		potassium_level = 'less'
	elif int(potassium_content) >= 51 and int(potassium_content) <= 100:
		potassium_level = 'medium'
	elif int(potassium_content) >=101:
		potassium_level = 'high'

	if float(ph_content) >=0 and float(ph_content) <=5:                                                       
		phlevel = 'acidic' 
	elif float(ph_content) >= 6 and float(ph_content) <= 8:
		phlevel = 'neutral'
	elif float(ph_content) >= 9 and float(ph_content) <= 14:
		phlevel = 'alkaline'
	
	print(crop_name)
	print(humidity_level)
	print(temperature_level)
	print(rainfall_level)
	print(nitrogen_level)
	print(phosphorus_level)
	print(potassium_level)
	print(phlevel)



    
window.close() 
layout = [[sg.Text('Recommended Crop is: ' + crop_name, font=("Helvetica", 30), text_color = 'yellow')],                                                                                                         
         [sg.Text('Report :-', font=("Helvetica", 20))],
         [sg.Text('Humidity level : ' + humidity_level, font=("Helvetica", 20))],
         [sg.Text('Temperature level : ' + temperature_level, font=("Helvetica", 20))],
         [sg.Text('Rainfall level : ' + rainfall_level, font=("Helvetica", 20))],
         [sg.Text('Nitrogen level : ' + nitrogen_level, font=("Helvetica", 20))],
         [sg.Text('Phosphorus level : ' + phosphorus_level, font=("Helvetica", 20))],
         [sg.Text('Potassium level : ' + potassium_level, font=("Helvetica", 20))],
         [sg.Button('Ok', font=("Helvetica", 20))]
        #  [sg.Text('PH level :', + phlevel,font=("Helvetica", 20))]
         ]
window = sg.Window('something', layout) 
while True: 
	event, values = window.read()
	if event == sg.WINDOW_CLOSED or event == 'Ok':                                                                                            
		break
window.close() 
    
