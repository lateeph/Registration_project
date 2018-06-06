
def register():
    return dict()

def store():
    submitted_firstname = request.vars.firstname
    submitted_lastname = request.vars.lastname
    submitted_email = request.vars.email
    submitted_password = request.vars.password

    results = db.users.insert(
        db_firstname=submitted_firstname,
        db_lastname=submitted_lastname,
        db_email=submitted_email,
        db_password=submitted_password
    )

    if results:
        return "User Saved Successfully"
    else:
        return "An Error Occurred"

def seeUsers():
    users=db().select(db.users.ALL)
    return dict(users=users)

def login():
    return dict()

def authenticate():
    submitted_email = request.vars.email
    submitted_password = request.vars.password

    if db(db.users.db_email==submitted_email
            and db.users.db_password==submitted_password).count()>0:
        return "User Logged in Successfully"

    else:
        return "User Not found. Please Sign up"