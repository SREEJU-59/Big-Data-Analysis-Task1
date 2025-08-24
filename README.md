# Big-Data-Analysis-Task1

COMPANY NAME: CODTECH IT SOLUTIONS

NAME: SREEJU SV

INTERN ID: CT04DZ2078

DOMAIN: DATA ANALYSIS

DURATION: 4 WEEKS

MENTOR: NEELA SANTOSH

DESCRIPTION::

Task Description – Big Data Analysis (Internship Task-1)
Big data has become one of the most important aspects of modern data science, where the volume, variety, and velocity of information go beyond the capabilities of traditional data processing tools. As part of this internship project, the goal of Task-1 was to perform Big Data Analysis on a real-world dataset to demonstrate the ability to handle, process, and extract insights from large amounts of information. For this task, the Netflix Titles Dataset (November 2019 release) was selected as the source of data, and the analysis was carried out using PySpark in Google Colab. The final outcome of this task includes a working script and notebook that clearly showcase the use of big data tools for deriving meaningful insights.

*)Objective of the Task
The primary objective of this task was to perform scalable data analysis on a dataset containing thousands of entries about Netflix movies and TV shows. Netflix, being one of the largest streaming platforms in the world, provides a diverse and extensive content library. Analyzing such data is a perfect real-world use case of big data analytics because it involves working with structured data that has multiple attributes such as title, type, director, cast, country, genre, release year, and more. The project aimed to answer important business questions like:
How many movies vs. TV shows exist in the dataset?
Which countries contribute the most content on Netflix?
What are the most popular genres or categories?
How has the content trend changed over the years?
*)Tools and Environment Used
Google Colab: A cloud-based notebook environment that makes it easier to run PySpark without local installation.
PySpark: The Python API for Apache Spark, used for distributed data processing and big data analysis.
Pandas & Matplotlib: For visualization and conversion of Spark DataFrames into smaller, manageable datasets for plotting.
Dataset: Netflix Titles Dataset (CSV format, ~6234 rows and multiple columns).
The use of PySpark ensures that even if the dataset size grows to millions of records, the same codebase can handle the scalability challenge, making this approach future-proof.
*)Methodology
The steps followed in this project include:
Dataset Loading – The dataset was uploaded into Google Colab and read using the Spark DataFrame API with automatic schema inference.
Data Exploration – Schema inspection and preview of rows to understand column types and potential missing values.
Big Data Analysis:
Count of Movies vs. TV Shows.
Aggregation by Country to identify regions contributing maximum content.
Grouping by listed_in (genre/categories) to find most common genres.
Grouping by release_year to study the trend of content production over time.
Data Cleaning – Filtering out invalid or null values from the release_year column to ensure accurate trend analysis.
Visualization – Using Matplotlib to create plots that show how Netflix content has evolved over the years.
Result Exporting – Saving analysis results like country counts into a CSV file for further reporting.
*Key Insights Derived
     Netflix has a larger proportion of movies compared to TV shows.
The United States, India, and the United Kingdom dominate Netflix’s content library.
Popular genres include Dramas, Comedies, and Documentaries.
Content addition has grown rapidly after 2010, showing Netflix’s global expansion strategy.
These insights are not only useful for understanding Netflix’s catalog but also demonstrate the value of big data tools in analyzing entertainment industry trends.
*Conclusion
       This internship task successfully demonstrates how big data tools like PySpark can be applied to real-world datasets to generate insights that would be difficult to manage with traditional tools like Excel or simple Python scripts. The Netflix dataset provided an excellent case study to showcase data cleaning, aggregation, transformation, and visualization. By completing this task, the project proves that large datasets can be effectively handled in a distributed computing environment while still delivering clear business insights. This aligns with the overall goal of the internship, which is to strengthen practical skills in big data analytics, preparing for future challenges in data-driven industries.

OUTPUT:<img width="1768" height="695" alt="Image" src="https://github.com/user-attachments/assets/b483d79f-49dd-4709-ba95-fc28d843d894" />     

