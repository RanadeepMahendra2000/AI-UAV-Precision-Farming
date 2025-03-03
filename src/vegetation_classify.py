import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# ------------------ STEP 4: Vegetation Classification ------------------

def classify_vegetation(ndvi_values):
    """Classify vegetation using K-Means clustering."""
    ndvi_reshaped = ndvi_values.flatten().reshape(-1, 1)
    kmeans = KMeans(n_clusters=3, random_state=42).fit(ndvi_reshaped)
    classified_ndvi = kmeans.labels_.reshape(ndvi_values.shape)
    
    return classified_ndvi

# Load NDVI values from pipeline
ndvi_values = np.load("processed_data/ndvi_values.npy")

# Apply K-Means Classification
classified_ndvi = classify_vegetation(ndvi_values)

# Display results
plt.imshow(classified_ndvi, cmap='viridis')
plt.title("Vegetation Classification Using K-Means")
plt.show()

# ------------------ STEP 5: NDVI Prediction Using Machine Learning ------------------

def train_model(ndvi_values):
    """Train Random Forest model on NDVI classification."""
    X = ndvi_values.flatten().reshape(-1, 1)
    y = np.random.choice([0, 1, 2], size=len(X))  # Simulated Labels (0=Healthy, 1=Stressed, 2=Diseased)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    
    print(f"🌿 Random Forest Model Accuracy: {accuracy:.2f}")
    
    return model

# Train Model
rf_model = train_model(ndvi_values)

# Save Classified NDVI Image
plt.imsave("processed_data/classified_ndvi.png", classified_ndvi, cmap="viridis")

print("✅ Vegetation Classification & Prediction Completed Successfully!")
