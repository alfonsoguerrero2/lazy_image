# lazy_image

## Description

Python script to retriving images 

## Prerequisites

Before you begin, ensure you have met the following requirements:
- You have Python 3 installed on your machine. You can download it from [python.org](https://www.python.org/).
- You have `pip`, Python's package installer, installed. It typically comes with Python.

## Setup

### Step 1: Clone the Repository

Clone the repository to your local machine using the following command:

```cmd
git clone https://github.com/alfonsoguerrero2/lazy_image
cd lazy_image
```


### Step 2: Create a Virtual Environment
Create a virtual environment to ensure that your project's dependencies are isolated from other Python projects. Run the following command to create a virtual environment in your project directory:

```cmd
python -m venv venv
```

Activate the virtual environment:

```cmd
.\venv\Scripts\activate
```

### Step 3: Install Requirements

Use the `requirements.txt` file to install the necessary packages:

```cmd
pip install -r requirements.txt
```

This will install all the dependencies listed in the `requirements.txt` file.

### Step 4: Run the Python Script

Once the environment is set up and dependencies are installed, you can run the Python script. Use the following command to execute the script:

```cmd
python picture.py
```


## Additional Notes
 To deactivate the virtual environment, simply run the `deactivate` command:
  ```cmd
  deactivate
  ```

  If you need to add new dependencies, use `pip install <package-name>` and then update your `requirements.txt` using:
  ```cmd
  pip freeze > requirements.txt
  ```