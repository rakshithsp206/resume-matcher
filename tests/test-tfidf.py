from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
    
resume = """
# Rakshith S

**Skills:** Python, Java, C++, SQL

**Education:** First-year Technology Student

**Projects:**
- Resume Matching System
- College Management Information System

**Experience:**
- Participated in CodeCraft Hackathon.
- Technical event volunteer.

**Interests:** Artificial Intelligence, Machine Learning, Backend Development.
"""

job_description = """
# Job Description: Python Backend Developer Intern

**Position:** Python Backend Developer Intern  
**Experience:** Fresher / Students  
**Employment Type:** Internship

### About the Role
We are looking for a motivated Python Backend Developer Intern who is passionate about software development, problem-solving, and emerging technologies. The candidate should have a good understanding of programming fundamentals, data structures, algorithms, and database management.

### Required Skills
- Programming knowledge in Python, Java, or C++.
- Understanding of Data Structures and Algorithms (DSA).
- Basic knowledge of SQL and relational databases.
- Understanding of Object-Oriented Programming (OOP).
- Familiarity with backend development concepts and REST APIs.
- Knowledge of Git and GitHub for version control.
- Basic understanding of software development principles and design patterns.

### Responsibilities
- Develop and maintain backend components using Python.
- Write clean, reusable, and efficient code.
- Work with relational databases and execute SQL queries.
- Build and integrate REST APIs.
- Participate in debugging, testing, and code reviews.
- Collaborate with team members to develop software applications.
- Apply problem-solving skills to improve application performance.

### Preferred Qualifications
- Experience developing academic or personal software projects.
- Knowledge of Java, JDBC, and database connectivity.
- Understanding of design patterns such as Singleton and Factory.
- Interest in Artificial Intelligence and Machine Learning.
- Participation in hackathons, coding competitions, or technical events.

### Eligibility
- Undergraduate students pursuing Computer Science, Information Technology, or related technical disciplines.
- First-year and second-year students with strong programming fundamentals are encouraged to apply.
- No prior professional experience required.

### What We Offer
- Hands-on experience in backend software development.
- Exposure to real-world programming practices.
- Opportunity to work with experienced developers.
- Practical experience with databases, APIs, and software engineering concepts.
"""

documents = [resume, job_description]

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)

print("TF-IDF Matrix:")
print(tfidf_matrix.toarray())


similarity = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])
print(f"Similarity between resume and job description: {similarity}")