from fastapi import FastAPI
from pydantic import BaseModel
from keras_preprocessing.sequence import pad_sequences
from keras.models import load_model
import pickle
from training.b2_preprocessing_function import CustomPreprocess

# Initialize FastAPI app
app = FastAPI()

# Load model and tokenizer
model_path = "models/model.h5"
tokenizer_path = "tokeniser/tokenizer.pkl"

sentiment_model = load_model(model_path)

with open(tokenizer_path, "rb") as f:
    loaded_tokenizer = pickle.load(f)

# Load Preprocess function
custom = CustomPreprocess()


# Define request body
class TextInput(BaseModel):
    text: str


@app.post("/predict")
def predict_sentiment(input_data: TextInput):
    # Preprocess input text
    processed_text = custom.preprocess_text(input_data.text)

    # Convert text to numeric form
    text_sequence = loaded_tokenizer.texts_to_sequences([processed_text])

    # Padding to match input length
    text_padded = pad_sequences(text_sequence, padding="post", maxlen=100)

    # Predict sentiment
    prediction = sentiment_model.predict(text_padded)[0][0]

    sentiment = "Positive" if prediction > 0.5 else "Negative"

    return {"sentiment": sentiment, "confidence": float(prediction)}


# Run using: uvicorn app:app --reload
