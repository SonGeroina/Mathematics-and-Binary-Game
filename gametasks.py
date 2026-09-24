def printInstructions(instruction):
    print('Instruction ', instruction)

def getUserScore(userName):
    try:
        input = open('userScore.txt', 'r')
        for line in input:
            content = line.split(', ')
            if content[0] == userName:
                input.close()
                return content[ 1]
        input.close()
        return '-1'
    except IOError:
        print("File not found. A new file will be created.")
        input = open('userScore.txt', 'w')
        input.close()
        return '-1'

def updateUserScore(newUser, userName, score):
    from os import remove, rename

    if newUser:
        with open('userScore.txt', 'a') as f:
            f.write(userName + ', ' + score + '\n')
    else:
        temp = open('userScore.tmp', 'w')
        input = open('userScore.txt', 'r')

        for line in input:
            content = line.strip().split(', ')
            if content[0] == userName:
                temp.write(userName + ', ' + score + '\n')
            else:
                temp.write(line)

        input.close()
        temp.close()

        remove('userScore.txt')
        rename('userScore.tmp', 'userScore.txt')    
            
