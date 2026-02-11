import os
import json

initial_blogposts = [
    {
        "id": 1,
        "author": "John Doe",
        "title": "First Post",
        "content": "This is my first post.",
    },
    {
        "id": 2,
        "author": "Jane Doe",
        "title": "Second Post",
        "content": "This is another post.",
    },
    # More blog posts can go here...
]


def get_blogposts():
    """
    Returns a list of dictionaries that
    contains the blogpost information in the database.

    The function loads the information from the JSON
    file and returns the data.

    For example, the function may return:
    [
    {"id": 1, "author": "John Doe", "title": "First Post", "content": "This is my first post."},
    {"id": 2, "author": "Jane Doe", "title": "Second Post", "content": "This is another post."}
    # More blog posts can go here...
    ]
    """
    if not os.path.exists("data/data.json"):
        print("data.json file not found. Creating a new one.")
        with open("data/data.json", "w") as file:
            json.dump({}, file)
    with open("data/data.json", "r") as file:
        blogposts = json.load(file)
    return blogposts


def save_blogposts(blogposts):
    """
    Gets all your movies as an argument and saves them to the JSON file.
    """
    with open("data/data.json", "w") as file:
        json.dump(blogposts, file, indent=4)


def add_blogpost(author, title, content):
    """
    Adds a movie to the movies database.
    Loads the information from the JSON file, add the movie,
    and saves it. The function doesn't need to validate the input.
    """
    blogposts = get_blogposts()
    newest_id = blogposts[-1]['id']
    id = newest_id + 1
    blogposts.append({'id': id, 'author': author, 'title': title, 'content': content})
    save_blogposts(blogposts)