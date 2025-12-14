# agents/fact_checker.py
import requests
import os
from dotenv import load_dotenv
#load .env file
load_dotenv()


API_KEY = os.getenv("FACTCHECK_API_KEY")
BASE_URL = "https://factchecktools.googleapis.com/v1alpha1/claims:search"

def fact_check(claim: str) -> str:
    """
    Fact Checker Agent (Google Fact Check API)
    Checks if claim/summary is verified or disputed.
    Returns:
        str: Verification status or error message.
    """
    params = {
        "query": claim,
        "key": API_KEY,
        "pageSize": 1
    }

    try:
        response = requests.get(BASE_URL, params=params)
        if response.status_code != 200:
            return f"API Error: {response.status_code}"

        data = response.json()

        if "claims" not in data or not data["claims"]:
            return "No results → Pending Verification"

        claim_info = data["claims"][0]
        reviews = claim_info.get("claimReview", [])

        if not reviews:
            return "No reviews → Pending Verification"

        review = reviews[0]
        text = review.get("textualRating", "Unknown")

        if "True" in text or "Correct" in text:
            return "Verified ✅"
        elif "False" in text or "Incorrect" in text:
            return "Disputed ❌"
        else:
            return f"Review: {text}"

    except Exception as e:
        return "Error: Unable to verify claim."
