from airflow.utils.session import create_session
from airflow.www.fab_security.manager import AUTH_DB
from airflow.www.app import create_app

def create_admin_user():
    app = create_app()
    appbuilder = app.appbuilder
    sm = appbuilder.sm  # SecurityManager

    username = "admin"
    email = "admin@example.com"
    password = "admin"
    role = sm.find_role("Admin")

    existing_user = sm.find_user(username=username)
    if existing_user:
        print(f"User '{username}' already exists.")
    else:
        sm.add_user(
            username=username,
            first_name="Admin",
            last_name="User",
            email=email,
            role=role,
            password=password,
        )
        print(f"✅ Admin user created successfully!\n   Username: {username}\n   Password: {password}")

if __name__ == "__main__":
    create_admin_user()
