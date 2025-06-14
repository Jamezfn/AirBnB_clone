# README.md

## Project Description

AirBnB\_clone is a command-line application that mimics a simplified version of Airbnb's core features. It allows users to create, view, update, and delete instances of different classes (e.g., User, Place, State, City, Amenity, Review) via an interactive console. The project helps reinforce understanding of object-oriented programming, data serialization, and CLI design in Python.

## Command Interpreter Description

The console (`console.py`) provides an interactive prompt `(hbnb)` where you can manage model instances. It uses Python's `cmd` module and connects to the storage engine (file storage or database storage) to persist data.

### How to Start

1. Ensure you have Python 3 installed (recommend 3.7+).
2. Clone the repository:

   ```bash
   git clone https://github.com/<your_org>/AirBnB_clone.git
   cd AirBnB_clone
   ```
3. (Optional) Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/macOS
   # venv\Scripts\activate  # Windows
   pip install -r requirements.txt  # if requirements.txt exists
   ```
4. Run the console:

   ```bash
   python3 console.py
   ```
5. You should see the prompt:

   ```
   (hbnb)
   ```

### How to Use

At the `(hbnb)` prompt, type commands to interact with objects. Available commands:

* `create <ClassName>`: Create a new instance of `ClassName`. Prints the new instance's `id`.
* `show <ClassName> <id>`: Display the string representation of an instance.
* `destroy <ClassName> <id>`: Delete an instance based on the class name and `id`.
* `all [ClassName]`: Display string representations of all instances, or all instances of `ClassName` if provided.
* `update <ClassName> <id> <attribute_name> "<value>"`: Update or add attribute to an instance.
* `count <ClassName>`: Count and display the number of instances of `ClassName`.
* `help [command]`: Show help on a specific command or list all commands.
* `quit` or `EOF`: Exit the console.

Note: ClassName must be one of the defined model classes in the project (e.g., `User`, `Place`, etc.).

### Examples

1. **Create a User**

   ```
   (hbnb) create User
   1234-abcd-5678-efgh
   ```
2. **Show the User**

   ```
   (hbnb) show User 1234-abcd-5678-efgh
   [User] (1234-abcd-5678-efgh) { ... }
   ```
3. **Update the User's email**

   ```
   (hbnb) update User 1234-abcd-5678-efgh email "user@example.com"
   ```
4. **Create a Place**

   ```
   (hbnb) create Place
   abcd-1234-efgh-5678
   ```
5. **List all instances**

   ```
   (hbnb) all
   [[User] (1234-abcd-5678-efgh) {...}, [Place] (abcd-1234-efgh-5678) {...}, ...]
   ```
6. **Count instances**

   ```
   (hbnb) count User
   1
   ```
7. **Destroy an instance**

   ```
   (hbnb) destroy User 1234-abcd-5678-efgh
   ```

### Storage

The console interacts with the storage engine defined in the project (e.g., `FileStorage` by default). When you run commands like `create`, `update`, or `destroy`, changes are saved automatically to the storage file (e.g., `file.json`) or database.

### Branches & Pull Requests

To organize work as a team:
OAOAOA
1. **Use Feature Branches**: Create a new branch for each feature or bugfix:

   ```bash
   git checkout -b feature/<short-description>
OAOAOA   ```
2. **Commit Often**: Make small, focused commits with clear messages.
3. **Push Branch & Open Pull Request**:

   ```bash
   git push origin feature/<short-description>
   ```

   Then open a pull request on GitHub.
4. **Code Review**: Team members review the PR, suggest changes, and approve.
5. **Merge**: After approval, merge into `main` (or `master`) with GitHub's merge tools.
6. **Keep Branches Updated**: Regularly pull from `main` into your branch to avoid conflicts.

This workflow ensures collaboration and code quality.

---

## AUTHORS

See the `AUTHORS` file at the root for a list of contributors and instructions on how to update it.

