# access-to-PostgreSQL
This repository converts Access DB csv files to PostgreSQL insert scripts

# General
This python codes, creates insert scripts from an existing MS Access database table for PostgreSQL.

# The Process

To begin with, this codes do not directly get data from Access database. Initially the table in the Access DB should be exported as an MS Excel file.

Following these steps will make it very easy for me to export Access tables to PostgreSQL while doing a small scale project.
1.	Saving the relevant table from Access DB as an Excel table,
2.	Updating column names in Excel table ( if the column names defined in PostgreSQL are different from those in Access DB.)
3.	Editing the data (Date fields must be in PostgreSQL date format, NULL values, etc.)
4.	Saving the Excel file as a CSV file.
5.	Converting the saved CSV file to a data frame with the Python Pandas library, looping the row and column values of the data frame, writing the data as an insert script and saving the script as a line in a txt file,
6.	The scripts from the txt file and pasting them into the PGAdmin query window and running them .

## Saving the relevant table as an Excel table from Access DB:
After selecting the relevant table, we select the "External Data" menu. Here we click on Excel. We save the Excel file by saying OK.

![image](https://user-images.githubusercontent.com/72765484/224379756-c1a2405d-4346-48c7-a6f7-f17b83671753.png)

##	Updating column names in Excel table
We have to do this because the column names in PostgreSQL and in the Excel file have to be consistent!

![image](https://user-images.githubusercontent.com/72765484/224379840-cec3fa1c-55d2-4b6c-9aab-8efe6498c97d.png)

## Organizing data

Only the “ change_date ” column in the Excel table is in date format. We have to save this format as text. The PostgreSQL format is "YYYY-MM-DD". We can use Excel's translate-to-text function for this . The formula will be as follows. Of course, the excel I use is in Turkish. English users should write “YYYY-MM-DD”!

![image](https://user-images.githubusercontent.com/72765484/224379934-5f227798-df08-4959-9e41-7df2ef3e33d5.png)

YYYY - > Year, 2026
MM-> Moon, 03
DD->Day,23
We convert the entire column to text with the fill handle. Then we paste it again in the “ change_date ” column. The Excel file will change as follows. Salaries are also in Excel currency format. We need to convert that into numbers as well.

![image](https://user-images.githubusercontent.com/72765484/224379981-eea3cfa6-4e1c-4a3f-a17d-990391a73389.png)

## Saving the Excel file as a CSV file.

Excel file as csv file in UTF-8 format

![image](https://user-images.githubusercontent.com/72765484/224380068-baaf1557-4c57-4ea5-8129-8669b8516a10.png)

## Converting the saved CSV file to a data frame with the Python Pandas library, looping the row and column values of the data frame, writing the data as an insert script and saving the script as a line in a txt file,

Let's create a new project in Anaconda Spyder . The appearance of the “100_salarychange.csv” file that we have saved in this project folder will be as follows. Here, decimals in numeric values are separated by “ , “ (comma). In this python, “ string ” will appear as a value. To avoid this, use the text editor to replace “,” with “.” The image is below:

![image](https://user-images.githubusercontent.com/72765484/224380431-424fa8ba-ad66-475a-8479-2b1f4787d656.png)

The codes will convert the csv file to SQL script and save it to the file named sql.txt.

The appearance of the sql.txt file will be as follows. 

![image](https://user-images.githubusercontent.com/72765484/224380571-50c31acc-e924-49a4-9e47-c2184926ecd3.png)

## Copy the scripts from the txt file and paste them into the PGAdmin query window and run them.

Just copy, paste and run!

![image](https://user-images.githubusercontent.com/72765484/224380709-d8d14482-8860-413d-bd2d-433fc1abf0ca.png)






