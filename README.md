# **Sentiment Analysis API - FastAPI**  

This repository contains a **FastAPI application** for sentiment analysis using a **pre-trained LSTM model**. The API takes movie reviews as input and predicts whether the sentiment is **positive** or **negative**.

---

## **Installation**  

1. **Clone the repository**  
   ```bash
   git clone https://github.com/AristideI/alu-sentiment-analysis-lstm.git
   cd alu-sentiment-analysis-lstm
   ```

2. **Create a virtual environment (optional but recommended)**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

---

## **Running the API**  

Start the FastAPI server using **Uvicorn**:  
```bash
uvicorn app:app --reload
```

By default, the API runs on `http://127.0.0.1:8000/`

---

## **API Endpoints**  

### **1. Health Check**  
- **Endpoint:** `/`  
- **Method:** `GET`  
- **Description:** Returns a welcome message confirming the API is running.  

### **2. Sentiment Prediction**  
- **Endpoint:** `/predict`  
- **Method:** `POST`  
- **Input:** JSON payload containing a movie review  
- **Example Request:**
  ```json
  {
      "review": "This movie was fantastic! The acting was great and the story was engaging."
  }
  ```
- **Example Response:**
  ```json
  {
      "sentiment": "positive",
      "confidence": 0.92
  }
  ```

---

## **Testing the API**  

You can test the API using **Postman**, **cURL**, or directly in the browser at:  
📌 `http://127.0.0.1:8000/docs` (Swagger UI)  

To send a request using **cURL**:  
```bash
curl -X 'POST' 'http://127.0.0.1:8000/predict' \
-H 'Content-Type: application/json' \
-d '{"review": "I did not like this movie. It was boring and predictable."}'
```

---

## **Model Details**  
- **Dataset:** IMDB Movie Reviews (50,000 samples)  
- **Model:** LSTM-based Deep Learning model  
- **Preprocessing:** Tokenization, stopword removal, sequence padding  
- **Embeddings:** Pre-trained GloVe embeddings (100D)  

---

## **Contributions & Future Work**  
Feel free to fork this repository and improve the model! Possible enhancements:  
✅ Fine-tune a **Transformer-based model** (e.g., BERT)  
✅ Deploy as a **Dockerized microservice**  
✅ Improve the frontend for interactive testing  

---

## **License**  
This project is open-source under the **MIT License**.  
