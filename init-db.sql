-- Create the database if it doesn’t exist
DO
$$
BEGIN
   IF NOT EXISTS (SELECT FROM pg_database WHERE datname = 'test_db') THEN
      CREATE DATABASE test_db;
   END IF;
END
$$;

-- Connect to the test_db database
\c test_db;

-- Create the user if it doesn’t exist
DO
$$
BEGIN
   IF NOT EXISTS (SELECT FROM pg_roles WHERE rolname = 'test_user') THEN
      CREATE USER test_user WITH ENCRYPTED PASSWORD 'test@123';
   END IF;
END
$$;

-- Grant privileges to user
GRANT ALL PRIVILEGES ON DATABASE test_db TO test_user;

-- Create the table if it doesn’t exist
CREATE TABLE IF NOT EXISTS skills (
    user_id SERIAL PRIMARY KEY,
    bio TEXT NOT NULL
);

-- Insert sample data only if the table is empty
INSERT INTO skills (bio)
SELECT unnest(array[
    'Experienced data engineer skilled in Databricks, SQL, and Apache Spark.',
    'Machine learning specialist with Python, TensorFlow, and SQL experience.',
    'Software engineer with expertise in Java, Spring Boot, and Kubernetes.',
    'Cloud architect experienced in AWS, Terraform, and CI/CD pipelines.',
    'Full-stack developer with React, Node.js, and PostgreSQL knowledge.',
    'Data scientist with strong skills in SQL, Databricks, and Python.',
    'Database administrator with experience in SQL, PostgreSQL, and MySQL.',
    'DevOps engineer proficient in Docker, Kubernetes, and Terraform.',
    'AI researcher skilled in NLP, OpenAI models, and deep learning.',
    'Cybersecurity expert with knowledge of SIEM, SOC, and threat hunting.'
])
WHERE NOT EXISTS (SELECT 1 FROM skills);
