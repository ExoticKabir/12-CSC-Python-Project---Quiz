from tkinter import *
import random
import webbrowser

names_list = []

global questions_answers

asked = []

score = 0





questions_answers = {
    1: [
        "1+2?", #First item, this is going to be the question, index 0
        "2", #Choice 1, index 1
        "4", #Choice 2, index 2
        "3", #Choice 3, index 3
        "43", #Choice 4, index 4
        "3", #index 5, An item, the correct choice/option <- this will be displayed if incorrect choice is selected
        3], #Last item, "3" <- index position of correct answer


    2: [
        "7x9?", #First item, this is going to be the question, index 0
        "49", #Choice 1, index 1
        "63", #Choice 2, index 2
        "23", #Choice 3, index 3
        "21", #Choice 4, index 4
        "63", #index 5, An item, the correct choice/option <- this will be displayed if incorrect choice is selected
        2], #Last item, "3" <- index position of correct answer


    3: [
        "2-9?", #First item, this is going to be the question, index 0
        "-7", #Choice 1, index 1
        "34", #Choice 2, index 2
        "3", #Choice 3, index 3
        "All of the above", #Choice 4, index 4
        "-7", #index 5, An item, the correct choice/option <- this will be displayed if incorrect choice is selected
        1], #Last item, "3" <- index position of correct answer

    4: [
        "7/2?", #First item, this is going to be the question, index 0
        "3", #Choice 1, index 1
        "4", #Choice 2, index 2
        "3.5", #Choice 3, index 3
        "2", #Choice 4, index 4
        "3.5", #index 5, An item, the correct choice/option <- this will be displayed if incorrect choice is selected
        3], #Last item, "3" <- index position of correct answer

    
    5: [
        "5+3x3? Follow BEDMAS", #First item, this is going to be the question, index 0
        "34", #Choice 1, index 1
        "333423423", #Choice 2, index 2
        "14", #Choice 3, index 3
        "None of the above", #Choice 4, index 4
        "14", #index 5, An item, the correct choice/option <- this will be displayed if incorrect choice is selected
        3], #Last item, "3" <- index position of correct answer

    6: [
        "Is math fun?", #First item, this is going to be the question, index 0
        "Yes!", #Choice 1, index 1
        "No! What is math?", #Choice 2, index 2
        "Maybe", #Choice 3, index 3
        "Who cares?", #Choice 4, index 4
        "Yes!", #index 5, An item, the correct choice/option <- this will be displayed if incorrect choice is selected
        1], #Last item, "3" <- index position of correct answer

    7: [
        "9^2?", #First item, this is going to be the question, index 0
        "23", #Choice 1, index 1
        "24", #Choice 2, index 2
        "69", #Choice 3, index 3
        "81", #Choice 4, index 4
        "81", #index 5, An item, the correct choice/option <- this will be displayed if incorrect choice is selected
        4], #Last item, "3" <- index position of correct answer

    8: [
        "What is discriminant?", #First item, this is going to be the question, index 0
        "b^2-2ab", #Choice 1, index 1
        "b^2-4ac", #Choice 2, index 2
        "c^2+2ab", #Choice 3, index 3
        "c^2-2ab", #Choice 4, index 4
        "b^2-4ac", #index 5, An item, the correct choice/option <- this will be displayed if incorrect choice is selected
        2], #Last item, "3" <- index position of correct answer

    9: [
        "What is the capital of Bangladesh?", #First item, this is going to be the question, index 0
        "New Delhi", #Choice 1, index 1
        "Suva", #Choice 2, index 2
        "Ankara", #Choice 3, index 3
        "Dhaka", #Choice 4, index 4
        "Dhaka", #index 5, An item, the correct choice/option <- this will be displayed if incorrect choice is selected
        4], #Last item, "3" <- index position of correct answer

    10: [
        "How many seconds are in a day?", #First item, this is going to be the question, index 0
        "99345", #Choice 1, index 1
        "72000", #Choice 2, index 2
        "86400", #Choice 3, index 3
        "None of the above", #Choice 4, index 4
        "86400", #index 5, An item, the correct choice/option <- this will be displayed if incorrect choice is selected
        3] #Last item, "3" <- index position of correct answer
}

