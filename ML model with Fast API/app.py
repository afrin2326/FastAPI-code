from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Literal, Annotated
import pickle
import pandas as pd

# import the ml model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

app = FastAPI()

# Bangladesh Cities - Tier 1 (Major Metropolitan Cities)
tier_1_cities = ["Dhaka", "Chittagong", "Gazipur", "Narayanganj", "Khulna", "Rajshahi", "Sylhet", "Rangpur"]

# Bangladesh Cities - Tier 2 (Important Cities)
tier_2_cities = [
    "Mymensingh", "Barishal", "Comilla", "Narsingdi", "Jessore", "Bogra", "Cox's Bazar", "Dinajpur",
    "Nawabganj", "Tangail", "Sirajganj", "Pabna", "Naogaon", "Faridpur", "Brahmanbaria", "Kushtia",
    "Satkhira", "Madaripur", "Gopalganj", "Manikganj", "Munshiganj", "Noakhali", "Feni", "Lakshmipur",
    "Chandpur", "Habiganj", "Maulvibazar", "Sunamganj", "Netrokona", "Sherpur", "Jamalpur", "Kishoreganj",
    "Thakurgaon", "Panchagarh", "Nilphamari", "Lalmonirhat", "Kurigram", "Gaibandha", "Joypurhat",
    "Chapai Nawabganj", "Natore", "Rajbari", "Shariatpur", "Magura", "Jhenaidah", "Meherpur", "Chuadanga",
    "Bagerhat", "Pirojpur", "Jhalokati", "Barguna", "Patuakhali", "Bhola", "Bandarban", "Rangamati",
    "Khagrachari"
]

# pydantic model to validate incoming data
class UserInput(BaseModel):

    age: Annotated[int, Field(..., gt=0, lt=120, description='Age of the user')]
    weight: Annotated[float, Field(..., gt=0, description='Weight of the user (kg)')]
    height: Annotated[float, Field(..., gt=0, lt=2.5, description='Height of the user (meters)')]
    income_lpa: Annotated[float, Field(..., gt=0, description='Annual income of the user in lakhs BDT')]
    smoker: Annotated[bool, Field(..., description='Is user a smoker')]
    city: Annotated[str, Field(..., description='The city that the user belongs to (Bangladesh)')]
    occupation: Annotated[Literal['retired', 'freelancer', 'student', 'government_job',
       'business_owner', 'unemployed', 'private_job'], Field(..., description='Occupation of the user')]
    
    @computed_field
    @property
    def bmi(self) -> float:
        return self.weight/(self.height**2)
    
    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.smoker and self.bmi > 30:
            return "high"
        elif self.smoker or self.bmi > 27:
            return "medium"
        else:
            return "low"
        
    @computed_field
    @property
    def age_group(self) -> str:
        if self.age < 25:
            return "young"
        elif self.age < 45:
            return "adult"
        elif self.age < 60:
            return "middle_aged"
        return "senior"
    
    @computed_field
    @property
    def city_tier(self) -> int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3

@app.get('/')
def root():
    return JSONResponse(status_code=200, content={'message': 'Insurance Premium Prediction API - Bangladesh Version'})

@app.get('/health')
def health_check():
    return JSONResponse(status_code=200, content={'status': 'healthy'})

@app.post('/predict')
def predict_premium(data: UserInput):

    input_df = pd.DataFrame([{
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }])

    prediction = model.predict(input_df)[0]
    
    # Get probabilities if the model supports it
    try:
        probabilities = model.predict_proba(input_df)[0].tolist()
        classes = model.classes_.tolist() if hasattr(model, 'classes_') else ['High', 'Low', 'Medium']
        class_probabilities = dict(zip(classes, probabilities))
        
        confidence = max(probabilities) if probabilities else 1.0
        
        return JSONResponse(status_code=200, content={
            'predicted_category': prediction,
            'confidence': round(confidence, 4),
            'class_probabilities': class_probabilities
        })
    except:
        return JSONResponse(status_code=200, content={'predicted_category': prediction})