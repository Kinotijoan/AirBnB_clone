# AirBnB_clone - The console

### project description
This is the initial stage of creating an AirBnB clone web application. It is crucial because the outcome of this project will be used in all subsequent projects such as HTML/CSS templating, database storage, API, and front-end integration. 

### What’s a command interpreter?

A command interpreter, also known as a shell or command-line interpreter, is a program that allows users to interact with the operating system or other software applications using a text-based interface rather than a graphical user interface (GUI). 

In our case, we want to be able to manage the objects of our project:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

## How to start it

#### Installation

First you clone the repository of the project from Github.
```
git clone https://github.com/Kinotijoan/AirBnB_clone.git
cd AirBnB_clone
```

#### How to use it
The command interpreter can work in two modes that is :
1. The interective
2. The Non-interactive

##### Interactive Mode

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```

##### Non-Interactive Mode

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

### Usage

This interpreter has basic console commands such as help, quit, EOF, create, show, destroy, update, all and count.

### Command Snytax and Usage:

| Command | Syntax                                                                                                                      | Output                                                                                                  |
| ------- | --------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| help    | `help [option]`                                                                                                             | Displays all available commands                                                                         |
| quit    | `quit`                                                                                                                      | Exit command interpreter                                                                                |
| EOF     | `EOF`                                                                                                                       | Exit command interpreter                                                                                |
| create  | `create [class_name]` or `[class_name].create()`                                                                            | Creates an instance of class_name                                                                       |
| update  | `update [class_name] [object_id] [update_key] [update_value]` or `[class].update([object_id] [update_key] [update_value]()` | Updates the key:value of class_name.object_id instance                                                  |
| show    | `show [class_name] [object_id]` or `[class_name].show([object_id])()`                                                       | Displays all attributes of class_name.object_id                                                         |
| all     | `all [class_name]`, `[class_name].all()`                                                                                    | Displays every instance of class_name, if used without option displays every instance saved to the file |
| destroy | `destroy [class_name] [object_id]` or `[class_name].destroy([object_id])()`                                                 | Deletes all attributes of class_name.object_id                                                          |
| count   | `count [class_name]` or `[class_name].count()`                                                                              | Counts all the instances with class name specified                                                      |

### Files

| File Name                        | Description                                                                              |
| -------------------------------- | ---------------------------------------------------------------------------------------- |
| `models/base_model.py`           | Base Class with public instance attributes and methods                                   |
| `models/amenity.py`              | An Amenity class that inherits from BaseModel                                            |
| `models/city.py`                 | A City class that inherits from BaseModel                                                |
| `models/place.py`                | A Place class that inherits from BaseModel                                               |
| `models/review.py`               | A Review class that inherits from BaseModel                                              |
| `models/state.py`                | A State class that inherits from BaseModel                                               |
| `models/user.py`                 | A User class that inherits from BaseModel                                                |
| `models/engine/file_storage.py`  | A class that serializes instances to a JSON file and deserializes JSON file to instances |
| `tests/test_models/`             | Unittests for BaseModel, User, amenity, city, place, review, and state                   |
| `tests/test_models/test_engine/` | Unittest for file storage                                                                |

### Example Usage

```python3
Kinoti@pop-os:~/alx/AirBnB_clone$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) create Place
e9672773-b189-4938-93fa-3ee99abd60ca
(hbnb) all Place
["[Place] (e9672773-b189-4938-93fa-3ee99abd60ca) {'id': 'e9672773-b189-4938-93fa-3ee99abd60ca', 'created_at': datetime.datetime(2019, 11, 13, 19, 42, 3, 491688), 'updated_at': datetime.datetime(2019, 11, 13, 19, 42, 3, 491721), '__class__': 'Place'}"]
(hbnb) destroy Place
** instance id missing **
(hbnb) destroy Place e9672773-b189-4938-93fa-3ee99abd60ca
(hbnb) show Place
** instance id missing **
(hbnb) show Place e9672773-b189-4938-93fa-3ee99abd60ca
** no instance found **
(hbnb) quit

```

### Environment

- Language: Python3
- OS: Ubuntu 14.04 LTS
- Style guidelines: [PEP 8 (version 1.7)](https://www.python.org/dev/peps/pep-0008/) \|| [Google Style Python Docstrings](http://sphinxcontrib-napoleon.readthedocs.io/en/l\atest/example_google.html)

### Authors

- Kinoti Joan | [GitHub](https://github.com/Kinotijoan) |

- Melanie Minayo | [GitHub](https://github.com/MinayoMelanie) |
