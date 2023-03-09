# 💻 Application Overview


## Data model

The application contains the following core features:

- USERS - have these roles:
  #### Notable Features:
  - `MASTER` - can:
    - ✅ Master have signup, login & logout
    - ✅ Master can view the total no of tasks, submitted, correct & wrong tasks, student lists in dashboard
    - ✅ Master can create an arithmetic task can assign to the students in create task page.
    - ✅ Master can view the task submitted by the students &can evaluate these tasks.
    - ✅ Master can view their own profile.
    - ✅ There was a dark mode in all pages.

  - `Student` - can:
    - ✅ Student have signup, login & logout
    - ✅ Student can view the total no of tasks, solved & unsolved tasks dashboard
    - ✅ Student can view the task assigned by the master & can solve these tasks.
    - ✅ Student can view the tasks solved by them in their solved tasks page.
    - ✅ Student can view their own profile.
    - ✅ There was a dark mode in all pages.
     
## Get Started

Prerequisites:

- Python v3.10.4
- Django v4.1.5
- HTML 5
- Css
- Java script

To set up the app execute the following guide.

### Setup, Installation and Run

To run the app on your local machine, you need Python 3+, installed on your computer. Follow all the steps to run this project.

1.  Create virtual environment:
```bash
virtualenv env
```
2.  Activate virtual environment:
```bash
On Linux - source env/bin/activate
On Windows - env/Scripts/activate
```
3. Firstly you need to clone or download my project from gitlab repositories:
```bash
git clone https://gitlab.com/Prempgk/next_growth_task.git
```

4. Then enter the corresponding directory:
```bash
cd Task2
```
5. Install dependencies
```bash
  pip install -r requirements.txt
``` 

6. Run local server, and DONE!
```python
  python manage.py runserver
  Linux or Mac - python3 manage.py runserver
```
7.  App in the development mode.\
Open [http://127.0.0.1:8000](http://127.0.0.1:8000) to view it in the browser.

