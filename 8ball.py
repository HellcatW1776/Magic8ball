import random
name = "Kav"

question = input('Ask me a question: ')

answer = ['It is decidedly so.', 'Without a doubt.', 'Reply hazy, try again.', 'Ask again later.', 'Better not tell you now.', 'My sources say no.', 'Outlook not so good.', 'Very doubtful.']
x = list(range(len(answer)))
print(x)
random_number = random.randint(0, 7)
print(random_number)
def magic(random_number, x):
  if random_number in x:
    return answer[random_number]
print(magic(random_number, x))
