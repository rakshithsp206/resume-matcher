
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# 1. Load pretrained model
model = SentenceTransformer("all-MiniLM-L6-v2")

# 2. Sample resume and job description
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

# 3. Generate embeddings
resume_embedding = model.encode(resume)
job_embedding = model.encode(job_description)

# 4. Calculate cosine similarity
similarity = cosine_similarity(
    [resume_embedding],
    [job_embedding]
)[0][0]

# 5. Display results
print("Resume embedding shape:", resume_embedding.shape)
print("Job embedding shape:", job_embedding.shape)

print("Similarity score:", similarity)
print("Match percentage:", round(similarity * 100, 2), "%")
