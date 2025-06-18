from typing import Dict, Any, Optional, List

class DSACurriculum:
    """Enhanced curriculum with more detailed progression"""
    
    MODULES = {
        1: {
            "id": 1, # Added ID
            "title": "Python Fundamentals - Getting Started",
            "topics": [
                "What is Programming?",
                "Installing Python & IDE Setup",
                "Variables and Data Types",
                "Basic Input/Output Operations",
                "Comments and Code Documentation",
                "Operators and Expressions",
                "Your First Python Programs"
            ],
            "difficulty": "Absolute Beginner",
            "estimated_hours": 12,
            "prerequisites": "None - Start here!",
            "projects": ["Simple Calculator", "Personal Info Display", "Basic Math Operations"]
        },
        2: {
            "id": 2, # Added ID
            "title": "Control Flow and Logic",
            "topics": [
                "Boolean Logic and Conditions",
                "If-Else Statements",
                "Nested Conditions",
                "For Loops - Iteration Basics",
                "While Loops - Conditional Iteration",
                "Loop Control (break, continue)",
                "Nested Loops and Patterns"
            ],
            "difficulty": "Beginner",
            "estimated_hours": 15,
            "prerequisites": "Module 1 - Python Fundamentals",
            "projects": ["Number Guessing Game", "Pattern Printer", "Simple Menu System"]
        },
        3: {
            "id": 3, # Added ID
            "title": "Functions and Code Organization",
            "topics": [
                "Function Basics - Why Functions?",
                "Parameters and Arguments",
                "Return Values and Scope",
                "Default Parameters",
                "Variable Arguments (*args, **kwargs)",
                "Lambda Functions",
                "Function Best Practices"
            ],
            "difficulty": "Beginner",
            "estimated_hours": 18,
            "prerequisites": "Module 2 - Control Flow",
            "projects": ["Function Library", "Advanced Calculator", "Code Organizer"]
        },
        4: {
            "id": 4, # Added ID
            "title": "Python Data Structures - Lists and Strings",
            "topics": [
                "Lists - Creation and Basic Operations",
                "List Indexing and Slicing",
                "List Methods and Manipulation",
                "String Fundamentals",
                "String Methods and Operations",
                "String Formatting",
                "List Comprehensions Introduction"
            ],
            "difficulty": "Beginner-Intermediate",
            "estimated_hours": 20,
            "prerequisites": "Module 3 - Functions",
            "projects": ["To-Do List Manager", "Text Processor", "Data Organizer"]
        },
        5: {
            "id": 5, # Added ID
            "title": "Advanced Data Structures",
            "topics": [
                "Tuples and When to Use Them",
                "Sets - Unique Collections",
                "Dictionaries - Key-Value Pairs",
                "Nested Data Structures",
                "Data Structure Selection",
                "Advanced List Comprehensions",
                "Dictionary and Set Comprehensions"
            ],
            "difficulty": "Intermediate",
            "estimated_hours": 22,
            "prerequisites": "Module 4 - Lists and Strings",
            "projects": ["Student Grade Manager", "Inventory System", "Contact Book"]
        },
        6: {
            "id": 6, # Added ID
            "title": "File Handling and Error Management",
            "topics": [
                "File I/O Fundamentals",
                "Reading and Writing Files",
                "Working with CSV Files",
                "Exception Handling - Try/Except",
                "Common Error Types",
                "Debugging Strategies",
                "Best Practices for Robust Code"
            ],
            "difficulty": "Intermediate",
            "estimated_hours": 16,
            "prerequisites": "Module 5 - Advanced Data Structures",
            "projects": ["File Manager", "Data Parser", "Log Analyzer"]
        },
        7: {
            "id": 7, # Added ID
            "title": "Object-Oriented Programming Basics",
            "topics": [
                "Classes and Objects Introduction",
                "Attributes and Methods",
                "Constructor (__init__) Method",
                "Instance vs Class Variables",
                "Basic Inheritance",
                "Method Overriding",
                "OOP Design Principles"
            ],
            "difficulty": "Intermediate",
            "estimated_hours": 20,
            "prerequisites": "Module 6 - File Handling",
            "projects": ["Bank Account System", "Library Management", "Game Character Classes"]
        },
        8: {
            "id": 8, # Added ID
            "title": "Algorithm Analysis and Big O Notation",
            "topics": [
                "What is Algorithm Analysis?",
                "Time Complexity Fundamentals",
                "Space Complexity Basics",
                "Big O, Big Ω, Big Θ Notation",
                "Best, Average, Worst Case Analysis",
                "Comparing Algorithms",
                "Practical Performance Considerations"
            ],
            "difficulty": "Intermediate",
            "estimated_hours": 14,
            "prerequisites": "Module 7 - OOP Basics",
            "projects": ["Algorithm Timer", "Performance Comparator", "Complexity Visualizer"]
        },
        9: {
            "id": 9, # Added ID
            "title": "Arrays and Basic Problem Solving",
            "topics": [
                "Array Fundamentals in Python (Lists)",
                "Array Traversal Techniques",
                "Two Pointer Technique",
                "Sliding Window Approach",
                "Array Manipulation Problems",
                "Matrix Operations",
                "Common Array Patterns"
            ],
            "difficulty": "Intermediate",
            "estimated_hours": 18,
            "prerequisites": "Module 8 - Algorithm Analysis",
            "projects": ["Array Processor", "Matrix Calculator", "Pattern Finder"]
        },
        10: {
            "id": 10, # Added ID
            "title": "Searching Algorithms",
            "topics": [
                "Linear Search Implementation",
                "Binary Search - Divide and Conquer",
                "Binary Search Variations",
                "Search in Rotated Arrays",
                "Finding Peak Elements",
                "Search Optimization Techniques",
                "When to Use Which Search"
            ],
            "difficulty": "Intermediate",
            "estimated_hours": 16,
            "prerequisites": "Module 9 - Arrays",
            "projects": ["Search Engine", "Data Finder", "Optimization Tool"]
        },
        11: {
            "id": 11, # Added ID
            "title": "Sorting Algorithms",
            "topics": [
                "Why Sorting Matters",
                "Bubble Sort - Understanding Basics",
                "Selection and Insertion Sort",
                "Merge Sort - Divide and Conquer",
                "Quick Sort - Efficient Sorting",
                "Heap Sort Introduction",
                "When to Use Each Algorithm"
            ],
            "difficulty": "Intermediate-Advanced",
            "estimated_hours": 22,
            "prerequisites": "Module 10 - Searching",
            "projects": ["Sorting Visualizer", "Performance Analyzer", "Custom Sorter"]
        },
        12: {
            "id": 12, # Added ID
            "title": "Linked Lists",
            "topics": [
                "What are Linked Lists?",
                "Singly Linked List Implementation",
                "Linked List vs Arrays",
                "Doubly Linked Lists",
                "Circular Linked Lists",
                "Common Linked List Problems",
                "Two Pointer Techniques in Linked Lists"
            ],
            "difficulty": "Advanced",
            "estimated_hours": 18,
            "prerequisites": "Module 11 - Sorting",
            "projects": ["Linked List Library", "Memory Manager", "Data Structure Comparator"]
        },
        13: {
            "id": 13, # Added ID
            "title": "Stacks and Queues",
            "topics": [
                "Stack Data Structure and LIFO",
                "Stack Implementation and Applications",
                "Expression Evaluation with Stacks",
                "Queue Data Structure and FIFO",
                "Queue Implementation Variations",
                "Priority Queues",
                "Real-world Applications"
            ],
            "difficulty": "Advanced",
            "estimated_hours": 16,
            "prerequisites": "Module 12 - Linked Lists",
            "projects": ["Expression Calculator", "Task Scheduler", "Browser History"]
        },
        14: {
            "id": 14, # Added ID
            "title": "Recursion and Problem Solving",
            "topics": [
                "Understanding Recursion",
                "Base Cases and Recursive Calls",
                "Call Stack and Recursion Depth",
                "Tail Recursion Optimization",
                "Memoization and Dynamic Programming Intro",
                "Backtracking Algorithms",
                "Recursive vs Iterative Solutions"
            ],
            "difficulty": "Advanced",
            "estimated_hours": 20,
            "prerequisites": "Module 13 - Stacks and Queues",
            "projects": ["Factorial Calculator", "Fibonacci Sequence Generator", "Maze Solver"]
        },
        15: {
            "id": 15, # Added ID
            "title": "Trees - Fundamentals",
            "topics": [
                "Tree Data Structure Introduction",
                "Binary Trees - Concepts and Terminology",
                "Tree Traversal (Inorder, Preorder, Postorder)",
                "Binary Search Trees (BST) - Properties",
                "BST Insertion and Deletion",
                "Balancing Trees (AVL, Red-Black - Concepts)",
                "Applications of Trees"
            ],
            "difficulty": "Advanced",
            "estimated_hours": 25,
            "prerequisites": "Module 14 - Recursion",
            "projects": ["Family Tree Visualizer", "File System Navigator", "Expression Tree Builder"]
        },
        16: {
            "id": 16, # Added ID
            "title": "Graphs - Fundamentals",
            "topics": [
                "Graph Data Structure Introduction",
                "Graph Representations (Adjacency Matrix, Adjacency List)",
                "Graph Traversal (BFS, DFS)",
                "Topological Sorting",
                "Minimum Spanning Trees (Prim's, Kruskal's)",
                "Shortest Path Algorithms (Dijkstra's, Bellman-Ford)",
                "Graph Applications"
            ],
            "difficulty": "Expert",
            "estimated_hours": 30,
            "prerequisites": "Module 15 - Trees",
            "projects": ["Social Network Analyzer", "Route Finder", "Dependency Graph Visualizer"]
        },
        17: {
            "id": 17, # Added ID
            "title": "Dynamic Programming",
            "topics": [
                "Introduction to Dynamic Programming",
                "Memoization vs Tabulation",
                "Optimal Substructure and Overlapping Subproblems",
                "Knapsack Problem",
                "Longest Common Subsequence",
                "Coin Change Problem",
                "Real-world DP Applications"
            ],
            "difficulty": "Expert",
            "estimated_hours": 25,
            "prerequisites": "Module 16 - Graphs",
            "projects": ["DP Problem Solver", "Resource Allocator", "Game Strategy Optimizer"]
        },
        18: {
            "id": 18, # Added ID
            "title": "Advanced Topics and Interview Prep",
            "topics": [
                "Greedy Algorithms",
                "Backtracking and Branch & Bound",
                "Bit Manipulation",
                "Disjoint Set Union (DSU)",
                "Tries (Prefix Trees)",
                "Segment Trees and Fenwick Trees",
                "Common Interview Patterns and Tips"
            ],
            "difficulty": "Expert",
            "estimated_hours": 35,
            "prerequisites": "All previous modules",
            "projects": ["Interview Problem Simulator", "Competitive Programming Toolkit", "DSA Cheatsheet Generator"]
        }
    }

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

    @staticmethod
    def get_topic_content(module_id: int, topic_title: str) -> str:
        """Generates placeholder content for a given topic."""
        module = DSACurriculum.get_module_info(module_id)
        if not module or topic_title not in module["topics"]:
            return "Topic not found."

        # In a real application, this would fetch content from a database or markdown files.
        # For now, we generate a placeholder.
        return f"<h2>{topic_title}</h2><p>This is placeholder content for the topic \"{topic_title}\" in Module {module_id} - {module['title']}. Here you would find detailed explanations, code examples, and exercises related to {topic_title}.</p>"



