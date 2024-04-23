from fastapi import FastAPI, HTTPException, Form
from pydantic import BaseModel, EmailStr

app = FastAPI()

# Pydantic model to represent portfolio details
class Portfolio(BaseModel):
    id: int
    title: str
    description: str

# In-memory 'database' for the example
portfolio_items = [
    {"id": 1, "title": "Personal Portfolio Website", "description": "A website to showcase my projects and skills."},
    {"id": 2, "title": "React To Do App", "description": "A todo list application built with React for learning purposes."},
]

# Route to get portfolio items
@app.get("/portfolio/")
async def get_portfolio():
    return portfolio_items

# Pydantic model for contact form submissions
class ContactForm(BaseModel):
    name: str
    email: EmailStr
    message: str

# Route to handle contact form submissions
@app.post("/contact/")
async def submit_contact_form(contact: ContactForm):
    return {"message": "Contact form submitted successfully."}
