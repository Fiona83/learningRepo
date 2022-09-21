# Load and Analyse the Dataset of Fertility and Women's Labor Supply
Author: Yerong Chen
Last updated: 2022-09-21

## Step 1: Load the Dataset
The original data comes from the data list provided by Kevyn Collins-Thomson from the University of Michigan School of Information.

https://vincentarelbundock.github.io/Rdatasets/datasets.html

Here I took the data list of Fertility2 with 30000 data records. The data is read from the file and import into the database "fertility.sqlite". Before import the data, I changed all the text fields into integer type.
1. mkids (morekids): integer, 0 = "no", 1 = "yes".
> In SQLite there is no real Boolean type. Therefore integer is used here.

2. gender: integer, 0 = "male", 1 = "female"
3. create a separate table in database for ethnicities.
1 = "Caucasian", 2 = "African-American", 3 = "Hispanic", 4 = "Other than 1, 2 and 3"

Also within the dataset, there are some records with conflicts in ethnicities. -1 is set to represent **error** (there are more than 1 "yes" in the ethnicity flags).

**To run the data import:**
```
python3 input_fertility.py
```

## Step 2: Analyse and Virtualize the Data
### Analysis 1: What is the gender distribution among all the families with more than 2 kids
Here we pick out all the families with more than 2 kids and look up the gender of their first 2 kids. How many families have male-male combination? How many have female-female and how many have first two kids with different genders?

### Analysis 2: How many families among all the families with same-gender-kids have more than 2 kids
Here we pick out all the families with same-gender-kids (male-male or female-female) and see how many of them decided to have more kids.

After analysing the data, the results are written into "gender_mkids.js".
**To run the data analyse:**
```
python3 analyse_fertility.py
```

**To see the virtualization:**
```
open gender_mkids.htm
```
