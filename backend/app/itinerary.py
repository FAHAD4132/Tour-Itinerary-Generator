from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

def generate_itinerary(tour_data):

    model = "llama3.2"
    llm = ChatOllama(model=model)

    prompt = ChatPromptTemplate.from_template(
        """You are a travel expert. Generate a detailed day-by-day itinerary for the following tour:
        **Tour Name**: {tour_name}
        **Duration**: {duration}
        **Tour Type**: {tour_type}
        **Trip Category**: {trip_category}
        **Location**: {location}
        **Included in the Tour**: {included}
        **Excluded in the Tour**: {excluded}
        **Tour Price (Per Adult Person)**: {price}

        Structure your response for each day as:
        - Day 1: [Activity Summary]
          - Morning: [Details]
          - Afternoon: [Details]
          - Evening: [Details]
          - Meals:
            - Breakfast: [Foods]
            - Lunch: [Foods]
            - Dinner: [Foods]
          - Accommodation: [Hotel Type]
        """
    )

    chain = prompt | llm | StrOutputParser()
    itinerary = chain.invoke(tour_data)
    return itinerary