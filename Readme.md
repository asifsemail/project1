# Credit Card Spending Behavior Analysis

## Installation and Setup

1. Clone the repository - [Credit Card Transactions Dataset](https://www.kaggle.com/datasets/priyamchoksi/credit-card-transactions-dataset/data)
2. Install the required packages by running the following:

    ```bash
    pip install pandas matplotlib seaborn numpy geopandas hvplot plotly
    ```

3. Download the dataset and place it in the project root directory.
4. Run the Jupyter Notebook `analysis_script.ipynb` to execute the analysis and generate visualizations.

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
- **Visuals**:
  - Customer loyalty by state
  - Customer loyalty by age group
  - Customer loyalty by job category

### 2. Spending Behavior by Merchants (Amit)

- **Goal**: Identify spending trends by merchant categories and transaction volume across different merchant types.
- **Insights**: Visualization of high-value merchants and seasonal spending patterns.

### 3. Age Segment Analysis (Jason)

- **Focus Areas**:
  - **Travel Purchases**: Spending patterns on travel across age groups.
  - **Frauds**: Fraud analysis, showing trends by age group and frequency of fraud incidents.

### 4. Fraud Analysis & Forecasting (Kade)

- **Goal**: To detect fraud and forecast potential fraud occurrences based on historical trends.
- **Method**: Monthly and weekly fraud forecasting using time series analysis.

### 5. Lifetime Value (LTV) Forecasting (Simran)

- **Goal**: Predict the customer lifetime value (LTV) and identify the top 25% of high-value customers.
- **Methodology**: LTV was calculated based on total spend and projected future spending patterns.

---

## Visualizations

Various visualizations were created throughout the project, and all visual outputs are saved as `.png` files in the `AK_Output` directory. Key visualizations include:

- **Monthly Transaction Trends**: Time series of total monthly transaction amounts.
- **Customer Loyalty by State**: Bar plots showing loyalty score by state.
- **Spending Patterns by Age Group**: Heatmaps showing transaction amounts by age group and time of day.
- **Fraud Forecasting**: Monthly and weekly fraud trends, highlighting high-risk periods.
- **Loyalty Segments by Job Category**: Stacked bar charts showing loyalty segments by job category.

---

## Limitations

- **.py file**: The .py file is specific to this project

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

- **Asif Khan** - Project Manager
- **Jason Brooks** - Data Analyst
- **Simranpreet Saini** - Data Analyst
- **Amit Gaikwad** - Data Analyst
- **Kade Thomas** - Data Analyst

---

This project showcases how transactional data can provide deep insights into customer behavior, fraud detection, and customer retention strategies. Through detailed segmentation and analysis, businesses can enhance their decision-making to drive growth and optimize revenue generation.