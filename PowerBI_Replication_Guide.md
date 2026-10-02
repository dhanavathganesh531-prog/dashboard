# Complete Power BI Desktop Replication Guide
## Project: Sales Analysis Report 2020 (Neomorphic & Embossed Design)

This guide walks you through building the exact dashboard from your reference image in **Power BI Desktop** in under 15 minutes.

---

## 📂 Project Assets in this Folder

All files are ready in `c:\Users\ganesh\OneDrive\Desktop\powerbi\`:

| File Name | Purpose |
| :--- | :--- |
| [`Sales_Analysis_2020.csv`](file:///c:/Users/ganesh/OneDrive/Desktop/powerbi/Sales_Analysis_2020.csv) | Ready-to-use dataset matching the exact numbers ($2.25M Sales, $1.01M Profit, 171 Orders, 116 Customers, 23K Quantity). |
| [`canvas_background.png`](file:///c:/Users/ganesh/OneDrive/Desktop/powerbi/canvas_background.png) | 1920x1080 HD canvas template with pre-rendered gradient, 3D embossed metallic cards, and header. |
| [`canvas_background.svg`](file:///c:/Users/ganesh/OneDrive/Desktop/powerbi/canvas_background.svg) | Scalable vector graphic source for the canvas background. |
| [`sales_analysis_theme.json`](file:///c:/Users/ganesh/OneDrive/Desktop/powerbi/sales_analysis_theme.json) | Power BI theme setting colors and 100% visual transparency. |
| [`Sales_Analysis_Measures.dax`](file:///c:/Users/ganesh/OneDrive/Desktop/powerbi/Sales_Analysis_Measures.dax) | Complete DAX calculations library with formatted numbers and Top-N filters. |
| [`dashboard_preview.html`](file:///c:/Users/ganesh/OneDrive/Desktop/powerbi/dashboard_preview.html) | Interactive live HTML5 preview with tab switching and hover tooltips. |
| [`icons/`](file:///c:/Users/ganesh/OneDrive/Desktop/powerbi/icons) | 5 vector KPI icons (Customers, Cart, Delivery Box, Sales Money Stack, Profit Hand). |

---

## 🚀 Step-by-Step Power BI Setup

### Step 1: Open Power BI Desktop & Load Data
1. Launch **Power BI Desktop**.
2. Click **Get Data** -> **Text/CSV**.
3. Select `c:\Users\ganesh\OneDrive\Desktop\powerbi\Sales_Analysis_2020.csv`.
4. Click **Load**.

---

### Step 2: Apply the Custom Theme
1. In the top ribbon, click **View**.
2. Click the dropdown arrow on **Themes** -> **Browse for themes**.
3. Select `sales_analysis_theme.json`.
4. *Result*: Color palettes and transparent visual backgrounds are automatically applied.

---

### Step 3: Apply the 3D Canvas Background
1. Ensure no visual is selected on the canvas.
2. In the **Visualizations** pane on the right, click **Format page** (the paintbrush with canvas icon).
3. Expand **Canvas background**:
   - Click **Image** -> **Browse** -> Select `canvas_background.png`.
   - Set **Image fit** to: `Fit` (or `Normal`).
   - Set **Transparency** to: `0%` (by default it is 100%, drag it to 0%).
4. *Result*: The sunset gradient, header, and card frames will instantly appear!

---

### Step 4: Create the DAX Measures Table
1. In the **Home** ribbon, click **Enter Data**.
2. Name the table `_Measures` and click **Load**.
3. Right-click `_Measures` in the Data pane -> **New Measure**.
4. Paste the DAX formulas from [`Sales_Analysis_Measures.dax`](file:///c:/Users/ganesh/OneDrive/Desktop/powerbi/Sales_Analysis_Measures.dax):
   ```dax
   Total Customers = DISTINCTCOUNT('Sales_Analysis_2020'[Customer Name])
   Total Orders    = DISTINCTCOUNT('Sales_Analysis_2020'[Order ID])
   Total Quantity  = SUM('Sales_Analysis_2020'[Quantity])
   Total Sales     = SUM('Sales_Analysis_2020'[Sales])
   Total Profit    = SUM('Sales_Analysis_2020'[Profit])
   Profit %        = DIVIDE([Total Profit], [Total Sales], 0)
   ```

---

### Step 5: Place the Visuals into the Pre-Rendered Card Frames

Because the canvas background already contains the 3D metallic card frames, you simply place your visuals inside the frames and make sure their backgrounds are set to **Off / 100% transparent**:

#### 1. Left Sidebar (5 KPI Cards)
- Insert a **Card** visual (or **New Card** visual).
- Drag in `[Total Customers]` (`116`).
- Under **Format Visual** -> **Callout Value**:
  - Color: `#C026D3` (Magenta / Pink)
  - Font Size: `28 pt`
  - Font: `Segoe UI Bold`