def randomiser():
    global qnum  #Question number is the key in our dictionary questions_answers, I will have 10 questions so 10 keys
    qnum = random.randint(1, 10)
    if qnum not in asked: #To ensure questions don't repeat
        asked.append(qnum)
    elif qnum in asked: #If it is not in asked list(near the top), then it will run randomiser
        randomiser()

class Introduction:
    def __init__(self, parent):
        background_color = "plum1"
        #setting up first frame
        self.quiz_frame = Frame(parent,
                                bg=background_color,
                                padx=100,
                                pady=100)
        self.quiz_frame.grid()
        
        #Label widget for our heading
        self.heading_label = Label(self.quiz_frame,
                                   text = "This test will test your math skills.",
                                   font=("Comic Sans MS", "13"),
                                   bg=background_color)
        self.heading_label.grid(row=0, padx=20)

        #creates a label to ask for the name
        self.user_label = Label(self.quiz_frame,
                                text="Enter your name to begin this journey...",
                                font=("Comic Sans MS", "13"),
                                bg=background_color)
        self.user_label.grid(row=1, padx=20, pady=20)

        #create an entry box for the name
        self.entry_box = Entry(self.quiz_frame)
        self.entry_box.grid(row=2, padx=20, pady=25)

        #create a Button - continue button
        self.continue_button = Button(self.quiz_frame,
                                      text="Continue",
                                      font=("Arial", "13"),
                                      bg="SpringGreen2",
                                      command=self.name_collection)
        self.continue_button.grid(row=3, padx=20, pady=20)


        #create a Button - privacy button
        self.privacy_button = Button(self.quiz_frame,
                                      text="Privacy Policy",
                                      font=("Arial", "13"),
                                      bg="Cyan",
                                      command = self.pp)
        self.privacy_button.grid(row=4, padx=20, pady=20)


    def pp(self):
        self.quiz_frame.destroy()
        Privacy_Policy(root)


    def name_collection(self):
        name = self.entry_box.get()  #this will collect the name from the entry box
        names_list.append(name)  #adds the user name to names list declared at the beginning
        self.quiz_frame.destroy()  #this will destroy the starter window
        Quiz(root)


class Privacy_Policy:
    def __init__(self, parent):

        background_color = "plum1"

        self.pp_frame = Frame(parent, bg = background_color, padx = 100, pady = 100)
        self.pp_frame.grid()

        self.pp_heading = Label(self.pp_frame, text = "   This is the privacy policy   ", font = ("Comic Sans MS", 22), bg = background_color, pady = 15)
        self.pp_heading.grid(row = 0)

        self.ppback_button = Button(self.pp_frame, text = " Back ", width = 15, bg = "Cyan", font=("Comic Sans MS", 12), command=self.privacy_policy_back)
        self.ppback_button.grid(row=4, pady=20)

        self.exit_button = Button(self.pp_frame, text = "Exit", width = 10, bg = "Red", font=("Comic Sans MS", 12), command = self.close_end)
        self.exit_button.grid(row=6, pady=20)

    def privacy_policy_back(self):
        self.pp_frame.destroy()  #this will destroy the starter window
        Introduction(root)

    def close_end(self):
        self.pp_frame.destroy()
        root.destroy()




