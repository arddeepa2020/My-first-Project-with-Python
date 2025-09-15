import sqlite3


print("Welcome to Simple CRUD App!!")


connection= sqlite3.connect("crud.db")

cursor = connection.cursor()

def create_table():
    create_table_query="""
            CREATE TABLE IF NOT EXISTS cli(
            ID INTEGER PRIMARY KEY,
            NAME TEXT NOT NULL,
            AGE INTEGER,
            EMAIL TEXT UNIQUE
            )
    """
    try:
        cursor.execute(create_table_query)
        print("Table created successfully")
    except Exception as e:
        print("Table failed to create")
        print(e)
create_table()



def display():
    print('=' *30)
    print("Simple Crud App")
    print('=' *30)
    print("1. Add User")
    print("2. Show All Users")
    print("3. Update User")
    print("4. Delete User")
    print("5. Exit")
    print('=' *30)
# add_user function

def add_user():
    print("\n---Add New User ---")
    name=input("Enter Name: ")
    age=int(input("Enter Age: "))
    email= input("Enter Email: ")
    return(name,age,email)

# update function 
def update_user_value():
    user_id = int(input("\nEnter user ID to update: "))

    # Get the current values for this user
    cursor.execute("SELECT NAME, AGE, EMAIL FROM cli WHERE ID=?", (user_id,))
    current = cursor.fetchone()

    if not current:
        print(f"\nUser with ID {user_id} not found.")
        return None

    print("Enter new information (press Enter to keep current):")

    # Ask for new values, keep current if user presses Enter
    new_name = input("New name: ") or current[0]

    new_age_input = input(f"New age: ")
    new_age = int(new_age_input) if new_age_input.strip() else current[1]

    

    new_email = input("New email: ") or current[2]

    

    return (new_name, new_age, new_email, user_id)


# inserting value in database query
def insert_user():
    user=add_user()
    insert_user_query="""
        INSERT INTO cli(NAME,AGE,EMAIL) VALUES(?,?,?);
    """

    try:
        cursor.execute(insert_user_query,user)
        connection.commit()
        print(f"\nUser {user[0]} added successfully")
    except Exception as e:
        print("User failed to add")
        print(e)


#reading the value

def reading_query():

    select_query="""
        SELECT * FROM cli;
    """
    try:
        cursor.execute(select_query)
        all_user= cursor.fetchall()

        for user in all_user:
            print(f"{user[0]} | {user[1]} | {user[2]} | {user[3]}")
    except Exception as e:
        print("Error creating table:")
        print(e)

# update the user

def update_user():
    update_value= update_user_value()
    update_user_query="""
        UPDATE cli
        SET
            NAME=?,
            AGE=?,
            EMAIL=?
        WHERE ID=?;
    """
    try:
        cursor.execute(update_user_query,update_value)
        connection.commit()
        if cursor.rowcount > 0:
            print(f"\nUser ID {update_value[3]} updated successfully")
        else:
            print(f"\nUser with ID {update_value[3]} not found.")
    except Exception as e:
        print("ID failed to update")
        print(e)

# delete query:

def delete_user():
    del_id=int(input("\nEnter the ID to be deleted: "))

    delete_user_query="""
        DELETE FROM cli where ID=?;
    """
    try:
        cursor.execute(delete_user_query, (del_id,))
        connection.commit()
        if cursor.rowcount > 0:
            print(f"\nData with ID {del_id} deleted successfully.")
        else:
            print(f"\nNo user found with ID {del_id}.")

    except Exception as e:
        print("Error printing")
        print(e)



while True:

    display()

    choose= int(input("\nChoose an option (1-5): "))

    if choose==1:
       insert_user()
       input("\nPress enter to continue")

    elif choose==2:
        print("\n----All user----")
        print("\nID | NAME | AGE | EMAIL ")
        print('-' *30)
        reading_query()
        print('-' *30)
        input("\nPress enter to continue")

    elif choose==3:
        print("\n----All user----")
        print("\nID | NAME | AGE | EMAIL ")
        print('-' *30)
        reading_query()
        print('-' *30)

        update_user()
        input("\nPress enter to continue")

    elif choose==4:
        print("\n----All user----")
        print("\nID | NAME | AGE | EMAIL ")
        print('-' *30)
        reading_query()
        print('-' *30)

        delete_user()
        print("\n----All user----")
        print("\nID | NAME | AGE | EMAIL ")
        print('-' *30)
        reading_query()
        print('-' *30)
        input("\nPress enter to continue")
    
    elif choose==5:
        break

    else:
        print("Wrong input! Enter the valid number from 1 to 5.")
       
    
