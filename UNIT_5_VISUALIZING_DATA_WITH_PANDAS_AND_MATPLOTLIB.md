# UNIT 5: VISUALIZING DATA WITH PANDAS AND MATPLOTLIB (CO5)
**Course:** DSA05 / DSA0501 – Query Processing for Data Science  
**Target:** 180-Question MCQ Exam Preparation & Comprehensive Concept Mastery  
**Assessment Framework:** Bloom's Revised Taxonomy (Levels L1 to L6)

---

## 📌 TABLE OF CONTENTS
1. [Matplotlib Architecture & Core Paradigms](#1-matplotlib-architecture--core-paradigms)
   - 1.1 The 3 Architectural Layers (Backend, Artist, Scripting)
   - 1.2 Object-Oriented (OO) vs State-Based (`pyplot`) Interface
   - 1.3 Figure vs Axes vs Axis Hierarchy
2. [Plot Components, Customization & Options](#2-plot-components-customization--options)
   - 2.1 Anatomy of a Plot (Titles, Labels, Ticks, Spines, Grid, Legend)
   - 2.2 Annotations & Text Highlights (`ax.annotate`)
   - 2.3 Visual Styling (Colors, Hex Codes, Markers, Linestyles, Transparency, Colormaps)
   - 2.4 Multi-Plot Layouts & Subplots (`plt.subplots`, `tight_layout`, `savefig`)
3. [Plotting Directly with Pandas (`df.plot`)](#3-plotting-directly-with-pandas-dfplot)
   - 3.1 Evolution Over Time (Line & Area Plots)
   - 3.2 Relationships Between Variables (Scatter & Hexbin Plots)
   - 3.3 Distributions (Histograms, KDE / Density, Box Plots)
   - 3.4 Counts & Frequencies (Vertical & Horizontal Bar Charts, Stacked Bars)
4. [The `pandas.plotting` Subpackage](#4-the-pandasplotting-subpackage)
   - 4.1 Scatter Matrices (`scatter_matrix`, Diagonal Hist/KDE)
   - 4.2 Lag Plots (`lag_plot`, Lag-1 Autoregressive Diagnostics vs Random Noise)
   - 4.3 Autocorrelation Plots (`autocorrelation_plot`, 95%/99% Confidence Bands, Seasonality)
   - 4.4 Bootstrap Plots (`bootstrap_plot`, Resampling Uncertainty, Mean & Median CIs)
5. [High-Yield Exam Tips & Common MCQ Traps](#5-high-yield-exam-tips--common-mcq-traps)
6. [Bloom's Taxonomy-Aligned MCQ Question Bank (40+ Questions)](#6-blooms-taxonomy-aligned-mcq-question-bank)
   - [6.1 Level 1: Remember (Knowledge & Recall)](#61-level-1-remember-knowledge--recall)
   - [6.2 Level 2: Understand (Comprehension & Explanation)](#62-level-2-understand-comprehension--explanation)
   - [6.3 Level 3: Apply (Application, Computation & Code Output)](#63-level-3-apply-application-computation--code-output)
   - [6.4 Level 4: Analyze (Analysis, Logic & Bug Detection)](#64-level-4-analyze-analysis-logic--bug-detection)
   - [6.5 Level 5 & 6: Evaluate & Create (Judgment, Architecture & Design)](#65-level-5--6-evaluate--create-judgment-architecture--design)

---

## 1. MATPLOTLIB ARCHITECTURE & CORE PARADIGMS

```
┌─────────────────────────────────────────────────────────────┐
│ 1. Scripting Layer (matplotlib.pyplot)                      │  ◄── User Interface (MATLAB-like procedural calls)
├─────────────────────────────────────────────────────────────┤
│ 2. Artist Layer (Figure, Axes, Axis, Line2D, Text, Patch)   │  ◄── Rendering Canvas Hierarchy (Every visual element)
├─────────────────────────────────────────────────────────────┤
│ 3. Backend Layer (Renderer & Graphics Context)              │  ◄── Output Device (PNG/Agg, PDF, SVG, GUI Windows)
└─────────────────────────────────────────────────────────────┘
```
* **Figure:** Top-level window/canvas.
* **Axes:** Individual subplot containing coordinate system and data graphics.
* **Axis:** Number lines with tick marks, labels, and limits.

---

## 2. PLOT CUSTOMIZATION & ANNOTATIONS

```python
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x, y, color='#2B5B84', linewidth=2, linestyle='--', marker='o', label='Trajectory')
ax.set_title("Performance Trend", fontsize=14, fontweight='bold')
ax.set_xlabel("Time (Months)")
ax.set_ylabel("Revenue ($k)")
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(loc='upper left')

# Annotation
ax.annotate('Peak', xy=(5, 1850), xytext=(4, 2000),
            arrowprops=dict(facecolor='red', shrink=0.05, width=1))

plt.tight_layout()
```

---

## 3. THE `pandas.plotting` DIAGNOSTIC SUITE

```python
from pandas.plotting import scatter_matrix, lag_plot, autocorrelation_plot, bootstrap_plot
```
1. **`scatter_matrix(df, diagonal='kde')`**: Pairwise scatter matrix. Diagonal displays univariate distributions (Histogram or KDE).
2. **`lag_plot(series, lag=1)`**:
   * **Shapeless / Circular Cloud** ➔ **Random Noise** (Uncorrelated).
   * **Diagonal Line ($y = x$)** ➔ **Strong Positive Autocorrelation**.
3. **`autocorrelation_plot(series)`**:
   * Horizontal dashed lines = **95% and 99% confidence bands**.
   * Spikes crossing confidence bands indicate **statistically significant seasonality / trend ($p < 0.05$)**.
4. **`bootstrap_plot(series, size=50, samples=500)`**: Evaluates uncertainty and sampling distribution for **Mean**, **Median**, and **Midrange**.

---

## 6. BLOOM'S TAXONOMY-ALIGNED MCQ QUESTION BANK

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                    BLOOM'S REVISED TAXONOMY DISTRIBUTION                     ║
╠════════════════════════════════════╦══════════════════════╦══════════════════╣
║ Cognitive Level                    ║ Focus Area           ║ Questions        ║
╠════════════════════════════════════╬══════════════════════╬══════════════════╣
║ **L1: Remember (Knowledge)**       ║ Recall & Definitions ║ Q1 – Q8          ║
║ **L2: Understand (Comprehension)** ║ Explain & Distinguish║ Q9 – Q16         ║
║ **L3: Apply (Application)**        ║ Execute & Compute    ║ Q17 – Q26        ║
║ **L4: Analyze (Analysis)**         ║ Debug & Edge Cases   ║ Q27 – Q34        ║
║ **L5 & L6: Evaluate & Create**     ║ Judge, Design & Plan ║ Q35 – Q40        ║
╚════════════════════════════════════╩══════════════════════╩══════════════════╝
```

### 6.1 Level 1: Remember (Knowledge & Recall)

#### Question 1 [Bloom's Level: L1 - Remember]
**In the three-tier architecture of Matplotlib, which layer is responsible for rendering vector instructions into output formats like PNG, PDF, and SVG?**  
A) Scripting Layer  
B) Artist Layer  
C) Backend Layer  
D) Application Layer  
**Answer: C**  
*Explanation:* The Backend Layer communicates directly with the underlying graphics devices and renderers (e.g. `Agg`, `PDF`, `SVG`, `TkAgg`) to produce visual outputs.

---

#### Question 2 [Bloom's Level: L1 - Remember]
**Which Matplotlib layer contains all visual elements such as Figure, Axes, Line2D, Text, and Rectangle?**  
A) Scripting Layer  
B) Artist Layer  
C) Backend Layer  
D) Operating System Layer  
**Answer: B**  
*Explanation:* In Matplotlib, every visible component is an instance of an `Artist` residing inside the Artist Layer.

---

#### Question 3 [Bloom's Level: L1 - Remember]
**What is the highest-level container in Matplotlib that represents the entire window/canvas?**  
A) `Axes`  
B) `Figure`  
C) `Axis`  
D) `Spine`  
**Answer: B**  
*Explanation:* The `Figure` object is the top-level canvas container that holds all subplots (`Axes`), titles, legends, and canvas properties.

---

#### Question 4 [Bloom's Level: L1 - Remember]
**What is the default plot type when calling `df.plot()` on a Pandas DataFrame without specifying the `kind` argument?**  
A) `'bar'`  
B) `'scatter'`  
C) `'line'`  
D) `'hist'`  
**Answer: C**  
*Explanation:* By default, `df.plot()` generates a Line Plot (`kind='line'`).

---

#### Question 5 [Bloom's Level: L1 - Remember]
**Which marker symbol represents a square in Matplotlib?**  
A) `'o'`  
B) `'s'`  
C) `'^'`  
D) `'D'`  
**Answer: B**  
*Explanation:* `'s'` denotes square markers, `'o'` circle, `'^'` triangle up, and `'D'` diamond.

---

#### Question 6 [Bloom's Level: L1 - Remember]
**From which Pandas subpackage are `scatter_matrix`, `lag_plot`, `autocorrelation_plot`, and `bootstrap_plot` imported?**  
A) `pandas.analytics`  
B) `pandas.tools`  
C) `pandas.plotting`  
D) `pandas.graphics`  
**Answer: C**  
*Explanation:* Advanced diagnostic visualization functions in Pandas are located in the `pandas.plotting` subpackage.

---

#### Question 7 [Bloom's Level: L1 - Remember]
**Which 3 statistical summary measures are evaluated and displayed by `pandas.plotting.bootstrap_plot()`?**  
A) Standard Deviation, Skewness, Kurtosis  
B) Mean, Median, and Midrange  
C) Mode, Range, IQR  
D) Minimum, Maximum, Quantile  
**Answer: B**  
*Explanation:* `bootstrap_plot` computes and plots the bootstrap sampling distributions for the **Mean**, **Median**, and **Midrange** ($\frac{\min + \max}{2}$).

---

#### Question 8 [Bloom's Level: L1 - Remember]
**Which colormap in Matplotlib is perceptually uniform and accessible to individuals with color vision deficiencies?**  
A) `'jet'`  
B) `'viridis'`  
C) `'rainbow'`  
D) `'hsv'`  
**Answer: B**  
*Explanation:* `'viridis'` is perceptually uniform across both color and grayscale representations.

---

### 6.2 Level 2: Understand (Comprehension & Explanation)

#### Question 9 [Bloom's Level: L2 - Understand]
**Why is the Object-Oriented (OO) interface (`fig, ax = plt.subplots()`) preferred over the state-based `pyplot` interface for building complex dashboards?**  
A) Because `pyplot` cannot save to PNG  
B) The OO interface provides explicit, independent control over multiple subplots (`Axes`) without relying on a hidden global state  
C) The OO interface uses less CPU memory  
D) `pyplot` is deprecated in Python 3  
**Answer: B**  
*Explanation:* The OO paradigm passes explicit `Figure` and `Axes` references, eliminating global state ambiguity and allowing clean, scalable multi-panel dashboard generation.

---

#### Question 10 [Bloom's Level: L2 - Understand]
**What is the purpose of `plt.tight_layout()` in Matplotlib?**  
A) To compress image file size  
B) To automatically adjust subplot padding so that titles, axis labels, and tick marks do not overlap  
C) To limit data to 100 points  
D) To convert the plot into 3D  
**Answer: B**  
*Explanation:* `plt.tight_layout()` computes optimal subplot padding to eliminate overlaps between adjacent subplots and labels.

---

#### Question 11 [Bloom's Level: L2 - Understand]
**What does `pandas.plotting.scatter_matrix()` display along its main diagonal?**  
A) Blank empty cells  
B) Pairwise scatter plots  
C) Histograms (`'hist'`) or Kernel Density Estimation plots (`'kde'`) of individual variables  
D) Numerical correlation coefficients  
**Answer: C**  
*Explanation:* Because a scatter plot of a variable against itself is just a redundant straight line, `scatter_matrix` displays the univariate distribution (Histogram or KDE) along the diagonal.

---

#### Question 12 [Bloom's Level: L2 - Understand]
**If a `lag_plot(series, lag=1)` displays a structureless, shapeless circular cloud of points, what does this indicate about the time series?**  
A) Strong linear autocorrelation  
B) The data is completely random white noise with no autocorrelation  
C) A severe positive trend  
D) Strong quarterly seasonality  
**Answer: B**  
*Explanation:* A random, uncorrelated sequence produces no relationship between $y(t)$ and $y(t+1)$, yielding an unstructured circular cloud of scatter points.

---

#### Question 13 [Bloom's Level: L2 - Understand]
**If a `lag_plot` displays points clustering tightly along a positive 45-degree diagonal line ($y = x$), what does this indicate?**  
A) High positive autocorrelation (values at time $t+1$ depend strongly on values at time $t$)  
B) The data is completely random  
C) High negative correlation  
D) Measurement corruption  
**Answer: A**  
*Explanation:* Points clustering along the line $y = x$ indicate strong positive serial correlation (persistence from one time step to the next).

---

#### Question 14 [Bloom's Level: L2 - Understand]
**What do the horizontal dashed lines in a `pandas.plotting.autocorrelation_plot` represent?**  
A) Upper and lower boundaries of raw data values  
B) 95% and 99% statistical confidence bands for zero autocorrelation  
C) Target sales goals  
D) Moving averages  
**Answer: B**  
*Explanation:* In an autocorrelation plot, the horizontal dashed lines mark the 95% and 99% confidence bands. Values extending beyond these bands are statistically significant ($p < 0.05$).

---

#### Question 15 [Bloom's Level: L2 - Understand]
**What is the purpose of `pandas.plotting.bootstrap_plot()`?**  
A) To bootstrap server memory  
B) To evaluate the uncertainty and sampling distribution of summary statistics (Mean, Median, Midrange) via resampling with replacement  
C) To train a decision tree model  
D) To scrape web pages  
**Answer: B**  
*Explanation:* `bootstrap_plot` repeatedly resamples subsets of the data with replacement to generate empirical sampling distributions for the Mean, Median, and Midrange, illustrating estimation uncertainty.

---

#### Question 16 [Bloom's Level: L2 - Understand]
**In Matplotlib, what does the `alpha` parameter control?**  
A) Font size  
B) Opacity / Transparency of visual elements (from 0.0 transparent to 1.0 fully opaque)  
C) Line thickness  
D) Rotation angle  
**Answer: B**  
*Explanation:* `alpha` defines the blending transparency on a scale from 0.0 (completely see-through) to 1.0 (completely solid).

---

### 6.3 Level 3: Apply (Application, Computation & Code Output)

#### Question 17 [Bloom's Level: L3 - Apply]
**What is the structure of `fig, axes = plt.subplots(2, 2)`?**  
A) A single Figure and a 1D list of 4 numbers  
B) A Figure object and a 2D NumPy array of 4 `Axes` objects (`shape=(2, 2)`) accessible via `axes[row, col]`  
C) Two separate Figures  
D) A dictionary of plots  
**Answer: B**  
*Explanation:* `plt.subplots(2, 2)` instantiates a `Figure` and returns a $2 \times 2$ NumPy array containing 4 `Axes` subplot instances.

---

#### Question 18 [Bloom's Level: L3 - Apply]
**How do you set custom X-axis tick labels rotated by 45 degrees in Matplotlib OO API?**  
A) `ax.rotate_ticks(45)`  
B) `ax.set_xticklabels(labels, rotation=45)`  
C) `ax.ticks.rotate(45)`  
D) `plt.turn_x(45)`  
**Answer: B**  
*Explanation:* `ax.set_xticklabels(labels, rotation=45)` assigns custom tick label strings and rotates their text orientation by 45 degrees.

---

#### Question 19 [Bloom's Level: L3 - Apply]
**Which method is used to draw an arrow pointing to a specific data coordinate with a descriptive text label?**  
A) `ax.text()`  
B) `ax.annotate()`  
C) `ax.arrow_label()`  
D) `ax.point_to()`  
**Answer: B**  
*Explanation:* `ax.annotate(text, xy=(target_x, target_y), xytext=(label_x, label_y), arrowprops=...)` draws an annotated callout box with a connecting arrow.

---

#### Question 20 [Bloom's Level: L3 - Apply]
**How do you hide the top and right spines of a plot for a modern minimalist design?**  
A) `ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)`  
B) `ax.hide_spines()`  
C) `ax.remove_border()`  
D) `plt.clean_spines()`  
**Answer: A**  
*Explanation:* Setting `.set_visible(False)` on the spine dictionary keys hides the respective boundary lines.

---

#### Question 21 [Bloom's Level: L3 - Apply]
**Which plotting method is best suited for comparing quantities across discrete categories when category names are very long?**  
A) `df.plot.pie()`  
B) `df.plot.barh()` (Horizontal Bar Plot)  
C) `df.plot.scatter()`  
D) `df.plot.kde()`  
**Answer: B**  
*Explanation:* Horizontal bar charts (`barh`) display category names along the vertical Y-axis, allowing long labels to read horizontally without rotation.

---

#### Question 22 [Bloom's Level: L3 - Apply]
**What is the purpose of setting `stacked=True` in `df.plot.bar(stacked=True)`?**  
A) To sort bars alphabetically  
B) To stack category sub-segments vertically on top of one another to show both total and part-to-whole composition  
C) To remove spacing between bars  
D) To convert the bar chart into a histogram  
**Answer: B**  
*Explanation:* `stacked=True` places multiple column values sequentially on top of each other within each bar to display aggregate sums and compositional shares.

---

#### Question 23 [Bloom's Level: L3 - Apply]
**What does `ax.axhspan(ymin=1000, ymax=1500, color='yellow', alpha=0.3)` draw?**  
A) A vertical line  
B) A continuous horizontal shaded band across the entire width of the plot between $Y = 1000$ and $Y = 1500$ with 30% opacity  
C) A single scatter point  
D) An arrow  
**Answer: B**  
*Explanation:* `ax.axhspan()` draws a shaded horizontal band across the full X range between specified Y limits.

---

#### Question 24 [Bloom's Level: L3 - Apply]
**Which parameter in `plt.savefig()` prevents axis labels and external legends from being cut off in the exported image file?**  
A) `dpi=300`  
B) `bbox_inches='tight'`  
C) `transparent=True`  
D) `format='png'`  
**Answer: B**  
*Explanation:* `bbox_inches='tight'` automatically expands the saved canvas bounding box to enclose all external text, titles, and legends.

---

#### Question 25 [Bloom's Level: L3 - Apply]
**What does `figsize=(10, 6)` in `plt.subplots()` specify?**  
A) Image dimensions in pixels (10px by 6px)  
B) Canvas width and height in **inches** (10 inches wide by 6 inches tall)  
C) 10 rows and 6 columns of subplots  
D) Font sizes  
**Answer: B**  
*Explanation:* Matplotlib `figsize` is specified in inches as `(width, height)`.

---

#### Question 26 [Bloom's Level: L3 - Apply]
**What is the default sample size and bootstrap repetition count in `bootstrap_plot(series)` if omitted?**  
A) `size=10, samples=50`  
B) `size=50, samples=500`  
C) `size=100, samples=1000`  
D) `size=500, samples=5000`  
**Answer: B**  
*Explanation:* `bootstrap_plot` defaults to `size=50` and `samples=500`.

---

### 6.4 Level 4: Analyze (Analysis, Logic & Bug Detection)

#### Question 27 [Bloom's Level: L4 - Analyze]
**Analyze why `ax.legend()` fails to display legend labels when executed after `ax.plot(x, y)`:**  
A) `ax.legend()` requires GPU rendering  
B) `ax.plot()` did not specify the `label='...'` argument; `ax.legend()` inspects Artist labels to construct legend entries  
C) `ax.legend()` only works on bar charts  
D) The figure size is too small  
**Answer: B**  
*Explanation:* `ax.legend()` scans Artists on the Axes and extracts their `label` parameter. If no labels are defined, the legend remains empty or raises a warning.

---

#### Question 28 [Bloom's Level: L4 - Analyze]
**What error occurs if you call `df.plot(kind='scatter')` without passing `x` and `y` column arguments?**  
A) It automatically picks the first two columns  
B) Raises a `ValueError: scatter requires an x and y column`  
C) Plots a line chart instead  
D) Creates an empty image  
**Answer: B**  
*Explanation:* Bivariate scatter plots require explicit mapping of variables to coordinates; omitting either raises a `ValueError`.

#### Question 29 [Bloom's Level: L4 - Analyze]
**Analyze why `df.plot.hexbin()` is superior to standard scatter plots when visualizing a dataset with 500,000 coordinate points:**  
A) Hexbin charts use less RAM  
B) Scatter plots suffer from severe overplotting where thousands of overlapping dots merge into a solid uninformative blob; hexbin tiles the 2D plane into regular hexagons color-coded by point density  
C) Scatter plots cannot plot floats  
D) Hexbin plots run in 3D  
**Answer: B**  
*Explanation:* Hexagonal binning aggregates 2D data into spatial frequency bins, cleanly communicating local point density without overplotting clutter.

---

#### Question 30 [Bloom's Level: L4 - Analyze]
**In daily supermarket sales data, the `autocorrelation_plot` exhibits a prominent peak crossing outside the dashed confidence band at lag 7. Analyze the operational meaning:**  
A) Day 7 had a data entry error  
B) Statistically significant weekly (7-day) recurring seasonality, meaning sales on any day are strongly correlated with sales on the same day of the preceding week  
C) The data is non-stationary noise  
D) The model has overfit  
**Answer: B**  
*Explanation:* A lag-7 autocorrelation exceeding the 95% confidence interval proves significant cyclical weekly buying behavior.

---

#### Question 31 [Bloom's Level: L4 - Analyze]
**Analyze what the `diagonal='kde'` parameter achieves in `scatter_matrix(df, diagonal='kde')`:**  
A) Replaces scatter plots with lines  
B) Computes and plots smooth Kernel Density Estimation probability curves along the main diagonal instead of binned histograms  
C) Inverts the color palette  
D) Normalizes column data  
**Answer: B**  
*Explanation:* `diagonal='kde'` renders continuous non-parametric density curves along the diagonal subplots.

---

#### Question 32 [Bloom's Level: L4 - Analyze]
**Why does `df.plot(kind='pie')` raise a `ValueError` when called on a multi-column DataFrame without specifying `y='col'`?**  
A) Pie charts can only display negative numbers  
B) A pie chart can only represent 1-dimensional categorical proportions of a single metric; multi-column DataFrames require specifying which column values represent slice sizes  
C) Pandas does not support pie charts  
D) Pie charts require integer indexes  
**Answer: B**  
*Explanation:* Pie charts visualize 1D part-to-whole proportions. Without specifying `y`, Pandas cannot determine which numeric column defines slice sizes.

---

#### Question 33 [Bloom's Level: L4 - Analyze]
**Analyze the difference between `ax.set_xticks([0, 1, 2])` and `ax.set_xticklabels(['Jan', 'Feb', 'Mar'])`:**  
A) `set_xticks` sets the numeric coordinate positions where ticks appear; `set_xticklabels` assigns the custom text strings displayed at those positions  
B) Both commands do the same thing  
C) `set_xticks` is deprecated  
D) `set_xticklabels` changes the Y-axis  
**Answer: A**  
*Explanation:* `set_xticks` fixes the numeric coordinate locations of tick marks, and `set_xticklabels` maps human-readable strings to those locations.

---

#### Question 34 [Bloom's Level: L4 - Analyze]
**In `ax.legend(loc='best')`, how does Matplotlib determine the placement location?**  
A) Always places it in the upper-right corner  
B) Evaluates data point densities across 9 possible bounding quadrants and places the legend in the quadrant with the least overlap over data Artists  
C) Places it outside the canvas  
D) Hides the legend  
**Answer: B**  
*Explanation:* `loc='best'` runs an internal bounding-box collision algorithm to locate the emptiest quadrant.

---

### 6.5 Level 5 & 6: Evaluate & Create (Judgment, Architecture & Design)

#### Question 35 [Bloom's Level: L5 - Evaluate]
**Evaluate the optimal visualization strategy: A senior executive requires an executive dashboard displaying (1) Monthly Revenue Trajectory, (2) Product Category Revenue Breakdown, (3) Price Distribution, and (4) Advertising vs Sales Correlation on a single screen:**  
A) Create 4 separate HTML pages  
B) Create a $2 \times 2$ subplot grid using `fig, axes = plt.subplots(2, 2, figsize=(12, 8))` containing a Line Chart, Bar Chart, Histogram, and Scatter Plot, finalized with `plt.tight_layout()`  
C) Plot all 4 metrics on a single pie chart  
D) Print raw numbers in the terminal  
**Answer: B**  
*Explanation:* A multi-panel $2 \times 2$ subplot grid cleanly segregates distinct analytical dimensions (trends, categories, distributions, relationships) into an integrated dashboard view.

---

#### Question 36 [Bloom's Level: L5 - Evaluate]
**Evaluate which time-series diagnostic plot is most appropriate to determine whether an autoregressive AR(1) modeling approach is suitable for stock price prediction:**  
A) Pie Chart  
B) Lag Plot (`lag_plot(series, lag=1)`)  
C) Donut Chart  
D) Treemap  
**Answer: B**  
*Explanation:* A lag-1 plot directly visualizes $(y_t, y_{t+1})$ autoregressive dependency. A tight linear diagonal alignment confirms strong AR(1) suitability.

---

#### Question 37 [Bloom's Level: L6 - Create]
**Design a clean Python Matplotlib script that plots an annotated line chart of hospital patient visits with grid lines, peak annotations, and formatted axes:**  
A)
```python
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(months, visits, color='#2B5B84', marker='o', linewidth=2, label='Visits')
ax.set_title("Monthly Patient Visits", fontsize=14, fontweight='bold')
ax.set_xlabel("Month")
ax.set_ylabel("Visits")
ax.grid(True, linestyle='--', alpha=0.5)
ax.annotate('Peak (June: 1850)', xy=(5, 1850), xytext=(4, 1950),
            arrowprops=dict(facecolor='red', shrink=0.05))
ax.legend()
plt.tight_layout()
```
B)
```python
plt.plot(months, visits)
plt.save('plot.png')
```
C)
```python
visits.plot()
```
D)
```python
plt.title("Visits")
plt.show()
```
**Answer: A**  
*Explanation:* Option A builds a complete annotated visualization adhering to the OO paradigm, including labels, titles, grid, callout annotations, and layout optimization.

---

#### Question 38 [Bloom's Level: L6 - Create]
**Which code snippet correctly generates a pairwise scatter matrix for numeric features with KDE diagonal plots in Pandas?**  
A)
```python
from pandas.plotting import scatter_matrix
scatter_matrix(df[['age', 'salary', 'experience']], alpha=0.5, figsize=(8, 8), diagonal='kde')
```
B)
```python
df.plot.scatter_matrix()
```
C)
```python
df.scatter()
```
D)
```python
scatter_matrix(df, kind='3D')
```
**Answer: A**  
*Explanation:* Option A imports `scatter_matrix` from `pandas.plotting` and specifies numeric columns, transparency `alpha`, `figsize`, and `diagonal='kde'`.

---

#### Question 39 [Bloom's Level: L5 - Evaluate]
**Evaluate the effect of resampling uncertainty using `bootstrap_plot()`. What does a narrow, symmetric sampling distribution of the Mean indicate?**  
A) High estimator variance and unreliable data  
B) High statistical confidence and stability of the sample mean estimate across random subsamples  
C) Severe measurement errors  
D) Data is non-numeric  
**Answer: B**  
*Explanation:* A tight, narrow bootstrap distribution indicates low standard error and high precision/reliability of the estimated population mean.

---

#### Question 40 [Bloom's Level: L6 - Create]
**Design a Matplotlib layout that exports a publication-quality 300 DPI image of a sales dashboard without clipping external labels:**  
A) `plt.savefig('dashboard.png', dpi=300, bbox_inches='tight')`  
B) `plt.export('dashboard.png')`  
C) `fig.dump('dashboard.png', res='high')`  
D) `plt.show(dpi=300)`  
**Answer: A**  
*Explanation:* `plt.savefig()` with `dpi=300` ensures high resolution, and `bbox_inches='tight'` prevents text and legend clipping along the canvas perimeter.
