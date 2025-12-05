# Expense Management System

A simple and efficient application to track, analyze, and manage daily expenses.  
It allows users to add and update expenses, view category-wise trends, and analyze monthly spending patterns through a clean and interactive interface.

## 📌 Overview

The Expense Management System helps users stay in control of their finances by providing a structured way to record and analyze expenses.  
It includes three major views:

- **Tab 1:** Add and update daily expenses  
- **Tab 2:** View expense breakdown by categories like rent, shopping, travel, entertainment and more  
- **Tab 3:** View month-wise financial trends to understand spending habits over time  

The goal of the project is to make personal finance tracking simple, fast, and visually clear.

## 🛠️ Tech Stack

| Layer      | Tool        |
|------------|-------------|
| Frontend   | Streamlit   |
| Backend    | FastAPI     |
| Database   | MySQL       |
| Visualization | pandas, matplotlib |

## 📂 Project Structure

<img src="assets/Project_Architecture.png" alt="Expense Tracking System Architecture" width="800">

##  Setup Instructions

### 1. Clone the Repository

```bash
https://github.com/itsmoksh/Expense-Management-System.git
cd project_expense_management
```

### 2. Create Virtual Environment & Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Setup MySQL Database

- Create a database named `expense_db` (or your choice).
- Create the `expenses` table:

```sql
CREATE TABLE expenses (
  id INT AUTO_INCREMENT PRIMARY KEY,
  expense_date DATE,
  amount DECIMAL(10,2),
  category VARCHAR(50),
  notes TEXT
);
```
- Update your MySQL credentials in `db_helper.py`

---

##  Running the Project

### 1. Start FastAPI Backend

```bash
cd Backend
uvicorn server:app --reload
```

### 2. Start Streamlit Frontend

```bash
cd ../Frontend
streamlit run app.py
```

---

##  Dashboard Preview

- Form: quick add/update of daily expenses

- Table: total and percentage share by category

- Bar chart: category-wise expense breakdown

- Bar chart: month-wise spending overview

- Summary: clear monthly and category totals

---

##  TODO / Future Improvements

- Add user authentication
- Export filtered data as CSV/Excel
---

##  Author

**Virat Singh Chauhan**  
 [LinkedIn](https://www.linkedin.com/in/virats02/)  
 [GitHub](https://github.com/DsVirat)

---

##  License

MIT License – free to use and modify.