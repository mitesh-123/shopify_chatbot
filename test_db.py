from langchain.llms import OpenAI
from langchain_experimental.sql import S
OPENAI_API_KEY=""
# Step 1: Create an instance of the language model
llm = OpenAI(openai_api_key=OPENAI_API_KEY, temperature=0, verbose=True)
# Step 2: Create an instance of the SQL database connection
db = SQLDatabaseChain(host='localhost', port=3306, username='root', password='', database='shopifyapi')

# Step 3: Create the database chain
db_chain = create_sql_query_chain(llm, db)
