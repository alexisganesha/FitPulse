> python -m venv .venv
> .venv\Scripts\Activate.ps1
> deactivate
> .venv\Scripts\Activate.ps1
> pip install -r requirements.txt



> Dans SQL create table users
CREATE TABLE users(
	id SERIAL PRIMARY KEY,
	email VARCHAR(255) NOT NULL,
	last_name VARCHAR(100),
	role VARCHAR(50)
)

SELECT * FROM users