class Quiz:
    def __init__(self, parent):
        background_color = "plum1"
        #setting up first frame
        self.quiz_frame = Frame(parent,
                                bg=background_color,
                                padx=100,
                                pady=100)
        self.quiz_frame.grid()

        randomiser() #this will randomly pick a question so the same questions don't keep repeating
        
        #Label widget for our question
        self.question_label = Label(self.quiz_frame,
                                   text = questions_answers[qnum][0],
                                   font=("Comic Sans MS", "16"),
                                   bg=background_color)
        self.question_label.grid(row=0, padx=150)

        #This holds value of radio buttons
        self.var1 = IntVar()

        #radio button 1, in order to hold first choice
        self.rb1 = Radiobutton(self.quiz_frame,
                               text=questions_answers[qnum][1],
                               font=("Comic Sans MS", "12"),
                               bg=background_color,
                               value=1,
                               padx=10,
                               pady=15,
                               variable=self.var1,
                               indicator=0,
                               background="burlywood1")
        self.rb1.grid(row=2) #placement


        #radio button 2, in order to hold first choice
        self.rb2 = Radiobutton(self.quiz_frame,
                               text=questions_answers[qnum][2],
                               font=("Comic Sans MS", "12"),
                               bg=background_color,
                               value=2,
                               padx=10,
                               pady=15,
                               variable=self.var1,
                               indicator=0,
                               background="burlywood1")
        self.rb2.grid(row=3) #placement


        #radio button 3, in order to hold first choice
        self.rb3 = Radiobutton(self.quiz_frame,
                               text=questions_answers[qnum][3],
                               font=("Comic Sans MS", "12"),
                               bg=background_color,
                               value=3,
                               padx=10,
                               pady=15,
                               variable=self.var1,
                               indicator=0,
                               background="burlywood1")
        self.rb3.grid(row=4) #placement


        #radio button 1, in order to hold first choice
        self.rb4 = Radiobutton(self.quiz_frame,
                               text=questions_answers[qnum][4],
                               font=("Comic Sans MS", "12"),
                               bg=background_color,
                               value=4,
                               padx=10,
                               pady=15,
                               variable=self.var1,
                               indicator=0,
                               background="burlywood1")
        self.rb4.grid(row=5) #placement
        
        #confirm button to move on to the next question
        self.confirm_button = Button(self.quiz_frame,
                                    text = "Confirm",
                                    bg="SpringGreen2",
                                    command=self.test_progress,
                                    padx=10)
        self.confirm_button.grid(row=6) #placement of continue button

        # Creating a score label for the user to know how well they have done so far.
        self.score_label = Label(self.quiz_frame,
                                    text="SCORE",
                                    font=("Arial", "15"),
                                    bg=background_color)
        self.score_label.grid(row=7, padx=10, pady=1)

        self.exit_button = Button(self.quiz_frame, text = "Exit", width = 10, bg = "Red", font=("Comic Sans MS", 12), command = self.close_end)
        self.exit_button.grid(row=9, pady=20)



    #Method for the appearance of the next question
    def questions_setup(self):
        randomiser()
        self.var1.set(0)
        self.question_label.config(text = questions_answers[qnum][0])
        self.rb1.config(text = questions_answers[qnum][1])
        self.rb2.config(text = questions_answers[qnum][2])
        self.rb3.config(text = questions_answers[qnum][3])
        self.rb4.config(text = questions_answers[qnum][4])

    #This is the method which will be called when the confirm button is clicked <- taking care of progress
    def test_progress(self):
        global score
        scr_label = self.score_label
        choice = self.var1.get()
        # Checking how many items are in the asked list
        if len(asked) > 9: #If this is the last question
            if choice == questions_answers[qnum][6]: #If they select the correct choice for last question
                score += 1 # Adding one point to the score
                
                self.finish_quiz_help = Button(self.quiz_frame, 
                                    text = "Continue",
                                    font = ("Comic Sans MS", 13), 
                                    bg = "SpringGreen2", 
                                    command = self.end_screen)
                self.finish_quiz_help.grid(row = 8, padx = 5, pady = 5)
                
                self.confirm_button.destroy()
                self.question_label.destroy()
                self.rb1.destroy()
                self.rb2.destroy()
                self.rb3.destroy()
                self.rb4.destroy()
                self.exit_button.destroy()

                
                
                if score == 1: #singular grammar, 1 question, no "s" after question
                    scr_label.configure(text = "You finished my quiz! You correctly answered " + str(score) + " question.")
                    
                else: #plural, correctly answered more than 1 question. So "s" after question
                    scr_label.configure(text = "You finished my quiz! You correctly answered " + str(score) + " questions.")
                
                
            else: #If they select the incorrect choice for last question
                score +=0
                
                self.finish_quiz_help = Button(self.quiz_frame, 
                                    text = "Continue",
                                    font = ("Comic Sans MS", 13), 
                                    bg = "SpringGreen2", 
                                    command = self.end_screen)
                self.finish_quiz_help.grid(row = 8, padx = 5, pady = 5)
                
                scr_label.configure(text = "The answer to the previous question was '" + questions_answers[qnum][5] + "' .That was the last question so you have now finished my quiz!")
                self.confirm_button.destroy()
                self.question_label.destroy()
                self.rb1.destroy()
                self.rb2.destroy()
                self.rb3.destroy()
                self.rb4.destroy()
                self.exit_button.destroy()


        else: #If it is not the last question
            if choice == 0: #boundary testing <- ensuring the user actually selects a choice
                self.confirm_button.config(text = "Please select a choice!")
                choice = self.var1.get()

            else: #If it isn't the last question and they HAVE selected a choice.
                if choice == questions_answers[qnum][6]: #If they selected the correct choice
                    score += 1

                    if score == 1: #singular grammar, 1 question, no "s" after question
                        scr_label.configure(text = "Well done! You have now correctly answered " + str(score) + " question.")
                    
                    else: #plural, correctly answered more than 1 question. So "s" after question
                        scr_label.configure(text = "Well done! You have now correctly answered " + str(score) + " questions.")
                    
                    self.confirm_button.config(text = "Confirm")
                    self.questions_setup() #Will move to the next question
                
                else: #If the choice is incorrect 
                    score += 0
                    scr_label.configure(text = "The answer to the previous question was '" + questions_answers[qnum][5] + "'.")
                    self.confirm_button.config(text = "Confirm")
                    self.questions_setup() #Will move to the next question


    def end_screen(self):
        self.quiz_frame.destroy()
        End(root)


    def close_end(self):
        self.quiz_frame.destroy()
        root.destroy()
    

