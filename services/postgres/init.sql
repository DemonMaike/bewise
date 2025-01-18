CREATE TABLE applications (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_name VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO applications (user_name, description) VALUES
    ('Alice', 'Fix the login issue'),
    ('Bob', 'Update the user dashboard'),
    ('Charlie', 'Add a new feature for reports');
