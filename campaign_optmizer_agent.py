from crewai import Agent , Task 
from typing import Dict,List,Any 
import json


class CampaignOptimizerAgent:
    def __init__(self,llm):
        self.agent = Agent(
            role = 'Campaign Optimizer Agent',
            goal = 'The goal of the Advanced Campaign Optimizer is to optimize multi-channel campaign scheduling and content delivery in order to maximize engagement, conversions, and overall campaign effectiveness.'
              'The optimizer task is to make data-driven decisions about channel prioritization, content distribution, and audience targeting. By analyzing historical performance data and real-time feedback, the optimizer must adjust and refine campaign strategies on the fly.'
                'The ultimate aim is to create a highly responsive, well-coordinated campaign plan that uses predictive models and performance metrics to continually enhance its effectiveness. '
                'This includes testing various elements (such as time, frequency, and messaging) through A/B testing, ensuring that every decision contributes to achieving the highest ROI possible.',
            backstory = 'You are a seasoned digital marketing strategist with a deep focus on data-driven campaign optimization. After beginning your career as a marketing analyst, you quickly rose to prominence in the field by applying advanced analytics and machine learning to large-scale digital campaigns. Over the years, you have mastered the art of coordinating multi-channel campaigns, including social media, email marketing, and paid search. '
            'Your expertise lies in predictive analytics, where you use historical data and audience insights to forecast campaign performance and recommend the best timing, frequency, and content distribution strategies.'

            'Your track record includes several high-profile campaigns where you successfully increased engagement and conversions by optimizing the timing and placement of content across multiple platforms. You have built sophisticated frameworks for cross-channel synergies and adaptive campaign strategies that respond dynamically to audience behavior in real time. '
            'This deep understanding of the intricacies of each platform audience and algorithm has allowed you to become an expert at balancing aggressive growth goals with the delicate management of audience fatigue and oversaturation.'

            'You thrive in the fast-paced digital landscape, constantly testing new hypotheses and iterating campaigns to discover what works best. Your ultimate mission is to ensure that every campaign reaches its full potential by optimizing every variable — from the right platform and content to the perfect moment of delivery.',

            verbose = True,

            llm = llm
        )

        self.task = Task(
            description = 'The Advanced Campaign Optimizer is a highly specialized marketing strategist focused on maximizing the effectiveness of multi-channel marketing campaigns. By leveraging data analytics, audience behavior insights, and content performance metrics, this agent is responsible for ensuring that the right message reaches the right audience at the right time. The optimizer works across digital channels like social media, email, paid ads, and SEO, identifying the optimal combination of timing, content, and delivery frequency for each channel. This role requires expertise in predictive analytics, campaign management, and adaptive strategies that allow for real-time adjustments based on live campaign performance. The Advanced Campaign Optimizer doesn’t just improve campaign efficiency; they ensure a strategic balance between maximizing conversions and maintaining audience engagement across all touchpoints.',
            agent = self.agent 
        )

    def optimize_campaign(self, content: Dict[str, Any], channels: List[str], historical_data: Dict[str, Any], audience_data: Dict[str, Any]) -> Dict[str, Any]:
        prompt = self._create_prompt(content,channels,historical_data,audience_data)
        optimization_plan = self.task.execute({"prompt":prompt})
        return self.parse_optimization_plan(optimization_plan)
    
    def _create_prompt(self, content: Dict[str, Any], channels: List[str], historical_data: Dict[str, Any], audience_data: Dict[str, Any]) -> str:
        prompt = f"""
        As an Advanced Campaign Optimizer, your task is to create a comprehensive optimization plan for a multi-channel marketing campaign. Use the provided data to make data-driven decisions on timing, frequency, and channel selection to maximize engagement and conversions.

        Content to be distributed:
        {json.dumps(content, indent=2)}

        Available channels:
        {channels}

        Historical campaign performance data:
        {json.dumps(historical_data, indent=2)}

        Audience behavior and preferences data:
        {json.dumps(audience_data, indent=2)}

        Please provide an optimization plan that includes:

        1. Channel Priority: Rank the channels based on predicted effectiveness for this campaign.
        2. Posting Schedule: Determine the optimal times and days for posting on each channel.
        3. Content Distribution: Assign specific content pieces to channels where they're likely to perform best.
        4. Frequency Recommendations: Suggest posting frequency for each channel to maintain engagement without oversaturation.
        5. Cross-Channel Synergies: Identify opportunities for cross-promotion or complementary messaging across channels.
        6. Audience Targeting: Recommend targeting strategies for each channel based on audience data.
        7. Performance Metrics: Specify key performance indicators (KPIs) to track for each channel.
        8. A/B Testing Plan: Suggest elements to test for improving campaign performance.
        9. Adaptive Strategies: Provide rules or triggers for adjusting the campaign based on real-time performance data.

        Format your response as a JSON object with the following structure:
        {
            "channel_priority": ["Channel1", "Channel2", ...],
            "posting_schedule": {
                "Channel1": [{"day": "Monday", "times": ["9:00 AM", "3:00 PM"]}, ...],
                ...
            },
            "content_distribution": {
                "Channel1": ["Content1", "Content2", ...],
                ...
            },
            "frequency_recommendations": {
                "Channel1": "Recommendation",
                ...
            },
            "cross_channel_synergies": [
                {"primary_channel": "Channel1", "secondary_channel": "Channel2", "strategy": "..."},
                ...
            ],
            "audience_targeting": {
                "Channel1": "Targeting strategy",
                ...
            },
            "performance_metrics": {
                "Channel1": ["Metric1", "Metric2", ...],
                ...
            },
            "ab_testing_plan": [
                {"element": "Element to test", "variants": ["Variant1", "Variant2"], "channel": "Channel1"},
                ...
            ],
            "adaptive_strategies": [
                {"trigger": "Condition", "action": "Adjustment to make"},
                ...
            ]
        }
        """
        return prompt

    def parse_optimization_plan(self, raw_plan: str) -> Dict[str, Any]:
        try:
            return json.loads(raw_plan)
        except json.JSONDecodeError:
            print("Error parsing optimization plan. Returning raw content.")
            return {"error": "Parsing failed", "raw_content": raw_plan}
    


