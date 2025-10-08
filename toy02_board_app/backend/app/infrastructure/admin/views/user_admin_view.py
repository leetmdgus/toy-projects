from sqladmin import ModelView
from app.infrastructure.orm.user_model import UserModel

class UserAdminView(ModelView, model=UserModel):
    name = "사용자"
    name_plural = "사용자 목록"
    
    column_labels = {
        UserModel.id: "ID",
        UserModel.username: "아이디",
        UserModel.email: "이메일",
        UserModel.role: "권한",
    }
    
    column_list = [UserModel.id, UserModel.username, UserModel.email, UserModel.role]
    column_searchable_list = [UserModel.username, UserModel.email]
    column_sortable_list = [UserModel.id]
    
