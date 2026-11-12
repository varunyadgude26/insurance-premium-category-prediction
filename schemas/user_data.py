from pydantic import BaseModel,Field,computed_field,field_validator
from typing import Annotated,Literal
from config.config import city_tier_2,city_tier_1


class UserData(BaseModel):
    age: Annotated[int,Field(...,description='Age of the person',gt=0,lt=100,examples=[25,65,63])]
    weight : Annotated[float,Field(...,description='weight of the person in KG',gt=1.0,examples=[52.0,65.0])]
    height : Annotated[float,Field(...,description='height of the person in mts',gt=0,examples=[1.25,1.01])]
    income_lpa : Annotated[float,Field(...,description='Income of the person in lakhs',gt=0,examples=[2.12,5.25])]
    smoker : Annotated[Literal[True,False],Field(...,description='Is person a smoker')]
    city : Annotated[str,Field(...,description='Resident City of the person')]
    occupation : Annotated[Literal['retired','freelancer','student','government_job','business_owner','unemployed','private_job'],Field(...,description='Select one Occupation')]

    @field_validator('city')
    @classmethod
    def validate_city(cls,value):
        v = value.lower()
        return v

    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight/(self.height**2),2)

    @computed_field
    @property
    def life_risk(self) ->str:
        if self.smoker and self.bmi > 30:
            return "high"
        elif self.smoker or self.bmi > 27:
            return "medium"
        else:
            return "low"
        
    @computed_field
    @property
    def age_group(self) ->str:
        if self.age < 25:
            return "young"
        elif self.age < 45:
            return "adult"
        elif self.age < 60:
            return "middle_aged"
        return "senior"

    @computed_field
    @property
    def city_tier(self)->str:
        if self.city in city_tier_1:
            return 'tier1'
        elif self.city in city_tier_2:
            return 'tier2'
        else:
            return 'tier3' 
