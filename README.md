# 🔐 AI-Based Network Intrusion Detection System (NIDS)

An Artificial Intelligence–driven Network Intrusion Detection System that applies Machine Learning techniques to identify malicious network traffic. This project is primarily developed for academic and learning purposes and demonstrates how intelligent models can improve cybersecurity by detecting abnormal network behavior in near real time.

---

## ❗ Problem Statement

The continuous growth of computer networks and online services has significantly increased the frequency of cyber threats such as Denial of Service (DoS) attacks, unauthorized access, malware infections, and data breaches. Conventional security solutions, including firewalls and signature-based intrusion detection systems, often fail to detect newly emerging or unknown attack patterns.

To overcome these limitations, this project proposes an AI-based Network Intrusion Detection System that leverages Machine Learning algorithms to automatically analyze network traffic and identify potential intrusions with improved accuracy and efficiency.

---

## 📖 Project Overview

The AI-Based NIDS is a machine learning–enabled cybersecurity system designed to monitor network traffic and distinguish between normal and malicious activities. The system utilizes a Random Forest classifier, which is well known for its robustness and reliability in classification tasks.

A web-based interactive dashboard is developed using Streamlit, enabling users to train the model, simulate network traffic, and view intrusion detection results in real time. By default, the system runs in simulation mode, allowing easy demonstration without the need for external datasets. However, the project can be extended to support real-world datasets such as CIC-IDS2017 for advanced experimentation.

This project highlights the role of Artificial Intelligence in modern cybersecurity and emphasizes the importance of automated intrusion detection systems in protecting network infrastructures.

---

## 👥 End Users

- Network Administrators  
- Cybersecurity Analysts  
- IT Security Teams  
- Organizations managing enterprise networks  
- Educational Institutions  
- Students and researchers in cybersecurity  
- Security professionals and analysts  

---

## 🧠 Technologies Used

- **Programming Language:** Python  
- **Machine Learning Algorithm:** Random Forest Classifier  
- **Data Processing Libraries:** Pandas, NumPy  
- **Web Framework:** Streamlit  
- **Visualization Tools:** Matplotlib, Seaborn  
- **Development Environment:** Visual Studio Code  
- **Dataset (Optional):** CIC-IDS2017  

---

## ⚙️ System Workflow

1. Network traffic data is collected (simulated or real).  
2. The data is cleaned, processed, and prepared for training.  
3. A Random Forest model is trained using the prepared dataset.  
4. Users provide live or simulated traffic parameters.  
5. The trained model predicts whether the traffic is normal or malicious.  
6. Detection results are displayed through an interactive dashboard.  

---

## 🧪 Data Operating Modes

### ✅ Simulation Mode (Default)
- Uses synthetically generated network traffic data  
- No external dataset is required  
- Ideal for demonstrations, academic evaluations, and project submissions  

### 🔁 Real Dataset Mode (Optional)
- Dataset: CIC-IDS2017  
- Can be enabled by modifying the data loading module  
- Suitable for research-oriented and advanced testing  
---

## ▶️ How to Execute the Project

```bash
pip install -r requirements.txt
streamlit run nids_main.py
```
Once executed, the application will be accessible at:
```bash
http://localhost:8501
```
---
## 📸 Screenshots
<img width="1911" height="1013" alt="Screenshot 2026-01-03 203242" src="https://github.com/user-attachments/assets/f778335c-7c57-455d-9380-34931c91cfb0" />


<img width="1919" height="1021" alt="Screenshot 2026-01-03 203336" src="https://github.com/user-attachments/assets/d46d0300-1850-460d-9d6e-ec2c4b494633" />

---

## 🚀 Applications

- Academic project presentation  
- Cybersecurity education and training  
- Network traffic monitoring  
- Intrusion detection simulation  
- Evaluation of machine learning models  

---

## 🌟 Key Advantages

- Automatic detection of intrusions  
- Capable of identifying unknown and suspicious attacks  
- Real-time interactive visualization  
- Scalable and customizable architecture  
- Simple deployment and user-friendly interface  

---

## 🔮 Future Enhancements

- Integration with real-time packet capturing tools  
- Implementation of deep learning models (CNN, LSTM)  
- Support for multi-class attack classification  
- Cloud-based deployment  
- Alert and notification mechanisms  

---

## 📚 References

- Python Documentation: https://docs.python.org/3/
- Streamlit Documentation: https://docs.streamlit.io/
- Scikit-learn Documentation: https://scikit-learn.org/
- CIC-IDS2017 Dataset: https://www.unb.ca/cic/datasets/ids-2017.html 