final_score = score

class End:
    def __init__(self, parent):
            background_color = "plum1"

            self.end_frame = Frame(parent, bg = background_color, padx = 100, pady = 100)
            self.end_frame.grid()

            self.end_heading = Label(self.end_frame, text = "   Thanks for playing!   ", font = ("Comic Sans MS", 22), bg = background_color, pady = 15)
            self.end_heading.grid(row = 0)

            if score < 5:
                self.helper_button = Button(self.end_frame, text = "Resources", width = 13, bg = "Cyan", font = ("Comic Sans MS", 13), command = self.help_continue_less_than_5)
                self.helper_button.grid(row=4, pady=20)
            

            else:
                self.helper_button_smart = Button(self.end_frame, text = "Resources", width = 13, bg = "Cyan", font = ("Comic Sans MS", 13), command = self.help_continue_more_than_5)
                self.helper_button_smart.grid(row=5, pady=20)

            self.exit_button = Button(self.end_frame, text = "Exit", width = 10, bg = "Red", font = ("Comic Sans MS", 13), command = self.close_end)
            self.exit_button.grid(row=7, pady=20)

            

    def close_end(self):
        self.end_frame.destroy()
        root.destroy()

    def help_continue_less_than_5(self):
        self.end_frame.destroy()  #this will destroy the starter window
        Helper(root)


    def help_continue_more_than_5(self):
        self.end_frame.destroy()  #this will destroy the starter window
        Helper_Smart(root)



