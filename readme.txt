# 113_2_visualize

Team 04 Visualization Final Project
SeeFood: Food Nutrition and Calorie Tracking Interactive Visualization System

---

System Overview

  * SeeFood(See Your Food 👀) is an interactive food nutrition visualization dashboard. Users can explore both macro and micro nutrition data of various foods, drag items onto a personalized plate to simulate daily intake, and utilize a range of features such as multi-dimensional filtering, nutritional comparison, and TDEE calculation.

---

🔗 Live Demo

deployed as a static website using GitHub Pages:

[👉 Click here to try it online](https://a1093351.github.io/)
Demo Vedio:👉  https://youtu.be/P7LwIqrf8ZQ
---

How to Run Locally

1. Open the main file
   Use a modern web browser (Chrome recommended) to open `index.html` in your project folder.

2. If you encounter data loading problems (CORS/browser security issues):
   Start a local server in the project directory:

   Using Python 3:

     ```bash
     python -m http.server 8000
     ```
   Then open `http://localhost:8000` in your browser.

---

Environment and Libraries

  * Any modern web browser (e.g., Chrome, Edge, Firefox)
  * No backend or Node.js installation required
  * Frontend uses [D3.js v6](https://github.com/d3/d3/releases/tag/v6.7.0) for interactive visualizations

---

Data Files

  * Main dataset file:

   `v2_test_labeled.csv`
   (Legacy or backup files: `test_labeled.csv`, `test_labeled_new.csv`)

  * Data CSV files must be in the same directory as `index.html` to function properly.

  * You can download these CSV files directly from this repository.

---

Data Source

  * Download the dataset from the [GitHub repository](https://github.com/a1093351/a1093351.github.io) or [direct CSV link](https://github.com/a1093351/a1093351.github.io/raw/main/v2_test_labeled.csv).

  * Data is based on the [USDA National Nutrient Database](https://www.kaggle.com/datasets/haithemhermessi/usda-national-nutrient-database?select=train.csv) test set (original source: United States Department of Agriculture).

  * Each record represents the nutrient composition of 100g of a specific food in the US, including calories, protein, and many other nutrients. This dataset is intended to support researchers, policy makers, and consumers in analyzing and predicting the nutritional value of foods. The data has been pre-processed and grouped for applications in food categorization and nutritional analysis.

  * The "Diet\_Group" field was automatically labeled using ChatGPT 4o-mini. Details on the labeling prompt can be found in `labeling.py`.

---

Team Contributions

* **Team 04**

  * M134020001 Ping-Yun Huang（黃品勻）: Interactive Web Components
  * M134020016 Yu-Fu Wang（王予芙）: Plate Module Development
  * M134020019 Liang-Tzu Huang（黃亮慈）: Visualization & Comparison Panel

Demo Vedio:https://youtu.be/P7LwIqrf8ZQ
---

**Professor and TAs,Thank you ! Have a wonderful summer break! 🥳❤️**

---