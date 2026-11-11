# Module 10 Assignment Reflection

In this assignment, I learned more about user authentication, password hashing, database testing, and CI/CD.

The most difficult part for me was fixing dependency and version problems. At first, some tests failed because of database issues. Later, I also had problems with Python versions and different package requirements. I spent quite a lot of time checking the error messages and fixing them one by one.

Another challenge was the Docker security scan. GitHub Actions failed several times because some packages had security vulnerabilities. After updating the dependencies and Dockerfile, I finally got all three jobs to pass.

I also learned why storing hashed passwords is important and how GitHub Actions can automatically test and deploy an application.

Overall, this assignment took more time than I expected, but I learned a lot from solving these problems.