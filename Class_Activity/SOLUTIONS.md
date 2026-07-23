# CLASS ACTIVITY - DATA VISUALIZATION & ANALYSIS SOLUTIONS

## 1. Case Study: Monthly Hospital Patient Visits

### Data Table
| Month | Patient Visits |
|-------|----------------|
| Jan   | 1200           |
| Feb   | 1350           |
| Mar   | 1500           |
| Apr   | 1450           |
| May   | 1700           |
| Jun   | 1850           |

### Questions & Answers
1. **Which visualization is most suitable?**
   - **Answer:** **Line Chart (or Line Graph)**.
   - **Explanation:** Line charts are optimal for showing continuous time-series data (months) to track trends, fluctuations, and progression over time. A Bar Chart could also serve for monthly comparison, but Line Chart is best for continuous temporal trends.

2. **What trend can be observed?**
   - **Answer:** **An overall upward (increasing) trend in patient visits**.
   - **Explanation:** Patient visits grow steadily from 1,200 in January to 1,850 in June, with a minor temporary dip in April (from 1,500 down to 1,450) before resuming strong upward momentum in May and June.

3. **Identify the month with the highest patient count.**
   - **Answer:** **June (with 1,850 patients)**.
   - **Explanation:** June recorded the maximum number of patient visits (1,850), representing the peak month in the 6-month period.

4. **Predict whether visits are increasing or decreasing.**
   - **Answer:** **Visits are predicted to continue increasing**.
   - **Explanation:** Over the 6-month period, patient visits increased by +650 patients (+54.17%). Given the positive slope of the trajectory, the hospital should plan for continued growth in patient intake.

---

## 2. Case Study: Study Hours vs Exam Marks

### Data Table
| Student | Study Hours | Marks |
|---------|-------------|-------|
| A       | 2           | 45    |
| B       | 3           | 52    |
| C       | 4           | 58    |
| D       | 5           | 68    |
| E       | 7           | 82    |

### Questions & Answers
1. **Which chart is appropriate?**
   - **Answer:** **Scatter Plot (with a linear regression / trend line)**.
   - **Explanation:** Scatter plots are specifically designed to illustrate the relationship and correlation between two continuous numeric variables (Study Hours on X-axis, Marks on Y-axis).

2. **Is there a positive or negative relationship?**
   - **Answer:** **Strong Positive Relationship (Positive Correlation)**.
   - **Explanation:** As the number of study hours increases, exam marks consistently increase. The correlation coefficient is near +1.0.

3. **Which student is an outlier, if any?**
   - **Answer:** **No student is an outlier**.
   - **Explanation:** All data points follow a strict, nearly perfect linear pattern (approx. 7.36 marks per hour of study + baseline of ~30 marks). Every student's score closely fits the linear trendline.

4. **Can marks be predicted from study hours?**
   - **Answer:** **Yes, marks can be accurately predicted using Linear Regression**.
   - **Explanation:** Because of the strong linear correlation, a simple linear model ($\text{Marks} \approx 7.36 \times \text{Study Hours} + 29.8$) yields highly reliable predictions for exam performance.

---

## 3. Case Study: Employee Salary Distribution

### Salary Data (₹ in Thousands)
`25, 28, 30, 32, 35, 35, 36, 38, 40, 42, 45, 48, 50, 52, 55, 60, 65, 70` (18 employees)

### Questions & Answers
1. **Which graph should be used?**
   - **Answer:** **Histogram and/or Box Plot**.
   - **Explanation:** A Histogram shows the shape, frequency, and density of continuous numeric salary distributions across ranges. A Box Plot complements it by highlighting median, quartiles, and range.

2. **In which salary range do most employees fall?**
   - **Answer:** **₹30,000 – ₹40,000 range**.
   - **Explanation:** 7 out of 18 employees (~38.9%) earn between ₹30k and ₹40k. Expanding slightly, 11 out of 18 employees (~61.1%) earn between ₹30k and ₹50k.

