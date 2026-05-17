# Analysis and Prediction of Common Health Issues Using Machine Learning

> 🎓 **Academic Context:** This project was completed in **April 2023** as a **Bachelor of Engineering (B.E.) Final Year Project** at **Prof. Ram Meghe Institute of Technology & Research (PRMIT&R)**, Department of Computer Science & Engineering.

> 👤 **My Contribution:** This was a team project. My personal contribution was focused entirely on the **Lung Cancer prediction module** — specifically the CNN architecture design, DICOM-to-PNG preprocessing, model training using Keras/TensorFlow, and the lung app interface.
---

## Project Description

This project uses machine learning techniques to predict and analyze common health issues such as heart attack, diabetes, and lung cancer. The team analyzed respective datasets and trained machine learning models to provide accurate predictions. The goal is to assist medical practitioners and diagnostic centers in accurate disease prediction. Users can input attribute values for heart and diabetes disease predictions, and upload lung images in JPEG or PNG format for lung cancer prediction.
  
## Data Collection / Datasets

| Disease | Dataset | Format | Link |
|---|---|---|---|
| Heart Disease | UCI Heart Disease | CSV | [link](https://archive-beta.ics.uci.edu/dataset/45/heart+disease) |
| Diabetes | PIMA Indians Diabetes | CSV | [link](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database) |
| Lung Cancer | LIDC-IDRI (TCIA) | DICOM | [link](https://doi.org/10.7937/K9/TCIA.2015.LO9QL9SX) |

> **NOTE:** The Lung Cancer dataset is in DICOM format. Convert to PNG before use:

```python
import os
import pydicom
from PIL import Image

input_folder = "/path/to/dicom/images/"
output_folder = "/path/to/output/images/"

for filename in os.listdir(input_folder):
    ds = pydicom.dcmread(os.path.join(input_folder, filename))
    image = Image.fromarray(ds.pixel_array)
    image.save(os.path.join(output_folder, f"{filename[:-4]}.jpg"))
```

## Dependencies

**Python 3:** https://www.python.org/downloads/

**VS Code:** https://code.visualstudio.com/download

Install required libraries via pip:

```
pip install pandas numpy scikit-learn matplotlib seaborn django opencv-python tensorflow keras
```

> **Note:** The trained model file `NN.h5` is not included in this repository (204MB, exceeds GitHub's limit). To use the lung cancer prediction feature, run `main.py` inside `LungCancer/LungApp/` to retrain and save the model locally.

## Running the Project

Each sub-app is a separate Django project and must be run in its own terminal:

```bash
# Terminal 1 — Main landing page (port 8000)
cd Main
python manage.py runserver

# Terminal 2 — Heart Attack app (port 7000)
cd HeartAttack
python manage.py runserver 7000

# Terminal 3 — Diabetes app (port 9000)
cd Diabetes
python manage.py runserver 9000

# Terminal 4 — Lung Cancer app (port 5000)
cd LungCancer
python manage.py runserver 5000
```

Access the apps at:
- **Main:** http://localhost:8000/
- **Heart:** http://localhost:7000/
- **Diabetes:** http://localhost:9000/
- **Lung Cancer:** http://localhost:5000/

## Prediction & Analysis

**Main app** — landing page linking to all three disease modules.

**Heart app** — dashboard with graphs and charts. Click **Predictions** in the sidebar and enter heart-related attribute values to get a prediction.

**Diabetes app** — dashboard with risk analysis. Click **Prediction** in the sidebar and enter diabetes-related attribute values to get a prediction.

**Lung app** — Click **Prediction** in the sidebar and upload a lung scan image (PNG/JPG) to receive a cancer detection result.

## Credits

This project was developed as part of a B.E. Final Year Project at PRMIT&R, Amravati (2022–2023).

## Acknowledgement

We would like to express our profound thanks to Dr. R. R. Karwa for their guidance and constant supervision. We would also like to thank Dr. M. A. Pund, Head of the Department of Computer Science & Engineering, and Dr. G. R. Bamnote, Principal of PRMIT&R, for their kind co-operation and encouragement. We extend our heartfelt thanks to our parents, friends, and well-wishers for their support and timely help.
