import random
from random import choice

class responder():
    def __init__(self):
        self.__prefix = "Oh brother my brother"
    
    def respond(self, input, desync_percent, altered_percent):
        desyncThreshold = desync_percent

        desyncCheck = random.randint(0,100)

        if desyncCheck >= desyncThreshold:
            #input = self.InsertPrefix(40, input)
            return input
        else:
            #input = self.InsertPrefix(40, input)
            desyncText = []
            markText = []
            spaceIndex = []
            for i in range(0, len(input)):
                if input[i] == " ":
                    spaceIndex.append(i)
                else:
                    desyncText.append(input[i])

            alterRange = len(desyncText) * (altered_percent/100)
            markText = self.alterText(int(alterRange))
            scrambledText = self.scrambleText(alterRange, desyncText, markText, spaceIndex)
            
            return scrambledText

    def InsertPrefix(self, threshold, text):
        prefixCheck = random.randint(0,100)
        if prefixCheck <= threshold:
                text = text.lower()
                response = f'{self.__prefix}, {text}'
                return response
        else:
            return text
    
    def alterText(self, inputRange):
        list = []
        for i in range(0, int(inputRange)):
            markRange = random.randint(33,64)
            marks = markRange
            list.append(marks)

        return list

    def scrambleText(self, alterRange, desyncText, markText, spaceIndex):
        output = 'DESYNC ERROR:\n'
        inputIndex = [] 

        #GET INDICES
        for i in range(0,len(desyncText)):
            inputIndex.append(i)

        #SHUFFLE INDICES
        random.shuffle(inputIndex)

        #GET SHUFFLED INDICES UP TO % SCRAMBLED
        for i in range(0, int(alterRange)):
            index = inputIndex[i]
            desyncText[index] = chr(markText[i])

        #PUT SPACES BACK IN
        for i in range(0, len(spaceIndex)):
            index = spaceIndex[i]
            desyncText.insert(index, " ")
        
        #ADD TO STRING
        for i in range(0,len(desyncText)):
            output += desyncText[i]
        return output

