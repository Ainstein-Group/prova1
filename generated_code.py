```
from crewai import Agent, Task, Crew
from typing import List, Dict
import logging

class TripPlannerAgent(Agent):
    def __init__(self, llm: str):
        super().__init__(role="Trip Planner", goal="Plan a trip", backstory="Expert in multi-agent systems.", llm=llm)
        self.preferences: Dict[str, str] = {}
        self.itinerary: List[Dict[str, str]] = []

    def plan_trip(self, preferences: Dict[str, str]) -> List[Dict[str, str]]:
        self.preferences = preferences
        # TO DO: implement trip planning logic
        return self.itinerary

    def book_flight(self, flight_info: Dict[str, str]) -> Dict[str, str]:
        # TO DO: implement flight booking logic
        return flight_info

    def book_hotel(self, hotel_info: Dict[str, str]) -> Dict[str, str]:
        # TO DO: implement hotel booking logic
        return hotel_info

    def book_activity(self, activity_info: Dict[str, str]) -> Dict[str, str]:
        # TO DO: implement activity booking logic
        return activity_info

class NotificationAgent(Agent):
    def __init__(self, llm: str):
        super().__init__(role="Notification", goal="Send notifications", backstory="Expert in notification systems.", llm=llm)
        self.notifications: List[Dict[str, str]] = []

    def send_notification(self, notification: Dict[str, str]) -> None:
        self.notifications.append(notification)
        logging.info("Notification sent: %s", notification)

class Crew:
    def __init__(self, agents: List[Agent], tasks: List[Task]):
        self.agents = agents
        self.tasks = tasks

    def kickoff(self) -> None:
        for agent in self.agents:
            agent.start()
        for task in self.tasks:
            task.start()

if __name__ == "__main__":
    llms1 = "your_llm_model_here"
    llms2 = "your_llm_model_here"
    agent1 = TripPlannerAgent(llms1)
    agent2 = NotificationAgent(llms2)
    task = Task(description="Plan a trip", agent=agent1)
    crew = Crew(agents=[agent1, agent2], tasks=[task])
    crew.kickoff()
```