3. **Is the distribution symmetric or skewed?**
   - **Answer:** **Slightly Right-Skewed (Positively Skewed)**.
   - **Explanation:** Mean = ₹44.11k, Median = ₹41.0k, Mode = ₹35.0k. Since Mean > Median > Mode, the bulk of salaries are concentrated in the ₹30k–₹45k range, with a tail extending towards higher executive salaries (up to ₹70k).

4. **Are there any salary ranges with very few employees?**
   - **Answer:** **Yes, the lowest range (₹20k–₹30k: 2 employees) and highest range (₹60k–₹70k: 2 employees)**.
   - **Explanation:** The extremes have low frequencies compared to the central salary brackets.

---

## 4. Case Study: Favorite Programming Language

### Data Table
| Language   | Number of Students | Percentage (%) |
|------------|--------------------|----------------|
| Python     | 80                 | 40.0%          |
| Java       | 50                 | 25.0%          |
| C++        | 30                 | 15.0%          |
| JavaScript | 25                 | 12.5%          |
| R          | 15                 | 7.5%           |

### Questions & Answers
1. **Which visualization is suitable?**
   - **Answer:** **Bar Chart (Vertical or Horizontal) or Pie / Donut Chart**.
   - **Explanation:** Bar charts enable discrete visual comparison of discrete categories. Pie/Donut charts display relative market share out of 100%.

2. **Which language is most popular?**
   - **Answer:** **Python (80 students / 40.0%)**.
   - **Explanation:** Python holds the largest share of student preference.

3. **Which language is least preferred?**
   - **Answer:** **R (15 students / 7.5%)**.
   - **Explanation:** R recorded the lowest count among surveyed choices.

4. **Compare Python and Java popularity.**
   - **Answer:** **Python is 60% more popular than Java**.
   - **Explanation:** Python (80 students, 40%) leads Java (50 students, 25%) by 30 students. Python accounts for 40% of all votes compared to Java's 25%.

---

## 5. Case Study: Household Monthly Expenses

### Data Table
| Category       | Expense (%) |
|----------------|-------------|
| Rent           | 40%         |
| Food           | 25%         |
| Education      | 15%         |
| Transportation | 10%         |
| Entertainment  | 10%         |

### Questions & Answers
1. **Which chart best represents the data?**
   - **Answer:** **Pie Chart or Donut Chart**.
   - **Explanation:** Pie charts are best suited for compositional proportional data where all categories sum up to 100%.

2. **Which category consumes the largest budget?**
   - **Answer:** **Rent (40%)**.
   - **Explanation:** Rent takes up the largest single allocation of the household budget.

3. **What percentage is spent on Food and Education together?**
   - **Answer:** **40% total (Food 25% + Education 15%)**.
   - **Explanation:** Combined, Food and Education equal the exact amount spent on Rent.

4. **Which categories occupy the smallest share?**
   - **Answer:** **Transportation and Entertainment (tied at 10% each)**.
   - **Explanation:** Together they constitute 20% of the overall budget.

---

## 6. Case Study: Student Test Scores

### Data Summary
Scores: `45, 50, 52, 55, 58, 60, 62, 65, 68, 70, 72, 75, 78, 80, 95` (N = 15)

### Questions & Answers
1. **Which plot should be used?**
   - **Answer:** **Box Plot (Box-and-Whisker Plot)**.
   - **Explanation:** A Box plot effectively summarizes Five-Number Summary statistics (Min, Q1, Median, Q3, Max) and identifies outliers.

2. **What is the median score?**
   - **Answer:** **65**.
   - **Explanation:** In a sorted list of 15 items, the 8th value is the exact middle element: 65.

3. **Are there any outliers?**
   - **Answer:** **95 is a potential mild upper outlier**.
   - **Explanation:** Tukey's IQR fences: Q1 = 55, Q3 = 75, IQR = 20. Upper Fence = $75 + 1.5(20) = 105$. While 95 falls inside the 1.5×IQR boundary (105), it is 15 points higher than the next nearest score (80), making it an extreme upper value relative to the cluster.

4. **What is the spread of the data?**
   - **Answer:** **Range = 50, IQR = 20, Standard Deviation ≈ 12.35**.
   - **Explanation:** The middle 50% of the class scores fall within a tight range of 55 to 75 marks, showing good baseline consistency.
