from pydantic import BaseModel, Field
from typing import List, Optional
from pydantic import BaseModel, Field
from typing import Optional

class UserStory(BaseModel):
    title: Optional[str] = Field(..., description="The title of the user story")
    description: Optional[str] = Field(None, description="The description of the user story")
    acceptance_criteria: Optional[str] = Field(None, description="The detailed acceptance criteria for the given user story")
    feature_details: Optional[str] = Field(None, description="The detailed feature details for the given user story")
    technical_requirements: Optional[str] = Field(None, description="The detailed technical requirements for the given user story")
    testing_strategy: Optional[str] = Field(None, description="The testing strategy for the user story")
    security_compliance_concerns: Optional[str] = Field(None, description="The security compliance concerns related to the user story")
    story_points: Optional[int] = Field(None, description="The number of story points required to complete the given user story")
