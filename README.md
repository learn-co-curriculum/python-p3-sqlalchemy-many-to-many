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

- [Resource 1](https://www.python.org/doc/essays/blurb/)
- [Reused Resource][reused resource]

[reused resource]: https://docs.python.org/3/
