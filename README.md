# TO-DO:
- add postgres db
- add func for saving to db

# Database Application (intern assignment)

*Summary*: An application that takes a data source and puts it in a database.  

*Features*:
* can import data from a document
* can parse the contents of a document into db record data
* can add records to a database
* can perform basic queries on the database


## Installation
 [[ TODO ]]


## Running tests  
There are two test suites to run:  
1.  To test the CLI, run `python tests/test_cli.py` from the root project directory  
2.  To run the normal unit tests, run `pytest` from the root project directory

## Sample Usage
1. Add records from a document to a database
*Syntax*:  `$ dbtool <action> <resource_type> <resource_path>
*Example*: `$ dbtool import file games.csv psql:chessdb`
*Example*: `$ dbtool import file games.csv psql:chessdb -p games.parser.py`

2. Get summary information about a table
*Usage*: dbtool <action> <target> <summary_type> [-q (SQL query)]
*Example*: `$ dbtool query chessdb total`
*Example*: `$ dbtool query chessdb -q 'victory_status is "mate"`


# Original Assignment Prompt

    Find a relatively simple dataset that you can work with and perform some sort of aggregation on, such as movie scores, movie reviews, sporting event stats, web server stats, etc.
    Pick a dataset with a lot of different distinct entities (different movies, candies, etc.).
    Pick a dataset with a standard numerical range as a rating or average of some field within the data.
    Pick a dataset not too small, not too large. (5k rows < num < 1m rows)
    Try to save the dataset to disk so you’re not requesting the data from an API or web site each time you run your script.
    Write a script to ingest that data from a file and save to a database. (SQLite, PostgreSQL, MySQL/MariaDB)
    Don’t worry about adding indexes at this point.
    Write a script to output basic stats about that data from the database to prove the visibility and accessibility of the data.
    Push your code to your personal GitLab repo. (call it “onboarding” or something)
    Set up linting and testing and get your build to be successful/green. (see https://gitlab.s.fpint.net/collections/bmt/blob/master/.gitlab-ci.yml and https://gitlab.s.fpint.net/collections/bmt/blob/master/prova.unit.yml )

