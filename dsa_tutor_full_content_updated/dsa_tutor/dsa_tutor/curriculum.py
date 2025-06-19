from typing import Dict, Any, Optional, List
import re
import os
from bs4 import BeautifulSoup
import fitz # PyMuPDF

class DSACurriculum:
    """Enhanced curriculum with more detailed progression"""
    
    MODULES = {
        1: {
            "id": 1,
            "title": "Introduction to Data Structures and Algorithms",
            "topics": [
                "What are Data Structures?",
                "What are Algorithms?",
                "Why Python for DSA?"
            ],
            "difficulty": "Absolute Beginner",
            "estimated_hours": 12,
            "prerequisites": "None - Start here!",
            "projects": ["Simple Calculator", "Personal Info Display", "Basic Math Operations"]
        },
        2: {
            "id": 2,
            "title": "Built-in Data Structures in Python",
            "topics": [
                "Lists",
                "Tuples", 
                "Sets",
                "Dictionaries",
                "Strings"
            ],
            "difficulty": "Beginner",
            "estimated_hours": 15,
            "prerequisites": "Module 1 - Introduction to DSA",
            "projects": ["Number Guessing Game", "Pattern Printer", "Simple Menu System"]
        },
        3: {
            "id": 3,
            "title": "Advanced Data Structures",
            "topics": [
                "Linked Lists",
                "Stacks",
                "Queues",
                "Trees",
                "Graphs",
                "Heaps",
                "Hash Tables"
            ],
            "difficulty": "Beginner",
            "estimated_hours": 18,
            "prerequisites": "Module 2 - Built-in Data Structures",
            "projects": ["Function Library", "Advanced Calculator", "Code Organizer"]
        },
        4: {
            "id": 4,
            "title": "Algorithms",
            "topics": [
                "Searching Algorithms",
                "Sorting Algorithms",
                "Recursion and Backtracking",
                "Dynamic Programming",
                "Greedy Algorithms"
            ],
            "difficulty": "Beginner-Intermediate",
            "estimated_hours": 20,
            "prerequisites": "Module 3 - Advanced Data Structures",
            "projects": ["To-Do List Manager", "Text Processor", "Data Organizer"]
        },
        5: {
            "id": 5,
            "title": "Advanced Topics",
            "topics": [
                "Bit Manipulation",
                "Divide and Conquer",
                "Graph Algorithms",
                "String Algorithms",
                "Problem Solving Strategies"
            ],
            "difficulty": "Intermediate",
            "estimated_hours": 22,
            "prerequisites": "Module 4 - Algorithms",
            "projects": ["Student Grade Manager", "Inventory System", "Contact Book"]
        }
    }

    def __init__(self):
        # Get the absolute path to the directory containing this file
        base_dir = os.path.dirname(os.path.abspath(__file__))
        # Construct the path to content.txt relative to this file
        content_filepath = os.path.join(base_dir, "formatted_content.html")
        self.all_content = self.load_content_from_file(content_filepath)

    @staticmethod
    def load_content_from_file(filepath):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                html_content = f.read()

            soup = BeautifulSoup(html_content, 'html.parser')
            content_map = {}
            current_module_id = None
            current_topic_title = None
            current_content = []

            # Iterate through all <p> tags to find module and topic titles and their content
            for p_tag in soup.find_all('p'):
                text = p_tag.get_text(strip=True)

                # Check for Module title (e.g., "Module 1: Introduction to Data Structures and Algorithms")
                module_match = re.match(r'Module (\d+): (.+)', text)
                if module_match:
                    # Save previous topic content if exists
                    if current_module_id and current_topic_title and current_content:
                        content_map[current_module_id][current_topic_title] = ''.join(current_content)
                    
                    current_module_id = int(module_match.group(1))
                    content_map[current_module_id] = {}
                    current_topic_title = None
                    current_content = []
                    continue

                # Check for Topic title (e.g., "1.1 What are Data Structures?")
                topic_match = re.match(r'\d+\.\d+\s(.+)', text)
                if topic_match and current_module_id is not None:
                    # Save previous topic content if exists
                    if current_topic_title and current_content:
                        content_map[current_module_id][current_topic_title] = ''.join(current_content)
                    
                    current_topic_title = topic_match.group(1).strip()
                    current_content = []
                    continue

                # If we have a current module and topic, append the content
                if current_module_id is not None and current_topic_title is not None:
                    # Append the HTML content of the paragraph
                    current_content.append(str(p_tag))

            # Save the last topic content
            if current_module_id and current_topic_title and current_content:
                content_map[current_module_id][current_topic_title] = ''.join(current_content)

            return content_map
        except FileNotFoundError:
            print(f"Warning: Content file not found at {filepath}")
            return {}

    def get_topic_content(self, module_id: int, topic_title: str) -> str:
        """Retrieves content for a given topic from the loaded content."""
        module = self.get_module_info(module_id)
        if not module or topic_title not in module["topics"]:
            return "Topic not found."

        return self.all_content.get(module_id, {}).get(topic_title, "Content not available.")

    @staticmethod
    def get_module_info(module_id: int) -> Optional[Dict[str, Any]]:
        """Returns information for a specific module."""
        return DSACurriculum.MODULES.get(module_id)

    @staticmethod
    def get_all_modules() -> Dict[int, Dict[str, Any]]:
        """Returns all modules in the curriculum."""
        return DSACurriculum.MODULES

    @staticmethod
    def get_total_modules() -> int:
        """Returns the total number of modules."""
        return len(DSACurriculum.MODULES)



