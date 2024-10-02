from crewai import Agent , Task 
from typing import Dict,List,Any 
import json

class CustomerGenerationAgent:
    def __init__(self,llm):
        self.agent = Agent(
            role = 'Multi-platform Content Creator',
            goal = 'The goal of the Multi-Platform Content Creator is to generate personalized, platform-optimized content that resonates with distinct audience segments.'
            'The content should reflect the brands values and messaging while adhering to the specific demands and best practices of each social media platform.'
            'This includes crafting compelling headlines, creative media suggestions, strategic use of hashtags, and actionable calls-to-action that prompt audience interaction and drive business goals, whether it is increasing awareness, engagement, or sales.',
            backstory = 'You are a seasoned content producer with a unique ability to adapt to the ever-changing world of social media. Having worked across diverse industries, you have mastered the art of storytelling, visual design, and content marketing for platforms ranging from Instagram and TikTok to LinkedIn and Facebook. '
            'You began your career as a copywriter but soon transitioned into multi-platform content creation, driven by a passion for digital trends and understanding of audience psychology. Over the years, you have developed a sixth sense for what works on each platform — be it viral short-form videos, engaging community posts, or thought leadership articles.'
            'Your skills don not stop at content creation; you are also highly adept at interpreting audience data and feedback to iterate and improve content performance. With a strong grasp of branding and a deep familiarity with platform-specific algorithms,'
            'you create content that not only stands out but also fosters meaningful interactions, building both brand loyalty and business growth. You thrive on creativity, adapting quickly to new trends, technologies, and platforms.',
            verbose = True,
            llm = llm 
        )
        self.task = Task(
            description = 'The Multi-Platform Content Creator is responsible for crafting highly engaging and tailored content for various audience segments, ensuring the content aligns with platform-specific guidelines and brand identity.'
            'This content creator utilizes a deep understanding of digital marketing, consumer behavior, and platform dynamics to produce impactful and relevant content across social media platforms like Instagram, TikTok, LinkedIn, Facebook, and Twitter. '
            'The agent integrates both creative flair and data-driven insights to generate content that resonates with each audience, boosting engagement, conversions, and brand loyalty. '
            'Whether its short-form video for TikTok or professional articles for LinkedIn, this agent tailors the messaging, tone, and style to maximize audience engagement.',

            agent = self.agent
        )

    def generate_content(self, segments: List[Dict[str, Any]], brand_guidelines: Dict[str, Any], platforms: List[str]) -> Dict[str, Any]:
        prompt = self._create_prompt(segments, brand_guidelines, platforms)
        return self.task.execute({"prompt": prompt})


    def _create_prompt(self, segments: List[Dict[str, Any]], brand_guidelines: Dict[str, Any], platforms: List[str]) -> str:
    platform_guidelines = {
        "Twitter": "280 character limit, concise, use of hashtags, tap into trending conversations and use a witty tone",
        "Facebook": "Longer-form content, use of images or videos, community engagement, encourage comments or shares",
        "Instagram": "Highly visual, use of images or short videos, leverage relevant hashtags, prioritize aesthetics, and use interactive elements like stories or reels",
        "LinkedIn": "Professional tone, informative, use of industry insights, longer posts or articles, focus on value-driven and educational content",
        "TikTok": "Short, dynamic video content, trending sounds or challenges, engaging hooks in the first few seconds, use of humor or trends",
        "YouTube": "Longer-form video content, in-depth tutorials or stories, engaging titles, dynamic video descriptions, and strategic keyword use",
        "Pinterest": "Image-first platform, create visually appealing pins with clear text, product showcases, and links to articles or shopping pages"
    }

    prompt = f"""
    You are a versatile content creator tasked with generating personalized and platform-optimized content for the following audience segments:
    {segments}

    Your content must adhere to these brand guidelines:
    {brand_guidelines}

    You need to create content for the following social media platforms:
    {platforms}

    Each platform has its own set of content guidelines and best practices:
    {', '.join([f"{platform}: {platform_guidelines[platform]}" for platform in platforms])}

    For each audience segment and platform, provide the following details:
    1. **A Catchy Headline**: This should grab attention and encourage users to engage.
    2. **Main Content Body**: Ensure the content is engaging and aligns with the segment’s preferences. Keep tone and format tailored to each platform.
    3. **Call-to-Action**: This should prompt the audience to take a desired action, like following the brand, purchasing, subscribing, or sharing.
    4. **Relevant Hashtags**: Use hashtags that are both popular and relevant to the platform and audience segment (where applicable).
    5. **Suggestions for Visual Elements**: Outline ideas for images, videos, or other media that will accompany the content. Tailor the visuals to match the platform’s best practices.

    Ensure the content is personalized to each audience segment and optimized for each platform's format and engagement style.

    Format your response as a JSON object in the following structure:
    {{
        "segment_name": {{
            "platform_name": {{
                "headline": "...",
                "content": "...",
                "cta": "...",
                "hashtags": ["...", "..."],
                "visual_suggestions": "..."
            }}
        }}
    }}
    """
    return prompt

    def parse_content(self, raw_content: str) -> Dict[str, Any]:
        # Implement parsing logic here to convert the raw string response
        # from the LLM into a structured dictionary
        # This is a placeholder and should be replaced with actual parsing logic
        import json
        try:
            return json.loads(raw_content)
        except json.JSONDecodeError:
            print("Error parsing LLM response. Returning raw content.")
            return {"error": "Parsing failed", "raw_content": raw_content}



