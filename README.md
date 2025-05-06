# Flask Item Management Application

This project is a simple Flask-based web application for managing a list of items. Users can:
- View a list of items.
- Add a new item.
- View details of an individual item.
- Update an item's name.
- Delete an item.

## Features

- **Item List**: Displays all items in the system.
- **Item Detail**: Provides details of an individual item.
- **Add Item**: Allows adding a new item.
- **Edit Item**: Updates the name of an existing item.
- **Delete Item**: Deletes an existing item.

---

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/DavidIsraelN/Flasc_01.git
    cd Flasc_01
    ````

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: ./.venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Ensure Flask is installed and accessible.

---

## Usage

1. **Run the application:**

   ```bash
   python run.py # or - flask run
   ```

2. **Access the application in your browser:**
   Navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

## API Endpoints

* **GET `/`**: Retrieves and displays a list of all items.
* **POST `/items`**: Adds a new item. Requires a `name` parameter.
* **GET `/item/<item_id>`**: Retrieves details for a specific item.
* **PUT `/items`**: Updates an item. Requires `id` and `name` parameters.
* **DELETE `/items`**: Deletes an item. Requires an `id` parameter.

---

## File Structure

* **HTML Templates**:

  * `index.html`: Displays the item list and the add-item form.
  * `item.html`: Shows details and edit/delete options for a specific item.

* **Blueprint**:

  * `main_route`: Contains the main routes for managing items.

* **Static Assets**:

  * `static/style.css`: Styles for the application. (not exist).
  * `static/item_details.js`: JavaScript for handling PUT and DELETE operations via Fetch API.

---

## How to Add Items

1. Open the main page (`/`).
2. Enter the name of the item in the form and click "Add Item."

---

## How to Update or Delete Items

1. Click on an item from the list to open its detail page.
2. Use the provided form to update the item’s name.
3. Use the delete button to remove the item.

---

## Development

### Requirements

* Python 3.7+
* Flask

### Debug Mode

To enable Flask debug mode, modify the `run.py` file:

```python
app.run(debug=True)
```

---

## Customization

* **CSS Styling**: Modify `static/style.css` to change the application's appearance.
* **JavaScript Behavior**: Adjust `static/item_details.js` for custom PUT and DELETE handling.

---

## Notes

* For production, consider disabling debug mode and configuring a proper server.

