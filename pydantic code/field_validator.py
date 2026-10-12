from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: str
    email: str
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains = ['city.com', 'dbbl.com']
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        
        return value

    def update_patient_data(self):  # Added 'self' parameter
        print(self.name)
        print(self.age)
        print(self.weight)
        print(self.allergies)
        print(self.contact_details)
        print('updated into database successfully')

# Moved outside the class
patient_info = {
    'name': 'afrin', 
    'age': 25, 
    'email': 'abc@city.com',  
    'weight': 53.0,  
    'allergies': ['pollen', 'dust'],
    'married': False,  # Added missing required field
    'contact_details': {'email': 'afrin@gmail.com', 'phone': '98704563'}
} 

patient_1 = Patient(**patient_info)
patient_1.update_patient_data()  # Called as instance method