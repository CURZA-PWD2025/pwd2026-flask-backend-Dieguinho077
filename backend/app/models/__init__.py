from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_models():
    from .rol import Rol
    from .user import User
    from .categoria import Categoria
    from .proveedor import Proveedor
    from .producto import Producto