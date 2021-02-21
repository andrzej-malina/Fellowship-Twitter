import mysql.connector
import sys
import pandas as pd

# Connect to MariaDB Platform
try:
    conn = mysql.connector.connect(
        user="xxxxxxxxxxxxxx",
        password="xxxxxxxxxxxxxxxxx",
        host="xxxxxxxxxxxxxxxxxx",
        port=99999999999,
        database="xxxxxxxxxxxxxxxx"

    )
except mysql.connector.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# queries in SQL language
query_tweets: str = "SELECT * FROM fellowshipdb.tweets"
query_founders: str = "SELECT * FROM fellowshipdb.founders"

# download results of SQL query to pandas dataframe
df_tweets = pd.read_sql(query_tweets, conn)

# storing the dataframe to csv file on hard drive
df_tweets.to_csv('df_tweets.csv', index=False)

# download results of SQL query to pandas dataframe
df_founders = pd.read_sql(query_founders, conn)

# storing the dataframe to csv file on hard drive
df_founders.to_csv('df_founders.csv', index=False)