#creating class of players human and compiuter
# Parent class WOFplayers
import random


class WOFPlayer:
    def __init__(self, name, money=0):
        self.name = name
        self.prizeMoney: int = money
        self.prizes = []

    # Add amt to self.prizeMoney
    def addMoney(self, amt: int):
        self.prizeMoney = self.prizeMoney + amt

    # Set self.prizeMoney to 0
    def goBankrupt(self):
        self.prizeMoney = int(0)

    # Append prize to self.prizes
    def addPrize(self, prize):
        self.prizes.append(prize)
    def __str__(self):

        return "{} (${})".format(self.name,self.prizeMoney)

# creating Human player class
class WOFHumanPlayer(WOFPlayer):

    def getMove(self,category, obscuredPhrase, guessed):
        print("{} has ${}  Category: {} ".format(self.name, self.prizeMoney,category ))
        print( "Phrase: {}  Guessed: {}".format(obscuredPhrase, guessed))
        input_string = input("Guess a letter, phraase, or type 'exit' or 'pass':")
        return input_string


#class of compiuter player
class WOFComputerPlayer(WOFPlayer):
    SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'


    def __init__(self, name, difficulty, money=0, prize=[]):
        WOFPlayer.__init__(self, name, money)
        self.difficulty = difficulty
        self.letters_list ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        #self.SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'

    # This method will help us decide semi-randomly whether to make a “good” or “bad” move
    # True is goog, False is Bad
    def smartCoinFlip(self):
        rand_number = random.randint(1, 10)
        if rand_number > self.difficulty:
            return True
        else:
            return False
    # Method should return list of letters that can be guessed.
    def getPossibleLetters(self, guessed):

        VOWEL_COST = 250
        VOWELS =''
        p_letters = []
        for le in self.SORTED_FREQUENCIES:
            if le not in guessed.upper():
                if self.prizeMoney >= VOWEL_COST:
                    p_letters.append(le)
                elif le not in VOWELS:
                    p_letters.append(le)

        return p_letters
    #  Method should return valid moe
    def getMove( self, category, obscuredPhrase, guessed):


        possble_list= self.getPossibleLetters(guessed)
        if possble_list != []:
            if self.smartCoinFlip() == 'True':
                #possible_letter_list =  [letter for letter in self.SORTED_FREQUENCIES if letter not in guessed]
                quest_lettter = possble_list[len(possble_list)-1]
            else:
                quest_lettter =random.choice(possble_list)

            return quest_lettter

        else:
            return 'pass'


