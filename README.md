
# Student Performance Analysis and Visualization

This project analyzes student performance data and provides insights into factors influencing exam scores. The analysis includes data visualization and insights derived from the dataset.

## Dataset Information

The dataset contains the following columns:
- **Gender**: Sex of students (Male/Female)
- **Race/Ethnicity**: Ethnicity of students (Group A, B, C, D, E)
- **Parental Level of Education**: Final education level of parents (Bachelor's degree, some college, master's degree, associate's degree, high school)
- **Lunch**: Lunch status before the test (Standard or free/reduced)
- **Test Preparation Course**: Completion status of test preparation course (Complete or Not Complete)
- **Math Score**: Student's math exam score
- **Reading Score**: Student's reading exam score
- **Writing Score**: Student's writing exam score

  Dataset link: https://www.kaggle.com/datasets/spscientist/students-performance-in-exams?datasetId=74977

---

## Features of the Project

### 1. Data Exploration
- Analyzed and visualized the distribution of scores across various parameters.
- Examined the relationship between gender, race, parental education, lunch type, and test preparation on student performance.

### 2. Visualizations
- **Histogram**: Visualized the score distributions for math, reading, and writing.
- **Kernel Density Estimation (KDE)**: Used to analyze score patterns across different factors.

### 3. Insights

- **Factors Influencing Performance**:
  - Student performance is related to lunch type, race/ethnicity, and parental education.
  - Female students excel in overall performance.

---

## Deployment

This project has been deployed using **AWS Elastic Beanstalk** and **AWS CodePipeline**. You can access the application at the following URL:  
[Student Performance Application](http://studentperformance-env.eba-pwhhfbmt.us-east-1.elasticbeanstalk.com/)

### AWS Services Used
1. **AWS Elastic Beanstalk**: For deploying and running the web application.
2. **AWS CodePipeline**: For automating the deployment process.

---

## How to Use
1. Open the application link to explore the interactive visualizations and insights.
2. Analyze the distribution of student performance based on gender, race, parental education, lunch type, and test preparation.
3. Use the findings to draw conclusions about factors affecting academic success.

---

## Conclusions
- Student performance is influenced by lunch type, race/ethnicity, and parental education.
- Female students lead in both pass percentage and as top scorers.
- Completing the test preparation course improves performance but is not a major determinant.
- Parental education has a limited impact on student performance, particularly for female students.

---

