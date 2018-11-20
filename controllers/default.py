
def register():
    return dict()

def store():
    submitted_firstname = request.vars.firstname
    submitted_lastname = request.vars.lastname
    submitted_email = request.vars.email
    submitted_password = request.vars.password

    results = db.users.insert(
        firstname=submitted_firstname,
        lastname=submitted_lastname,
        email=submitted_email,
        password=submitted_password
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

    if db(db.users.email==submitted_email
            and db.users.password==submitted_password).count()>0:
        return "User Logged in Successfully"

    else:
        return "User Not found. Please Sign up"


def update():
    submitted_firstname = request.vars.firstname
    submitted_lastname = request.vars.lastname
    submitted_password = request.vars.password
    submitted_id = request.vars.id

    if db(db.users.id == submitted_id).select():

        db(db.users.id == submitted_id).update(
            firstname=submitted_firstname,
            lastname=submitted_lastname,
            password=submitted_password
            )
        return 'User Updated Successfully'

    else:
        return 'No User With the ID found'


def edit():
    parameters = request.args
    submitted_id=parameters[0]
    user=db(db.users.id==submitted_id).select()[0]
    return dict(user=user)



def delete():
    parameters = request.args
    submitted_id = parameters[0]

    if db(db.users.id ==submitted_id).select():

        db(db.users.id == submitted_id).delete()
        return 'User Deleted Successfully'

    else:
        return 'No User With the ID found'