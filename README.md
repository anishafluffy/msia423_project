# Web App for MSiA 423 Analytics Value Chain Class

### Team  
Developer: Anisha Dubhashi   
Project Owner: Jerry Chen   
QA: Yiwei Sun   

### Project Charter

### Vision 
Help people choose a cuisine for the next meal they cook based on ingredients they have in their pantry. This functionality will increase users' interactions with the recipe site, increasing engagement, retention, and brand awareness. 

### Mission 
Create a web app to predict the category of a dish's cuisine given  a user's input of a list of ingredients. The underlying model will be a classification model based on 40,000 recipes from Yummly. The data includes the cuisine and list of ingredients for each recipe id in json files. 

### Success criteria 
This project will be successful if the model is deployed on AWS, and if the user inputs in the web app score the model in real-time. 

### Dataset 
Over 40k recipes from Yummly including ingredients and classified cuisines: https://www.kaggle.com/kaggle/recipe-ingredients-dataset/data 

### Final presentation 
Presentation with project overview, including motivation, data description, model description, and webapp screenshot: [[deck](https://github.com/anishafluffy/msia423_project/blob/final_updates/cuisine_machine_deck.pdf)]

### Steps
```
# Set up virtual environment
# Set repository as working directory
> cd msia423_project
> source ./py/bin/activate
> pip install -r requirement.txt

# Prepare data
> python create_db.py 
> cd development 
> python clean_data.py 
> python train_model.py 

# Run app
> cd msia423_project
> python application.py
```


### Directory Structure 
 
    ├── README.md           	<- README for developers using this project   
    │
    ├── app                 	<- stores everything related to front-end web app  
    │ 
    │    ├── static 				<- stores webapp background images   
    │    │ 
    │    ├── templates 				<- stores webapp html   
    │	 │
    │    │   ├── index.html 				<- homepage with data entry  
    │    │   │
    │    │   ├── handle_data.html 			<- prediction page with response  
    │    │   │
    │    ├── __init__.py 			<- initializes flask  
    │    │
    │    ├── models.py 				<- creates database  
    │    │
    │    │
    ├── development         	<- stores everything related to data analysis and model build  
    │    │        
    │    ├── data              		<- test & train data from kaggle in .json files  
    │    │
    │    ├── notebooks 				<- jupyter notebooks from initial development  
    │    │
    │    ├── clean_data.py         	<- function to import and clean .json data  
    │    │
    │    ├── train_model.py        	<- function to vectorize data and train model   
    │    │
    │    ├── predict_response.py   	<- function to predict from user input   
    │    │
    │    ├── cl.pkl        			<- logistic regression classifier saved as pkl file  
    │    │ 
    │    ├── ve.pkl        			<- vectorizer saved as pkl file   
    │    │
    ├── docs                	<- stores Sphinx documentation   
    │   
    ├── static              	<- stores webapp background images    
    │   
    ├── application.py 			<- runs flask for webapp    
    │   
    ├── config.py 				<- links database    
    │   
    ├── create_db.py 			<- creates database    
    │   
    ├── requirements.txt 		<- requirements file  
  

### Pivotal Tracker Link 
https://www.pivotaltracker.com/n/projects/2141920 











