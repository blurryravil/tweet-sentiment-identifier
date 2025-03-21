# Tweet Sentiment Identifier

## Description
Tweet Sentiment Identifier is a Python-based project using Jupyter Notebook to analyze and identify the sentiment of tweets. The project involves machine learning model creation, serialization, and deployment.

## Installation
To set up this project, follow the steps below:
1. Clone the repository to your local machine
   ```bash
   git clone https://github.com/{username}/tweet-sentiment-identifier.git
   ```
2. Install the necessary Python packages by running the requirements.txt file in the root directory
   ```bash
   pip install -r Pegasus_Final/requirements.txt
   ```
3. Open and run the Jupyter notebook file (Model.ipynb) to build and train the model
   ```bash
   jupyter notebook Pegasus_Final/Model.ipynb
   ```

## Usage
After setup, you can use the project by running the main.py file:
```bash
python Pegasus_Final/main.py
```
You can also use the trained model (Model.pkl) and vectoriser (vectoriser-ngram-(1,2).pkl) for your own applications.

## Repository Structure
The repository structure is as follows:
```
/
├── Pegasus_Final/
│   ├── Model.ipynb          # Jupyter notebook for model creation.
│   ├── Model.pkl            # Serialized machine learning model.
│   ├── Procfile             # Used in cloud platforms to specify startup commands.
│   ├── app.yaml             # Configuration file for cloud deployment.
│   ├── elements/            # Directory containing static files for web application.
│   │   ├── index.html       # HTML template for web interface.
│   │   └── logo.png         # Logo image for web interface.
│   ├── main.py              # Main Python script to run the project.
│   ├── requirements.txt      # File listing required packages for installation.
│   ├── train.csv            # Dataset for training the model.
│   └── vectoriser-ngram-(1,2).pkl  # Serialized vectoriser used for text transformation.
├── README.md                # This file
└── test.py                 # Script for testing purposes.
```

## Key Directories and Files

- **Pegasus_Final**: Main project directory containing all necessary files and sub-directories:
  - `Model.ipynb`: Jupyter notebook used for creating and training the sentiment analysis model.
  - `Model.pkl`: Serialized version of the machine learning model that can be utilized after training.
  - `Procfile`: Specifies commands executed by apps on startup when deployed on cloud platforms like Heroku.
  - `app.yaml`: Configuration settings required for deploying on cloud services such as Google Cloud Platform or AWS Elastic Beanstalk.
  - **elements**: Contains static resources like HTML files and images used in web applications:
    - `index.html`: Base HTML page template used in rendering pages upon server response.
    - `logo.png`: Image asset used within web application UI elements. 
  - `main.py`: Entry point script responsible for executing sentiment analysis based on user input or predefined datasets.
  - `requirements.txt`: Lists all dependencies needed by this project; install them using pip with this command: `pip install -r requirements.txt`.
  - `train.csv`: The CSV dataset utilized during training processes; must have specific format conforming to expected features of input data.
  - `vectoriser-ngram-(1,2).pkl`: A serialized n-gram vectorizer which transforms textual data into numerical vectors fitting ML models.

## Frameworks and Libraries
While no specific frameworks or libraries were explicitly identified, it is inferred that various Python packages are utilized throughout this project. The specific packages can be found listed in requirements.txt.

## License  
No license information is provided in this repository.

## Release Notes  
- **New Features**: Initial implementation of tweet sentiment analysis functionality using machine learning techniques has been established.  
- **Improvements**: Enhanced data processing capabilities through better utilization of vectorization techniques.  
- **Release Date**: Changes were released on March 21, 2025 at 10:31 AM UTC.

---

Version: 1  
Last updated: March 21, 2025 
