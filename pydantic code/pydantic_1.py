from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50, title='Name of the patient',
                               description='Give me the name of the patient less than 40 characters', 
                               examples=['afrin', 'arin'])]
    
    age: Annotated[int, Field(gt=0, lt=35)]
    email: EmailStr
    linkedin_url: AnyUrl
    weight: Optional[float] = None
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

def insert_patient_data(patient_1: Patient):
    print(patient_1.name)
    print(patient_1.age)
    print(patient_1.weight)
    print(patient_1.allergies)
    print(patient_1.contact_details)
    print('inserted into database successfully')

def update_patient_data(patient_1: Patient):
    print(patient_1.name)
    print(patient_1.age)
    print(patient_1.weight)
    print(patient_1.allergies)
    print(patient_1.contact_details)
    print('updated into database successfully')  # Changed from 'inserted'

patient_info = {'name': 'afrin', 'age': 25, 'email': 'afrin@gmail.com', 
                'linkedin_url': 'http://linkedin.com/2326', 'weight': 53.0,  # Fixed: float instead of string
                'allergies': ['pollen', 'dust'],
                'contact_details': {'email': 'afrin@gmail.com', 'phone': '98704563'}} 

patient_1 = Patient(**patient_info)
insert_patient_data(patient_1)