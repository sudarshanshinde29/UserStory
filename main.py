from crewai import Crew
from textwrap import dedent
from agents import CodeRefactor
from tasks import TestTasks
import json
from dotenv import load_dotenv
load_dotenv()


class TripCrew:
    def __init__(self, description):
        self.description = description
        
    def run(self):
        agents = CodeRefactor()
        tasks = TestTasks()

        # Define your custom agents and tasks here
        analysis_agent=agents.analysis_agent()
        review_agent=agents.review_agent()

        analysis_task=tasks.analysis_task(analysis_agent,self.description)
        review_task=tasks.review_task(review_agent, self.description)
        
        # Define your custom crew here
        crew = Crew(
            agents=[analysis_agent,
                    review_agent
                    ],
            tasks=[
                analysis_task,
                review_task
            ],
            verbose=True,
        )

        result = crew.kickoff()
        return result
    
    def read_json_from_file(self, file_path):
        with open(file_path, 'r') as json_file:
            return json.load(json_file)
    
    def create_user_story(self):
        agent = CodeRefactor()
        tasks = TestTasks()

        scrum_master_agent=agent.scrum_master_agent()
        project_manager_agent=agent.project_manager_agent()

        data = self.read_json_from_file('final_review.json')
        with open('user_story.txt', 'w') as file:
            for epic in data['epics']:
                epic_title = epic['epicTitle']
                file.write(f"Epic Title: {epic_title}\n")
                
                for story in epic['userStories']:
                    story_title = story['storyTitle']
                    scrum_master_task=tasks.scrum_master_task(scrum_master_agent, epic_title, story_title, self.description)
                    project_manager_task=tasks.project_manager_task(project_manager_agent, epic_title, story_title, self.description)
                    crew = Crew(
                        agents=[scrum_master_agent,
                                project_manager_agent
                                ],
                        tasks=[
                            scrum_master_task,
                            project_manager_task
                        ],
                        verbose=True,
                    )
                    result = crew.kickoff()
                    file.write(f"{result}\n")
                
                file.write("\n")




# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome automatic test case genrator")
    print('-------------------------------')
    description = "I want to build an ecommerce website which will help me sell my products. Website will have pages for product catalog which will show product images, product video, price etc. One can register on website to shop. It will have payment gateway integration to make payment using credit card, net banking, or UPI. For use registration, email id, password, name, mobile number, country of residence, gender information is mandatory. Website should have search capabilities to be able to search based on product name, product category, type of product etc. It should allow me to filter my products based on price, gender, category etc."
    trip_crew = TripCrew(description=description)
    # result = trip_crew.run()
    trip_crew.create_user_story()
