import requests

BASE_URL = "https://jsonplaceholder.typicode.com/posts"


# GET Method - Retrieve all posts
def get_posts():
    response = requests.get(BASE_URL)
    
    if response.status_code == 200:
        posts = response.json()
        print("GET Request Successful\n")

        for post in posts:
            print(f"ID: {post['id']}")
            print(f"Title: {post['title']}")
            print(f"Body: {post['body']}")
        
    else:
        print("GET Requst Failed!")


# POST Method - Create a new post
def create_posts():
    new_post = {
        'title': 'Python tutorial',
        'body': 'Learning REST API using requests library.',
        'userId': 1
    }

    response = requests.post(BASE_URL, json=new_post)

    if response.status_code == 201:
        print('POST Request Successful\n')
        print(response.json())

    else:
        print('POST Request Failed!')


# PUT Method - Update an existing post
def update_post():
    updated_post = {
        'id': 1,
        'title': 'Updated Python version',
        'body': 'This post has been updated.',
        'userId': 1
    }

    response = requests.put(f"{BASE_URL}/1", json=updated_post)

    if response.status_code == 200:
        print('PUT Request Successful\n')
        print(response.json())

    else:
        print('PUT Request Failed!')


# PATCH Method - Update specific field
def patch_post():
    updated_data = {
        'title': 'Patched Title'
    }

    response = requests.patch(f"{BASE_URL}/1", json=updated_data)

    if response.status_code == 200:
        print('PATCH Request Successful\n')
        print(response.json())

    else:
        print('PATCH Request Failed!')


# DELETE Method - Delete a post
def delete_post():
    response = requests.delete(f'{BASE_URL}/1')

    if response.status_code == 200:
        print('DELETE Request Successful!')
    else:
        print("DELETE Request Failed!")


# Main Function Called
if __name__ == "__main__":
    
    # Retrieves all posts
    get_posts()

    # Creates a new post
    create_posts()

    # Updates the entire post using PUT
    update_post()

    # Updates only selected fields using PATCH
    patch_post()

    # Deletes a post using DELETE
    delete_post()
