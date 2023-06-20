import mysql.connector
import json

class user_model():

    # Constructor function which gets called when object is created
    def __init__(self):
        # Connections establishment code
        # If we don't extablish connections here then we have to extablish in every method
        try:
            self.con = mysql.connector.connect(host='localhost', user="root", password='Mukul123', database='flask_learning')
            self.con.autocommit = True
            self.cur = self.con.cursor(dictionary=True)
            # This line creates a cursor object (cur) using the cursor() method of the connection object (con). The dictionary=True argument specifies that the cursor should return the query results as a dictionary where the column names are the keys and the corresponding values are the values.
            print("Connedtion Successfully")
        except: 
            print("Some error")


    def  user_getall_model(self):
        self.cur.execute("SELECT * FROM users")
        result = self.cur.fetchall()
        print(result)
        if len(result) > 0:
            return {"payload": result}
        else:
            return {"message": "No Data Found"}


    def user_addone_model(self, data):
        self.cur.execute(f"INSERT INTO users(name, email, phone, role, password) VALUES('{data['name']}', '{data['email']}', '{data['phone']}', '{data['role']}', '{data['password']}')")
        print(data)
        return {"message": "User created successfully"}
    

    def user_update_model(self, data):
        self.cur.execute(f"UPDATE users SET name='{data['name']}', email='{data['email']}', phone='{data['phone']}', role='{data['role']}', password='{data['password']}' WHERE id={data['id']}")
        print(data)
        if self.cur.rowcount > 0:
            return {"message": "User Update successfully"}
        else:
            return {"message": "Nothing to Update"}


    def user_delete_model(self, id):
        self.cur.execute(f"DELETE FROM users WHERE id={id}")
        if self.cur.rowcount > 0:
            return {"message": "User Deleted Successfully"}
        else:
            return {"message": "Nothing to Delete"}


