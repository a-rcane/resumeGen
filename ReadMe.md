# Resume Generator
<hr>

## Instructions

Link to project: [project deployed on vercel]()

Github link: [Here]()

Used fastApi with basic HTML, CSS and JS

In the frontend send the project key and the pdf file

Change model as per your subscription in main.py
(default is set to gpt-4)
<hr>

## Approach to solve

Used PyPDF2 library to extract the pdf file

Set the system and user prompt, then specify the model

Return the response as HTMLResponse

Used simple javascript on frontend to handle api call to submit and fetch response 

