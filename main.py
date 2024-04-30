from fastapi import FastAPI, HTTPException, Form
from pydantic import BaseModel, EmailStr
import json

app = FastAPI()

def load_data(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []  

def save_data(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


class Portfolio(BaseModel):
    id: int
    title: str
    description: str


portfolio_items = load_data("portfolio_items.json")
if not portfolio_items: 
    portfolio_items = [
        {"id": 1, "title": "Personal Portfolio Website", "description": "A website to showcase my projects and skills."},
        {"id": 2, "title": "React To Do App", "description": "A todo list application built with React for learning purposes."},
    ]
    save_data(portfolio_items, "portfolio_items.json")

@app.get("/portfolio/")
async def get_portfolio():
    return portfolio_items

class ContactForm(BaseModel):
    name: str
    email: EmailStr
    message: str

@app.put("/portfolio/{item_id}")
async def update_portfolio_item(item_id: int, item: Portfolio):
    items = load_data("portfolio_items.json")
    for i in range(len(items)):
        if items[i]["id"] == item_id:
            items[i] = item.dict()
            save_data(items, "portfolio_items.json")
            return {"message": "Portfolio item updated successfully."}
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/contact/")
async def submit_contact_form(contact: ContactForm):
    contacts = load_data("contact_submissions.json")
    contact_data = contact.dict()
    contacts.append(contact_data)
    save_data(contacts, "contact_submissions.json")
    return {"message": "Contact form submitted successfully."}
