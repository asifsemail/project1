# Credit Card Spending Behavior Analysis

## Project Overview

This project analyzes credit card transaction data to gain insights into **customer loyalty**, **spending behavior**, and **fraud trends**. Our goal was to use data-driven insights to help credit card companies improve customer targeting, retention strategies, and fraud prevention. The analysis was conducted on 1.29M records spanning 983 unique credit card users over a 1.5-year period.

Key components of the analysis include **customer segmentation**, **loyalty scoring**, **spending behavior analysis**, **fraud forecasting**, and **LTV (lifetime value) forecasting**.

---

## Installation and Setup

1. Clone the repository - [SSH Link](git@github.com:asifsemail/project1.git)
2. Install the required packages by running the following:

    ```bash
    pip install pandas matplotlib seaborn numpy geopandas hvplot plotly
    ```

3. Download the dataset and place it in the project root director - [Credit Card Transactions Dataset](https://www.kaggle.com/datasets/priyamchoksi/credit-card-transactions-dataset/data)
4. Run the Jupyter Notebooks `ak_cc_analysis.ipynb`, `age_jbrooks.ipynb`, `KadeCorrelationAnalysis.ipynb`, `Kadefraudforcasting.ipynb`, `KadeCA2.ipynb`, `merchant.ipynb`, and `SimranAnalyzer.ipynb` to execute the analysis and generate visualizations.

---

## Dataset

The dataset consists of 1.29M records and 983 unique credit card numbers over a 1.5-year period. It includes the following columns:

- `trans_date_trans_time`: Transaction timestamp
- `category`: Transaction category
- `state`: Transaction location (state)
- `amt`: Transaction amount
- `gender`: Customer gender
- `cc_num`: Credit card number (unique customer identifier)
- `job`: Customer job title
- `dob`: Customer date of birth (for calculating age)
- Additional fields for customer details and transaction metadata.

---

## Key Analyses

### 1. Customer Loyalty Analysis (Asif)

- **Goal**: To assess customer loyalty by grouping users based on transaction frequency, recency, and spending habits.
- **Approach**: Customers were segmented into four categories: `Very Loyal`, `Loyal`, `At Risk`, and `Inactive`.
- **Method**: Customer loyalty was calculated by analyzing three key metrics for each customer: **transaction frequency**, **recency of transactions**, and **average spending**. These metrics were computed from the transaction data and then used to classify customers into loyalty segments.

1. **Frequency**: The number of transactions a customer made, segmented into `Low`, `Moderate`, `High`, and `Very High Frequency`.
2. **Recency**: The number of days since the last transaction, classified into `Very Recent`, `Recent`, `Not Recent`, and `Stale`.
3. **Spending Behavior**: The average amount spent per transaction, categorized as `Low Spender`, `Moderate Spender`, `High Spender`, or `Very High Spender`.

Using these classifications, customers were grouped into four loyalty segments:
- **Very Loyal**: Customers with very recent activity and high transaction frequency.
- **Loyal**: Customers with recent activity and moderate to high transaction frequency.
- **At Risk**: Customers with not recent or stale activity and low transaction frequency.
- **Inactive**: Customers with no recent transactions and low frequency.

- **Visuals**:
  - Customer loyalty by state
  - Customer loyalty by age group
  - Customer loyalty by job category
- **Files**:
    - ak_cc_analysis.ipynb
    - Resources Folder
    - AK_Output Folder

### 2. Spending Behavior by Merchants (Amit)

- **Goal**: Identify spending trends by merchant categories and transaction volume across different merchant types.
- **Insights**: Visualization of high-value merchants and seasonal spending patterns.
- **Files**:
    - merchant.ipynb
    - merchant-graphs.py
    - graphs Folder

### 3. Age Segment Analysis (Jason)

- **Focus Areas**:
  - **Travel Purchases**: Spending patterns on travel across age groups.
  - **Frauds**: Fraud analysis, showing trends by age group and frequency of fraud incidents.
- **Files**:
    - age_jbrooks.ipynb
    - jbrooks_plots_charts Folder
      
### 4. Seasonal Marketing Analysis (Kade)

- **Goal**: To analyze average spending patterns by age group across different seasons and categories to tailor marketing strategies effectively.
- **Method**: Aggregating spending data by age group for each season. Visualizing spending patterns with bar charts for easier comparison. Identifying age groups with higher spending in each season. Using insights to recommend seasonal marketing strategies aimed at age groups with the highest spending potential.
- **Files**:
    - CorrelationAnalysis.ipynb
    - CA2.ipynb
    - kade_output_file.zip Folder
      
### 4. Fraud Forecasting (Kade)

- **Goal**: To predict the occurrence of fraud charges over time and assess future fraud risks. This forecasting aims to help the organization anticipate and proactively manage fraud by understanding potential future trends in fraudulent activity.
- **Method**: Collecting historical data on actual fraud charges. Training a model to predict future fraud charges, generating forecasted values along with uncertainty intervals. Comparing actual fraud charge trends with forecasted values to evaluate model accuracy and identify potential anomalies or high-risk periods. Visualizing the results with a line chart showing actual vs. forecasted fraud charges, accompanied by an uncertainty interval to indicate the model's confidence level.

- **Files**:
    - fraudforcasting.ipynb
    - kade_output_file.zip Folder

### 5. Lifetime Value (LTV) Forecasting (Simran)

- **Goal**: Predict the customer lifetime value (LTV) and identify the top 25% of high-value customers.
- **Methodology**: LTV was calculated based on a weighted equation suming the total transactions, total spend, and total recent transactions. This was then used to create future projections.
- **Files**:
    - SimranAnalyzer.ipynb
    - SpenderlyticsApp Folder
    - figsfolder Folder
    - All_Graphs_Report.pdf

---

## Visualizations

Various visualizations were created throughout the project, and all visual outputs are saved as `.png` files in multiple folders:  `AK_Output`, `graphs`, `jbrooks_plots_charts`, `kade_output_file.zip`, and `figsfolder`. Key visualizations include:

- **Monthly Transaction Trends**: Time series of total monthly transaction amounts.
- **Customer Loyalty by State**: Bar plots showing loyalty score by state.
- **Spending Patterns by Age Group**: Heatmaps showing transaction amounts by age group and time of day.
- **Fraud Forecasting**: Monthly and weekly fraud trends, highlighting high-risk periods.
- **Loyalty Segments by Job Category**: Stacked bar charts showing loyalty segments by job category.
- **LTV Forecast**: Using multiple forecasting models.

---

## Limitations

- **.py file**: The UI demonstration in the Spenderlytics App folder is specific to this project and file.
- **Fraud Forecasting Accuracy**: Further improvement could be made by integrating more advanced machine learning models for better fraud detection accuracy.

---

## Future Improvements

- **Generalized .py package**: Updating the code to take on any CC file and provide the required analysis as output.
- **Source File**: Future improvment can have a source file that can be pulled by doing API request
- **Advanced Segmentation**: Using machine learning algorithms for clustering and customer segmentation.
- **Real-Time Data Integration**: Implementing real-time analytics to provide up-to-date insights.
- **Customizable Dashboards**: Enhancing data visualization with customizable dashboards for better interaction.

---

## Team

This project was conducted by the following team members:

- **Asif Khan** - Project Manager, Customer Loyalty Analysis Lead
- **Jason Brooks** - Data Analyst, Age Segment Analysis Lead
- **Simranpreet Saini** - Data Analyst, LTV Forecasting Lead
- **Amit Gaikwad** - Data Analyst, Spending Behavior by Merchants Lead
- **Kade Thomas** - Data Analyst, Fraud Analysis & Forecasting Lead

---

This project showcases how transactional data can provide deep insights into customer behavior, fraud detection, and customer retention strategies. Through detailed segmentation and analysis, businesses can enhance their decision-making to drive growth and optimize revenue generation.
