import bcrypt
from ...repositores.name_repository import NameRepository
from django.core.validators import ValidationError # type: ignore

name_repo = NameRepository()
def verify_password(plain_password, hashed_password):
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

def login_user(email, password):
    # 이메일로 사용자 찾기
    try:
        user = name_repo.model.objects.get(email=email)
    except name_repo.model.DoesNotExist:
        raise ValidationError('해당 이메일이 존재하지 않습니다')
    
    # 비밀번호 확인
    if not verify_password(password, user.password):
        raise ValidationError('비밀번호가 틀립니다')
    return user