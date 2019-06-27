#
# Main application script
# Creates application instance using imported factory function(s)
# 

import os                                                   # os will be used to grab environment variables
from app import create_app, db                              # import create_app and db from app package constructor
from app.models import User, Post                           # import User and Post models from app/models
                                                            # from flask_migrate import Migrate

app = create_app(os.getenv('FLASK_CONFIG') or 'default')    # instantiate application instance from blueprint
# migrate = Migrate(app, db)

@app.shell_context_processor                                # create python shell for application after app is instantiated
def make_shell_context():
    return dict(db=db, User=User, Post=Post)

if __name__ == '__main__':                                  #Run application when executed from main .py file rather than by Flask run
    app.run()