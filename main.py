# main.py
import os
from crewai import Crew, Process
from langchain.llms import Groq
from Audience_segmentation_agent import AudienceSegmentationAgent
from Content_Generation_agent import CustomerGenerationAgent
from campaign_optmizer_agent import CampaignOptimizerAgent
from Real_time_adaption_agent import RealTimeAdaptionAgent
from typing import Dict, Any, List
import json
from datetime import datetime, timedelta

# Set up Groq API key
os.environ["GROQ_API_KEY"] = "your-groq-api-key-here"

# Initialize Groq LLM
llm = Groq(model_name="llama2-70b-4096", temperature=0.7)

# Initialize agents
audience_agent = AudienceSegmentationAgent(llm)
content_agent = CustomerGenerationAgent(llm)
campaign_agent = CampaignOptimizerAgent(llm)
adaptation_agent = RealTimeAdaptionAgent(llm)

# Sample data (replace with your actual data)
customer_data = {
    "demographics": {"age_range": "25-45", "locations": ["New York", "Los Angeles", "Chicago"]},
    "interests": ["technology", "fitness", "travel"],
    "behavior": {"purchase_frequency": "monthly", "preferred_channels": ["email", "social_media"]}
}

brand_guidelines = {
    "tone": "friendly and professional",
    "colors": ["#1DA1F2", "#14171A"],
    "logo_usage": "Always use the latest version of the logo",
    "key_messages": ["Innovate everyday", "Customer-first approach"]
}

channels = ["Email", "Facebook", "Instagram", "Twitter", "LinkedIn"]

historical_data = {
    "Email": {"open_rate": 0.25, "click_through_rate": 0.05},
    "Facebook": {"engagement_rate": 0.08, "conversion_rate": 0.02},
    "Instagram": {"engagement_rate": 0.12, "follower_growth_rate": 0.03},
    "Twitter": {"retweet_rate": 0.06, "click_through_rate": 0.04},
    "LinkedIn": {"engagement_rate": 0.07, "lead_generation_rate": 0.015}
}

def run_campaign(duration_days: int = 30):
    # Step 1: Segment Audience
    segments = audience_agent.segment_audience(customer_data)
    print("Audience Segments:", json.dumps(segments, indent=2))

    # Step 2: Generate Content
    content = content_agent.generate_content(segments, brand_guidelines, channels)
    print("Generated Content:", json.dumps(content, indent=2))

    # Step 3: Optimize Campaign
    optimization_plan = campaign_agent.optimize_campaign(content, channels, historical_data, segments)
    print("Campaign Optimization Plan:", json.dumps(optimization_plan, indent=2))

    # Step 4: Run campaign simulation with real-time adaptation
    campaign_data = {
        "content": content,
        "optimization_plan": optimization_plan,
        "start_date": datetime.now(),
        "end_date": datetime.now() + timedelta(days=duration_days)
    }

    for day in range(duration_days):
        current_date = campaign_data["start_date"] + timedelta(days=day)
        print(f"\nDay {day + 1} - {current_date.strftime('%Y-%m-%d')}")

        # Simulate daily performance metrics
        performance_metrics = simulate_daily_metrics(campaign_data, day)
        print("Daily Performance Metrics:", json.dumps(performance_metrics, indent=2))

        # Real-time adaptation
        adaptation_plan = adaptation_agent.adapt_real_time(
            campaign_data, performance_metrics, historical_data, optimization_plan
        )
        print("Adaptation Plan:", json.dumps(adaptation_plan, indent=2))

        # Apply adaptations
        campaign_data = adaptation_agent.apply_adaptations(adaptation_plan, campaign_data)
        print("Updated Campaign Data:", json.dumps(campaign_data, indent=2))

    # Final campaign report
    generate_campaign_report(campaign_data, performance_metrics)

def simulate_daily_metrics(campaign_data: Dict[str, Any], day: int) -> Dict[str, Any]:
    # This is a placeholder function to simulate daily performance metrics
    # In a real scenario, this would be replaced with actual data collection
    import random

    metrics = {}
    for channel in channels:
        base_engagement = historical_data[channel].get("engagement_rate", 0.05)
        base_conversion = historical_data[channel].get("conversion_rate", 0.02)
        
        # Simulate some daily fluctuation and a slight upward trend over time
        engagement_rate = max(0, min(1, base_engagement + random.uniform(-0.02, 0.03) + (day * 0.001)))
        conversion_rate = max(0, min(1, base_conversion + random.uniform(-0.005, 0.01) + (day * 0.0005)))
        
        metrics[channel] = {
            "engagement_rate": round(engagement_rate, 4),
            "conversion_rate": round(conversion_rate, 4),
            "reach": random.randint(1000, 10000)
        }
    
    return metrics

def generate_campaign_report(campaign_data: Dict[str, Any], final_metrics: Dict[str, Any]):
    print("\n=== Final Campaign Report ===")
    print(f"Campaign Duration: {campaign_data['start_date'].strftime('%Y-%m-%d')} to {campaign_data['end_date'].strftime('%Y-%m-%d')}")
    
    for channel in channels:
        print(f"\n{channel} Performance:")
        print(f"  Engagement Rate: {final_metrics[channel]['engagement_rate']:.2%}")
        print(f"  Conversion Rate: {final_metrics[channel]['conversion_rate']:.2%}")
        print(f"  Total Reach: {final_metrics[channel]['reach']}")

    # Add more detailed reporting here based on your specific KPIs and goals

if __name__ == "__main__":
    marketing_crew = Crew(
        agents=[
            audience_agent.agent,
            content_agent.agent,
            campaign_agent.agent,
            adaptation_agent.agent
        ],
        tasks=[
            audience_agent.task,
            content_agent.task,
            campaign_agent.task,
            adaptation_agent.task
        ],
        verbose=2,
        process=Process.sequential
    )

    print("Starting Marketing Campaign Simulation")
    run_campaign(duration_days=30)  # Simulate a 30-day campaign
    print("Marketing Campaign Simulation Completed")