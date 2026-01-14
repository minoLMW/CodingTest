WITH scored AS (
  SELECT
    c.course_id,
    c.course_name,
    s.student_name,
    e.score,
    ROW_NUMBER() OVER (PARTITION BY c.course_id ORDER BY e.score DESC) AS rn_desc,
    ROW_NUMBER() OVER (PARTITION BY c.course_id ORDER BY e.score ASC)  AS rn_asc
  FROM course c
  LEFT JOIN enrollment en
    ON en.course_id = c.course_id
  LEFT JOIN exam e
    ON e.enrollment_id = en.enrollment_id
  LEFT JOIN student s
    ON s.student_id = en.student_id
)
SELECT
  course_name,
  MAX(CASE WHEN rn_desc = 1 THEN student_name END) AS top_student,
  MAX(CASE WHEN rn_asc  = 1 THEN student_name END) AS low_student
FROM scored
GROUP BY course_id, course_name
ORDER BY course_id;
