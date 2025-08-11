import requests

url = "http://127.0.0.1:8000/score"
payload = {
 'Fault':'Policy Holder',
 'PolicyType':'Sedan - All Perils',
 'VehicleCategory':'Sedan',
 'Month':'May',
 'VehiclePrice':'20000 to 29000',
 'Make':'BMW',
 'DayOfWeek':'Monday',
 'AgeOfVehicle':'6 years',
 'Deductible':'500',
 'Sex':'Female',
 'AccidentArea':'Urban',
 'AgentType':'External',
 'WeekOfMonthClaimed':'3'
    
}
response = requests.post(url, json=payload)

print(response.json())


# ['Policy Holder' 'Third Party']
# ['Sedan - All Perils' 'Sedan - Collision' 'Sport - Liability'
#  'Sport - Collision' 'Utility - All Perils' 'Utility - Collision'
#  'Utility - Liability' 'Sport - All Perils']
# ['Sedan' 'Sport' 'Utility']
# ['Aug' 'Dec' 'Feb' 'Jun' 'Jan' 'Nov' 'Jul' 'May' 'Oct' 'Sep' 'Mar' 'Apr']
# ['30000 to 39000' '20000 to 29000' 'less than 20000' 'more than 69000'
#  '40000 to 59000' '60000 to 69000']
# ['Honda' 'Chevrolet' 'Pontiac' 'Toyota' 'Mazda' 'Ford' 'Accura' 'Mercury'
#  'VW' 'Saturn' 'Dodge' 'Saab' 'BMW' 'Nisson' 'Porche' 'Ferrari' 'Jaguar'
#  'Mecedes']
# ['Friday' 'Tuesday' 'Sunday' 'Monday' 'Thursday' 'Wednesday' 'Saturday']
# ['7 years' '5 years' '6 years' '3 years' 'more than 7' 'new' '2 years'
#  '4 years']
# [400 500 700 300]
# ['Male' 'Female']
# ['Urban' 'Rural']
# ['External' 'Internal']
# [5 3 4 2 1]



