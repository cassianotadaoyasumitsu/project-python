from user import User
from post import Post

app_user_one = User("email@email.com", "Cassiano", "pwd1", "Student")

app_user_one.get_user_info()
app_user_one.change_job_title("Dev Ops")
app_user_one.get_user_info()

app_user_two = User("mail@mail.com", "Maria", "pwd2", "Engineer")
app_user_two.get_user_info()

post_user = Post("on a secret mission today!", app_user_two.name)

post_user.get_post_info()
