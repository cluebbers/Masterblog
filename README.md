# Masterblog

Simple Flask blog app with JSON-based storage and CRUD operations.

## Functions

`app.py` (Routes)

- `index()`: Loads all posts and renders the homepage.
- `add()`: Shows add form (GET) and creates a post (POST).
- `delete(post_id)`: Deletes a post by id and redirects home.
- `update(post_id)`: Shows update form (GET) and edits a post (POST).

`storage.py`

- `get_blogposts()`: Reads posts from `data/data.json`.
- `save_blogposts(blogposts)`: Writes posts back to JSON file.
- `add_blogpost(author, title, content)`: Appends a new post with a new id.
- `fetch_post_by_id(post_id)`: Returns a single post by id.
- `delete_blogpost(post_id)`: Removes a post by id.
- `update_blogpost(post_id, author, title, content)`: Updates an existing post.

## Run

```bash
cd Assessment/Masterblog
python app.py
```
