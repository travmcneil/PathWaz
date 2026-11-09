idea for a new application named PathWaz. 
1. you input you starting destination and ending destination
2. The app will connect to multiple apis like flights and busses and trains and google maps. to return a list of all you options on how to get to your destination with prices for each.
3. it will also so how long it will take using each form of transportation
4. it will mix and match different form of transportations to find the method that will be the fastes with the cheapest.
5. it will show a graph with with two lines showing time and prices
6. i want to add ai into it so that all you have to do is say things like "i am willing to drive 6 hours a day" or "i have only $300" or "i have to be 
7. i want to use FastApi, PostgreSQL, and a React front end

# PathWaz API

Multimodal trip planning backend: flights, buses, trains, and driving, ranked by time vs. price.

**Stack:** FastAPI · PostgreSQL · SQLAlchemy 2.0 (async) · Alembic · Pydantic v2

**To Start:**  uvicorn app.main:app --reload