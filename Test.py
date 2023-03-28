import pandas as pd
import datetime


def sendEmail(to,sub,msg):
    print(f"Email to {to} Sent with sub{sub} and message{msg}")

if __name__=='__main__':
    df = pd.read_excel("Data.xlsx")
    #print(df)
    Today = datetime.datetime.now().strftime("%d-%m")
    Yearnow = datetime.datetime.now().strftime("%Y")

    #print(Today)
    

Writeind=[]
for index,item in df.iterrows():
    bday = item['Birthday'].strftime("%d-%m")
        #print(bday)
    if (Today==bday) and Yearnow not in str(item['Year']):
        sendEmail(item['Email']," Happy Birth Day ",item['Dialogue'])
        Writeind.append(index)
            

for i in Writeind:
        
    yr = df.loc[i,'Year']
    print(yr)
    df.loc[i,'Year']=str(yr)+','+ str(Yearnow)
    print( df.loc[i,'Year'])
    

    #df.to_excel('Data.xlsx', index=False)

