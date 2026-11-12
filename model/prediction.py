import pickle

with open('V:/Education/Fastapi/project/model/model.pkl','rb') as f:
    model = pickle.load(f)

def prediction(user_data:dict):
    prediction = model.predict(user_data)[0]
    return prediction