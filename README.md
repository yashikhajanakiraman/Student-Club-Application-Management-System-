
# Student Application API Documentation

## Setup and Execution

### Prerequisites
**Python** and **Flask** library.

Install Flask  
```bash
pip install Flask
````

---

### Running the Application

Run the application from your terminal:

```bash
python stu_data.py
```

The server will start at:
**[http://127.0.0.1:5000/](http://127.0.0.1:5000/)**

---

All application records are stored as **JSON objects** with the following structure:

| **Key**      | **Description**                    | **Type** | **Example**        |
| ------------ | ---------------------------------- | -------- | ------------------ |
| `ID`         | Auto-Generated Unique number       | Integer  | `1`                |
| `Name`       | Student's full name                | String   | `"Yashikha J"`     |
| `Roll_no`    | Student's roll number              | String   | `"62"`             |
| `Department` | Student's Department name          | String   | `"CSE"`            |
| `Section`    | Student's Section                  | String   | `"F"`              |
| `Intrests`   | Student's interests                | String   | `"Backend"`        |

---
These are the all the endpoints

| **Route**                   | **Method** | **Description**                       | **Request Body** | **Success Status** | **Error Status**  |
| --------------------------- | ---------- | ------------------------------------- | ---------------- | ------------------ | ----------------- |
| `/`                         | `GET`      | To check if application is working             | None             | `200 OK`           | -                 |
| `/apply`                    | `POST`     | **Creates** a new application          | JSON (see below) | `201 Created`      | `400 Bad Request` |
| `/application`              | `GET`      | **Reads** all applications             | None             | `200 OK`           | -                 |
| `/application/<int:stu_id>` | `GET`      | **Reads** a specific application using its ID | None             | `200 OK`           | `404 Not Found`   |
| `/application/<int:stu_id>` | `DELETE`   | **Deletes** an application using its ID       | None             | `200 OK`           | `404 Not Found`   |

---

## Example POST Request

### **Endpoint**

`POST /apply`

### **Request Body**

```json
{
    "Name": "Yashikha J",
    "r_n": 062,
    "Dept": "Computer Science",
    "Sec": "F",
    "Intr": "Backend"
}
```
#### Additional Notes 
The syntax of this application is very similar to the syntax of creating a binary file in python.
To test this code I used Postman.I installed it from Chrome.
