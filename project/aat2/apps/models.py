from werkzeug import generate_password_hash, check_password_hash
from apps import db
from flask_login import UserMixin

# from sqlalchemy.orm import sessionmaker, db.relationship, db.backref


user_proj = db.Table(
    "user_proj",
    db.metadata,
    db.Column("user_id", db.Integer, db.ForeignKey("users.id")),
    db.Column("project_id", db.Integer, db.ForeignKey("projects.id")),
)


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    pwdhash = db.Column(db.String(54))

    projects = db.relationship(
        "Project",
        backref="users",
        secondary=user_proj
    )

    def __init__(self, email, password, projects):
        pro = Project.query.filter_by(id=projects).first()
        self.projects.append(pro)
        self.email = email.lower()
        self.set_password(password)
        print("done creation of user")

    def set_password(self, password):
        self.pwdhash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pwdhash, password)

    @staticmethod
    def get_projects(user_id):
        projs = User.query.filter_by(id=user_id).first().projects
        return dict([(p.id, p.name) for p in projs])


class Project(db.Model):
    __tablename__ = "projects"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    desc = db.Column(db.String(500))
    testcases = db.relationship('TestCases', backref='projects',
                                lazy='dynamic')
    apis = db.relationship('ApiRequests',
                           backref='projects',
                           lazy='dynamic')

    def __init__(self, name, desc=""):
        self.name = name
        self.desc = desc

    def get_id(name):
        return self.query.filter_by(name=name).first()


class TestCases(db.Model):
    __tablename__ = "testcases"
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
    # req_api_id = db.Column(db.Integer, db.ForeignKey('request.id'))

########################


class Headers(db.Model):
    __tablename__ = 'headers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    value = db.Column(db.String)
    request_id = db.Column(db.Integer, db.ForeignKey('request.id'))
    request = db.relationship("ApiRequests", backref="headers")


class Cookies(db.Model):
    __tablename__ = "cookies"
    id = db.Column(db.Integer, primary_key=True)
    request_id = db.Column(db.Integer, db.ForeignKey('request.id'))
    request = db.relationship("ApiRequests", backref="cookies")
    name = db.Column(db.String)
    value = db.Column(db.String)
    expires = db.Column(db.String)
    httpOnly = db.Column(db.Boolean)
    secure = db.Column(db.Boolean)

    def __init__(self, data, req):
        for d in data:
            setattr(self, d, data[d])
        self.request = req


class Params(db.Model):
    __tablename__ = "params"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String)
    value = db.Column(db.String)
    postData_id = db.Column(db.Integer, db.ForeignKey('postData.id'))


class PostData(db.Model):
    __tablename__ = "postData"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    mimeType = db.Column(db.String)
    text = db.Column(db.String)
    params = db.relationship("Params",
                             backref="postData",
                             cascade="all,delete,delete-orphan")


class QueryString(db.Model):
    __tablename__ = "queryString"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    value = db.Column(db.String)
    request_id = db.Column(db.Integer, db.ForeignKey('request.id'))


class ApiRequests(db.Model):
    __tablename__ = "request"
    id = db.Column(db.Integer, primary_key=True)
    flag_used = db.Column(db.Boolean, default=False)
    method = db.Column(db.String)
    url = db.Column(db.String)
    httpVersion = db.Column(db.String)
    # headers_id = db.Column(db.Integer, db.ForeignKey('headers.id'))
    # headers = db.relationship("Headers", backref="request",
    #                           cascade="all,delete,delete-orphan")
    postData_id = db.Column(db.Integer, db.ForeignKey('postData.id'))
    postData = db.relationship("PostData",
                               backref=db.backref("request",
                                                  uselist=False),
                               cascade="all,delete")
    queryString = db.relationship("QueryString", backref="request",
                                  cascade="all,delete,delete-orphan")
    # cookies = db.relationship("Cookies", backref="request", lazy='dynamic',
    #                           cascade="all,delete,delete-orphan")
    responses_id = db.Column(db.Integer, db.ForeignKey('response.id'))
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
    response = db.relationship("ApiResponse",
                               backref=db.backref("request", uselist=False))

    testcases_id = db.Column(db.Integer, db.ForeignKey('testcases.id'))
    testcases = db.relationship("TestCases", backref="request",
                                cascade="all,delete")

    def update_attribs(self, kwargs):
        # all those keys will be initialized as class attributes
        allowed_keys = set(['method', 'url', 'headers'])
        # initialize all allowed keys to false
        # self.__dict__.update((key, False) for key in allowed_keys)
        # and update the given keys by their given values
        self.__dict__.update((key, value)
                             for key, value in kwargs.items()
                             if key in allowed_keys)

    def add_cookies(self, cookie):
        self.cookies.append(cookie)

    def get_free_apis(self, project):
        apis = self.query.filter_by(flag_used=False) \
                   .filter_by(project_id=project) \
                   .options(db.load_only('id', "url"))
        return apis


class RespHeaders(db.Model):
    __tablename__ = 'resp_headers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    value = db.Column(db.String)
    response_id = db.Column(db.Integer, db.ForeignKey('response.id'))
    # response = db.relationship("ApiResponse", backref="resp_headers")

    def __init__(self, data, req):
        for d in data:
            setattr(self, d, data[d])
        self.response = req


class RespCookies(db.Model):
    __tablename__ = "resp_cookies"
    id = db.Column(db.Integer, primary_key=True)
    response_id = db.Column(db.Integer, db.ForeignKey('response.id'))
    name = db.Column(db.String)
    value = db.Column(db.String)
    path = db.Column(db.String)
    expires = db.Column(db.String)
    httpOnly = db.Column(db.Boolean)
    secure = db.Column(db.Boolean)

    def __init__(self, data, req):
        for d in data:
            setattr(self, d, data[d])
        self.response = req


class Content(db.Model):
    __tablename__ = "content"

    id = db.Column(db.Integer, primary_key=True)
    # response_id = db.Column(db.Integer, db.ForeignKey('response.id'))
    size = db.Column(db.Integer)
    mimeType = db.Column(db.String)
    compression = db.Column(db.Integer)
    text = db.Column(db.String)
    encoding = db.Column(db.String)

    def __init__(self, data):
        for d in data:
            setattr(self, d, data[d])
        # self.response = req


class ApiResponse(db.Model):
    __tablename__ = "response"
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String)
    statusText = db.Column(db.String)
    httpVersion = db.Column(db.String)
    # request_id = db.Column(db.Integer, db.ForeignKey('request.id'))
    headers = db.relationship("RespHeaders", backref="response",
                              cascade="all,delete,delete-orphan")
    cookies = db.relationship("RespCookies", backref="response",
                              cascade="all,delete,delete-orphan")
    content_id = db.Column(db.Integer, db.ForeignKey('content.id'))
    content = db.relationship("Content",
                              backref=db.backref("response", uselist=False))


def main():
    req = ApiRequests()
    print(req.get_free_apis())


if __name__ == '__main__':
    main()
