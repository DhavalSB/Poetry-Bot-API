import os
import random
import json


filePaths = ["prompts1.json", "prompts2.json", "prompts3.json"]

def selectPrompt():

    fileChoice = random.choice(filePaths)

    with open(fileChoice, 'r', encoding='utf-8') as file:
        prompts = json.load(file)

    randomIndex = random.randint(0, len(prompts) - 1)
    randomPrompt = prompts[randomIndex]

    return randomPrompt

print(selectPrompt())
