import pickle

def predict_temperature(model_path, features):
    with open(model_path, 'rb') as file:
        model = pickle.load(file)

    predicted_temp = model.predict(features)
    return float(predicted_temp[0])