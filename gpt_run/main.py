import openai
import pandas as pd

df = pd.read_excel('/content/data.xlsx')

def generate_train(sent):
    prompt = 'Translate this into Bengali:\n'
#     print(sent)
    for ban,ben in zip(sent['Banglish'], sent['Bangla']):
        ban = str(ban)
        ben = str(ben)
        ban = ban.replace('\n','')
        ben = ben.replace('\n','')
        prompt += 'English: {} => Bengali: {}\n'.format(ban, ben)
    return prompt

train_prompt_1 = generate_train(df[df['1-Shot']=='Train'])
train_prompt_10 = generate_train(df[df['10-Shot']=='Train'])
train_prompt_25 =  generate_train(df[df['25-Shot']=='Train'])


def create_prompt(context, sent):
    context += 'English: {} => Bengali:'.format(str(sent))
    return context
    

def call_api(prompt):
    openai.api_key = 'beta.openai_api_key'
    response = openai.Completion.create(
      model="text-davinci-002",
      prompt=prompt,
      max_tokens=150,
      top_p=0.5,
      frequency_penalty=0.0,
      presence_penalty=0.0
    )
    return str(response["choices"][0].text)



output=[]
def generate_sentence(current_set):
#     output = []
    for idx, val in enumerate(df.Banglish[388:]):
        prompt = create_prompt(current_set, val)
        output.append(call_api(prompt))
        if idx>0 and idx %25==0:
            print('Complete '+str(idx))
    return output

output_25 = generate_sentence(train_prompt_25)

print(output.__len__())


df2 = pd.DataFrame (output, columns = ['25shot2'])
print (df2)


index=df2["25shot2"].str.find('E')
p=index
for i in range(0,len(df2['25shot2'])):
    x=df2.loc[i]['25shot2']
    x=x[:index[i]]
    p[i]=x

df3 = pd.DataFrame (p, columns = ['25shot2'])
print(df3)


index=df3["25shot2"].str.find('\\')
p=index
for i in range(0,len(df3['25shot2'])):
    x=df3.loc[i]['25shot2']
    x=x[:index[i]]
    p[i]=x

df4 = pd.DataFrame (p, columns = ['25shot2'])
print(df4)


df4.to_csv('shot25(388-500).csv',index=False)
