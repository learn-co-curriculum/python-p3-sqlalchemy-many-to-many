# Many-to-Many Relationships

## Learning Goals

- Use SQLAlchemy to join tables with one-to-one, one-to-many, and
  many-to-many relationships.

***

## Introduction

In the previous lesson, we saw how to create a **one-to-many** association
between two models using SQLAlchemy by following certain naming conventions,
use of the `relationship()` and `backref()` methods, and using the right
foreign key on our tables when generating the migrations.

In the SQL section, we learned about one other kind of relationship: the
**many-to-many**, also known as the **has many through**, relationship. For
instance, in a domain where a **cat** has many **owners** and an **owner** can
also have many **cats**, we needed to create another table to join between those
two tables:

![Pets Database ERD](https://curriculum-content.s3.amazonaws.com/phase-3/sql-table-relations-creating-join-tables/cats-cat_owners-owners.png)

In this lesson, we'll learn how to create a **many-to-many** relationship in
SQLAlchemy. We'll continue working on our games and reviews domain, but this
time we'll add a third model into the mix: a users model. We'll be setting up
these relationships:

- A game **has many** reviews
- A game **has many** users, **through** reviews
- A review **belongs to** a game
- A review **belongs to** a user
- A user **has many** reviews
- A user **has many** games, **through** reviews

Once we're done setting up the database tables, here's what the ERD will look like:

![Game Reviews ERD](https://curriculum-content.s3.amazonaws.com/phase-3/active-record-associations-many-to-many/games-reviews-users-erd.png)

To get started, run `pipenv install` and `pipenv shell`, then follow along with
the code.

***

## Creating a Join Table

Right now, we've got code for the `Game` model (and the `games` table), along
with the code for the `Review` model (and the `reviews` table) from the previous
lesson.

To start, let's add the code we'll need for the `User` model as well. Let's
create the `users` table with a `name` column and timestamps:

```py
# app/db.py

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    created_at = Column(DateTime(), default=func.now())
    updated_at = Column(DateTime(), onupdate=func.now())

    # don't forget your __repr__!
    def __repr__(self):
        return f'User(id={self.id}, ' + \
            f'name={self.name})'
```

We'll also need to modify the `reviews` table and add a foreign key to refer to
our `users` table. Remember, each review now **belongs to** a specific user. Any
time we create a **belongs to** relationship, we need a foreign key to establish
this relationship:

```py
# app/db.py

# User model
    reviews = relationship('Review', backref=backref('user'))
```

Let's also edit the `Review` model to add our new foreign key:

```py
# app/db.py

# Review model
    user_id = Column(Integer(), ForeignKey('users.id'))
```

Now run `alembic revision --autogenerate -m'Add User model'` from the
`many-to-many` directory to make our migration. If all goes well, run
`alembic upgrade head` to push your migrations to the database.

```console
$ alembic upgrade head
# => INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
# => INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
# => INFO  [alembic.runtime.migration] Running upgrade  -> 9e396fc70825, Add User model
```

Run the seed file as well to populate the `games` and `reviews` tables:

```console
$ python app/seed.py
```

***

## Lesson Section

Lorem ipsum dolor sit amet. Ut velit fugit et porro voluptas quia sequi quo
libero autem qui similique placeat eum velit autem aut repellendus quia. Et
Quis magni ut fugit obcaecati in expedita fugiat est iste rerum qui ipsam
ducimus et quaerat maxime sit eaque minus. Est molestias voluptatem et nostrum
recusandae qui incidunt Quis 33 ipsum perferendis sed similique architecto.

```py
# python code block
print("statement")
# => statement
```

```js
// javascript code block
console.log("use these for comparisons between languages.")
// => use these for comparisons between languages.
```

```console
echo "bash/zshell statement"
# => bash/zshell statement
```

<details>
  <summary>
    <em>Check for understanding text goes here! <code>Code statements go here.</code></em>
  </summary>

  <h3>Answer.</h3>
  <p>Elaboration on answer.</p>
</details>
<br/>

***

## Instructions

This is a **test-driven lab**. Run `pipenv install` to create your virtual
environment and `pipenv shell` to enter the virtual environment. Then run
`pytest -x` to run your tests. Use these instructions and `pytest`'s error
messages to complete your work in the `lib/` folder.

Instructions begin here:

- Make sure to specify any class, method, variable, module, package names
  that `pytest` will check for.
- Any other instructions go here.

Once all of your tests are passing, commit and push your work using `git` to
submit.

***

## Conclusion

Conclusion summary paragraph. Include common misconceptions and what students
will be able to do moving forward.

***

## Resources

- [Python 3.8.13 Documentation](https://docs.python.org/3/)
- [SQLAlchemy ORM Documentation](https://docs.sqlalchemy.org/en/14/orm/)
- [Alembic 1.8.1 Documentation](https://alembic.sqlalchemy.org/en/latest/)
- [Basic Relationship Patterns - SQLAlchemy](https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html)
