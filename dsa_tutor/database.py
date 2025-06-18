import sqlite3
from contextlib import contextmanager
import json
from typing import Dict

class DatabaseManager:
    """Handles all database operations for user progress tracking"""
    
    def __init__(self, db_path='dsa_tutor.db'):
        self.db_path = db_path
        self.init_database()
    
    def init_database(self):
        """Initialize database with required tables"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # User progress table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS user_progress (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id TEXT UNIQUE,
                    current_module INTEGER DEFAULT 1,
                    completed_topics TEXT DEFAULT '[]',
                    solved_problems TEXT DEFAULT '[]',
                    total_learning_time INTEGER DEFAULT 0,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Learning sessions table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS learning_sessions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id TEXT,
                    module_id INTEGER,
                    topic TEXT,
                    session_duration INTEGER,
                    problems_solved INTEGER DEFAULT 0,
                    session_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            conn.commit()
    
    @contextmanager
    def get_db_connection(self):
        """Context manager for database connections"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        try:
            yield conn
        finally:
            conn.close()
    
    def get_user_progress(self, user_id: str) -> Dict:
        """Get user's learning progress"""
        try:
            with self.get_db_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM user_progress WHERE user_id = ?", (user_id,))
                row = cursor.fetchone()

                if row:
                    return {
                        'current_module': row['current_module'],
                        'completed_topics': json.loads(row['completed_topics']),
                        'solved_problems': json.loads(row['solved_problems']),
                        'total_learning_time': row['total_learning_time']
                    }
                else:
                    # Create new user
                    cursor.execute("""
                        INSERT INTO user_progress (user_id) VALUES (?)
                    """, (user_id,))
                    conn.commit()
                    return {
                        'current_module': 1,
                        'completed_topics': [],
                        'solved_problems': [],
                        'total_learning_time': 0
                    }
        except Exception as e:
            # Log the error for debugging purposes
            print(f"Database error in get_user_progress for user_id {user_id}: {e}")
            # Return a default empty progress dictionary in case of any error
            return {
                'current_module': 1,
                'completed_topics': [],
                'solved_problems': [],
                'total_learning_time': 0
            }

    def update_user_progress(self, user_id: str, **kwargs):
        """Update user's progress"""
        with self.get_db_connection() as conn:
            cursor = conn.cursor()
            
            set_clauses = []
            values = []
            
            for key, value in kwargs.items():
                if key in ["completed_topics", "solved_problems"]:
                    value = json.dumps(value)
                set_clauses.append(f"{key} = ?")
                values.append(value)
            
            set_clauses.append("updated_at = CURRENT_TIMESTAMP")
            values.append(user_id)
            query = f"UPDATE user_progress SET {', '.join(set_clauses)} WHERE user_id = ?"
            cursor.execute(query, values)
            conn.commit()
