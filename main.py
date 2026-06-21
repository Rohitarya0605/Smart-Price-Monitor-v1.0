from fastapi import FastAPI, Request, Form, Cookie
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from jose import jwt, JWTError

from database import Base, engine, SessionLocal
from models import Product, PriceHistory, User
from auth import hash_password, verify_password, create_access_token

# =========================
# DATABASE
# =========================
Base.metadata.create_all(bind=engine)

# =========================
# APP SETUP
# =========================
app = FastAPI()

SECRET_KEY = "my_super_secret_key_123"
ALGORITHM = "HS256"

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


# =========================
# AUTH ROUTES
# =========================
@app.get("/signup")
def signup_page(request: Request):
    return templates.TemplateResponse(
        "signup.html",
        {"request": request}
    )


@app.post("/signup")
def signup(
    username: str = Form(...),
    password: str = Form(...)
):
    db = SessionLocal()

    existing_user = db.query(User).filter(
        User.username == username
    ).first()

    if existing_user:
        db.close()
        return RedirectResponse("/signup", status_code=303)

    new_user = User(
        username=username,
        hashed_password=hash_password(password)
    )

    db.add(new_user)
    db.commit()
    db.close()

    return RedirectResponse("/login", status_code=303)


@app.get("/login")
def login_page(request: Request):
    return templates.TemplateResponse(
        "login.html",
        {"request": request}
    )


@app.post("/login")
def login(
    username: str = Form(...),
    password: str = Form(...)
):
    db = SessionLocal()

    user = db.query(User).filter(
        User.username == username
    ).first()

    if not user:
        db.close()
        return RedirectResponse("/login", status_code=303)

    if not verify_password(password, user.hashed_password):
        db.close()
        return RedirectResponse("/login", status_code=303)

    token = create_access_token({"sub": username})

    response = RedirectResponse("/", status_code=303)

    response.set_cookie(
        key="access_token",
        value=token,
        httponly=True
    )

    db.close()
    return response


@app.get("/logout")
def logout():
    response = RedirectResponse("/login", status_code=303)
    response.delete_cookie("access_token")
    return response


# =========================
# HOME DASHBOARD
# =========================
@app.get("/")
def home(
    request: Request,
    access_token: str = Cookie(None)
):
    if not access_token:
        return RedirectResponse("/login", status_code=303)

    try:
        jwt.decode(
            access_token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
    except JWTError:
        return RedirectResponse("/login", status_code=303)

    db = SessionLocal()

    products = db.query(Product).all()
    history = db.query(PriceHistory).all()

    response = templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "products": products,
            "history": history
        }
    )

    db.close()
    return response


# =========================
# ADD PRODUCT
# =========================
@app.post("/add-product")
def add_product(
    product_name: str = Form(...),
    your_price: float = Form(...),
    amazon_price: float = Form(...),
    flipkart_price: float = Form(...)
):
    db = SessionLocal()

    product = Product(
        product_name=product_name,
        your_price=your_price,
        amazon_price=amazon_price,
        flipkart_price=flipkart_price
    )

    db.add(product)
    db.commit()
    db.refresh(product)

    history = PriceHistory(
        product_id=product.id,
        day="Day 1",
        your_price=your_price,
        amazon_price=amazon_price,
        flipkart_price=flipkart_price
    )

    db.add(history)
    db.commit()
    db.close()

    return RedirectResponse("/", status_code=303)


# =========================
# DELETE PRODUCT
# =========================
@app.post("/delete-product/{product_id}")
def delete_product(product_id: int):
    db = SessionLocal()

    product = db.query(Product).filter(
        Product.id == product_id
    ).first()

    if product:
        db.delete(product)
        db.commit()

    db.close()
    return RedirectResponse("/", status_code=303)


# =========================
# EDIT PAGE
# =========================
@app.get("/edit-product/{product_id}")
def edit_product_page(request: Request, product_id: int):
    db = SessionLocal()

    product = db.query(Product).filter(
        Product.id == product_id
    ).first()

    response = templates.TemplateResponse(
        "edit.html",
        {
            "request": request,
            "product": product
        }
    )

    db.close()
    return response


# =========================
# UPDATE PRODUCT
# =========================
@app.post("/update-product/{product_id}")
def update_product(
    product_id: int,
    product_name: str = Form(...),
    your_price: float = Form(...),
    amazon_price: float = Form(...),
    flipkart_price: float = Form(...)
):
    db = SessionLocal()

    product = db.query(Product).filter(
        Product.id == product_id
    ).first()

    if product:
        product.product_name = product_name
        product.your_price = your_price
        product.amazon_price = amazon_price
        product.flipkart_price = flipkart_price

        db.commit()

        history_count = db.query(PriceHistory).filter(
            PriceHistory.product_id == product_id
        ).count()

        new_history = PriceHistory(
            product_id=product_id,
            day=f"Day {history_count + 1}",
            your_price=your_price,
            amazon_price=amazon_price,
            flipkart_price=flipkart_price
        )

        db.add(new_history)
        db.commit()

    db.close()
    return RedirectResponse("/", status_code=303)