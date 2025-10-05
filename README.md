
# Student Application API Documentation

## Setup and Execution

### Prerequisites
**Python** and **Flask** library.

Install Flask using:
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
| `ID`         | Unique Identifier (Auto-generated) | Integer  | `1`                |
| `Name`       | Student's full name                | String   | `"Yashikha J"`     |
| `Roll_no`    | Student's roll number (from `r_n`) | String   | `"062"`            |
| `Department` | Department name (from `Dept`)      | String   | `"CSE"`            |
| `Section`    | Section (from `Sec`)               | String   | `"A"`              |
| `Intrests`   | Student interests (from `Intr`)    | String   | `"Backend"` |

---


| **Route**                   | **Method** | **Description**                       | **Request Body** | **Success Status** | **Error Status**  |
| --------------------------- | ---------- | ------------------------------------- | ---------------- | ------------------ | ----------------- |
| `/`                         | `GET`      | Health check / API status             | None             | `200 OK`           | -                 |
| `/apply`                    | `POST`     | **Create** a new application          | JSON (see below) | `201 Created`      | `400 Bad Request` |
| `/application`              | `GET`      | **Read** all applications             | None             | `200 OK`           | -                 |
| `/application/<int:stu_id>` | `GET`      | **Read** a specific application by ID | None             | `200 OK`           | `404 Not Found`   |
| `/application/<int:stu_id>` | `DELETE`   | **Delete** an application by ID       | None             | `200 OK`           | `404 Not Found`   |

---

## Example POST Request

### **Endpoint**

`POST /apply`

### **Request Body**

```json
{
    "Name": "",
    "r_n": "CS2025",
    "Dept": "Computer Science",
    "Sec": "B",
    "Intr": "AI, Robotics"
}
```

