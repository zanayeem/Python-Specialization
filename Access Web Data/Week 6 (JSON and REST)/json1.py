#JSON FILE FORMAT AND DATA EXTRACTION 1
import json

data = '''{
    "name" : "Zannatun Nayeem",
    "phone" : {
        "provider" : "Robi",
        "number" : "01847161909"    
    },
    "email" : "nayeem123able@gmail.com"
}'''

info = json.loads(data)
print("Name: ",info["name"])
print("Phone number: ",info["phone"]["number"] ," ", "Provider: ", info["phone"]["provider"])
print("Email: ",info["email"])



