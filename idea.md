# Models Architecture:

## User:

- first_name (charfield)
- last_name (charfield)
- email (emailfield)
- password (passwordfield)
- photo (imagefield)
- gender (charfield(choices))
- date of birth (datefield)
- address (charfield)
- contact informaition (integerfield)

---

## Instructor:
---

### InstructorDetails:

- user (onetoonefield)
- degree (charfield (choices))
- vacancy (charfield choices)
- shortbio (textfield)
- course (onetomanyfield)
- reviews (? (ratingfield))

---

## Student:
---

### StudentProfile:

- user(ontoonefield)
- enrolled_courses(manytomanyfield)
---

## Courses:
---

### Course Details:

- title (charfield)
- category (charfield(choice))
- instructor (onetomanyfield)
- description (textfield)

### Course Module:

- name = (charfield)
- order_number = (integerfield)
- course = (foriegnkey)

### Lesson:

- link (urlfield)
- type (choice)
- order_number = (integerfield)
- course_module = (manytomanyfield)





## apps

- users
- courses
- instructors
- students





- User
    - Apna kch b ni
    - Ye inherit kr rha ha AbstractUser se

- AbstractUser
    - username, email, first_name, last_name  etc 
    - PermissionsMixin , is_superuser

- PermissionsMixin
    - Provides functionality for using django builtin permissions

- AbstractBaseUser
    - Basic Authentication