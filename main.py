from tkinter import *
import random

names_list = []

global questions_answers

asked = []




questions_answers = {
    1: [
        "Sample question one?", #First item, this is going to be the question, index 0
        "Option 1", #Choice 1, index 1
        "Option 2", #Choice 2, index 2
        "Option 3", #Choice 3, index 3
        "Option 4", #Choice 4, index 4
        "Option 3", #index 5, An item, the correct choice/option <- this will be displayed if incorrect choice is selected
        3], #Last item, "3" <- index position of correct answer


    2: [
        "Sample question two?", #First item, this is going to be the question, index 0
        "Option 1", #Choice 1, index 1
        "Option 2", #Choice 2, index 2
        "Option 3", #Choice 3, index 3
        "Option 4", #Choice 4, index 4
        "Option 3", #index 5, An item, the correct choice/option <- this will be displayed if incorrect choice is selected
        2], #Last item, "3" <- index position of correct answer


    3: [
        "Sample question three?", #First item, this is going to be the question, index 0
        "Option 1", #Choice 1, index 1
        "Option 2", #Choice 2, index 2
        "Option 3", #Choice 3, index 3
        "Option 4", #Choice 4, index 4
        "Option 3", #index 5, An item, the correct choice/option <- this will be displayed if incorrect choice is selected
        1], #Last item, "3" <- index position of correct answer

    4: [
        "Sample question four?", #First item, this is going to be the question, index 0
        "Option 1", #Choice 1, index 1
        "Option 2", #Choice 2, index 2
        "Option 3", #Choice 3, index 3
        "Option 4", #Choice 4, index 4
        "Option 3", #index 5, An item, the correct choice/option <- this will be displayed if incorrect choice is selected
        3], #Last item, "3" <- index position of correct answer

    
    5: [
        "Sample question five?", #First item, this is going to be the question, index 0
        "Option 1", #Choice 1, index 1
        "Option 2", #Choice 2, index 2
        "Option 3", #Choice 3, index 3
        "Option 4", #Choice 4, index 4
        "Option 3", #index 5, An item, the correct choice/option <- this will be displayed if incorrect choice is selected
        3], #Last item, "3" <- index position of correct answer

    6: [
        "Sample question six?", #First item, this is going to be the question, index 0
        "Option 1", #Choice 1, index 1
        "Option 2", #Choice 2, index 2
        "Option 3", #Choice 3, index 3
        "Option 4", #Choice 4, index 4
        "Option 3", #index 5, An item, the correct choice/option <- this will be displayed if incorrect choice is selected
        1], #Last item, "3" <- index position of correct answer

    7: [
        "Sample question seven?", #First item, this is going to be the question, index 0
        "Option 1", #Choice 1, index 1
        "Option 2", #Choice 2, index 2
        "Option 3", #Choice 3, index 3
        "Option 4", #Choice 4, index 4
        "Option 3", #index 5, An item, the correct choice/option <- this will be displayed if incorrect choice is selected
        4], #Last item, "3" <- index position of correct answer

    8: [
        "Sample question eight?", #First item, this is going to be the question, index 0
        "Option 1", #Choice 1, index 1
        "Option 2", #Choice 2, index 2
        "Option 3", #Choice 3, index 3
        "Option 4", #Choice 4, index 4
        "Option 3", #index 5, An item, the correct choice/option <- this will be displayed if incorrect choice is selected
        2], #Last item, "3" <- index position of correct answer

    9: [
        "Sample question nine?", #First item, this is going to be the question, index 0
        "Option 1", #Choice 1, index 1
        "Option 2", #Choice 2, index 2
        "Option 3", #Choice 3, index 3
        "Option 4", #Choice 4, index 4
        "Option 3", #index 5, An item, the correct choice/option <- this will be displayed if incorrect choice is selected
        4], #Last item, "3" <- index position of correct answer

    10: [
        "Sample question ten?", #First item, this is going to be the question, index 0
        "Option 1", #Choice 1, index 1
        "Option 2", #Choice 2, index 2
        "Option 3", #Choice 3, index 3
        "Option 4", #Choice 4, index 4
        "Option 3", #index 5, An item, the correct choice/option <- this will be displayed if incorrect choice is selected
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
                                   bg=background_color)
        self.heading_label.grid(row=0, padx=20)

        #creates a label to ask for the name
        self.user_label = Label(self.quiz_frame,
                                text="Enter your name to begin this journey...",
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

    def name_collection(self):
        name = self.entry_box.get()  #this will collect the name from the entry box
        names_list.append(name)  #adds the user name to names list declared at the beginning
        self.quiz_frame.destroy()  #this will destroy the starter window
        Quiz(root)

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
                                   bg=background_color)
        self.question_label.grid(row=0, padx=20)

        #This holds value of radio buttons
        self.var1 = IntVar()

        #radio button 1, in order to hold first choice
        self.rb1 = Radiobutton(self.quiz_frame,
                               text=questions_answers[qnum][1],
                               font=("Helvetica", "12"),
                               bg=background_color,
                               value=1,
                               padx=10,
                               pady=15,
                               variable=self.var1,
                               indicator=0,
                               background="red")
        self.rb1.grid(row=2) #placement


        #radio button 2, in order to hold first choice
        self.rb2 = Radiobutton(self.quiz_frame,
                               text=questions_answers[qnum][2],
                               font=("Helvetica", "12"),
                               bg=background_color,
                               value=2,
                               padx=10,
                               pady=15,
                               variable=self.var1,
                               indicator=0,
                               background="red")
        self.rb2.grid(row=3) #placement


        #radio button 3, in order to hold first choice
        self.rb3 = Radiobutton(self.quiz_frame,
                               text=questions_answers[qnum][3],
                               font=("Helvetica", "12"),
                               bg=background_color,
                               value=3,
                               padx=10,
                               pady=15,
                               variable=self.var1,
                               indicator=0,
                               background="red")
        self.rb3.grid(row=4) #placement


        #radio button 1, in order to hold first choice
        self.rb4 = Radiobutton(self.quiz_frame,
                               text=questions_answers[qnum][4],
                               font=("Helvetica", "12"),
                               bg=background_color,
                               value=4,
                               padx=10,
                               pady=15,
                               variable=self.var1,
                               indicator=0,
                               background="red")
        self.rb4.grid(row=5) #placement
        

####### program start ##########

if __name__ == "__main__":
    root = Tk()
    root.title("Math Helper :)")
    Introduction_object = Introduction(root)
    root.mainloop() #This loops the window for to it stay and not disappear.