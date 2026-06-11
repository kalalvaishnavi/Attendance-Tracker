"""Centralized SQL queries for the Attendance Tracker application."""

INIT_DB_SCRIPT = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    full_name TEXT NOT NULL,
    role TEXT NOT NULL CHECK(role IN ('Admin', 'Teacher')),
    email TEXT,
    phone TEXT,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    last_login TEXT
);

CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    roll_number TEXT NOT NULL UNIQUE,
    class_name TEXT NOT NULL,
    section TEXT NOT NULL,
    enrollment_date TEXT NOT NULL,
    contact_number TEXT,
    email TEXT,
    status TEXT NOT NULL DEFAULT 'Active' CHECK(status IN ('Active', 'Archived')),
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS attendance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    attendance_date TEXT NOT NULL,
    status TEXT NOT NULL CHECK(status IN ('Present', 'Absent', 'Excused')),
    marked_by INTEGER NOT NULL,
    remarks TEXT,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    UNIQUE(student_id, attendance_date),
    FOREIGN KEY(student_id) REFERENCES students(id) ON DELETE CASCADE,
    FOREIGN KEY(marked_by) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS face_profiles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL UNIQUE,
    image_hash TEXT NOT NULL,
    image_path TEXT,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    FOREIGN KEY(student_id) REFERENCES students(id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_students_search
    ON students(first_name, last_name, roll_number, class_name, section);
CREATE INDEX IF NOT EXISTS idx_attendance_date
    ON attendance(attendance_date);
"""

GET_RECENT_ATTENDANCE = """
SELECT s.roll_number, s.first_name || ' ' || s.last_name AS student,
       s.class_name || '-' || s.section AS class, a.attendance_date, a.status, u.full_name AS marked_by
FROM attendance a
JOIN students s ON s.id = a.student_id
JOIN users u ON u.id = a.marked_by
ORDER BY a.attendance_date DESC, a.updated_at DESC
LIMIT 15
"""

GET_STUDENT_MATCH = """
SELECT fp.student_id, fp.image_hash, s.roll_number,
       s.first_name || ' ' || s.last_name AS student,
       s.class_name, s.section
FROM face_profiles fp
JOIN students s ON s.id = fp.student_id
WHERE s.status = 'Active'
"""
