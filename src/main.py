from app import create_app
from app.config import DevelopmentConfig as Config

app = create_app()


if __name__ == '__main__':
    app.run(port= Config.PORT, debug=Config.DEBUG)

# localhost:5000/user/