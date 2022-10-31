
import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'radius_mean':17.99, 'texture_mean':10.38, 'perimeter_mean':122.8, 'area_mean':1001, 'smoothness_mean':0.1184, 'compactness_mean':0.2776, 'concavity_mean':0.3001, 'concave points_mean':0.1471, 'symmetry_mean':0.2419, 'fractal_dimension_mean':0.07871})
print(r.json())
