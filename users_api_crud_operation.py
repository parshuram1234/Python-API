import requests

BASE_URL = "https://jsonplaceholder.typicode.com/users"

# GET Method - Retrieve all users
def get_users():
    response = requests.get(BASE_URL)
    
    if response.status_code == 200:
        users = response.json()
        print("Get Request Successful\n")
        for user in users:
            print(f"ID: {user['id']}, Name: {user['name']}, Email: {user['email']},")

    else:
        print("GET Request Failed!")


# POST Method - Create a new user
def create_user():
    new_user = {
        "name": "John Doe",
        "username": "johndoe",
        "email": "john@example.com",
        "phone": 123-456-7890,
        "website": "johndoe.com"
    }

    response = requests.post(BASE_URL, json=new_user)

    if response.status_code == 201:
        print("\nPOST Request Successfull!")
        print(response.json())
    else:
        print("POST Request Failed!")


# PUT Method - Update an existing user
def update_user(user_id):

    update_user = {
        "id": user_id,
        "name": "Jane Smith",
        "username": "janesmith",
        "email": "jane@exampl.com",
        "phone": 999-999-9999,
        "website": "janesmith.com"
    }

    response = requests.put(f"{BASE_URL}/{user_id}", json=update_user)

    if response.status_code == 200:
        print("\nPUT Request Successful!")
        print(response.json())
    else:
        print("PUT Request Failed!")


# PATCH Method - Partially update a user fields
def patch_user(user_id):

    update_company_name = {
        "company": {
            "name": "OpenAI Technologies"
        }
    }

    response = requests.patch(f"{BASE_URL}/{user_id}", json=update_company_name)

    if response.status_code == 200:
        print("\nPATCH Request Successful!")
        print(response.json())
    else:
        print("PATCH Request Failed!")


# DELETE Method - Delete a user
def delete_user(user_id):
    
    response = requests.delete(f"{BASE_URL}/{user_id}")
    
    if response.status_code == 200:
        print(f"\nDELETE Request Successful! User {user_id} deleted.")
    else:
        print("DELETE Requests Failed!") 


# Main Program
if __name__ == "__main__":
    print("--- Get Users ---")
    get_users()

    print("\n--- Create User ---")
    create_user()

    print("\n--- update User ---")
    update_user(1)

    print("\n--- Patch user ---")
    patch_user(2)

    print("\n--- Delete user ---")
    delete_user(8)