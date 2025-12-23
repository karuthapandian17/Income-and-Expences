from fastapi import FastAPI , Body, Depends
from database import databaseConfigration
from database.models.model import UserModel, CategoryModel
from fastapi.exceptions import HTTPException

app=FastAPI()

databaseConfigration.create_database()

def get_db():
    connection = databaseConfigration.create_database()
    if connection is None:
        raise Exception(status_code=500, detail="Database connection error")

    try:
        yield connection
    finally:
        if connection and connection.is_connected():
            print("connected Successfully")

@app.get("/")
def home():
    return {"message":"Welcome to Income and Expense Tracker API"}  

@app.post("/create_users/", response_model=dict)
async def create_user(users: UserModel = Body(...), connection=Depends(get_db)):
    try:
        cursor = connection.cursor()
        insert_query = "INSERT INTO USERS (FULLNAME, EMAIL, PASSWORD_HASH) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (users.full_name, users.email, users.password_hash))
        connection.commit()
        print("Users created successfully")
        def connectionClose(connection, cursor=None):
            if cursor:
                cursor.close()
            if connection:
                connection.close()
        return {"message": "User created"}
    except Exception as e:
        connection.rollback()
        raise HTTPException(status_code=500, detail=f"database error:{str(e)}")
    
@app.get("/get_users/", response_model=dict)
async def get_users(connection=Depends(get_db)): 
    try:
        cursor = connection.cursor()
        insert_query = "SELECT * FROM USERS"
        cursor.execute(insert_query)
        data = cursor.fetchall()
        connection.commit()
        if not data:
            return {"message": "No users"}
        def connectionClose(connection, cursor=None):
            if cursor:
                cursor.close()
            if connection:
                connection.close()
        # databaseConfigration.connectionClose(connection)
        return {"message": data}
    except Exception as e:
        connection.rollback()
        raise HTTPException(status_code=500, detail=f"database error:{str(e)}")   

@app.post("/update_users/", response_model=dict)   
async def update_user(users: UserModel = Body(...), connection=Depends(get_db)):
    try:
        cursor = connection.cursor()
        insert_query = "UPDATE USERS SET FULLNAME=%s, EMAIL=%s, PASSWORD_HASH=%s WHERE ID=%s"
        cursor.execute(insert_query, (users.full_name, users.email, users.password_hash, users.id))
        connection.commit()
        def connectionClose(connection, cursor=None):
            if cursor:
                cursor.close()
            if connection:
                connection.close()
        return {"message": "updated successfully"}
    except Exception as e:
        connection.rollback()
        raise HTTPException(status_code=500, detail=f"database error:{str(e)}")
    
@app.delete("/delete_users/", response_model=dict)
async def delete_user(user_id: int = Body(...), connection=Depends(get_db)):
    try:
        cursor = connection.cursor()
        insert_query = "DELETE FROM USERS WHERE ID=%s"
        cursor.execute(insert_query, (user_id,))
        connection.commit()
        def connectionClose(connection, cursor=None):
            if cursor:
                cursor.close()
            if connection:
                connection.close()
        return {"message": "deleted successfully"}
    except Exception as e:
        connection.rollback()
        raise HTTPException(status_code=500, detail=f"database error:{str(e)}")
    
@app.post("/create_category/", response_model=dict)
async def create_category(category: CategoryModel = Body(...), connection=Depends(get_db)):
    try:
        cursor = connection.cursor()
        insert_query = "INSERT INTO CATEGORIES (USER_ID, NAME, TYPE) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (category.user_id, category.name, category.type))
        connection.commit()
        print("Category created successfully")
        def connectionClose(connection, cursor=None):
            if cursor:
                cursor.close()
            if connection:
                connection.close()
        return {"message": "Category created"}
    except Exception as e:
        connection.rollback()
        raise HTTPException(status_code=500, detail=f"database error:{str(e)}")
    
@app.get("/get_categories/", response_model=dict)
async def get_categories(connection=Depends(get_db)):
    try:
        cursor = connection.cursor()
        insert_query = "SELECT * FROM CATEGORIES"
        cursor.execute(insert_query)
        data = cursor.fetchall()
        connection.commit()
        if not data:
            return {"message": "No categories"}
        def connectionClose(connection, cursor=None):
            if cursor:
                cursor.close()
            if connection:
                connection.close()
        return {"message": data}
    except Exception as e:
        connection.rollback()
        raise HTTPException(status_code=500, detail=f"database error:{str(e)}")
    
@app.post("/update_category/", response_model=dict)   
async def update_category(category: CategoryModel = Body(...), connection=Depends(get_db)):
    try:
        cursor = connection.cursor()
        insert_query = "UPDATE CATEGORIES SET USER_ID=%s, NAME=%s, TYPE=%s WHERE ID=%s"
        cursor.execute(insert_query, (category.user_id, category.name, category.type, category.id))
        connection.commit()
        def connectionClose(connection, cursor=None):
            if cursor:
                cursor.close()
            if connection:
                connection.close()
        return {"message": "Category updated successfully"} 
    except Exception as e:
        connection.rollback()
        raise HTTPException(status_code=500, detail=f"database error:{str(e)}")
    
@app.delete("/delete_category/", response_model=dict)
async def delete_category(category_id: int = Body(...), connection=Depends(get_db)):
    try:
        cursor = connection.cursor()
        insert_query = "DELETE FROM CATEGORIES WHERE ID=%s"
        cursor.execute(insert_query, (category_id,))
        connection.commit()
        def connectionClose(connection, cursor=None):
            if cursor:
                cursor.close()
            if connection:
                connection.close()
        return {"message": "Category deleted successfully"}       

    except Exception as e:
        connection.rollback()
        raise HTTPException(status_code=500, detail=f"database error:{str(e)}")