#Version 8 -> Applies design and feedback peers


from tkinter import * #For GUI
import random #To randomise the questions
import webbrowser #This is needed to launch the user to certain websites

names_list = [] #This will contain the user's name, which will be used later on

global questions_answers #Making questions_answers dictionary global so it can be called from anywhere

asked = [] #Will contain the questions that have already been asked so they don't display again

score = 0 #Setting the initial score or questions correct to zero




# I have replaced the questions now with proper math questions.
questions_answers = {
    1: [
        "Which number equals 𝑖3?", #First item, this is going to be the question, index 0
        "𝑖", #Choice 1, index 1
        "-1", #Choice 2, index 2
        "-𝑖", #Choice 3, index 3
        "1", #Choice 4, index 4
        "-𝑖", #index 5, An item, the correct choice/option <- this will be displayed if incorrect choice is selected
        3], #Last item, "3" <- index position of correct answer


    2: [
        "Complex conjugate of 5+10i?", #First item, this is going to be the question, index 0
        "10+20𝑖", #Choice 1, index 1
        "5-10𝑖", #Choice 2, index 2
        "15", #Choice 3, index 3
        "π/4", #Choice 4, index 4
        "5-10𝑖", #index 5, An item, the correct choice/option <- this will be displayed if incorrect choice is selected
        2], #Last item, "3" <- index position of correct answer


    3: [
        "How many radians is 90°?", #First item, this is going to be the question, index 0
        "(π/2) radians", #Choice 1, index 1
        "(π/6) radians", #Choice 2, index 2
        "(π/4) radians", #Choice 3, index 3
        "(π/3) radians", #Choice 4, index 4
        "(π/2) radians", #index 5, An item, the correct choice/option <- this will be displayed if incorrect choice is selected
        1], #Last item, "3" <- index position of correct answer

    4: [
        "2+√(15-2x3)?", #First item, this is going to be the question, index 0
        "-3", #Choice 1, index 1
        "+4", #Choice 2, index 2
        "-1", #Choice 3, index 3
        "+2", #Choice 4, index 4
        "-1", #index 5, An item, the correct choice/option <- this will be displayed if incorrect choice is selected
        3], #Last item, "3" <- index position of correct answer

    
    5: [
        "8÷2(2+2)?", #First item, this is going to be the question, index 0
        "1", #Choice 1, index 1
        "100", #Choice 2, index 2
        "16", #Choice 3, index 3
        "None of the above", #Choice 4, index 4
        "16", #index 5, An item, the correct choice/option <- this will be displayed if incorrect choice is selected
        3], #Last item, "3" <- index position of correct answer

    6: [
        "What does differentiation do?", #First item, this is going to be the question, index 0
        "Gives gradient", #Choice 1, index 1
        "Finds area of graph", #Choice 2, index 2
        "Makes it a quadratic", #Choice 3, index 3
        "Helps with integration", #Choice 4, index 4
        "Gives gradient", #index 5, An item, the correct choice/option <- this will be displayed if incorrect choice is selected
        1], #Last item, "3" <- index position of correct answer

    7: [
        "What does integration do?", #First item, this is going to be the question, index 0
        "Converts to radians", #Choice 1, index 1
        "Finds time", #Choice 2, index 2
        "Helps with differentiation", #Choice 3, index 3
        "Finds area of graph", #Choice 4, index 4
        "Finds area of graph", #index 5, An item, the correct choice/option <- this will be displayed if incorrect choice is selected
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
        "What is the equation of a circle?", #First item, this is going to be the question, index 0
        "y = mx + c", #Choice 1, index 1
        "x^3 - y^3 = r", #Choice 2, index 2
        "y = x^2 - r", #Choice 3, index 3
        "(x – h)^2 + (y – k)^2 = r^2", #Choice 4, index 4
        "(x – h)^2 + (y – k)^2 = r^2", #index 5, An item, the correct choice/option <- this will be displayed if incorrect choice is selected
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

def randomiser(): #My question randomiser
    global qnum  #Question number is the key in our dictionary questions_answers, I will have 10 questions so 10 keys
    qnum = random.randint(1, 10)
    if qnum not in asked: #To ensure questions don't repeat
        asked.append(qnum) #Will add the question number to the asked list so it doesn't repeat
    elif qnum in asked: #If it is not in asked list(near the top), then it will run randomiser
        randomiser()



class Introduction: #This is the introduction class
    def __init__(self, parent):
        background_color = "#DA6FE4" #Setting the background colour
        #setting up first frame
        self.quiz_frame = Frame(parent, #The frame
                                bg = background_color,
                                padx = 100,
                                pady = 100)
        self.quiz_frame.grid()
        
        #Label widget for our heading
        self.heading_label = Label(self.quiz_frame, #The heading label
                                   text = "How good are you at math?",
                                   font = ("Comic Sans MS", "13"),
                                   bg = background_color)
        self.heading_label.grid(row = 0, padx = 20)

        #creates a label to ask for the name
        self.user_label = Label(self.quiz_frame,
                                text = "Enter your name to begin this journey...",
                                font = ("Comic Sans MS", "13"),
                                bg  =background_color)
        self.user_label.grid(row = 1, padx = 20, pady = 20)

        #create an entry box for the name
        self.entry_box = Entry(self.quiz_frame)
        self.entry_box.grid(row = 2, padx = 20, pady = 25)

        #creates a button - continue button
        self.continue_button = Button(self.quiz_frame,
                                      text = "Continue",
                                      font = ("Comic Sans MS", "13"),
                                      bg = "SpringGreen2",
                                      command = self.name_collection)
        self.continue_button.grid(row = 3, padx = 20, pady = 20)


        #creates a button - privacy button
        self.privacy_button = Button(self.quiz_frame,
                                      text = "Privacy Policy",
                                      font = ("Comic Sans MS", "13"),
                                      bg = "#ffd64f",
                                      command = self.pp)
        self.privacy_button.grid(row = 4, padx = 20, pady = 20)

        #this is the error label which will be used if the user doesn't enter a name or enters one which is too big, setting it as blank so it appears invisble.
        #I will be able to config it later to change the text
        self.error_label = Label(self.quiz_frame,
                                text = "",
                                font = ("Comic Sans MS", "13"),
                                bg = background_color)
        self.error_label.grid(row = 5)

    #Will run the privacy policy class and destroy the quiz frame or the introduction page
    def pp(self):
        self.quiz_frame.destroy()
        PrivacyPolicy(root)

    #This will collect the name from the entry box
    def name_collection(self):
        name = self.entry_box.get()  #this will collect the name from the entry box
        if len(name) > 1 and len(name) < 13: #Boundary testing, the name has to be between 1 and 13 characters, using len this is possible
            names_list.append(name)  #adds the user name to names list declared at the beginning
            self.quiz_frame.destroy()  #this will destroy the window
            Quiz(root) #Will run the quiz class

        else: #if the name is less than 1 or greater than 13 characters, returns the error message below
            self.error_label.config(text = "Please enter a name which has a min of 2 letters and max of 12 letters.")



class PrivacyPolicy: #my privacy policy component
    def __init__(self, parent):

        background_color = "#DA6FE4" #the background colour

        self.pp_frame = Frame(parent, bg = background_color, padx = 100, pady = 100)
        self.pp_frame.grid() #creating the frame

        self.pp_heading = Label(self.pp_frame, text = "   Privacy Policy   ", font = ("Comic Sans MS", 22), bg = background_color, pady = 15)
        self.pp_heading.grid(row = 0) #setting the heading to privacy policy so the user knows it's the privacy policy page

        #pp_info 1, 2 and 3 display what I want the privacy policy to state
        self.pp_info1 = Label(self.pp_frame, text = "This privacy policy explains the privacy practices of this program. This program was created by Tousif Kabir.", font = ("Comic Sans MS", 12), bg = background_color, pady = 5)
        self.pp_info1.grid(row = 1)

        self.pp_info1 = Label(self.pp_frame, text = "I created this program for my level 2 computer science internal. I do not intend on making this program commercial.", font = ("Comic Sans MS", 12), bg = background_color, pady = 5)
        self.pp_info1.grid(row = 2)

        self.pp_info2 = Label(self.pp_frame, text = "No data is stored or shared. The code for this project can also be found on GitHub.", font = ("Comic Sans MS", 12), bg = background_color, pady = 5)
        self.pp_info2.grid(row = 3)

        #This is a back button which will bring the user back to the introduction page
        self.ppback_button = Button(self.pp_frame, text = " Back ", width = 10, bg = "#ffd64f", font = ("Comic Sans MS", 12), command = self.privacy_policy_back)
        self.ppback_button.grid(row = 4, pady = 15)

        #Exits the quiz
        self.exit_button = Button(self.pp_frame, text = "Exit", width = 10, bg = "Red", font = ("Comic Sans MS", 12), command = self.close_end)
        self.exit_button.grid(row = 6, pady = 10)

        #the function to go back to the introduction component
    def privacy_policy_back(self):
        self.pp_frame.destroy()  #this will destroy the window
        Introduction(root)

        #closes quiz
    def close_end(self):
        self.pp_frame.destroy() #this will destroy the window
        root.destroy()



#my quiz component
class Quiz:
    def __init__(self, parent):
        background_color = "#DA6FE4" #background colour
        #setting up first frame
        self.quiz_frame = Frame(parent, #the frame
                                bg = background_color,
                                padx = 100,
                                pady = 25)
        self.quiz_frame.grid()

        randomiser() #this will randomly pick a question so the same questions don't keep repeating
        
        #Label widget for our question
        self.question_label = Label(self.quiz_frame,
                                   text = questions_answers[qnum][0],
                                   font = ("Comic Sans MS", "16"),
                                   bg = background_color)
        self.question_label.grid(row = 0, padx = 150)

        #creating space between question and choices
        self.empty_space = Label(self.quiz_frame,
                                    text = " ",
                                    font = ("Comic Sans MS", "15"),
                                    bg = background_color)
        self.empty_space.grid(row = 1)

        #This holds value of radio buttons
        self.var1 = IntVar()

        #radio button 1, in order to hold first choice
        self.rb1 = Radiobutton(self.quiz_frame,
                               text = questions_answers[qnum][1],
                               font = ("Comic Sans MS", "12"),
                               value = 1,
                               padx = 10,
                               pady = 15,
                               width = 20,
                               variable = self.var1,
                               indicator = 0,
                               background = "#ffd64f")
        self.rb1.grid(row = 2) #placement


        #radio button 2, in order to hold second choice
        self.rb2 = Radiobutton(self.quiz_frame,
                               text = questions_answers[qnum][2],
                               font = ("Comic Sans MS", "12"),
                               value = 2,
                               padx = 10,
                               pady = 15,
                               width = 20,
                               variable = self.var1,
                               indicator = 0,
                               background = "#ffd64f")
        self.rb2.grid(row = 3) #placement


        #radio button 3, in order to hold third choice
        self.rb3 = Radiobutton(self.quiz_frame,
                               text = questions_answers[qnum][3],
                               font = ("Comic Sans MS", "12"),
                               value = 3,
                               padx = 10,
                               pady = 15,
                               width = 20,
                               variable = self.var1,
                               indicator = 0,
                               background = "#ffd64f")
        self.rb3.grid(row = 4) #placement


        #radio button 4, in order to hold fourth choice
        self.rb4 = Radiobutton(self.quiz_frame,
                               text = questions_answers[qnum][4],
                               font = ("Comic Sans MS", "12"),
                               value = 4,
                               padx = 10,
                               pady = 15,
                               width = 20,
                               variable = self.var1,
                               indicator = 0,
                               background = "#ffd64f")
        self.rb4.grid(row = 5) #placement


        #creating space between continue button and choices
        self.empty_space = Label(self.quiz_frame,
                                    text = " ",
                                    font = ("Comic Sans MS", "15"),
                                    bg = background_color)
        self.empty_space.grid(row = 6)
        
        #confirm button to move on to the next question
        self.confirm_button = Button(self.quiz_frame,
                                    text = "Confirm",
                                    bg = "SpringGreen2",
                                    font = ("Comic Sans MS", "12"),
                                    width = 16,
                                    pady = 10,
                                    padx = 5,
                                    command = self.test_progress)
        self.confirm_button.grid(row = 7) #placement of continue button

        # Creating a score label for the user to know how well they have done so far. This is essentially how many questions they have got correct
        self.score_label = Label(self.quiz_frame,
                                    text = " ", #making it invisible for the time being so that I can config it later on
                                    font = ("Comic Sans MS", "15"),
                                    bg = background_color)
        self.score_label.grid(row = 8)

        
        # questions correct = qc
        self.questions_correct_label = Label(self.quiz_frame,
                                    text = " ", #making it invisible for the time being so that I can config it later on
                                    font = ("Comic Sans MS", "15"),
                                    bg = background_color)
        self.questions_correct_label.grid(row = 9, pady = 10)        
        
        
        self.exit_button = Button(self.quiz_frame, text = "Exit", width = 10, bg = "Red", font = ("Comic Sans MS", 12), command = self.close_end)
        self.exit_button.grid(row = 10, pady = 10)
        #the exit button to close the quiz



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
        qc_label = self.questions_correct_label
        choice = self.var1.get() #collects the choice of the user
        # Checking how many items are in the asked list
        if len(asked) > 9: #If this is the last question
            if choice == 0: #boundary testing <- ensuring the user actually selects a choice for the last question
                self.confirm_button.config(text = "Please select a choice!")
                choice = self.var1.get()

            else: #If it is the last question and they HAVE selected a choice.
                if choice == questions_answers[qnum][6]: #If they select the correct choice for last question
                    score += 1 # Adding one point to the score

                    self.finish_quiz_help = Button(self.quiz_frame, 
                                    text = "Continue",
                                    font = ("Comic Sans MS", 13), 
                                    bg = "SpringGreen2", 
                                    command = self.end_screen) #will move on to the end-screen
                    self.finish_quiz_help.grid(row = 10, padx = 5, pady = 5)
                
                    #destroying all the buttons and labels bcz the end is near
                    self.confirm_button.destroy()
                    self.rb1.destroy()
                    self.rb2.destroy()
                    self.rb3.destroy()
                    self.rb4.destroy()
                    self.exit_button.destroy()

                    self.question_label.configure(text = "You finished my quiz!")
                    scr_label.configure(text = "Correct!")
                    qc_label.configure(text = "Number of questions right: " + str(score))
                
                
                

                
                else: #If they select the incorrect choice for last question
                    score += 0
                
                    self.finish_quiz_help = Button(self.quiz_frame, 
                                    text = "Continue",
                                    font = ("Comic Sans MS", 13), 
                                    bg = "SpringGreen2", 
                                    command = self.end_screen)
                    self.finish_quiz_help.grid(row = 10, padx = 5, pady = 5)


                    self.question_label.configure(text = "You finished my quiz!")
                    scr_label.configure(text = "The answer was '" + questions_answers[qnum][5] + "'.")
                    qc_label.configure(text = "Number of questions right: " + str(score))

                    #destroying all the buttons and labels bcz the end is near
                    self.confirm_button.destroy()
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

                    scr_label.configure(text = "Correct!")
                    qc_label.configure(text = "Number of questions right: " + str(score))
                    
                    self.confirm_button.config(text = "Confirm")
                    self.questions_setup() #Will move to the next question
                
                else: #If the choice is incorrect 
                    score += 0
                    scr_label.configure(text = "The answer was '" + questions_answers[qnum][5] + "'.")
                    qc_label.configure(text = "Number of questions right: " + str(score))
                    self.confirm_button.config(text = "Confirm")
                    self.questions_setup() #Will move to the next question

        #running the end component
    def end_screen(self):
        self.quiz_frame.destroy()
        End(root)

        #exit
    def close_end(self):
        self.quiz_frame.destroy()
        root.destroy()
    

#creating the end class or the end window
class End:
    def __init__(self, parent):
            background_color = "#DA6FE4" #background colour

            self.end_frame = Frame(parent, bg = background_color, padx = 100, pady = 100) #the frame
            self.end_frame.grid()

            self.end_heading = Label(self.end_frame, text = "   Thanks for playing!   ", font = ("Comic Sans MS", 22), bg = background_color, pady = 15)
            self.end_heading.grid(row = 0) #heading, thanks for playing

            if score < 5: #if they answer LESS than 5 questions correctly, this will move them to easier content
                self.helper_button = Button(self.end_frame, text = "Resources", width = 13, bg = "#ffd64f", font = ("Comic Sans MS", 13), command = self.help_continue_less_than_5)
                self.helper_button.grid(row = 4, pady = 20)
            

            else: #if they answer MORE than 5 or equal to 5 questions correctly, this will move them to easier content
                self.helper_button_smart = Button(self.end_frame, text = "Resources", width = 13, bg = "Cyan", font = ("Comic Sans MS", 13), command = self.help_continue_more_than_5)
                self.helper_button_smart.grid(row = 5, pady = 20)

            #exit button
            self.exit_button = Button(self.end_frame, text = "Exit", width = 10, bg = "Red", font = ("Comic Sans MS", 13), command = self.close_end)
            self.exit_button.grid(row = 7, pady = 20)

            
    #exit
    def close_end(self):
        self.end_frame.destroy()
        root.destroy()

    #links to the helper class, which suggests easier content
    def help_continue_less_than_5(self):
        self.end_frame.destroy()  #this will destroy the window
        Helper(root)

    #links to the helpersmart class, which suggests harder content
    def help_continue_more_than_5(self):
        self.end_frame.destroy()  #this will destroy the window
        HelperSmart(root)


#the helper class - easier content or easier links
class Helper:
    def __init__(self, parent):

        background_color = "#DA6FE4" #background colour

        self.help_frame = Frame(parent, bg = background_color, padx = 100, pady = 50)
        self.help_frame.grid() #the frame

        self.help_heading = Label(self.help_frame, text = "  Below are resources to aid in your math!  ", font = ("Comic Sans MS", 22), bg = background_color, pady = 15)
        self.help_heading.grid(row = 0) #A label

        self.help_heading_2 = Label(self.help_frame, text = "Your final percentage was " + str((score/10)*100) + "%. With this in mind, you might want to look at these websites.", font = ("Comic Sans MS", 16), bg = background_color, pady = 15)
        self.help_heading_2.grid(row = 1) #converting the score into a percentage -> (score divided by ten) multiplied by 100, will convert into percentage.

        self.help_heading_3 = Label(self.help_frame, text = "Come on! You can do better '" + str(names_list[0]) +  "'. I'm recommending slightly easier content.", font = ("Comic Sans MS", 16), bg = background_color, pady = 15)
        self.help_heading_3.grid(row = 2) #the str(names_list[0]) will give the first item in the names_list which will be the user's name

        self.link_button_1 = Button(self.help_frame, text = "Resource 1", width = 15, bg = "#ffd64f", font = ("Comic Sans MS", 13), command = self.ixl) #links
        self.link_button_1.grid(row = 4, pady = 20)

        self.link_button_2 = Button(self.help_frame, text = "Resource 2", width = 15, bg = "#ffd64f", font = ("Comic Sans MS", 13), command = self.khan) #links
        self.link_button_2.grid(row = 5, pady = 20)

        self.link_button_3 = Button(self.help_frame, text = "Resource 3", width = 15, bg = "#ffd64f", font = ("Comic Sans MS", 13), command = self.math) #links
        self.link_button_3.grid(row = 6, pady = 20)

        self.exit_button = Button(self.help_frame, text = "Exit", width = 10, bg = "Red", font = ("Comic Sans MS", 13), command = self.close_end) #exit
        self.exit_button.grid(row = 7, pady = 20)

    def ixl(self):
        
        webbrowser.open("https://nz.ixl.com/maths/year-12") #this will launch them to that website
        root.destroy()

    def khan(self):
        
        webbrowser.open("https://www.khanacademy.org/math/algebra2") #this will launch them to that website
        root.destroy()

    def math(self):
        
        webbrowser.open("http://www.math.com/homeworkhelp/Algebra.html") #this will launch them to that website
        root.destroy()

    def close_end(self):
        self.help_frame.destroy() #exit
        root.destroy()



class HelperSmart:
    def __init__(self, parent):

        background_color = "#DA6FE4" #background colour

        self.help_frame = Frame(parent, bg = background_color, padx = 100, pady = 50) #the frame
        self.help_frame.grid()

        self.help_heading = Label(self.help_frame, text = "  Below are resources to aid in your math!  ", font = ("Comic Sans MS", 22), bg = background_color, pady = 15)
        self.help_heading.grid(row = 0) #the heading label

        self.help_heading_2 = Label(self.help_frame, text = "Your final percentage was " + str((score/10)*100) + "%. With this in mind, you might want to look at these websites.", font = ("Comic Sans MS", 16), bg = background_color, pady = 15)
        self.help_heading_2.grid(row = 1) #converting the score into a percentage -> (score divided by ten) multiplied by 100, will convert into percentage.

        self.help_heading_3 = Label(self.help_frame, text = "You are well adept at math '" + str(names_list[0]) + "'. I'm recommending more advanced content.", font = ("Comic Sans MS", 16), bg = background_color, pady = 15)
        self.help_heading_3.grid(row = 2) #the str(names_list[0]) will give the first item in the names_list which will be the user's name

        self.link_button_1 = Button(self.help_frame, text = "Resource 1", width = 15, bg = "#ffd64f", font = ("Comic Sans MS", 13), command=self.ixl) #links
        self.link_button_1.grid(row = 4, pady = 20)

        self.link_button_2 = Button(self.help_frame, text = "Resource 2", width = 15, bg = "#ffd64f", font = ("Comic Sans MS", 13), command=self.khan) #links
        self.link_button_2.grid(row = 5, pady = 20)

        self.link_button_3 = Button(self.help_frame, text = "Resource 3", width = 15, bg = "#ffd64f", font = ("Comic Sans MS", 13), command=self.math) #links
        self.link_button_3.grid(row = 6, pady = 20)

        self.exit_button = Button(self.help_frame, text = "Exit", width = 10, bg = "Red", font = ("Comic Sans MS", 13), command = self.close_end) #exit
        self.exit_button.grid(row = 7, pady = 20)

    def ixl(self):
        
        webbrowser.open("https://nz.ixl.com/maths/year-13") #this will launch them to that website
        root.destroy()

    def khan(self):
        
        webbrowser.open("https://www.khanacademy.org/math/precalculus") #this will launch them to that website
        root.destroy()

    def math(self):
        
        webbrowser.open("http://www.math.com/homeworkhelp/Calculus.html") #this will launch them to that website
        root.destroy()

    def close_end(self):
        self.help_frame.destroy() #exit
        root.destroy()
    
#I've linked to actual math websites now.


####### program start ##########

if __name__ == "__main__":
    root = Tk()
    root.title("Math Helper by Tousif") #the title of my program
    Introduction_object = Introduction(root)
    root.mainloop() #This loops the window for to it stay and not disappear.