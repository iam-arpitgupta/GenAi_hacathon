from crewai import Agent,Task 
from typing import Dict,Any,List
import json 
from datetime import datetime 

class RealTimeAdaptionAgent:
    def __init__(self,llm):
        self.agent = Agent(
            role = 'Real time Adaption agent',
            goal = 'The goal of the Real-time Campaign Adaptation Specialist is to actively monitor, assess, and adjust ongoing multi-channel campaigns to maximize their effectiveness in real-time. This includes tracking performance metrics, identifying emerging trends, and applying rapid, data-driven optimizations. The specialist ensures that campaigns remain adaptable and responsive to audience behavior, channel performance, and market conditions, preventing underperformance and capitalizing on opportunities to increase engagement, conversions, and ROI.',
            backstory = 'You are a marketing expert with extensive experience in real-time analytics and adaptive marketing strategies. Over the years, you have built a reputation for saving high-budget campaigns by making crucial, real-time adjustments based on live performance data. Your ability to analyze patterns, predict shifts in audience behavior, and quickly implement optimizations has made you indispensable to leading marketing teams.'

            'Your career began in marketing analysis, where you became proficient in tracking and analyzing digital campaign metrics. You soon developed a unique talent for identifying trends and anomalies in real-time, allowing you to suggest immediate adjustments that improve performance. As you honed your skills, you transitioned into a strategist role focused on live campaign optimization. You have led high-stakes, multi-channel campaigns and earned recognition for maximizing ROI through adaptive strategies.'

            'You pride yourself on being able to quickly interpret data, formulate responses, and execute effective changes without delay. Whether it’s reallocating ad spend, modifying content, or adjusting audience targeting, you are always one step ahead of campaign underperformance.',

            verbose = True,
            llm = llm
        )

    def adapt_real_time(self, campaign_data: Dict[str, Any], performance_metrics: Dict[str, Any], historical_benchmarks: Dict[str, Any], optimization_plan: Dict[str, Any]) -> Dict[str, Any]:
        prompt = self._create_prompt(campaign_data, performance_metrics, historical_benchmarks, optimization_plan)
        adaptation_plan = self.task.execute({"prompt": prompt})
        return self.parse_adaptation_plan(adaptation_plan)
    



    def _create_prompt(self, campaign_data: Dict[str, Any], performance_metrics: Dict[str, Any], historical_benchmarks: Dict[str, Any], optimization_plan: Dict[str, Any]) -> str:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        prompt = f"""
        As a Real-time Campaign Adaptation Specialist, your task is to analyze the current campaign performance and suggest immediate adjustments to optimize its effectiveness. Use the provided data to make data-driven decisions for real-time campaign adaptation.

        Current time: {current_time}

        Campaign data:
        {json.dumps(campaign_data, indent=2)}

        Current performance metrics:
        {json.dumps(performance_metrics, indent=2)}

        Historical performance benchmarks:
        {json.dumps(historical_benchmarks, indent=2)}

        Current optimization plan:
        {json.dumps(optimization_plan, indent=2)}

        Please provide a real-time adaptation plan that includes:

        1. Performance Analysis:
           - Identify any metrics that are underperforming or overperforming compared to benchmarks.
           - Detect any unusual patterns or anomalies in the data.

        2. Trend Identification:
           - Identify short-term trends in engagement, conversions, or other relevant metrics.
           - Compare current trends with historical data to contextualize performance.

        3. Channel-specific Adjustments:
           - Suggest specific adjustments for each channel based on its current performance.
           - Recommend reallocation of resources or budget if necessary.

        4. Content Optimization:
           - Identify top-performing content and suggest ways to capitalize on its success.
           - Recommend modifications or replacements for underperforming content.

        5. Audience Targeting Refinement:
           - Suggest refinements to audience targeting based on current engagement data.
           - Identify any segments that are responding particularly well or poorly.

        6. Timing Adjustments:
           - Recommend changes to posting schedules based on real-time engagement data.
           - Suggest optimal times for pushing high-performing content or offers.

        7. A/B Test Recommendations:
           - Propose new A/B tests based on current performance data.
           - Suggest early conclusions from ongoing A/B tests if clear winners are emerging.

        8. Risk Mitigation:
           - Identify any potential risks or negative trends and suggest preventive actions.

        9. Opportunity Exploitation:
           - Highlight any unexpected positive outcomes and how to leverage them.

        10. KPI Projections:
            - Provide short-term projections for key performance indicators based on suggested adjustments.

        Format your response as a JSON object with the following structure:
        {
            "performance_analysis": {
                "underperforming_metrics": ["Metric1", "Metric2"],
                "overperforming_metrics": ["Metric3"],
                "anomalies": ["Description of anomaly"]
            },
            "trend_identification": [
                {"trend": "Description of trend", "significance": "High/Medium/Low"}
            ],
            "channel_adjustments": {
                "Channel1": ["Adjustment1", "Adjustment2"],
                "Channel2": ["Adjustment1", "Adjustment2"]
            },
            "content_optimization": {
                "top_performing": ["Content1", "Content2"],
                "recommendations": ["Recommendation1", "Recommendation2"]
            },
            "audience_targeting": {
                "refinements": ["Refinement1", "Refinement2"],
                "responsive_segments": ["Segment1", "Segment2"]
            },
            "timing_adjustments": {
                "Channel1": {"old_time": "9:00 AM", "new_time": "10:00 AM"},
                "Channel2": {"old_time": "2:00 PM", "new_time": "3:00 PM"}
            },
            "ab_test_recommendations": [
                {"test": "New test description", "hypothesis": "Expected outcome"},
                {"ongoing_test": "Test name", "early_conclusion": "Preliminary result"}
            ],
            "risk_mitigation": [
                {"risk": "Description of risk", "preventive_action": "Suggested action"}
            ],
            "opportunity_exploitation": [
                {"opportunity": "Description of opportunity", "action": "Suggested action"}
            ],
            "kpi_projections": {
                "Metric1": {"current": 0.1, "projected": 0.15},
                "Metric2": {"current": 1000, "projected": 1200}
            }
        }
        """
        return prompt

    def parse_adaptation_plan(self, raw_plan: str) -> Dict[str, Any]:
        try:
            return json.loads(raw_plan)
        except json.JSONDecodeError:
            print("Error parsing adaptation plan. Returning raw content.")
            return {"error": "Parsing failed", "raw_content": raw_plan}

    def apply_adaptations(self, adaptation_plan: Dict[str, Any], campaign_data: Dict[str, Any]) -> Dict[str, Any]:
        # This method would implement the logic to apply the suggested adaptations
        # to the campaign data. This is a placeholder and should be customized based
        # on your specific campaign structure and requirements.
        adapted_campaign = campaign_data.copy()
        
        # Example of applying channel adjustments
        if 'channel_adjustments' in adaptation_plan:
            for channel, adjustments in adaptation_plan['channel_adjustments'].items():
                if channel in adapted_campaign:
                    adapted_campaign[channel]['adjustments'] = adjustments

        # Example of applying content optimization
        if 'content_optimization' in adaptation_plan:
            adapted_campaign['optimized_content'] = adaptation_plan['content_optimization']

        # Add more adaptation logic here based on the structure of your campaign data
        # and the adaptation plan

        return adapted_campaign