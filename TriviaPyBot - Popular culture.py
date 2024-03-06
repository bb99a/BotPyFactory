import random
import time

"""
Pop Culture Trivia Bot: A fun, interactive command-line application that quizzes users on pop culture questions. 
Key Features:
- Colorful terminal output for an engaging user experience.
- A diverse range of pop culture questions with fun facts for correct answers.
- Streak tracking to reward users for consecutive correct answers.
- Automatic quiz reset for replayability without restarting the script.
"""

# ANSI escape codes for colors for better readability in terminal output
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'  # Resets color to default
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RAINBOW = [OKBLUE, OKCYAN, OKGREEN, WARNING, FAIL, HEADER]  # A list to cycle through for rainbow effects

class PopCultureTriviaBot:
    def __init__(self):
        # Initial setup for the trivia bot with a predetermined set of questions.
        self.original_questions = [
            {"question": "Which artist is known as 'The King of Pop'?", "answer": "Michael Jackson", "fun_fact": "Michael Jackson is one of the most significant cultural figures of the 20th century."},
            {"question": "Who stars as the main character in the 'John Wick' series?", "answer": "Keanu Reeves", "fun_fact": "Keanu Reeves performs many of his own stunts in the 'John Wick' series."},
            {"question": "Who is known as the 'Queen of Pop'?", "answer": "Madonna", "fun_fact": "Madonna has sold more than 300 million records worldwide."},
            {"question": "Which movie features the song 'My Heart Will Go On'?", "answer": "Titanic", "fun_fact": "'Titanic' is one of the highest-grossing movies of all time."},
            {"question": "In what year did the television show 'Friends' first premiere?", "answer": "1994", "fun_fact": "The iconic orange couch in 'Friends' was found in the Warner Bros. studio's basement."},
            {"question": "Who starred as the lead role in the movie 'Lara Croft: Tomb Raider'?", "answer": "Angelina Jolie", "fun_fact": "Angelina Jolie performed many of her own stunts in the movie."},
            {"question": "Which movie features a giant ape named Kong?", "answer": "King Kong", "fun_fact": "The original 'King Kong' movie was released in 1933."},
            {"question": "What social media platform was founded by Mark Zuckerberg?", "answer": "Facebook", "fun_fact": "Facebook is one of the largest social networking sites in the world, with billions of users globally."},
            {"question": "What animated film features a character named 'Woody'?", "answer": "Toy Story", "fun_fact": "'Toy Story' was the first feature-length film made entirely with CGI."},
            {"question": "What band was Paul McCartney a member of?", "answer": "The Beatles", "fun_fact": "Paul McCartney is one of the most successful composers and performers of all time."},
            {"question": "Who directed the movie 'Jurassic Park'?", "answer": "Steven Spielberg", "fun_fact": "'Jurassic Park' was a breakthrough in the use of computer-generated imagery to create dinosaurs."},
            {"question": "Who painted the Mona Lisa?", "answer": "Leonardo da Vinci", "fun_fact": "The Mona Lisa is considered an archetypal masterpiece of the Italian Renaissance."}
            # Additional new questions here...
        ]
        self.questions = self.original_questions.copy()  # Copy of questions for the current game session
        self.score = 0  # User's score
        self.streak = 0  # Number of consecutive correct answers
        self.encouragements = ["Awesome!", "Correct!", "Nice job!", "Spot on!", "You're on fire!"]  # Feedback messages

    def print_in_color(self, text, color):
        """Prints text in specified ANSI color for enhanced readability."""
        print(color + text + Colors.ENDC)

    def print_fun_fact_in_rainbow(self, fun_fact, streak):
        """Highlights fun facts in rainbow colors based on the user's answer streak."""
        color_index = (streak // 5 - 1) % len(Colors.RAINBOW)
        self.print_in_color(fun_fact, Colors.RAINBOW[color_index])

    def ask_question(self):
        """Interactively quizzes the user, checks responses, and updates scores and streaks."""
        if not self.questions:
            self.print_in_color("No more questions available.", Colors.WARNING)
            return False  # Indicates no more questions are available
        question = random.choice(self.questions)
        start_time = time.time()
        user_answer = input(question["question"] + " ").strip()
        end_time = time.time()
        time_taken = end_time - start_time

        if user_answer.lower() == question["answer"].lower():
            self.handle_correct_answer(question, time_taken)
        else:
            self.handle_incorrect_answer(question)
        self.questions.remove(question)  # Remove answered question from the pool
        return True

    def handle_correct_answer(self, question, time_taken):
        """Handles user's correct answers and provides encouragement."""
        self.score += 1
        self.streak += 1
        encouragement = random.choice(self.encouragements)
        self.print_in_color(encouragement, Colors.OKGREEN)
        if time_taken < 20:
            self.score += 1
            self.print_in_color("Bonus point for quick thinking!", Colors.OKGREEN)
        if self.streak % 5 == 0:
            self.print_in_color("Streak bonus! +5 points!", Colors.OKGREEN)
            self.score += 5
            self.print_fun_fact_in_rainbow(question['fun_fact'], self.streak)
        else:
            self.print_in_color("Fun Fact: " + question['fun_fact'], Colors.OKCYAN)

    def handle_incorrect_answer(self, question):
        """Provides feedback for incorrect answers and resets streak."""
        self.print_in_color("Wrong! The correct answer was " + question['answer'] + ".", Colors.FAIL)
        self.streak = 0

    def start_quiz(self):
        """Begins the trivia quiz, cycling through questions until all are answered or the user decides to stop."""
        play_again = "yes"
        while play_again.lower() == "yes":
            self.print_in_color("Welcome to the Pop Culture Trivia Bot!", Colors.BOLD)
            while self.questions:
                if not self.ask_question():
                    break
                print(f"Current score: {self.score}")
            self.print_in_color(f"Quiz over! Final score: {self.score}", Colors.BOLD)
            play_again = input("Would you like to play again? (yes/no): ").strip()
            if play_again.lower() == "yes":
                self.reset_quiz()

    def reset_quiz(self):
        """Resets the quiz for a new game session, allowing for replayability."""
        self.questions = self.original_questions.copy()  # Resets the questions list
        self.score = 0
        self.streak = 0
        print("The quiz has been reset for a new game session.")

# Main execution
if __name__ == "__main__":
    trivia_bot = PopCultureTriviaBot()
    trivia_bot.start_quiz()
