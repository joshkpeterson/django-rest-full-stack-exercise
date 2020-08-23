# django-rest-full-stack-exercise
API-first backend and React frontend


### Prerequisite
- Use Django Rest Framework (DRF) for the backend
- Use ReactJS for the frontend
- Deploy the final product in a cloud based environment (Heroku/AWS/etc)
- Implement Authentication via JWT
- Use PostgreSQL database

### Requirements (backend and frontend)

- **Tickets** - Break the following down into GitHub Issues in a GitHub Project. Each ticket should have a meaningful intent and level of effort (hours) in it. At the end of this project all issues should be closed and linked to pull requests. You can merge your own pull requests. We would also like to see clean Git History -- telling a story of your thought process is important part of Git History
- **Create endpoint** - This endpoint will **not** be authenticated - Input: FirstName, LastName, SSN, Username, Password, role (two options - User or Admin). Output: HTTP 201 response with JSON output of the record created. The returned JSON should not show password. 
- **login** - This endpoint will **not** be authenticated - Input: username, password. Output: JWT web token in JSON format. 
- **Upload endpoint** - This endpoint will be authenticated - POST-BODY: a pipe delimitted TXT file and JWT token. Output: HTTP 200 response with JSON output of the number of lines in the file. JSON output shall contain the id of the upload. There can be multiple uploads for each user. Action: The uploaded file is persisted into a PostgreSQL database. The format of the file will be: `<order_id> | <product_name> | <product_quantity>`. Example: `2 | Eggs | 20`
- **Read Single endpoint** - This endpoint will be authenticated - Input: upload id, and JWT token. Output: HTTP 200 response with JSON output of the upload id
- **Delete endpoint** - This endpoint will be authenticated - Input: upload id, and JWT token. Output: HTTP 200 response with JSON output of the upload id that got deleted
- **Frontend** - Create frontend in ReactJS that makes the above endpoints usable. The UI can be bare bones but should still look compelling. You can use Bootstrap or similar CSS frameworks.
- **CORS** - There should be no CORS isussues between frontend and backend. There should be no JS errors in the console on the frontend.

### Deliverable:
- GitHub Source Code (provide omnipresent07 read access)
- URL of the application hosted in the cloud 
- Access to the underlying PostgreSQL database