class Helper:
    def __init__(self, parent):

        background_color = "plum1"

        self.help_frame = Frame(parent, bg = background_color, padx = 100, pady = 100)
        self.help_frame.grid()

        self.help_heading = Label(self.help_frame, text = "   This will be where you can help youself   ", font = ("Comic Sans MS", 22), bg = background_color, pady = 15)
        self.help_heading.grid(row = 0)

        self.help_heading_2 = Label(self.help_frame, text = "You're final percentage was " + str((score/10)*100) + "%. With this in mind, you might want to look at these websites.", font = ("Comic Sans MS", 16), bg = background_color, pady = 15)
        self.help_heading_2.grid(row = 1)

        self.link_button_1 = Button(self.help_frame, text = "  IXL  ", width = 15, bg = "Cyan", font = ("Comic Sans MS", 13), command=self.ixl)
        self.link_button_1.grid(row=4, pady=20)

        self.link_button_2 = Button(self.help_frame, text = "  Khan Academy  ", width = 15, bg = "Cyan", font = ("Comic Sans MS", 13), command=self.khan)
        self.link_button_2.grid(row=5, pady=20)

        self.link_button_3 = Button(self.help_frame, text = "  The Verge  ", width = 15, bg = "Cyan", font = ("Comic Sans MS", 13), command=self.verge)
        self.link_button_3.grid(row=6, pady=20)

        self.exit_button = Button(self.help_frame, text = "Exit", width = 10, bg = "Red", font = ("Comic Sans MS", 13), command = self.close_end)
        self.exit_button.grid(row=7, pady=20)

    def ixl(self):
        
        webbrowser.open("https://nz.ixl.com/")
        root.destroy()

    def khan(self):
        
        webbrowser.open("https://www.khanacademy.org/")
        root.destroy()

    def verge(self):
        
        webbrowser.open("https://www.theverge.com/")
        root.destroy()

    def close_end(self):
        self.help_frame.destroy()
        root.destroy()



class Helper_Smart:
    def __init__(self, parent):

        background_color = "plum1"

        self.help_frame = Frame(parent, bg = background_color, padx = 100, pady = 100)
        self.help_frame.grid()

        self.help_heading = Label(self.help_frame, text = "   This will be where you can help youself   ", font = ("Comic Sans MS", 22), bg = background_color, pady = 15)
        self.help_heading.grid(row = 0)

        self.help_heading_2 = Label(self.help_frame, text = "You're final percentage was " + str((score/10)*100) + "%. With this in mind, you might want to look at these websites.", font = ("Comic Sans MS", 16), bg = background_color, pady = 15)
        self.help_heading_2.grid(row = 1)

        self.link_button_1 = Button(self.help_frame, text = "  You're SMORT  ", width = 15, bg = "Cyan", font = ("Comic Sans MS", 13), command=self.ixl)
        self.link_button_1.grid(row=4, pady=20)

        self.link_button_2 = Button(self.help_frame, text = "  Khan Academy  ", width = 15, bg = "Cyan", font = ("Comic Sans MS", 13), command=self.khan)
        self.link_button_2.grid(row=5, pady=20)

        self.link_button_3 = Button(self.help_frame, text = "  The Verge  ", width = 15, bg = "Cyan", font = ("Comic Sans MS", 13), command=self.verge)
        self.link_button_3.grid(row=6, pady=20)

        self.exit_button = Button(self.help_frame, text = "Exit", width = 10, bg = "Red", font = ("Comic Sans MS", 13), command = self.close_end)
        self.exit_button.grid(row=7, pady=20)

    def ixl(self):
        
        webbrowser.open("https://nz.ixl.com/")
        root.destroy()

    def khan(self):
        
        webbrowser.open("https://www.khanacademy.org/")
        root.destroy()

    def verge(self):
        
        webbrowser.open("https://www.theverge.com/")
        root.destroy()

    def close_end(self):
        self.help_frame.destroy()
        root.destroy()     
    



####### program start ##########

if __name__ == "__main__":
    root = Tk()
    root.title("Math Helper :)")
    Introduction_object = Introduction(root)
    root.mainloop() #This loops the window for to it stay and not disappear.