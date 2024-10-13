from crewai import Task
from textwrap import dedent
from userStory import UserStory

class TestTasks:

    def analysis_task(self, agent, description):
        return Task(
            description=dedent(f'''
            Analyze the provided project description and identify all possible epic points along with the associated user stories for each epic. 
            - Project Description: {description}

            Your output must follow this specific format for consistency:
            ```
            {{
                "epics": [
                    {{
                        "epicTitle": "User Authentication and Profile Management",
                        "userStories": [
                            {{ "storyTitle": "As a new user, I want to register an account so that I can access the site and make purchases." }},
                            {{ "storyTitle": "As a returning user, I want to log in so that I can view my previous orders and continue shopping." }},
                            {{ "storyTitle": "As a user, I want to reset my password so that I can regain access to my account." }}
                        ]
                    }},
                    {{
                        "epicTitle": "Product Catalog Management",
                        "userStories": [
                            {{ "storyTitle": "As a user, I want to browse the product catalog by category so that I can find the products I am interested in." }},
                            {{ "storyTitle": "As a product manager, I want to add new products with descriptions, images, and pricing so that customers can purchase them." }}
                        ]
                    }}
                ]
            }}
            ```

            **Important Note**: Make sure to provide a comprehensive set of user stories that cover both frontend and backend development task for each epic.
            '''),
            expected_output="Your final answer must include a detailed list of epic titles and associated user stories in the specified JSON format, with no additional text.",
            output_file="final1.txt",
            agent=agent
        )


    def review_task(self, agent, description):
        return Task(
            description=dedent(f'''
            Review the provided JSON data, which contains epics and associated user stories, to ensure clarity, feasibility, and alignment with project objectives.
            - Project Description: {description}

        Also do the review of JSON structure and for any missing brackets or any syntax related issue.
            '''),
            expected_output="Your final answer must include a detailed review of each epic and associated user stories in the specified JSON format, with no additional text.",
            output='JSON',
            output_file="final_review.json",
            agent=agent
        )
    

    # def scrum_master_task(self, agent, epic, user_story, project_description):
    #     return Task(
    #         description=dedent(f'''
    #         Analyze the provided epic Name, user story title and project description given below,
    #         - Epic Title: {epic}
    #         - User Story Title: {user_story}
    #         - project Description: {project_description}

    #         Based on the your analysis fill out the `UserStory` model with as much information as possible in detail.
    #         ```
    #         class UserStory(BaseModel):
    #             title: Optional[str] = Field(..., description="The title of the user story")
    #             description: Optional[str] = Field(None, description="The description of the user story")
    #             acceptance_criteria: Optional[str] = Field(None, description="The detailed acceptance criteria for the given user story")
    #             feature_details: Optional[str] = Field(None, description="The detailed feature details for the given user story")
    #             technical_requirements: Optional[str] = Field(None, description="The detailed technical requirements for the given user story")
    #             testing_strategy: Optional[str] = Field(None, description="The testing strategy for the user story")
    #             security_compliance_concerns: Optional[str] = Field(None, description="The security compliance concerns related to the user story")
    #             story_points: Optional[int] = Field(None, description="The number of story points required to complete the given user story")
    #         ```
    #         '''),
    #         expected_output="Fill out the `UserStory` model with as much information as possible.Ensure all information is align with story point and project, nothing else",
    #         output_pydantic=UserStory,
    #         agent=agent
    #     )
    
    def scrum_master_task(self, agent, epic, user_story, project_description):
        return Task(
            description=dedent(f'''
            Analyze the provided epic Name, user story title and project description given below,
            - Epic Title: {epic}
            - User Story Title: {user_story}
            - project Description: {project_description}

            Based on the your analysis fill out the below deatils with as much information as possible in detail.
            ```
            title: The title of the user story
            description: The description of the user story
            acceptance_criteria: The detailed acceptance criteria for the given user story
            feature_details: The detailed feature details for the given user story
            technical_requirements: The detailed technical requirements for the given user story
            testing_strategy: The testing strategy for the user story
            security_compliance_concerns: The security compliance concerns related to the user story
            story_points: "The number of story points required to complete the given user story
            ```
            '''),
            expected_output="Fill out the given output format model with as much information as possible.Ensure all information is align with story point and project, nothing else",
            agent=agent
        )
    
    def project_manager_task(self, agent, epic, user_story, project_description):
        return Task(
            description=dedent(f'''
            Perform final review and if any fields require any changes based on your review, do that. Ref the below given pic Name, user story title and project description
            - Epic Title: {epic}
            - User Story Title: {user_story}
            - project Description: {project_description}
            Note - Do not try to add any new field in exsiting output format.
            '''),
            expected_output="Ensure the output format model is fully populated and all information is align with story point and project, nothing else",
            agent=agent
        )