- Under **General** -> **Effects**:
  - Background: **Off** (Transparent)
  - Visual border: **Off**
- Add the customer icon using **Insert** -> **Image** -> `icons/customer_icon.svg` and place it to the left of the number.
- Repeat for the other 4 cards:
  - **Total Orders**: `171` + Cart Icon
  - **Total Quantity**: `23K` + Box Icon
  - **Total Sales**: `2.25M` + Money Stack Icon
  - **Total Profit**: `1.01M` + Profit Hand Icon

#### 2. Center Top (Donut Chart - Sales by Segment)
- Insert a **Donut Chart**.
- **Legend**: `Segment`
- **Values**: `Sales`
- **Format Visual**:
  - Slices:
    - Consumer: `#1E293B` (Dark Slate)
    - Corporate: `#0284C7` (Sky Blue)
    - Home Office: `#FB7185` (Soft Rose)
  - Detail labels: **Percent of total**
  - Background: **Off**

#### 3. Center Bottom Left (Top 5 Products by Sales)
- Insert a **Clustered Bar Chart** (Horizontal).
- **Y-axis**: `Product Name`
- **X-axis**: `Sales`
- In the **Filters** pane:
  - Filter type on `Product Name`: **Top N** -> Show top `5` by `Sales` -> Click **Apply filter**.
- **Bars Color**: `#F59E0B` (Amber / Golden Orange).
- **Data labels**: **On** (Display units: Millions).
- Background: **Off**.

#### 4. Center Bottom Right (Top 5 Customers by Sales)
- Insert a **Clustered Bar Chart** (Horizontal).
- **Y-axis**: `Customer Name`
- **X-axis**: `Sales`
- Filter type on `Customer Name`: **Top N** -> Show top `5` by `Sales`.
- **Bars**: Color with gradient from Navy (`#1E3A5F`) to Rose (`#E05D6F`).
- **Data labels**: **On**.
- Background: **Off**.

#### 5. Right Top (Sales vs Profit by City)
- Insert a **Clustered Bar Chart**.
- **Y-axis**: `City`
- **X-axis**: `Sales` and `Profit`
- Top 5 Cities filter.
- Series colors: Sales = `#F59E0B`, Profit = `#1E3A8A`.
- Background: **Off**.

#### 6. Right Middle (Monthly Sales Trend)
- Insert an **Area Chart** or **Line Chart**.
- **X-axis**: `Order Date (Month)`
- **Y-axis**: `Sales`
- Format:
  - Line stroke: **Dashed / Dotted**
  - Line color: `#2D3E5E`
  - Data markers: **On** (Filled circle, size 5)
  - Shaded Area transparency: `40%`
  - Data labels: **On** (Position: Above)
- Background: **Off**.

#### 7. Right Bottom (Profit % by Segment)
- Insert a **Donut Chart**.
- **Legend**: `Segment`
- **Values**: `Profit`
- Detail labels: **Percent of total**.
- Background: **Off**.

---

### Step 6: Configure the Tab Buttons (Sales by Month / Category / Segment)
1. In the **View** ribbon, enable **Bookmarks** and **Selection**.
2. Create 3 views of the Center Top card (Donut by Segment, Donut by Category, Monthly Column chart).
3. Hide/Unhide the respective visuals in the Selection pane and click **Add Bookmark** (`View_Month`, `View_Category`, `View_Segment`).
4. Add 3 transparent buttons over the top pill buttons, setting **Action** -> **Type: Bookmark** -> choose the corresponding bookmark.

---

🎉 **Done!** Your Power BI report will look identical to the reference image, with smooth neomorphic 3D embossed cards and high-contrast executive visuals.
