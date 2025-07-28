from app import app
from models import db, Author, Post

with app.app_context():
    print("Clearing database...")
    db.drop_all()
    db.create_all()

    print("Seeding database...")

    author1 = Author(name="John Doe", phone_number="1234567890")
    author2 = Author(name="Jane Smith", phone_number="0987654321")

    db.session.add_all([author1, author2])
    db.session.commit()

    post1 = Post(
        title="You Won't Believe This Secret",
        content="A" * 300,
        summary="This is a summary.",
        category="Fiction",
        author_id=author1.id,
    )

    post2 = Post(
        title="Top 10 Things You Must Guess",
        content="B" * 400,
        summary="Another valid summary.",
        category="Non-Fiction",
        author_id=author2.id,
    )

    db.session.add_all([post1, post2])
    db.session.commit()

    print("Database seeded!")
