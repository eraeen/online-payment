import streamlit as s
import pandas as pd
import pickle as p
import sys

s.title('fraud detection')

step = s.number_input('enter step')
type = s.text_input('enter type')
amount = s.number_input('enter amount')
oldbalanceOrg = s.number_input('enter old balance org')
newbalanceOrig = s.number_input('enter new balance org')
oldbalanceDest = s.number_input('enter old balance dest')
newbalanceDest = s.number_input('enter new balance dest  ')

uploaded_file = s.file_uploader("OR, upload file", type = ['csv'])
in_pickle = open("fraud.pkl", 'rb')
pipe = p.load(in_pickle)


if s.button('predict'):
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        s.dataframe(df)
        modelpred = pipe.predict(df)
    
    else:       
        result = pd.DataFrame(
            [[step,type,amount,oldbalanceOrg,newbalanceOrig,oldbalanceDest,newbalanceDest]],
                              columns = ['step','type','amount','oldbalanceOrg','newbalanceOrig','oldbalanceDest','newbalanceDest'])
        r = pipe.predict(result)
            
        if r == 1:
            s.success('fraud Transaction')
        else:
            s.success('fraud not detected')
                                                                                               

    
    
    


        



        


    
    
        






#with open('pipe.pkl', 'rb') as file:
 #   final = pickle.load(file)