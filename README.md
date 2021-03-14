# Python-flask
Sample implementation of DDD based flask api

## Introduction
This is an example I wanted to implement just to share my idea of what a Domain Driven Design implementation with Python (flask) would be. 

This is still a work in progress project. 

The main concepts demonstrated in this repository are:
- Domain Driven Design [https://martinfowler.com/tags/domain%20driven%20design.html]
- Flask framework (used for Api implementation)
- Basic api implementation (CRUD implementation for users/planets)
- ORM usage (SQLQlchemy)
- Security Token authorization implementation 
- Email notification implementation


## How to use?
- Clone / download the repository 
- install requirements (pip install requirements.txt)
- Run the api using (flask run) command. 
- Enjoy !!

## Endpoints
| URL | body | response |
| --- | ---- | -------- |
| POST /api/v1/users | form body | 201/400/409
| PUT /update_user | form body | 200/404
| DELETE /removeuser?id={id} | Id | 200/404 | 

## Domain models
### User
| Field | Type | Description |
| ----- | ---- | ----------- |
|id | integer | Unique identifier of a user (this corresponds to the primary key in the db) |
| first_name | string | First name of the user |
| last_name | string | Last name of the user |
| email | string | User's email address |
| password | string | User's password |

### Planet

| Field | Type | Description |
| ----- | ---- | ----------- |
| planet_id | integer | Unique identifier of a planet (this corresponds to the primary key in the db) |
| planet_name | string | Planet's name |
| planet_type | string | Planet's type |
| home_star | string | Star that the planet rotates around |
| mass | float | the value of the planet's mass |
| radius | float | the value of the planet's radius |
| distance | float | the value of the planet's dsitance from the earth |

## Updates to come:
- Update the routes to make them restful compliant
- Implement Patch endoint 
- Apply authorization for all the endpoints (make the bearer authorization token mandatory)
- Add swagger documentation
- Integrate proxies
- Add api management 
- Please send me any idea you have to improve this little API
