# Flask VUE

**Flask** for backend and **Vue.js** for frontend

### Development notes

* cd to `frontend`, start server: `npm run dev`
* cd to `backend`, start server: `run_DEV.bat`, or
    * in CMD:
        ```cmd
        set FLASK_DEBUG=1
        set FLASK_APP=main.py
        # start app
        flask run
        ```
* access `http://localhost:5000/` for development serving by Flask, (`http://localhost:8080/` for frontend serving by Node)

### IDE PyCharm notes

* For support `Vue.js`, need follow configs:
    * Make sure you have `Node.js` on your computer.
    * Make sure the `JavaScript` and `TypeScript` plugin is enabled on the Settings/Preferences | Plugins page, tab Installed, see Managing plugins for details.
    * Install and enable the Vue.js plugin on the Settings/Preferences | Plugins page, tab Marketplace, as described in Installing plugins from JetBrains repository.
    
### References

* Application structure: https://codeburst.io/full-stack-single-page-application-with-vue-js-and-flask-b1e036315532
* Flask login management: https://pythonawesome.com/flask-user-session-management/
