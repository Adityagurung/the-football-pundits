# The Football Pundits: Decoding the beautiful game ⚽️

![alt text](<Power_BI visualisation/the_football_pundits.png>)

## Table of Contents
- [Introduction](#introduction)
    - [Background and Motivation](#background-and-motivation)
    - [Data sources](#data-sources)
    - [Objectives](#objectives)
- [Data Pipeline](#data-pipeline)
    - [Tools/ Resources Used](#tools-resources-used)
    - [Reproducibility](#reproducibility)
    - [Visualisation/Dashboard](#visualisationdashboard)
- [Follow-up Work](#follow-up-work)
- [Contributors](#contributors)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [Contributions and Feedback](#contributions-and-feedback)

# [INTRODUCTION](#introduction)

## [Background and Motivation](#background-and-motivation)

In professional football, gaining a competitive edge increasingly relies on actionable insights derived from data. This project addresses that need by systematically monitoring and analyzing player contributions across Europe’s top leagues. The core objective is to identify patterns, trends, and anomalies in performance metrics—insights that can guide clubs in refining their recruitment strategies, tactical planning, and player development initiatives. Furthermore, analyzing league-level statistics provides valuable context for comparing the relative strengths and weaknesses of various football competitions, enriching our overall understanding of the sport.

> This initiative delivers an in-depth evaluation of team and player performances across the top six first-division football leagues worldwide, covering the period from 2020 to 2025. Using key performance indicators (KPIs) such as goals, assists, and disciplinary actions, the project presents a comprehensive, data-driven dashboard. By integrating multiple performance metrics, it supports informed decision-making for a wide range of stakeholders, including club managers, scouts, and sports analysts.

## [Data sources](#data-sources)

The raw data for this project comes from football statistics originally scraped from the [Transfermarkt](https://en.wikipedia.org/wiki/Transfermarkt) website. The dataset consists of multiple CSV files containing information on competitions, matches, clubs, players, player valuations, and appearances. It is automatically updated on a weekly basis. Each file includes attributes specific to an entity, along with unique IDs that allow the files to be joined together for analysis.

We access this dataset through [Kaggle](https://www.kaggle.com/datasets/davidcariboo/player-scores), downloading it directly into the `data/` folder of our GitHub repository using the **Kaggle API**. For more details about the dataset, refer to [our instructions](./data/README.md) or visit the [Kaggle dataset page](https://www.kaggle.com/datasets/davidcariboo/player-scores).


## [Objectives](#objectives)

The key objectives for our project are:
Certainly! Here's a clearer, more professional rewrite of your project objectives:

### Key Objectives of the Project:

1. **Data Extraction and Structuring**
   Extract raw football datasets from Transfermarkt, transform them into a clean, structured format, and store them in a centralized data lake for further processing.

2. **Data Processing and Integration**
   Process and integrate relevant datasets to create a unified, reliable source of truth. This step involves exporting the consolidated data as an external table into a data warehouse, utilizing orchestration tools and distributed computing frameworks to handle large-scale transformations efficiently.

3. **Data Modeling and Transformation**
   Convert the external table into materialized views or tables within the data warehouse. These tables are designed to highlight key performance indicators (KPIs) and metrics essential for tracking player, team, and league performance.

4. **Data Visualization and Analysis**
   Build interactive dashboards to visualize the KPIs and perform in-depth analysis of players, clubs, and leagues—enabling actionable insights and data-driven decision-making.


## [DATA PIPELINE](#data-pipeline)

---

⚠️ **Note:** This project is running on Google Cloud Platform (GCP) and Power BI trial accounts, both of which will expire on **July 23, 2025**. ⚠️

---

To achieve the project objectives, we have built a complete end-to-end data pipeline. The pipeline begins with raw football data sourced from Kaggle (originally scraped from Transfermarkt) and culminates in a Power BI dashboard designed to deliver actionable insights on players, teams, and leagues.

## [Tools/ Resources Used](#tools-resources-used)

1. **Terraform** – Used to provision and manage GCP infrastructure as code in a consistent and repeatable manner.

2. **GCP Compute Engine virtual machine** – Served as the main processing node for running data pipeline components and orchestration tools.

3. **GCP Cloud Storage** – Acted as the data lake for storing raw and intermediate datasets extracted from Kaggle.

4. **GCP BigQuery** – Functioned as the data warehouse for storing transformed datasets and running analytical queries.

5. **GCP Dataproc** – Enabled distributed data processing using Apache Spark for efficient transformation of large datasets.

6. **Power BI** – Used to build interactive dashboards for visualizing KPIs and analyzing player, team, and league performance.

7. **Docker/docker-compose** – Containerized project components to ensure consistent environments for development, orchestration, and deployment.

8. **Mage.ai** – Served as the data orchestration tool to automate, schedule, and monitor pipeline tasks from extraction to transformation.

9. **DBT Cloud** – Used to define, test, and manage SQL-based data transformations and materialized views in BigQuery.

10. **Spark/pySpark** – Handled large-scale data transformations and processing tasks within the Dataproc cluster.

11. **git/git lfs** – Managed source code versioning and efficiently tracked large files such as datasets and notebooks.

12. **Kaggle API** – Automated the download of raw football datasets from Kaggle into the project’s `data/` folder.

13. **VS Code** - IDE used for development, debugging, running Bash/shell terminal and source version control.

## **🔁 Reproducibility**
*Reproducibility of this project can be ensured by following the instructions for each step below.*

1. **Download Data** – Download raw football data on player appearances and competitions from Kaggle using the Kaggle API.
   👉 [Instructions](./data/README.md)

2. **Set Up Environment** – Configure your Google Cloud environment, including project setup, service accounts, SSH access, and a Compute Engine VM.
   👉 [Instructions](./gcp-cloud-infrastructure/README.md)

3. **Infrastructure as Code (Terraform)** – Use Terraform to provision essential GCP resources like a Cloud Storage bucket, BigQuery dataset, and Dataproc cluster.
   👉 [Instructions](./terraform-iac/README.md)

4. **Containerized Data Orchestration (Mage.ai)** – Use Mage as an orchestration tool to build an ETL pipeline that structures raw data and exports it to Cloud Storage.
   👉 [Instructions](./mage-orchestrator/README.md)

5. **Distributed Data Processing (PySpark + Dataproc)** – Use PySpark on a Dataproc cluster to transform structured data into a unified dataset and export it to BigQuery as an external table.
   👉 [Instructions](./spark-distributed-computing/README.md)

6. **Data Transformation in BigQuery (dbt)** – Use dbt to transform the external table into materialized tables focusing on data from the top five European leagues.
   👉 [Instructions](./dbt-data-transformation/README.md)

7. **Partitioning and Clustering** – Optimize BigQuery materialized tables by partitioning data by date and clustering by `player_id` for improved performance and cost-efficiency.

8. **Build Dashboard (Power BI)** – Create interactive visualizations to analyze player and league performance using key metrics such as goal contributions and disciplinary records.

![alt text](e2e_football_data_workflow.PNG)


## [Visualisation/Dashboard](#visualisationdashboard)
Link to Power BI workspace - https://app.powerbi.com/links/pOuedtK5r7?ctid=56c1d497-700b-49cf-8f8d-3dd6b20d522f&pbi_source=linkShare

The dashboard consists of 6 visualisation charts:

Data is collected from 2020-2025 mid year for respective 6 leagues - Bundesliga, Eredivisie, Laliga, Ligue-1, Premier-League, Serie-a of first class/division league in Germany, Netherlands, Spain, France, Italy and England(UK)

1. Chart 1: League Performance Over Time
Displays the average goals per game for each league, broken down year by year, to analyze scoring trends over time.

2. Chart 2: Country-wise League Summary
Compares leagues within each country, showing their average goals per match, win percentage, and total match points, to provide a multi-metric performance overview that can be drill down to clubs.

3. Chart 3: Top Clubs by League - Team Stats
Highlights the top 10 clubs from each league based on matches played, market value, and win percentage, offering insight into the most dominant and valuable teams.

4. Chart 4: Top Players by Club - Player Stats
Displays the top 10 players from each club, focusing on goal contributions (goals + assists) and disciplinary records (yellow/red cards), allowing for performance and behavior comparison.

5. Chart 5: Year Slicer (2020–2025)
An interactive year slicer that allows users to filter data across all charts based on a selected year within the 2020–2025 range.

6. Chart 6: League Slicer(Bundesliga, Eredivisie, Laliga, Ligue-1, Premier-League, Serie-a)
A league filter that lets users dynamically update all visualizations based on the selected league, for focused analysis.

## 🔄 [Follow-up Work](#follow-up-work)

Planned improvements and future enhancements for the project:

* ✅ Add automated tests to validate data transformations and pipeline reliability
* 🛠 Integrate `make` for simplified task management and reproducibility
* 🚀 Set up a CI/CD pipeline to automate testing, deployment, and updates
* 🔁 Build a fully automated end-to-end data pipeline from ingestion to visualization

## 👥 [Contributor](#contributor)

**Aditya Gurung**
📧 [aditya.grng@gmail.com](mailto:aditya.grng@gmail.com)

## 📄 [License](#license)

This project is licensed under the terms of the [MIT License](./LICENSE).

## 🙏 [Acknowledgments](#acknowledgments)

Special thanks to the following individuals and communities for their contributions, inspiration, and datasets:

* [Alexey Grigorev](https://github.com/alexeygrigorev)
* [DataTalks.Club](https://datatalks.club/)
* [transfermarkt-datasets by dcaribou](https://github.com/dcaribou/transfermarkt-datasets)