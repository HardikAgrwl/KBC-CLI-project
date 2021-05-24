from questions import QUESTIONS


def isAnswerCorrect(question, answer):

    '''
    :param question: question (Type JSON)
    :param answer:   user's choice for the answer (Type INT)
    :return:
        True if the answer is correct
        False if the answer is incorrect
    '''

    return True if answer == question["answer"] else False   #remove this


def lifeLine(ques):

    '''
    :param ques: The question for which the lifeline is asked for. (Type JSON)
    :return: delete the key for two incorrect options and return the new ques value. (Type JSON)
    '''

def isValid(ans):
    if(ans == "lifeline" or ans == "quit"):
        return True
    elif(len(ans) == 1 and ans[0] >= '1' and ans[0] <= '4' ):
        return True
    else: 
        return False

def lifeline(question):
    ans_list = []
    i = 1
    j = 1
    while(len(ans_list) < 2 ):
        if(int(question["answer"]) != i and j <= 2):
            j += 1
            i += 1
        else :
            ans_list.append(str(i))
            i += 1
    return ans_list

def kbc():
    '''
        Rules to play KBC:
        * The user will have 15 rounds
        * In each round, user will get a question
        * For each question, there are 4 choices out of which ONLY one is correct.
        * Prompt the user for input of Correct Option number and give feedback about right or wrong.
        * Each correct answer get the user money corresponding to the question and displays the next question.
        * If the user is:
            1. below questions number 5, then the minimum amount rewarded is Rs. 0 (zero)
            2. As he correctly answers question number 5, the minimum reward becomes Rs. 10,000 (First level)
            3. As he correctly answers question number 11, the minimum reward becomes Rs. 3,20,000 (Second Level)
        * If the answer is wrong, then the user will return with the minimum reward.
        * If the user inputs "lifeline" (case insensitive) as input, then hide two incorrect options and
            prompt again for the input of answer.
        * NOTE:
            50-50 lifeline can be used ONLY ONCE.
            There is no option of lifeline for the last question( ques no. 15 ), even if the user has not used it before.
        * If the user inputs "quit" (case insensitive) as input, then user returns with the amount he has won until now,
            instead of the minimum amount.
    '''

    #  Display a welcome message only once to the user at the start of the game.
    #  For each question, display the prize won until now and available life line.
    # For now, the below code works for only one question without LIFE-LINE and QUIT checks

    print("\t Welcome to Kaun Banega Crorepati ")
    print("\n\t Read the rules carefully")
    print("\n\t* You will have 15 rounds")
    print("\n\t* In each round, you will get a question")
    print("\n\t* For each question, there are 4 choices out of which ONLY one is correct.")
    print("\n\t* For answering the question type the number of option")
    print("\n\t* You wil have a lifeline 50-50 which you can use only once")
    print("\n\t* For using the lifeline type 'lifeline'(case sensitive) only")
    print("\n\t* You can't use the lifeline for answering the last question")
    print("\n\t* You can quit anytime, if you face any difficulty")
    print("\n\t* For quitting just type 'quit' only\n")

    qnum = 0
    total_money = 0
    minimum_money = 0
    lifelines = 1
    while qnum<15:
        print(f'\tQuestion {qnum+1}: {QUESTIONS[qnum]["name"]}' )
        print(f'\t\tOptions:')
        print(f'\t\t\tOption 1: {QUESTIONS[qnum]["option1"]}')
        print(f'\t\t\tOption 2: {QUESTIONS[qnum]["option2"]}')
        print(f'\t\t\tOption 3: {QUESTIONS[qnum]["option3"]}')
        print(f'\t\t\tOption 4: {QUESTIONS[qnum]["option4"]}')


        #Input from the User and validate the input
        ans = input('Your choice ( 1-4 ) : ')
        while(isValid(str(ans)) == False):
            print("\n Incorrect Input! Enter again \n")
            ans = input('Your choice ( 1-4 ) : ')

        # If User wants to quit 
        if(ans == "quit"):
            print(f'\n Congratulations!')
            print(f'\n You have Won Rs.{total_money}\n\n')
            break

        # If User has a lifeline and wants to use it

        ## If user uses the lifeline for last question
        if(ans == "lifeline" and qnum == 14):
            print("\n You can't use lifeline in the last question ")
            ans = input(" Enter again")
            while((isValid(str(ans)) == False) or (ans == "lifeline")):
                ans = input('Your Choice : ')

        ## User uses the lifeline for other questions
        if(ans == "lifeline" and lifelines != 0):
            left_opt = lifeline(QUESTIONS[qnum])
            print(f'\n Options left : {left_opt}')
            lifelines -= 1
            ans = input('Your Choice : ')
            while(str(ans) not in left_opt):
                ans = input('Wrong Choice! Enter again : ')

        # If User had used the lifeline but still types lifeline  
        elif(ans == "lifeline" and lifelines == 0):
            print("\n You don't have any lifeline left")
            ans = input('Your Choice : ')
            while((isValid(str(ans)) == False) or (ans == "lifeline")):
                ans = input('Your Choice : ')

        # If user has answeres the question then check whether its correct and print it
        if isAnswerCorrect(QUESTIONS[qnum], int(ans) ):
            total_money = QUESTIONS[qnum]["money"]
            if(qnum == 4 or qnum == 9):
                minimum_money = total_money
            print('\nCorrect !')
            print(f'\n You have Won Rs.{total_money}')
            if(qnum == 4):
                print(f'\n You have crossed level 1 . Now you will win atleast {minimum_money} ')
            if(qnum == 9):
                print(f'\n You have crossed level 2 . Now you will win atleast {minimum_money}')
            qnum += 1

        else:
            print('\nIncorrect ! You Lost')
            print(f'\n Correct Answer : {QUESTIONS[qnum]["answer"]}')
            print( f'\n You Won : {minimum_money}' )
            break
    # print the total money won in the end.

    if(qnum == 15):
        print(f'\n You are a Crorepati now\n\n')


kbc()
