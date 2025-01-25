<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Quiz Application README</title>
  <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
  <style>
    body {
      font-family: Arial, sans-serif;
      line-height: 1.6;
      padding: 20px;
      background-color: #f4f4f4;
    }
    h1 {
      color: #333;
    }
    pre {
      background-color: #eee;
      padding: 10px;
      border-radius: 5px;
    }
    code {
      background-color: #f1f1f1;
      padding: 2px 6px;
      border-radius: 3px;
    }
  </style>
</head>
<body>

  <h1>Quiz Application README</h1>
  <div id="readme-content"></div>

  <script>
    const readmeMarkdown = `
# Quiz Application  

**A fun and interactive platform to test your knowledge, track progress, and compete with others!**  

## 🚀 Features  

### Admin Features  
- Create and manage quizzes.  
- Add, edit, and organize questions.  
- Save quizzes as drafts and publish them.  

### User Features  
- Take quizzes and view results.  
- Track progress with scores, percentages, and detailed feedback.  
- Compete on the leaderboard based on scores and submission time.  

### Additional Features  
- Randomized questions for every user.  
- Question order changes every 10 seconds during the quiz.  
- Anti-cheating measures to ensure fairness.  

---

## 🛠️ Tech Stack  

- **Backend**: Django Rest Framework (DRF)  
- **Frontend**: React with Vite  
- **Styling**: Tailwind CSS  

---

## 📚 How It Works  

1. **Login or Sign Up**  
   - Admins and users can create an account or log in.  

2. **Admin Dashboard**  
   - Create quiz sets, add questions, and manage drafts.  
   - Publish quizzes for users to attempt.  

3. **User Interaction**  
   - Browse all published quizzes.  
   - Take a quiz, with random question order for each user.  
   - View detailed results, including correct and wrong answers.  

4. **Leaderboard**  
   - Compare scores and ranks with others.  
   - Faster submissions are ranked higher in case of tied scores.  

---

## 🖥️ Installation  

### Clone the Repository  

\`\`\`bash  
git clone <repository-url>  
cd quiz-application  
\`\`\`

### Install Dependencies  

\`\`\`bash  
pip install -r requirements.txt  # For Backend (Django & DRF dependencies)  
cd frontend  
npm install  # For Frontend (React dependencies)  
\`\`\`

### Environment Setup  

#### Backend:  

1. Create a \`.env\` file and configure the environment variables (such as database credentials, secret keys, etc.).  
2. Run migrations to set up the database:  

\`\`\`bash  
python manage.py migrate  
\`\`\`

3. Create a superuser for the Admin panel:  

\`\`\`bash  
python manage.py createsuperuser  
\`\`\`

#### Frontend:  

1. Go to the \`frontend\` directory.  
2. Set up environment variables as needed (e.g., API URL).  
3. Start the development server:  

\`\`\`bash  
npm run dev  
\`\`\`

---

## 🎯 Usage  

### Admin Panel  

- Access the Admin Dashboard at \`http://localhost:8000/admin/\`  
- Log in with the superuser account.  
- Manage quizzes and users.  

### User Interaction  

- Access the application at \`http://localhost:3000/\`.  
- Browse available quizzes, take them, and view results.

---

## 🧪 Testing  

Run tests for both frontend and backend:  

### Backend Tests:  

\`\`\`bash  
python manage.py test  
\`\`\`

### Frontend Tests:  

\`\`\`bash  
npm test  
\`\`\`

---

## 🤝 Contributing  

1. Fork the repository.  
2. Create your feature branch (\`git checkout -b feature-name\`).  
3. Commit your changes (\`git commit -m 'Add new feature'\`).  
4. Push to the branch (\`git push origin feature-name\`).  
5. Open a pull request.

---

## 📄 License  

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

    `;

    document.getElementById('readme-content').innerHTML = marked(readmeMarkdown);
  </script>

</body>
</html>
