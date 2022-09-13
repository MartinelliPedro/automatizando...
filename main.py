import os

def makeCommits (days):
    if days < 1:
        os.system('git push')
    else:
        dates = f"{days} days ago"
        with open('data.txt', 'a') as file:
            file.write(f'{dates} <- this was the commit for the day!!\n')
        
        # staging 
        os.system('git add data.txt')

        # commit 
        os.system('git commit --date="'+ dates +'" -m "First commit for the day!"')

        # days * makeCommits(days - 1)

cont = 0
maxNumero = 1600
while True:
    # makeCommits(1)
    makeCommits(1600 - maxNumero)
    cont += 1
    maxNumero -= 1
    if cont == 1600:
        break