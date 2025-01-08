class User:
    def __init__(self, email, name, password, current_job_title):
        self.email = email
        self.name = name
        self.password = password
        self.current_job_title = current_job_title

    def change_password(self, new_password):
        self.password = new_password

    def change_job_title(self, new_job_title):
        self.current_job_title = new_job_title

    def get_user_info(self):
        print(f"User {self.name} currently works as a {self.current_job_title}. You can contact them at {self.email}.")

app_user_one = User("raissairutingabo@gmail.com","Raissa IRUTINGABO", "pwd1", "software dev")

app_user_one.get_user_info()
app_user_one.change_job_title("DEvOps trainer")
app_user_one.get_user_info()
app_user_two = User("raissairutingabo@gmail.com","Raissa IRUTINGABO", "pwd1", "software dev")
app_user_two.get_user_info
