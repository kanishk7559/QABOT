
<br />
<p align="center">
  <a href="https://github.com/kanishk7559/QABOT">
    <img src="https://i.ibb.co/MBLCHKQ/ss1.jpg" alt="Logo" width="800" height="350">
  </a>

  <p align="center">
    <h2 align="center">Question answering model based on a pre-trained BERT model<br />
    fine-tuned on Stanford Question Answering Dataset (SQuAD) 2.0 </h3>
    <br />
  </p>
</p>
<br />
<h3>Here I built a BERT-based discord bot which returns an answer, given a user question and a passage, which includes the answer of the question.
<br>

## What is SQuAD?
Stanford Question Answering Dataset (SQuAD) is a reading comprehension dataset, consisting of questions posed by crowdworkers on a set of Wikipedia articles, where the answer to every question is a segment of text, or span, from the corresponding reading passage, or the question might be unanswerable.

<b>SQuAD 2.0</b> combines the 100,000 questions in SQuAD 1.1 with over 50,000 unanswerable questions written adversarially by crowdworkers to look similar to answerable ones. To do well on SQuAD 2.0, systems must not only answer questions when possible, but also determine when no answer is supported by the paragraph and abstain from answering. For more information regarding the SQuAD dataset and the current leaderboard, you can visit the following [_link_](https://rajpurkar.github.io/SQuAD-explorer/).
<br />

## Pretrained Model :
You can download the pretrained bert model by <a href="https://drive.google.com/file/d/1RwinDgJZllyo3dy5tHHFHSM8x1_9Ys_F/view?usp=sharing">clicking here</a> then save it to the "/bertquestionanswering" folder.

## How to use the bot? 
1. To use the bot, you need to have a discord bot account. You can follow any youtube video to create account.
2. After that clone this repository and install all required dependencies.
3. Move pretrained bert model to the "/bertquestionanswering" folder.
4. Replace the token (line no. 9 in bot .py ) with your bot token.
5. Run the bot by typing "python3 bot .py" in the terminal.



## Output Screenshot :
<img src="https://i.ibb.co/y6gYpwq/ss.png" alt="Logo" >

<br>

## Invite link
<a href="https://discord.com/api/oauth2/authorize?client_id=903339124491182080&permissions=0&scope=bot">
Click here to invite QABOT to your discord server
</a>



