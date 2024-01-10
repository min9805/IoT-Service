import uvicorn

from app.config.database import create_tables

# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    uvicorn.run("app.run:app", host="127.0.0.1", port=8000, reload=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

