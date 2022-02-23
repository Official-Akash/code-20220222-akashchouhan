# CODE-20220222-AKASHCHOUHAN

Python application that can be used as a backend/CLI Application to generate identify the Health Risk Factor based on the individual BMI.

### 1. Prerequisites

```
Python >= 3.8.x
```

### 2. Setting Up

a. clone the repository to the system

b. Go into the directory CODE-20220222-AKASHCHOUHAN

c. Install the requirements

```
> pip3 install -r requirements.txt
```

d. Once installed run the following command to make sure all the dependencies are resolved

```
> pip3 list

The output will look like following

Package         Version
--------------- -------
click           8.0.4
numpy           1.22.2
pandas          1.4.1
pip             22.0.3
python-dateutil 2.8.2
pytz            2021.3
setuptools      60.9.3
six             1.15.0
wheel           0.33.1

```

### 3. Testing the Suite

CD to the Code Directory and run the following for testing

```
> python3 -m unittest -v
```

### 4. Running the application

#### 4a. To Run the application on sample data

Sample input json Data file is available under `resources/` directory. The sample output CSV file will also be stored under `resources/` directory of the code.

```
> python3 execute.py
```

#### 4b. To run the application on new Files

This is a CLI based application that accepts the command line arguments as input.

```
USAGE: execute.py [Options]

Options:
    --input_file    Input File Name with absolute path
    --output_file   Output File Name with absolute path
    
Example:

> python3 execute.py --input_file <path_to_file> --output_file <path_to_new_file>
```