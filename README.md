# Image-Blog-System
## Description
The **Image Blog System** is a web application built using Django that allows users to create, manage, and share image-based blog posts. Users can upload images, add descriptions, and comment on posts, making it a vibrant community for sharing visual content.

## Features
- User registration and authentication
- Create, edit, and delete blog posts
- Upload and display images
- Commenting system for user interactions
- User profile management

## Technologies Used
- **Backend**: Django
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (or your choice of database)
- **Deployment**: Heroku or PythonAnywhere (for future deployment)

## Setup Instructions

### 1. Clone the Repository
Clone the repository to your local machine:  
git clone https://github.com/yourusername/image-blog-system.git  
cd image-blog-system  
### 2. Create the Virtual Environment  
Create a virtual environment in the root directory:    
python -m venv venv  
Activate the virtual environment:  
venv\Scripts\activate   

### 3. Install Dependencies
Install the required dependencies:  
pip install -r requirements.txt  
### 4. Set Up the Database  
Run the migrations to set up the database:  
python manage.py migrate  
### 5. Create Media Folder  
Create a folder named media in the root directory. This folder will store user-uploaded images:  
mkdir media  
### 6. Create a Superuser  
Create a superuser to access the admin panel:  
python manage.py createsuperuser  
### 7. Run the Development Server  
Start the development server:  
python manage.py runserver  
### 8. Access the Application  
Open your web browser and navigate to http://127.0.0.1:8000/ to view the application.  

### Usage
Register an account or log in if you already have one.  
Create a new blog post by navigating to the blog creation page.  
Upload images and add descriptions.  
View and interact with posts in the blog section.  
### Contributing  
Contributions are welcome! Feel free to submit a pull request or open an issue to discuss improvements.  

### License  
This project is licensed under the MIT License. See the LICENSE file for details.  

### Acknowledgments
Django documentation for guidance on best practices.  
Community support and tutorials that helped in the development of this project.  
