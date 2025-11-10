# Rice Classification on Rice Dataset

**Project Duration:** 19/09/2024 – 28/11/2024  
**Team Members:** 2  

---

## 📖 Description
This project is a **machine learning application** designed to classify rice grains based on their physical characteristics. The system allows users to input specific measurements of each rice grain, including:

- **Perimeter**  
- **Major Axis Length**  
- **Minor Axis Length**  
- **Eccentricity**  
- **Convex Area**  
- **Extent**  

Based on these features, the system applies one of several machine learning algorithms chosen by the user to predict the **type or quality of the rice grain**. Supported algorithms include:

- Decision Tree  
- Logistic Regression  
- Bagging Classifier  
- Random Forest  
- Naive Bayes  

The application provides prediction results along with probability scores for each class. It is designed to save time and effort for rice inspection and classification and can be applied in production facilities, sorting centers, or quality control labs.

---

## 🛠 Technologies Used
- **Python** – for data processing, model training, and predictions  
- **Flask** – for web integration and user interface  

---

## ⚡ Features
- Manual input of rice grain features  
- Selection of different machine learning algorithms for predictions  
- Display of predicted class along with probability scores  
- Comparison of results from multiple models  

---

## 📌 How to Run
1. Clone the repository:  
   ```bash
   git clone https://github.com/CaoHoangKhai/Rice_Classification.git
   ```

2. Navigate to the project folder:
   ```bash
   cd Rice_Classification
   ```
3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Flask application:

   ``` bash
   python app.py
   ```
5. Open your browser and go to:
   ``` cpp
   http://127.0.0.1:5000/
   ```
---

## ⚠️ Limitations
- Currently, the system **does not support batch input from Excel or CSV files**. Users must enter rice grain measurements manually for each sample.


