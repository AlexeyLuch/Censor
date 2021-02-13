from app import app,db
from war.blueprint import war
import view

app.register_blueprint(war,url_prefix="/war")

if __name__ == '__main__':
    app.run()

