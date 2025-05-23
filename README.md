# Itinero
Personal Travel Recommendation Model

[Figma Wireframe](https://www.figma.com/team_invite/redeem/mGhBfs7l41S3IAZCViwB4f)
### Setting Up Virtual Environment and Installing Requirements

#### **For Windows:**

1. **Open Command Prompt:**
    - Press `Win + R`, type "cmd", and press `Enter` to open the Command Prompt.

2. **Create Virtual Environment:**
    ```bash
    python -m venv venv
    ```

3. **Activate Virtual Environment:**
    ```bash
    .\venv\Scripts\activate
    ```

4. **Install Requirements:**
    ```bash
    pip install -r requirements.txt
    ```

5. **Deactivate Virtual Environment:**
    ```bash
    deactivate
    ```
    
#### **For macOS:**

1. **Open Terminal:**
    - Press `Cmd + Space` to open Spotlight Search.
    - Type "Terminal" and press `Enter` to open the terminal.

2. **Create Virtual Environment:**
    ```bash
    python3 -m venv venv
    ```

3. **Activate Virtual Environment:**
    ```bash
    source venv/bin/activate
    ```

4. **Install Requirements:**
    ```bash
    pip install -r requirements.txt
    ```

5. **Deactivate Virtual Environment:**
    ```bash
    deactivate
    ```

### Notes:

- Replace `python3` with `python` if your default Python version is Python 3 on macOS.
- `venv` is the name of the virtual environment folder. You can use a different name if you prefer.
- The `requirements.txt` file should contain a list of your project dependencies.
- The `activate` and `deactivate` commands are used to activate and deactivate the virtual environment, respectively.

### Populating Database with Cities and States

#### **Step 1: Set Up Database Connection**

- Ensure your PostgreSQL database is created and running.

#### **Step 2: Run the Python Script**

- Locate the existing Python script: `backend/app/popuST.py`.

- Open a terminal or command prompt.

- Navigate to the script's directory.

- Run the script:

  ```bash
  python popuST.py
  

# Setting up PostgreSQL Database

### Step 1: Download and Install PostgreSQL

- Visit the official PostgreSQL website & download the installer appropriate for your operating system:
https://www.postgresql.org/download/


### Step 2: Follow the installation prompts

- Keep the default install directory
- **Uncheck *StackBuilder* from "Select Components".**
- Keep default Data Directory.
- Set superuser password - *Remember It*
- Keep default port (5432).
- Keep Default Locale - Language option

### Step 3: Start PgAdmin4

- Open *Servers* drop down menu.
- Enter the password from installation when prompted.


### Step 4: Create a new local database

- Right-click on the "Database" in the dropdown menu.
- Select Create -> Database...
- Name database: itinero_db
- Save
- Double check database is initialized correctly by going back to the dropdown menu and selecting the newly created database.



# Setting up a Django Project with PostgreSQL and psycopg2-binary

### Step 1: Install Python and pip

Make sure you have Python and Pip installed on your system.
This project works with Python 3.11.6+ and should by default already come with pip installed.

### Step 2: Clone this repository and CD to the folder


### Step 3: Install Django and psycopg2-binary

```
pip install django psycopg2-binary
```
### Step 4: Edit the Setting.py file
- In backend/django/itinero directory edit the database line in the Settings.py file and add your password to the field.
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', 'itinero_db'),
        'USER': os.environ.get('DB_USER', 'postgres'),
        'PASSWORD': os.environ.get('DB_PASSWORD', ''),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}
```
### Step 5: Move To Backend Directory

```
cd backend/django/itinero
```

### Step 6: Migrate and Run the Server

```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Now your Django project is set up with a PostgreSQL database. You can access the development server at `http://127.0.0.1:8000/`.

### Access the URLs in your web browser:
   - Login: [http://127.0.0.1:8000/login](http://127.0.0.1:8000/login)
   - Register: [http://127.0.0.1:8000/register](http://127.0.0.1:8000/register)



# How to utilize the 'CrimeClassifier' class of Itinero

### Step 1: Download Git LFS

The path file containing the current model state of the 'CrimeClassifier' feature is too large to add to the repository.
Therefore, it is necessary to download Git Large File Storage (LFS) from:
https://git-lfs.com/.
This Git extension will be automatically added to your native 'git' path on your PC.

### Step 2: Fetching the 'best_crime_classifier.pth' file

Once you have pulled the most recent code into your repo, with Git LFS installed, go to your repo's terminal/console and run:

```
git lfs install
git lfs fetch
```

*Note:
    - It is only necessary to run the commands above when Git LFS has NOT been set up yet, after that, a simple pull request will suffice.

## Now you will have any and all 'large files' within the '.gitattributes' directory installed locally

### Step 3: Utilizing the 'CrimeClassifier' feature/class

Any and all functions of the CrimeClassifier feature are defined within the 'itinero_model.py' file within "Itinero/backend/app"

In short, as long as you import the file and class at the top of your code...

```
from itinero_model import CrimeClassifier
```

...and you create an object instance of the class:

```
crime_classifier = CrimeClassifier()
```

You can use any of its functions freely.

## A short demo of how to utilize the feature can be found in "Itinero/backend/app/__init__.py"
## Project Origin  
This project was my initiative, proposed as a class project in 2023. While hosted under [@alec0322](https://github.com/alec0322)'s repository, I led development and contributed the majority of the codebase.

## Attribution  
Developed in collaboration with:  
- [@alec0322](https://github.com/alec0322)  
- [@hamzo23](https://github.com/hamzo23)  
- [@csole014](https://github.com/csole014)  
- [@CrisBlu](https://github.com/CrisBlu)  
- [@frsant](https://github.com/frsant)  

**Original repository**: [Itinero](https://github.com/alec0322/Itinero)  
**My contributions**:  
- **Led backend architecture and API design**: Established the foundational structure for the project, ensuring seamless integration between components.  
- **Contributed 33 commits (35% of total)**: Focused on backend implementation, authentication, and ensuring the product ran end-to-end.  
- **Designed and implemented the authentication flow**: Used to secure user data and enable seamless login functionality.  
- **Collaborated on ML model integration**: Worked with teammates to integrate machine learning features and ensure the system was production-ready.  
- **Improved frontend stability**: Debugged and resolved crashes, ensuring a smoother user experience.  
- **Ensured project continuity**: Acted as the primary developer for setup and integration, enabling the team to build on a stable foundation.  
