# CSV HASHING CODE

This project was created using python libraries: csv, json, hashlib.
The program prompts the user to enter name of existing csv file name without ".csv" file extension.
The same filename will be used to create the output csv with the format "filename.output.csv".

## Process
1. The input file is first opened to be read and row_count increments by one to compute the series total.
2. After reading the data is stored in a variable. so it can be converted to json.
3. The input and output files are both opened with read and write mode respectively since the process is simultaneous
4. The data in input and output files are opened with DictReader and DictWriter respectively.
5. Eacher header is added to the output file
6. A loop begins in other to insert values for the attributes into the json format and set for converting
7. The output csv file is created and ready for hashing within the loop.
8. The hashlib uses the Secure Hash Algorith to create a hash for the json file and store it in the hashed field of the output csv file.
9. Lastly, the program writes the rows into the output file.
10. File closes.