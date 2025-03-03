# 🚀 AI-Driven UAV Precision Agriculture Using NDVI & Machine Learning 🌿

**🌍 A Smart UAV-Based Solution for Precision Farming Using AI, Computer Vision, and Geospatial Analysis.**

---

## 📜 Project Overview
Agriculture plays a crucial role in global food production and economic stability. However, **traditional crop monitoring methods** are **labor-intensive, time-consuming, and inefficient**, making it challenging for farmers to **detect plant diseases, nutrient deficiencies, and irrigation issues in large farmlands**.  

This project introduces an **AI-powered UAV (drone) system** that **automates the process of monitoring plant health** using **multispectral imaging, NDVI (Normalized Difference Vegetation Index), and AI-based classification**. By integrating **computer vision, machine learning, and geospatial mapping**, this system provides **real-time insights into crop health, enabling precision agriculture at a lower cost**.

---

## 🔍 Why Was This Project Developed?
- 🌾 **Farmers struggle with large-scale crop monitoring**, leading to **late disease detection and yield loss**.  
- 🔍 **Traditional methods rely on manual field inspection**, which is **inefficient, error-prone, and time-consuming**.  
- 📷 **Multispectral imaging technology (NDVI) helps analyze plant health**, but commercial solutions are **expensive**.  
- 🚁 **Drones provide an effective solution**, but high-end multispectral cameras are **not accessible to small-scale farmers**.  
- 💡 **This project offers a cost-effective solution** by modifying a **low-cost consumer camera to function as a multispectral sensor** and **using AI to classify crop stress levels**.  

---

## 🚀 How Does This Project Help Farmers?
✅ **Early Disease Detection** – Detects unhealthy plants **before visual symptoms appear**.  
✅ **Efficient Resource Allocation** – Helps farmers **use water, fertilizers, and pesticides** in the right areas.  
✅ **Cost-Effective Precision Agriculture** – Uses **low-cost UAV and AI-driven classification**.  
✅ **Reduces Crop Loss** – **Timely intervention increases yield & profitability**.  
✅ **Real-Time Insights** – **Automated data processing & cloud-based mapping** help in **farm management**.  

---

## 📌 Key Features
✅ **UAV-Based Crop Health Analysis** – Autonomous drone captures **multispectral images (NIR & Red bands)**.  
✅ **AI-Powered Image Processing** – NDVI computation using **OpenCV & NumPy**.  
✅ **ML-Based Vegetation Classification** – K-Means **Clustering & Random Forest** categorize crops into **Healthy, Stressed, Diseased**.  
✅ **Automated Data Pipeline** – Structured **data ingestion, cleaning, processing, and mapping**.  
✅ **Geospatial Mapping for Decision-Making** – NDVI results are **exported as GIS-compatible shapefiles** for precision farming.  

---

## 🖥️ Tech Stack
- **Python, OpenCV, NumPy, Matplotlib**
- **Scikit-learn (K-Means, Random Forest)**
- **GeoPandas for Geospatial Mapping**
- **UAV Flight Controller: Pixhawk**
- **Mission Planner for Autonomous Flight**
- **Cloud Storage & GIS Tools (AWS S3, QGIS, Google Earth)**  

---

## 📊 Project Methodology
### **Step 1: UAV Development**
- Built a **custom UAV with a Pixhawk flight controller** for **autonomous flight over farmlands**.  
- **Programmed the UAV using Mission Planner**, enabling **automated flight paths** to cover large areas efficiently.  

### **Step 2: Multispectral Camera Modification**
- **Low-cost action camera modified** by **removing the IR-blocking filter** and **adding custom filters** to capture **Near-Infrared (NIR) & Red bands**.  
- Enables **cost-effective NDVI analysis**, making it **accessible for small-scale farmers**.  

### **Step 3: Data Acquisition & Preprocessing**
- UAV **captures images with GPS metadata** (latitude, longitude, altitude) for precise mapping.  
- **Preprocessing includes**:
  - **Noise reduction** using Gaussian Blur.  
  - **Georeferencing** to map images to real-world coordinates.  
  - **Band separation** to extract NIR and Red channels for NDVI computation.  

### **Step 4: NDVI Computation**
- NDVI formula used:
  NDVI = (NIR - Red) / (NIR + Red)

  
- Implemented using **OpenCV & NumPy**, and results are visualized using **NDVI heatmaps**.  

### **Step 5: Vegetation Classification (AI & ML)**
- **K-Means Clustering & Random Forest Classifier** categorize crops into:  
- 🌿 **Healthy Vegetation**  
- 🌾 **Stressed Plants**  
- ❌ **Diseased or Non-Vegetation Areas**  

### **Step 6: Geospatial Mapping**
- Results are **exported as GIS shapefiles** using **GeoPandas** for farm management.  
- Farmers can **visualize results on GIS platforms** like QGIS, Google Earth, or a web-based dashboard.  

---

## 📌 Installation & Setup
Clone the repository and install dependencies:
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/AI-UAV-Precision-Farming.git
cd AI-UAV-Precision-Farming
pip install -r requirements.txt
