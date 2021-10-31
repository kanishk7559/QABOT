import discord
import re
import random
import torch
from transformers import BertForQuestionAnswering
from transformers import BertTokenizer
from nltk.corpus import stopwords

TOKEN = "<YOUR BOT TOKEN>"

model = BertForQuestionAnswering.from_pretrained(r'bertquestionanswering')
tokenizer = BertTokenizer.from_pretrained(r'bertquestionanswering')


s_list = [
    "I can't understand ..Is it not working between us... and just so you know ..it's not you.. Its me",
    "How about we talk something else, Okay I'll be honest, I didn't get you :P",
    "I'm not sure what you mean. Please ask me something else.",
    "This is getting complicated... Lets find something else to begin with",
    "Is it hangover or what...I am crashed... Lets try this with another conversation",
    "Sorry, I didn;t get you.I am bad at  catching people..Another disadvantage of being introvert :/",
    "Lets give this another try!",
    "Are you Christopher Nolan ?..Its hard to understand you!"
]

def para2sentence_needed(para, keyword):
    sentenceEnders = re.compile('[.!?]')
    sentenceList = sentenceEnders.split(para)
    for sentence in sentenceList:
        if keyword in sentence:
            return sentence
    return(random.choice(s_list))

def predict_class(answer_text, question):
    answer_text = answer_text.lower()
    # tokenize
    encoded_dict = tokenizer.encode_plus(
        text=question, text_pair=answer_text, add_special=True)
    # Apply the tokenizer to the input text, treating them as a text-pair.
    input_ids = encoded_dict['input_ids']
    # Report how long the input sequence is.
    print('Query has {:,} tokens.\n'.format(len(input_ids)))
    # Segment Ids
    segment_ids = encoded_dict['token_type_ids']
    # evaluate
    output = model(torch.tensor([input_ids]),
                   token_type_ids=torch.tensor([segment_ids]))
    # Find the tokens with the highest `start` and `end` scores.
    answer_start = torch.argmax(output['start_logits'])
    answer_end = torch.argmax(output['end_logits'])
    # Get the string versions of the input tokens.
    tokens = tokenizer.convert_ids_to_tokens(input_ids)
    # Start with the first token.
    answer = tokens[answer_start]
    # Select the remaining answer tokens and join them with whitespace.
    for i in range(answer_start + 1, answer_end + 1):
        # If it's a subword token, then recombine it with the previous token.
        if tokens[i][0:2] == '##':
            answer += tokens[i][2:]
        # Otherwise, add a space then the token.
        else:
            answer += ' ' + tokens[i]
    stop_words = set(stopwords.words('english'))
    if answer in stop_words:
        answer = "$$somerandomanswer$$"
    return(para2sentence_needed(answer_text, answer))


unlocked = False
channelsAllowed = set()
client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    channel = message.channel.id
    flag = 0
    global unlocked
    global answer_text
    if message.author == client.user:
        return
    if message.content == 'start':
        print(f"{channel} is now unlocked")
        channelsAllowed.add(channel)
        unlocked = True
        flag = 1
        await message.reply("```Hi , I am QABOT.\nTo use me , you need to follow given syntax.\nContext ='c=<context>'\nQuestion='q=<question>' ```")
    if message.content == 'stop':
        unlocked = False
        channelsAllowed.remove(channel)
        await message.reply("Command is now locked")
    channel = message.channel.id
    if message.author == client.user:
        return
    if flag == 0:
        if (unlocked and message.content.startswith("c=")):
            answer_text = message.content[2:]
            print(answer_text)
            await message.reply("```I am very smart, so dont worry I will try to remember this ! :)```")
        if (unlocked and message.content.startswith("q=")):
            question = message.content[2:]
            print(question)
            reply = predict_class(answer_text, question)
            print(reply)
            await message.reply(f"```{reply}```")


client.run(TOKEN)