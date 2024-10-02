from crewai import Agent,Task 

class AudienceSegmentationAgent:
    def __init__(self,llm):
        self.agent = Agent(
            role = "audience Segmentation Agent",
            goal = 'Analyze complex customer datasets to discover actionable audience segments.'
            'The goal is to enable businesses to better understand their customers, enhance personalization,'
            'and drive effective marketing strategies by providing deep insights into customer behavior and preferences.' 
            'The agent must deliver clear, data-backed audience profiles that can be used for strategic decision-making.'
        ,
        backstory = 'You are a highly experienced data analysis and segmentation expert with years of working with diverse customer datasets across industries.'
          'Known for your ability to interpret and synthesize vast amounts of information, you specialize in uncovering hidden patterns within customer data. '
          'Your past achievements include leading segmentation projects for major corporations, resulting in significant improvements in marketing ROI, customer engagement, and retention.' 
          'You have a solid background in data science, machine learning, and consumer psychology, which enables you to create segments that resonate with business objectives. '
        'Your motivation lies in helping businesses unlock the full potential of their customer base through precise, impactful segmentation strategies.',
        verbose = True,
        llm = llm 
        )

        self.task = Task(
            description = 'The Audience Segmentation Specialist is responsible for analyzing large volumes of customer data to identify distinct and meaningful audience segments. '
            'This involves working with various demographic, behavioral, and transactional data, utilizing advanced analytical techniques and machine learning models to derive insights.'
            'The specialist must develop strategies for data-driven marketing, targeting specific customer groups with tailored recommendations, and improving business outcomes through precision audience targeting.'

            agent = self.agent 
        )

    def segement_audience(self,customer_data):
        return self.task.execute({"customer_data":customer_data})
        
        
        























































from langgraph.agents import create_openai_agent
from sklearn import KMeans 
import pandas as pd 
import numpy as np 
from langgarph.prompts import PromptTeamplate 


# this agents helps in the customer segementation 
segmentation_prompt = PromptTeamplate(
    input_variables = ["customer_data"],
    templates = "you are the "
)


def segmentation_audience(data):
    # using the k-means clsutering 
    df = pd.DataFrame(df)
    kmeans = KMeans(n_clusters = 5, random_state = 42)