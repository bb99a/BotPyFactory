import random
import time

# ANSI escape codes for colors
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RAINBOW = [OKBLUE, OKCYAN, OKGREEN, WARNING, FAIL, HEADER]

class PopCultureTriviaBot:
    def __init__(self):
        self.questions = [
            {"question": "Who is known as the 'Queen of Pop'?", "answer": "Madonna", "fun_fact": "Madonna has sold more than 300 million records worldwide."},
            {"question": "Which movie features the song 'My Heart Will Go On'?", "answer": "Titanic", "fun_fact": "'Titanic' is one of the highest-grossing movies of all time."},
            {"question": "Who wrote the Harry Potter series?", "answer": "J.K. Rowling", "fun_fact": "The Harry Potter series has been translated into over 80 languages."},
            {"question": "What is the real name of the rapper Eminem?", "answer": "Marshall Bruce Mathers III", "fun_fact": "Eminem won an Academy Award for Best Original Song for 'Lose Yourself' from the movie 8 Mile."},
            {"question": "In what year did the television show 'Friends' first premiere?", "answer": "1994", "fun_fact": "The iconic orange couch in 'Friends' was found in the Warner Bros. studio's basement."},
            {"question": "Who played Jack Dawson in the movie 'Titanic'?", "answer": "Leonardo DiCaprio", "fun_fact": "Titanic was the first film to reach the billion-dollar mark."},
            {"question": "Which artist is known for the hit song 'Thriller'?", "answer": "Michael Jackson", "fun_fact": "'Thriller' is the best-selling album of all time."},
            {"question": "What is the name of Batman's butler?", "answer": "Alfred Pennyworth", "fun_fact": "Alfred has been portrayed in live-action films by actors including Michael Caine and Jeremy Irons."},
            {"question": "Who is the author of 'The Hunger Games' series?", "answer": "Suzanne Collins", "fun_fact": "Suzanne Collins is also the author of another series called 'The Underland Chronicles'."},
            {"question": "Which TV show features the characters Sheldon Cooper and Leonard Hofstadter?", "answer": "The Big Bang Theory", "fun_fact": "The Big Bang Theory's theme song was performed by the Barenaked Ladies."},
            {"question": "What year did the Beatles release their first album?", "answer": "1963", "fun_fact": "The Beatles' first album was titled 'Please Please Me'."},
            {"question": "Who is known as the 'Material Girl'?", "answer": "Madonna", "fun_fact": "Madonna has had more Billboard Hot 100 hits than any other female artist in history."},
            {"question": "What is the name of the theme park featured in 'Jurassic World'?", "answer": "Isla Nublar", "fun_fact": "Isla Nublar is a fictional island located off the Pacific coast of Costa Rica."},
            {"question": "Who starred as the lead role in the movie 'Lara Croft: Tomb Raider'?", "answer": "Angelina Jolie", "fun_fact": "Angelina Jolie performed many of her own stunts in the movie."},
            {"question": "What TV series is based on characters by author George R. R. Martin?", "answer": "Game of Thrones", "fun_fact": "Game of Thrones holds the record for the most Emmy Awards won by a scripted television series."},
            {"question": "Which artist painted 'Starry Night'?", "answer": "Vincent van Gogh", "fun_fact": "'Starry Night' depicts the view from the window of van Gogh's asylum room at Saint-Rémy-de-Provence."},
            {"question": "What is the real name of the superhero known as 'The Flash'?", "answer": "Barry Allen", "fun_fact": "There have been several versions of The Flash, but Barry Allen is the most famous one."},
            {"question": "Who is the lead singer of the band U2?", "answer": "Bono", "fun_fact": "Bono's real name is Paul David Hewson."},
            {"question": "Which movie features a giant ape named Kong?", "answer": "King Kong", "fun_fact": "The original 'King Kong' movie was released in 1933."},
            {"question": "Who wrote 'The Great Gatsby'?", "answer": "F. Scott Fitzgerald", "fun_fact": "'The Great Gatsby' is considered one of the greatest works of American literature."},
            {"question": "What is the name of the fictional British spy in the film series created by Ian Fleming?", "answer": "James Bond", "fun_fact": "James Bond is also known by his code number, 007."},
            {"question": "What is the longest-running Broadway show?", "answer": "The Phantom of the Opera", "fun_fact": "'The Phantom of the Opera' has been performed over 13,000 times since it opened in 1988."},
            {"question": "What animated film features a character named 'Woody'?", "answer": "Toy Story", "fun_fact": "'Toy Story' was the first feature-length film made entirely with CGI."},
            {"question": "Who directed the movie 'Jurassic Park'?", "answer": "Steven Spielberg", "fun_fact": "'Jurassic Park' was a breakthrough in the use of computer-generated imagery to create dinosaurs."},
            {"question": "Which singer is known as the 'Princess of Pop'?", "answer": "Britney Spears", "fun_fact": "Britney Spears' debut single '...Baby One More Time' was a global hit, topping the charts in 22 countries."},
            {"question": "What is the highest-selling video game of all time?", "answer": "Minecraft", "fun_fact": "'Minecraft' has sold more than 200 million copies worldwide."},
            {"question": "Who created the fictional detective Sherlock Holmes?", "answer": "Arthur Conan Doyle", "fun_fact": "Sherlock Holmes is one of the most portrayed literary characters in film and television."},
            {"question": "Which TV show is set in the fictional town of Hawkins, Indiana?", "answer": "Stranger Things", "fun_fact": "'Stranger Things' was inspired by various 1980s pop culture references."},
            {"question": "Who painted the Mona Lisa?", "answer": "Leonardo da Vinci", "fun_fact": "The Mona Lisa is considered an archetypal masterpiece of the Italian Renaissance."},
            {"question": "What band was Paul McCartney a member of?", "answer": "The Beatles", "fun_fact": "Paul McCartney is one of the most successful composers and performers of all time."},
            {"question": "Which movie features a young wizard named Harry Potter?", "answer": "Harry Potter and the Sorcerer's Stone", "fun_fact": "The Harry Potter film series is one of the highest-grossing film series of all time."},
            {"question": "What social media platform was founded by Mark Zuckerberg?", "answer": "Facebook", "fun_fact": "Facebook is one of the largest social networking sites in the world, with billions of users globally."}

            #add more questions and fun facts to the bot above, or change them to your liking.
        ]
        self.score = 0
        self.streak = 0
        self.encouragements = ["Awesome!", "Correct!", "Nice job!", "Spot on!", "You're on fire!"]

    def print_in_color(self, text, color):
        print(color + text + Colors.ENDC)

    def print_fun_fact_in_rainbow(self, fun_fact, streak):
        color_index = (streak // 5 - 1) % len(Colors.RAINBOW)  # Adjust for streak index and loop through colors
        self.print_in_color(fun_fact, Colors.RAINBOW[color_index])

    def ask_question(self):
        if not self.questions:
            self.print_in_color("No more questions available.", Colors.WARNING)
            return
        question = random.choice(self.questions)
        start_time = time.time()
        user_answer = input(question["question"] + " ")
        end_time = time.time()
        time_taken = end_time - start_time

        if user_answer.lower() == question["answer"].lower():
            self.score += 1
            self.streak += 1
            encouragement = random.choice(self.encouragements)
            self.print_in_color(encouragement, Colors.OKGREEN)
            if time_taken < 20:  # Bonus points for answering within 20 seconds
                self.score += 1
                self.print_in_color("Bonus point for quick thinking!", Colors.OKGREEN)
            if self.streak % 5 == 0:  # Every 5 correct answers in a row
                self.print_in_color("Streak bonus! +5 points!", Colors.OKGREEN)
                self.score += 5
                self.print_fun_fact_in_rainbow(f"Fun Fact: {question['fun_fact']}", self.streak)
            else:
                self.print_in_color(f"Fun Fact: {question['fun_fact']}", Colors.OKCYAN)
        else:
            self.print_in_color(f"Wrong! The correct answer was {question['answer']}.", Colors.FAIL)
            self.streak = 0  # Reset streak on wrong answer
        self.questions.remove(question)  # Remove the question from the pool to avoid repetition

    def start_quiz(self):
        self.print_in_color("Welcome to Awab's Pop Culture Trivia Bot!", Colors.BOLD)
        while self.questions:
            self.ask_question()
            print(f"Current score: {self.score}")
        self.print_in_color(f"Quiz over! Final score: {self.score}", Colors.BOLD)

# Initialize and start the quiz
trivia_bot = PopCultureTriviaBot()
trivia_bot.start_quiz()








































