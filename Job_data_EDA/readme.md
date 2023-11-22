![image](https://miro.medium.com/v2/resize:fit:1200/1*6ry-K4BYrrWjqEx5gGsfrw.png)
# AI Impact on Job Titles and Future of Work

## Introduction
In today's technology-driven landscape, the influence of Artificial Intelligence (AI) on various job roles across industries is profound. This project delves into a dataset that reveals the depth of AI's influence on different job titles, highlighting the potential risk of automation and the relationship between tasks and AI applications. Through exploratory data analysis (EDA) and visualization techniques, this project aims to provide insights into how AI might reshape the future of work across diverse domains.

## Dataset and Libraries Used
- **Dataset:** The project utilizes a dataset named "Job_Data.csv" containing information on job titles, AI impact, tasks, AI models, AI workload ratio, and domain.
- **Libraries:** Python libraries such as Pandas, Matplotlib, Seaborn, and NumPy are employed for data loading, data cleaning, and visualization.

## Exploratory Data Analysis (EDA)
The analysis is divided into several sections, each exploring different aspects of the dataset.

### 1. Data Loading and Cleaning
- The dataset is loaded using Pandas and an initial inspection of the dataset is performed.
- Missing values are checked and handled appropriately.
- Data types are converted, and summary statistics are computed for numerical columns.

### 2. Univariate Analysis
- Distributions of 'AI Impact', 'Tasks', 'AI models', and the count of job titles in each 'Domain' are explored.
- Histograms and count plots visualize the distribution of different variables, revealing insights into the dataset.

### 3. Bivariate Analysis
- Relationships between pairs of variables ('AI Impact' vs 'Tasks', 'AI models' vs 'Tasks') are explored using scatterplots.
- These visualizations help identify potential correlations or patterns between different variables.

## Key Findings and Insights
### Risk of AI Automation
- The 'AI Impact' variable suggests that the majority of job titles have a moderate risk of automation (between 10% and 40%). However, only a few roles exhibit an extremely high AI impact, indicating a lower risk of complete automation for most jobs.

### Task Complexity
- The distribution of 'Tasks' across job titles shows that many roles have a moderate number of tasks, with a noticeable peak between 0 and 200. Some roles have an extremely high number of tasks, indicating potential complexity.

### AI Applications
- The 'AI models' distribution reveals that many job titles have a moderate number of associated AI models (between 0 and 2500), indicating the prevalence of AI applications across various roles.

### Domain-wise Job Titles
- Certain domains, such as "Data & IT," have a higher count of job titles, while others, like "Transport & Logistics," have fewer representations in the dataset, suggesting varying degrees of influence across domains.

## Conclusions and Implications
- **Risk Awareness:** Understanding the risk of AI automation across job titles is crucial for strategic interventions such as reskilling or job redesign.
- **Task Complexity:** While a higher number of tasks might correlate with more AI models, it doesn't necessarily imply a higher risk of automation. Task nature and complexity are vital determinants.
- **AI Integration:** The dataset showcases AI's impact across domains, highlighting the need for future readiness in various sectors.
- **Strategic Planning:** Insights from this analysis can aid stakeholders in crafting strategies to future-proof the workforce through initiatives like reskilling, job redesign, and awareness programs.

The project provides valuable insights into the current landscape of AI's influence on job titles, emphasizing the need for proactive measures to adapt to the evolving job market.


