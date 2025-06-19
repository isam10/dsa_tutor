import requests
import logging
from typing import Dict, Any, Optional, List

logger = logging.getLogger(__name__)

class GeminiAPI:
    """Enhanced Gemini API wrapper with better error handling"""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent"
    
    def generate_response(self, prompt: str, max_tokens: int = 2048) -> str:
        """Generate response using Gemini API with enhanced error handling"""
        if not self.api_key:
            return "API key not configured. Please set your GEMINI_API_KEY."
        
        try:
            headers = {"Content-Type": "application/json"}
            
            data = {
                "contents": [{"parts": [{"text": prompt}]}],
                "generationConfig": {
                    "temperature": 0.7,
                    "topK": 40,
                    "topP": 0.95,
                    "maxOutputTokens": max_tokens,
                },
                "safetySettings": [
                    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
                    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
                    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
                    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"}
                ]
            }
            
            response = requests.post(
                f"{self.base_url}?key={self.api_key}",
                headers=headers,
                json=data,
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                if "candidates" in result and result["candidates"]:
                    candidate = result["candidates"][0]
                    if "content" in candidate and "parts" in candidate["content"]:
                        if candidate["content"]["parts"]:
                            return candidate["content"]["parts"][0]["text"]
                return "I received an incomplete response. Please try again."
            else:
                logger.error(f"API Error: {response.status_code} - {response.text}")
                return f"API Error ({response.status_code}): Please check your connection and try again."
                
        except requests.exceptions.Timeout:
            return "Request timed out. Please try again."
        except requests.exceptions.ConnectionError:
            return "Connection error. Please check your internet connection."
        except Exception as e:
            logger.error(f"Error calling Gemini API: {str(e)}")
            return f"Error: {str(e)}"


