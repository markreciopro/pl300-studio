import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="PL-300 Visual Learning Studio",
    page_icon="📊",
    layout="centered"
)

st.title("📊 Microsoft PL-300 Visual Exam Studio")
st.markdown("Official Certification Practice Assessment — **Voice Reader, Memory Anchors, 60-Question Bank & Personalized Recommendations**")
st.write("---")

tab = st.sidebar.radio("Assessment Mode", [
    "Interactive Practice Hub (All 60 + Voice)", 
    "🆓 Microsoft Free Practice Assessment Hub", 
    "⏱️ Official Timed Exam Simulator (100 Min)", 
    "DAX & Power Query Flashcards", 
    "Exam Blueprint & Skill Weights"
])

# Complete 60 Verified Question Repository
questions = [
    {
        "id": 1,
        "type": "Multiple Choice",
        "domain": "Visualize and Analyze (25-30%)",
        "question": "You need to create a visual that allows users to search for values by which to filter the other visuals on the report page. Which type of visualization should you use?",
        "keywords": ["search box", "filter other visuals", "Slicer"],
        "muscle_memory": "👆 **Muscle Memory Action:** In Visualizations pane -> Click **Slicer** icon -> Drag target text field to Field well -> Open visual header settings -> Enable **Search**.",
        "mnemonic": "🔑 **Memory Anchor:** *'Slicer Searches'* — When users need type-ahead search filtering across a canvas, the Slicer visual is the native tool.",
        "options": ["Funnel", "Matrix", "Scatter chart", "Slicer"],
        "answer": "Slicer",
        "explanation": "The slicer visualization can be used to filter other visuals on the page and can have a search box enabled for easy value lookup.",
        "video_url": "http://www.youtube.com/watch?v=uHAnAxwDrn4"
    },
    {
        "id": 2,
        "type": "Multiple Choice",
        "domain": "Visualize and Analyze (25-30%)",
        "question": "You need to create a visual that displays data as a set of nested rectangles. Which type of visualization should you use?",
        "keywords": ["nested rectangles", "Treemap"],
        "muscle_memory": "👆 **Muscle Memory Action:** Visualizations pane -> Select **Treemap** -> Drag category to **Group** and measure to **Values**.",
        "mnemonic": "🔑 **Memory Anchor:** *'Trees have nested blocks'* — Treemaps represent hierarchical data using nested rectangles.",
        "options": ["Treemap", "Funnel", "Matrix", "Scatter chart"],
        "answer": "Treemap",
        "explanation": "A treemap visualization displays hierarchical data as a set of nested rectangles sized by values.",
        "video_url": "http://www.youtube.com/watch?v=a35rFVTsuh4"
    },
    {
        "id": 3,
        "type": "Multiple Choice",
        "domain": "Manage and Secure (15-20%)",
        "question": "Which file format is used for custom dashboard and report themes in Power BI?",
        "keywords": ["dashboard themes", "JSON format"],
        "muscle_memory": "👆 **Muscle Memory Action:** View tab -> Themes dropdown -> Browse for themes -> Select custom `.json` color palette file.",
        "mnemonic": "🔑 **Memory Anchor:** *'JavaScript Object Notation for Themes (.json)'* — Power BI theme files are structured in JSON.",
        "options": ["XML", "JSON", "CSV", "YAML"],
        "answer": "JSON",
        "explanation": "Custom themes in Power BI are imported using JSON files containing color codes, font families, and visual styling defaults.",
        "video_url": "http://www.youtube.com/watch?v=Ul8J-rKe0sc"
    },
    {
        "id": 4,
        "type": "Multiple Choice",
        "domain": "Manage and Secure (15-20%)",
        "question": "You need to configure automatic daily data refreshes for a report connecting to an on-premises SharePoint file server. What component must you install?",
        "keywords": ["on-premises SharePoint file server", "automatic daily refreshes", "gateway"],
        "muscle_memory": "👆 **Muscle Memory Action:** Download Gateway installer on local server -> Sign in with tenant admin -> Configure data source mapping in Power BI Service gateway settings.",
        "mnemonic": "🔑 **Memory Anchor:** *'On-premises needs a Gateway bridge'* — Local file sources require an enterprise or personal data gateway to reach the cloud.",
        "options": ["On-premises data gateway", "Power BI Desktop Developer Mode", "Azure Active Directory Connect", "Excel Add-in"],
        "answer": "On-premises data gateway",
        "explanation": "An on-premises data gateway acts as a bridge to securely transfer data between local network file servers and the Power BI cloud service.",
        "video_url": "http://www.youtube.com/watch?v=GwKyxPMeiBg"
    },
    {
        "id": 5,
        "type": "Multiple Choice",
        "domain": "Manage and Secure (15-20%)",
        "question": "At what level are dataset and semantic model certification permissions assigned in Power BI?",
        "keywords": ["certification permissions", "Tenant level"],
        "muscle_memory": "👆 **Muscle Memory Action:** Power BI Admin Portal -> Tenant settings -> Certifiers settings -> Assign specific security groups.",
        "mnemonic": "🔑 **Memory Anchor:** *'Tenant governs Trust'* — Certification rights are granted by administrators at the tenant level.",
        "options": ["Workspace level", "Tenant level", "Report level", "Visual level"],
        "answer": "Tenant level",
        "explanation": "Dataset certification authority is controlled globally by Power BI administrators via Tenant settings.",
        "video_url": "http://www.youtube.com/watch?v=JgizPdne_0Y"
    },
    {
        "id": 6,
        "type": "Multiple Choice",
        "domain": "Manage and Secure (15-20%)",
        "question": "What is the maximum number of scheduled data refreshes per day allowed for a semantic model in Power BI shared capacity?",
        "keywords": ["maximum scheduled refreshes", "shared capacity", "8 times"],
        "muscle_memory": "👆 **Muscle Memory Action:** Dataset settings -> Scheduled refresh -> Add time slot (up to 8 daily slots in shared capacity).",
        "mnemonic": "🔑 **Memory Anchor:** *'Shared capacity allows 8 daily refreshes'* — Premium/Fabric scales higher, but shared capacity caps at 8.",
        "options": ["4", "8", "24", "48"],
        "answer": "8",
        "explanation": "Power BI shared capacity permits up to 8 scheduled data refreshes per 24-hour period.",
        "video_url": "http://www.youtube.com/watch?v=uHAnAxwDrn4"
    },
    {
        "id": 7,
        "type": "Multiple Choice",
        "domain": "Manage and Secure (15-20%)",
        "question": "You manage a Power BI workspace in shared capacity containing semantic model DS1. What is the number of consecutive refresh failures of DS1 that will automatically disable the refresh schedule?",
        "keywords": ["consecutive refresh failures", "automatically disable", "4 failures"],
        "muscle_memory": "👆 **Muscle Memory Action:** Power BI Service -> Workspace dataset settings -> Monitor gateway connection status and refresh failure emails.",
        "mnemonic": "🔑 **Memory Anchor:** *'Four strikes and refresh is disabled'* — Power BI automatically turns off scheduled refreshes after 4 consecutive failures.",
        "options": ["2", "4", "16", "64"],
        "answer": "4",
        "explanation": "If there are 4 consecutive semantic model refresh failures, Power BI automatically disables the refresh schedule to protect resources.",
        "video_url": "http://www.youtube.com/watch?v=a35rFVTsuh4"
    },
    {
        "id": 8,
        "type": "Multiple Choice",
        "domain": "Manage and Secure (15-20%)",
        "question": "You have multiple redundant semantic models across different workspaces causing user confusion. What is the best practice to indicate reliable models?",
        "keywords": ["indicate reliable models", "Certify semantic models"],
        "muscle_memory": "👆 **Muscle Memory Action:** Semantic model settings -> Endorsement -> Select **Certified** -> Save.",
        "mnemonic": "🔑 **Memory Anchor:** *'Certify to Clarify'* — Endorsing models as Certified establishes official organizational trust.",
        "options": ["Certify semantic models", "Share direct PBIX files via email", "Rename all models with 'FINAL'", "Disable workspace search"],
        "answer": "Certify semantic models",
        "explanation": "Certifying semantic models signals to the organization that the data is authoritative and reviewed.",
        "video_url": "http://www.youtube.com/watch?v=Ul8J-rKe0sc"
    },
    {
        "id": 9,
        "type": "Multiple Choice",
        "domain": "Manage and Secure (15-20%)",
        "question": "When configuring Row-Level Security (RLS), which DAX function matches Microsoft Entra ID login credentials with user email columns in security tables?",
        "keywords": ["Row-Level Security", "USERPRINCIPALNAME"],
        "muscle_memory": "👆 **Muscle Memory Action:** Modeling tab -> Manage Roles -> Create role -> Filter table expression: `[Email] = USERPRINCIPALNAME()`.",
        "mnemonic": "🔑 **Memory Anchor:** *'Principal Name matches User Email'* — USERPRINCIPALNAME() grabs the active cloud login identity.",
        "options": ["USERNAME()", "USERPRINCIPALNAME()", "LOOKUPVALUE()", "RELATED()"],
        "answer": "USERPRINCIPALNAME()",
        "explanation": "USERPRINCIPALNAME() returns the UPN of the currently logged-in user, essential for dynamic RLS implementation.",
        "video_url": "http://www.youtube.com/watch?v=GwKyxPMeiBg"
    },
    {
        "id": 10,
        "type": "Multiple Choice",
        "domain": "Manage and Secure (15-20%)",
        "question": "You want to give business users read-only access to view published reports within a workspace without allowing them to modify underlying datasets. What role should you assign?",
        "keywords": ["read-only access", "Viewer role"],
        "muscle_memory": "👆 **Muscle Memory Action:** Workspace access settings -> Add user/group -> Assign role dropdown to **Viewer**.",
        "mnemonic": "🔑 **Memory Anchor:** *'Viewer views only'* — The Viewer role restricts users strictly to reading published reports.",
        "options": ["Admin", "Member", "Contributor", "Viewer"],
        "answer": "Viewer",
        "explanation": "The Viewer role provides read-only access for users to consume reports without editing models or datasets.",
        "video_url": "http://www.youtube.com/watch?v=JgizPdne_0Y"
    },
    {
        "id": 11,
        "type": "Multiple Choice",
        "domain": "Visualize and Analyze (25-30%)",
        "question": "Which visualization displays data in two or more dimensions and cross-highlights with other report visuals?",
        "keywords": ["two or more dimensions", "Matrix visual"],
        "muscle_memory": "👆 **Muscle Memory Action:** Visualizations pane -> Click **Matrix** icon -> Drag row, column, and value fields into position.",
        "mnemonic": "🔑 **Memory Anchor:** *'Matrix is a pivot table on canvas'* — Rows and columns cross-highlight seamlessly.",
        "options": ["Card", "Matrix", "Funnel", "Gauge"],
        "answer": "Matrix",
        "explanation": "A matrix visual displays data across multiple row and column dimensions with built-in cross-highlighting.",
        "video_url": "http://www.youtube.com/watch?v=uHAnAxwDrn4"
    },
    {
        "id": 12,
        "type": "Multiple Choice",
        "domain": "Visualize and Analyze (25-30%)",
        "question": "Which visual is best suited for displaying hierarchical proportions as a set of nested rectangles?",
        "keywords": ["hierarchical proportions", "Treemap"],
        "muscle_memory": "👆 **Muscle Memory Action:** Visualizations pane -> Select **Treemap** -> Set Group and Values.",
        "mnemonic": "🔑 **Memory Anchor:** *'Treemaps size by rectangles'* — Proportional hierarchical comparison.",
        "options": ["Treemap", "Line chart", "KPI", "Slicer"],
        "answer": "Treemap",
        "explanation": "Treemaps display hierarchical data using nested rectangles proportional to their numerical values.",
        "video_url": "http://www.youtube.com/watch?v=a35rFVTsuh4"
    },
    {
        "id": 13,
        "type": "Multiple Choice",
        "domain": "Visualize and Analyze (25-30%)",
        "question": "You need to display linear processes with sequentially connected stages transitioning from one stage to the next. What visual should you use?",
        "keywords": ["linear processes", "sequentially connected stages", "Funnel"],
        "muscle_memory": "👆 **Muscle Memory Action:** Visualizations pane -> Click **Funnel** icon -> Add Stage category and Value metric.",
        "mnemonic": "🔑 **Memory Anchor:** *'Funnels show pipeline stages'* — Sequential progression from start to finish.",
        "options": ["Funnel", "Card", "Matrix", "Scatter chart"],
        "answer": "Funnel",
        "explanation": "A funnel chart helps visualize a linear process with progressive sequential stages (e.g., sales pipelines).",
        "video_url": "http://www.youtube.com/watch?v=Ul8J-rKe0sc"
    },
    {
        "id": 14,
        "type": "Multiple Choice",
        "domain": "Visualize and Analyze (25-30%)",
        "question": "What is a mandatory prerequisite action needed before creating a custom R script visual inside Power BI Desktop?",
        "keywords": ["custom R script visual", "Install R on your computer"],
        "muscle_memory": "👆 **Muscle Memory Action:** Download CRAN R distribution -> Install locally -> Power BI Options -> R Scripting -> Verify R home directory path.",
        "mnemonic": "🔑 **Memory Anchor:** *'Install R before scripting'* — Power BI requires a local R engine to execute R visuals.",
        "options": ["Install R on your computer", "Purchase a Power BI Premium license", "Enable DirectQuery mode", "Create a SQL Server database"],
        "answer": "Install R on your computer",
        "explanation": "Power BI Desktop requires a local installation of Microsoft R Open or CRAN R to run and render R script visuals.",
        "video_url": "http://www.youtube.com/watch?v=GwKyxPMeiBg"
    },
    {
        "id": 15,
        "type": "Multiple Choice",
        "domain": "Visualize and Analyze (25-30%)",
        "question": "Which chart visual displays employee performance trending over months with automatic ranking changes and highest values at the top?",
        "keywords": ["ranking changes", "highest values at top", "Ribbon chart"],
        "muscle_memory": "👆 **Muscle Memory Action:** Visualizations pane -> Select **Ribbon chart** -> Drag Date to X-axis, Measure to Y-axis, Category to Legend.",
        "mnemonic": "🔑 **Memory Anchor:** *'Ribbons wrap ranks'* — Ribbon charts show rank changes clearly over time with cascading visual ribbons.",
        "options": ["Ribbon chart", "Pie chart", "Card", "Scatter chart"],
        "answer": "Ribbon chart",
        "explanation": "Ribbon charts highlight which category is highest, with the highest-ranking category always displayed at the top for each time period.",
        "video_url": "http://www.youtube.com/watch?v=JgizPdne_0Y"
    },
    {
        "id": 16,
        "type": "Multiple Choice",
        "domain": "Visualize and Analyze (25-30%)",
        "question": "You need to analyze employee performance trending over time while observing category rank shifts across months. What visual should you use?",
        "keywords": ["trending over time", "category rank shifts", "Ribbon chart"],
        "muscle_memory": "👆 **Muscle Memory Action:** Visualizations -> Ribbon chart -> Observe ribbon crossovers.",
        "mnemonic": "🔑 **Memory Anchor:** *'Ribbons reveal rank shifts'* — Perfect for tracking leaderboard changes over time.",
        "options": ["Ribbon chart", "Doughnut chart", "KPI", "Table"],
        "answer": "Ribbon chart",
        "explanation": "Ribbon charts effectively demonstrate rank changes over time, connecting categories visually with ribbons.",
        "video_url": "http://www.youtube.com/watch?v=uHAnAxwDrn4"
    },
    {
        "id": 17,
        "type": "Multiple Select",
        "domain": "Visualize and Analyze (25-30%)",
        "question": "You implement the Q&A feature in a report. You need to improve your Q&A search capabilities for end-users. Which two configurations can you add? (Choose two)",
        "keywords": ["improve Q&A search", "linguistic schema", "synonyms"],
        "muscle_memory": "👆 **Muscle Memory Action:** Model view -> Q&A setup -> Add synonyms to fields -> Export/Import linguistic schema.",
        "mnemonic": "🔑 **Memory Anchor:** *'Synonyms and schemas speak user language'* — Enhances natural language comprehension.",
        "options": ["Add a linguistic schema to the dataset.", "Add synonyms to model fields.", "Configure the dataset as a composite model.", "Organize columns into display folders."],
        "answer": ["Add a linguistic schema to the dataset.", "Add synonyms to model fields."],
        "explanation": "Adding synonyms and linguistic schemas helps Q&A understand business terms and vernacular used by report consumers.",
        "video_url": "http://www.youtube.com/watch?v=a35rFVTsuh4"
    },
    {
        "id": 18,
        "type": "Multiple Choice",
        "domain": "Visualize and Analyze (25-30%)",
        "question": "You are creating a bookmark that should display only a clustered bar chart while hiding three KPI cards on the report canvas. What action should you take in the Selection Pane?",
        "keywords": ["hide three KPI cards", "Selection Pane"],
        "muscle_memory": "👆 **Muscle Memory Action:** View tab -> Selection Pane -> Click the eye icon next to the 3 KPI cards to hide them -> Update bookmark.",
        "mnemonic": "🔑 **Memory Anchor:** *'Eye icon hides visuals for bookmarks'* — Selection pane manages visual visibility states.",
        "options": ["Hide the three cards in the Selection Pane", "Delete the three cards permanently", "Set card opacity to 0% in formatting", "Group visuals into a folder"],
        "answer": "Hide the three cards in the Selection Pane",
        "explanation": "The Selection Pane lets you toggle visual visibility (eye icon) to capture precise states in bookmarks.",
        "video_url": "http://www.youtube.com/watch?v=Ul8J-rKe0sc"
    },
    {
        "id": 19,
        "type": "Multiple Choice",
        "domain": "Visualize and Analyze (25-30%)",
        "question": "When configuring visual interactions, what happens when filtered data drops below a threshold (e.g., 1% of total) on a target visual?",
        "keywords": ["filtered data drops", "filter interaction"],
        "muscle_memory": "👆 **Muscle Memory Action:** Format tab -> Edit Interactions -> Click filter icon vs highlight icon.",
        "mnemonic": "🔑 **Memory Anchor:** *'Filter filters, Highlight highlights'* — Controls how visual selections isolate data.",
        "options": ["filter", "highlight", "hide", "disable"],
        "answer": "filter",
        "explanation": "Setting visual interactions to 'filter' completely removes items that fall outside selection criteria rather than cross-highlighting.",
        "video_url": "http://www.youtube.com/watch?v=GwKyxPMeiBg"
    },
    {
        "id": 20,
        "type": "Multiple Choice",
        "domain": "Visualize and Analyze (25-30%)",
        "question": "What is the default data displayed in a report page tooltip when hovering over a visual data point?",
        "keywords": ["default data displayed", "filtered cross-highlighted data"],
        "muscle_memory": "👆 **Muscle Memory Action:** Hover over visual data point -> Observe tooltip pop-up showing context values.",
        "mnemonic": "🔑 **Memory Anchor:** *'Tooltips mirror cross-highlighted context'* — Hovering displays the filtered subset.",
        "options": ["the filtered (cross-highlighted) data", "the entire dataset summary", "raw SQL connection strings", "static help text"],
        "answer": "the filtered (cross-highlighted) data",
        "explanation": "Default tooltips dynamically display the specific filtered and cross-highlighted data values for the hovered data point.",
        "video_url": "http://www.youtube.com/watch?v=JgizPdne_0Y"
    },
    {
        "id": 21,
        "type": "Multiple Choice",
        "domain": "Manage and Secure (15-20%)",
        "question": "How do you validate role-based row-level security (RLS) locally inside Power BI Desktop before publishing?",
        "keywords": ["validate role-based row-level security", "View as feature"],
        "muscle_memory": "👆 **Muscle Memory Action:** Modeling tab -> **View as** -> Select role checkbox -> Test visual filtering.",
        "mnemonic": "🔑 **Memory Anchor:** *'View as tests security locally'* — Instantly simulates what different user roles will see.",
        "options": ["In the Report view, activate the View as feature", "Export PBIX to Excel", "Inspect Power Query formula bar", "Check Windows Event Logs"],
        "answer": "In the Report view, activate the View as feature",
        "explanation": "The 'View as' button under Modeling allows you to preview reports under specific RLS roles or user emails.",
        "video_url": "http://www.youtube.com/watch?v=uHAnAxwDrn4"
    },
    {
        "id": 22,
        "type": "Multiple Select",
        "domain": "Visualize and Analyze (25-30%)",
        "question": "You need to create a visual that will display information on a continuous axis. Which two data types can be used to display a continuous axis on a visual? (Choose two)",
        "keywords": ["continuous axis", "Date", "Decimal Number"],
        "muscle_memory": "👆 **Muscle Memory Action:** Data view -> Check column data type -> Ensure Date, Time, or Numeric format is set.",
        "mnemonic": "🔑 **Memory Anchor:** *'Numbers and Dates flow continuously'* — Categorical text breaks continuous axes.",
        "options": ["Binary", "Date", "Decimal Number", "Text"],
        "answer": ["Date", "Decimal Number"],
        "explanation": "Date and numeric data types support continuous range axes, whereas text and binary values are discrete.",
        "video_url": "http://www.youtube.com/watch?v=a35rFVTsuh4"
    },
    {
        "id": 23,
        "type": "Multiple Choice",
        "domain": "Visualize and Analyze (25-30%)",
        "question": "Which native AI visual helps explain the factors and correlations driving a specific target metric or category?",
        "keywords": ["explain factors and correlations", "Key influencers visual"],
        "muscle_memory": "👆 **Muscle Memory Action:** Visualizations pane -> Click **Key Influencers** icon -> Set Analyze and Explain by fields.",
        "mnemonic": "🔑 **Memory Anchor:** *'Key Influencers find the why'* — AI machine learning drivers for metrics.",
        "options": ["Key influencers visual", "Matrix visual", "Line chart", "Card visual"],
        "answer": "Key influencers visual",
        "explanation": "The Key Influencers visual uses built-in machine learning to analyze metrics and surface top driving factors.",
        "video_url": "http://www.youtube.com/watch?v=Ul8J-rKe0sc"
    },
    {
        "id": 24,
        "type": "Multiple Choice",
        "domain": "Visualize and Analyze (25-30%)",
        "question": "You need to add an analytics line to a visual. The value for the line must equal the result of a DAX measure that always returns a consistent single value. Which type of analytics line should you use?",
        "keywords": ["analytics line", "DAX measure", "Constant line"],
        "muscle_memory": "👆 **Muscle Memory Action:** Visualizations -> Analytics pane -> Constant line -> Add line -> Select fx (measure) for value.",
        "mnemonic": "🔑 **Memory Anchor:** *'Constant lines accept DAX measures'* — Dynamic benchmarks on charts.",
        "options": ["Average line", "Constant line", "Max line", "Min line"],
        "answer": "Constant line",
        "explanation": "A Constant line on X or Y axes supports dynamic DAX measures returning single scalar values.",
        "video_url": "http://www.youtube.com/watch?v=GwKyxPMeiBg"
    },
    {
        "id": 25,
        "type": "Multiple Choice",
        "domain": "Model the Data (25-30%)",
        "question": "You need to filter sales data by region. What relationship configuration should you establish between the 'Regions' lookup table and the 'Sales' table?",
        "keywords": ["filter sales data by region", "one-to-many relationship"],
        "muscle_memory": "👆 **Muscle Memory Action:** Model view -> Drag RegionID from Regions table and drop onto RegionID in Sales table -> Verify 1:* arrow.",
        "mnemonic": "🔑 **Memory Anchor:** *'One region, many sales'* — Standard star schema lookup to fact relationship.",
        "options": ["Create a one-to-many relationship from the 'Regions' table to 'Sales' table", "Create a many-to-many bidirectional relationship", "Merge tables in Power Query", "Write a DAX calculated column"],
        "answer": "Create a one-to-many relationship from the 'Regions' table to 'Sales' table",
        "explanation": "A one-to-many relationship from dimension table (Regions) to fact table (Sales) ensures proper filter propagation.",
        "video_url": "http://www.youtube.com/watch?v=JgizPdne_0Y"
    },
    {
        "id": 26,
        "type": "Multiple Choice",
        "domain": "Model the Data (25-30%)",
        "question": "When building a star schema model, what is the recommended filter direction for one-to-many relationships pointing from dimension tables to a fact table?",
        "keywords": ["star schema", "single-direction cross-filtering"],
        "muscle_memory": "👆 **Muscle Memory Action:** Edit Relationship -> Cross filter direction -> Set to **Single**.",
        "mnemonic": "🔑 **Memory Anchor:** *'Single-direction flows fast'* — Optimizes VertiPaq engine query performance.",
        "options": ["Single (from dimension to fact)", "Both (Bidirectional)", "None", "Cross-join"],
        "answer": "Single (from dimension to fact)",
        "explanation": "Single cross-filtering from dimension to fact tables maximizes performance and prevents ambiguity.",
        "video_url": "http://www.youtube.com/watch?v=uHAnAxwDrn4"
    },
    {
        "id": 27,
        "type": "Multiple Select",
        "domain": "Model the Data (25-30%)",
        "question": "Which actions are necessary to ensure a custom calendar table supports time intelligence functions like SAMEPERIODLASTYEAR? (Choose two)",
        "keywords": ["time intelligence functions", "Mark the table as a date table", "contiguous date range"],
        "muscle_memory": "👆 **Muscle Memory Action:** Modeling tab -> Mark as date table -> Select Date column.",
        "mnemonic": "🔑 **Memory Anchor:** *'Mark as Date Table unlocks time'* — Mandatory step for time intelligence DAX.",
        "options": ["Mark the table as a date table", "Ensure a contiguous date range without gaps", "Set relationship cross-filter to Both", "Convert date column to Text"],
        "answer": ["Mark the table as a date table", "Ensure a contiguous date range without gaps"],
        "explanation": "Time intelligence requires marking the table explicitly as a date table and having continuous dates.",
        "video_url": "http://www.youtube.com/watch?v=a35rFVTsuh4"
    },
    {
        "id": 28,
        "type": "Multiple Select",
        "domain": "Model the Data (25-30%)",
        "question": "Which model items can be organized into custom display folders in Power BI Desktop? (Choose two)",
        "keywords": ["display folders", "Calculated column", "Measure"],
        "muscle_memory": "👆 **Muscle Memory Action:** Model view -> Select measure/column -> Properties pane -> Display folder -> Type folder name.",
        "mnemonic": "🔑 **Memory Anchor:** *'Measures and columns organize in folders'* — Cleans up field list clutter.",
        "options": ["Calculated column", "Measure", "Table relationship", "Data gateway cluster"],
        "answer": ["Calculated column", "Measure"],
        "explanation": "Measures and calculated columns can be neatly structured into display folders for better model navigation.",
        "video_url": "http://www.youtube.com/watch?v=Ul8J-rKe0sc"
    },
    {
        "id": 29,
        "type": "Multiple Select",
        "domain": "Model the Data (25-30%)",
        "question": "You are designing a semantic model. Which two modeling best practices should you follow for fact and dimension tables? (Choose two)",
        "keywords": ["star schema best practices", "one-to-many relationships", "single-direction cross-filtering"],
        "muscle_memory": "👆 **Muscle Memory Action:** Model view -> Connect Lookup keys to Fact keys -> Verify 1:* single filter arrows.",
        "mnemonic": "🔑 **Memory Anchor:** *'Dimensions point to facts'* — Classic star schema design.",
        "options": ["Define one-to-many relationships from dimension tables to the fact table", "Set single-direction cross-filtering", "Use bidirectional relationships on all tables", "Combine all tables into a single wide table"],
        "answer": ["Define one-to-many relationships from dimension tables to the fact table", "Set single-direction cross-filtering"],
        "explanation": "Star schema best practices dictate one-to-many relationships with single direction from lookup dimensions to fact tables.",
        "video_url": "http://www.youtube.com/watch?v=GwKyxPMeiBg"
    },
    {
        "id": 30,
        "type": "Multiple Choice",
        "domain": "Model the Data (25-30%)",
        "question": "You plan to use the calculated table functionality to add a duplicate table in Power BI Desktop. Which characteristics of the original table will be duplicated?",
        "keywords": ["calculated table functionality", "data only"],
        "muscle_memory": "👆 **Muscle Memory Action:** Modeling tab -> New Table -> `CopyTable = 'OriginalTable'` -> Enter.",
        "mnemonic": "🔑 **Memory Anchor:** *'Calculated tables duplicate data only'* — Formatting and hierarchies must be recreated.",
        "options": ["hierarchies only", "data and hierarchies only", "data and column formatting only", "data only"],
        "answer": "data only",
        "explanation": "Calculated tables duplicate underlying row data via DAX expressions, but model configurations like formatting or hierarchies are not inherited.",
        "video_url": "http://www.youtube.com/watch?v=JgizPdne_0Y"
    },
    {
        "id": 31,
        "type": "Multiple Select",
        "domain": "Model the Data (25-30%)",
        "question": "In which Power BI Desktop views can you create a new DAX measure? (Choose two)",
        "keywords": ["create a new DAX measure", "Table view", "Report view"],
        "muscle_memory": "👆 **Muscle Memory Action:** Right-click table in Data pane (in Report or Table view) -> New measure.",
        "mnemonic": "🔑 **Memory Anchor:** *'Measures live in Report or Table view'* — Accessible wherever data is explored.",
        "options": ["Table view", "Report view", "Power Query Editor", "Model view (Relationships)"],
        "answer": ["Table view", "Report view"],
        "explanation": "Measures can be authored in Report view or Table view (they are not created inside Power Query Editor).",
        "video_url": "http://www.youtube.com/watch?v=uHAnAxwDrn4"
    },
    {
        "id": 32,
        "type": "Multiple Select",
        "domain": "Model the Data (25-30%)",
        "question": "Which two model items are created entirely through DAX-generated expressions in Power BI? (Choose two)",
        "keywords": ["DAX-generated expressions", "calculated table", "numeric range parameter"],
        "muscle_memory": "👆 **Muscle Memory Action:** Modeling tab -> New Table / New Parameter.",
        "mnemonic": "🔑 **Memory Anchor:** *'Calculated tables and parameters use DAX'* — Dynamic data structures.",
        "options": ["calculated table", "numeric range parameter", "Power Query custom function", "Gateway data source connection"],
        "answer": ["calculated table", "numeric range parameter"],
        "explanation": "Calculated tables and what-if parameters are built natively using underlying DAX expressions.",
        "video_url": "http://www.youtube.com/watch?v=a35rFVTsuh4"
    },
    {
        "id": 33,
        "type": "Multiple Select",
        "domain": "Manage and Secure (15-20%)",
        "question": "Which actions are required to set up row-level security matching user principal names for salespeople? (Choose two)",
        "keywords": ["row-level security", "Add a DAX expression filter", "Create a role"],
        "muscle_memory": "👆 **Muscle Memory Action:** Modeling -> Manage roles -> New role -> Add DAX filter `[Email] = USERPRINCIPALNAME()`.",
        "mnemonic": "🔑 **Memory Anchor:** *'Create role then filter with DAX'* — Two-step RLS setup.",
        "options": ["Add a DAX expression filter to the Salesperson table", "Create a role", "Enable DirectQuery mode across all tables", "Publish report to a public web link"],
        "answer": ["Add a DAX expression filter to the Salesperson table", "Create a role"],
        "explanation": "Implementing RLS requires creating a named security role and applying a DAX filter condition using USERPRINCIPALNAME().",
        "video_url": "http://www.youtube.com/watch?v=Ul8J-rKe0sc"
    },
    {
        "id": 34,
        "type": "Multiple Choice",
        "domain": "Prepare the Data (25-30%)",
        "question": "In Power BI Desktop, you plan to use M-language to define a common date table spanning a period of 10 years. What M-language syntax specifies consecutive days?",
        "keywords": ["M-language syntax", "consecutive days", "#duration"],
        "muscle_memory": "👆 **Muscle Memory Action:** Power Query Editor -> Advanced Editor -> Use `#duration(1, 0, 0, 0)` for 1-day step increments.",
        "mnemonic": "🔑 **Memory Anchor:** *'Duration defines date steps in M'* — `#duration(1,0,0,0)` adds single day increments.",
        "options": ["#date", "#duration", "List.Combine", "List.Durations"],
        "answer": "#duration",
        "explanation": "The `#duration` function in Power Query M-language allows you to specify time increments (days, hours, minutes, seconds) for list generation.",
        "video_url": "http://www.youtube.com/watch?v=GwKyxPMeiBg"
    },
    {
        "id": 35,
        "type": "Multiple Choice",
        "domain": "Prepare the Data (25-30%)",
        "question": "You need to reduce cardinality for hourly temperature analysis on a massive datetime column. What transformation action should you take?",
        "keywords": ["reduce cardinality", "start of the hour"],
        "muscle_memory": "👆 **Muscle Memory Action:** Power Query -> Transform -> Time -> **Start of Hour**.",
        "mnemonic": "🔑 **Memory Anchor:** *'Truncate time to drop cardinality'* — Groups timestamps into clean hourly buckets.",
        "options": ["Create a column that contains the time values for the start of the hour of the Reading Time value", "Multiply timestamp by 24", "Delete all rows with decimal temperatures", "Convert timestamp to Text"],
        "answer": "Create a column that contains the time values for the start of the hour of the Reading Time value",
        "explanation": "Extracting the start of the hour truncates minute and second precision, significantly lowering distinct cardinality and improving compression.",
        "video_url": "http://www.youtube.com/watch?v=JgizPdne_0Y"
    },
    {
        "id": 36,
        "type": "Multiple Choice",
        "domain": "Manage and Secure (15-20%)",
        "question": "What is the recommended first step before starting Performance Analyzer tests in Power BI Desktop to ensure the data engine cache does not skew results?",
        "keywords": ["Performance Analyzer", "cache", "DAX Studio"],
        "muscle_memory": "👆 **Muscle Memory Action:** Open DAX Studio -> Connect to PBI Desktop model -> Model menu -> Clear Cache.",
        "mnemonic": "🔑 **Memory Anchor:** *'Clear cache in DAX Studio first'* — Ensures cold-cache benchmark accuracy.",
        "options": ["Connect DAX Studio to the data model and clear cache", "Restart Windows Explorer", "Export all tables to CSV", "Disable background data refresh"],
        "answer": "Connect DAX Studio to the data model and clear cache",
        "explanation": "Clearing the VertiPaq cache via DAX Studio ensures Performance Analyzer records true query execution times rather than cached memory responses.",
        "video_url": "http://www.youtube.com/watch?v=uHAnAxwDrn4"
    },
    {
        "id": 37,
        "type": "Multiple Choice",
        "domain": "Manage and Secure (15-20%)",
        "question": "You need to disable the default behavior in Power BI Desktop that automatically applies cross-highlighting and filtering of visuals within the same report. What option should you configure?",
        "keywords": ["disable cross-highlighting", "Reduce number of queries"],
        "muscle_memory": "👆 **Muscle Memory Action:** File -> Options and settings -> Options -> Current File -> Query Reduction -> Check 'Disable cross highlighting/filtering'.",
        "mnemonic": "🔑 **Memory Anchor:** *'Reduce number of queries stops auto-crossfiring'* — Controls report query chatter.",
        "options": ["the Filters Query reduction settings", "the Persistent filters of Report settings", "the Reduce number of queries sent by Query reduction setting", "the Slicers Query reduction settings"],
        "answer": "the Reduce number of queries sent by Query reduction setting",
        "explanation": "Query reduction options allow disabling automatic cross-highlighting to optimize performance on large enterprise models.",
        "video_url": "http://www.youtube.com/watch?v=a35rFVTsuh4"
    },
    {
        "id": 38,
        "type": "Multiple Select",
        "domain": "Prepare the Data (25-30%)",
        "question": "What are two performance benefits of removing unnecessary columns from your Power BI data model? (Choose two)",
        "keywords": ["removing unnecessary columns", "refresh speed", "model size"],
        "muscle_memory": "👆 **Muscle Memory Action:** Power Query Editor -> Choose Columns -> Uncheck unneeded fields.",
        "mnemonic": "🔑 **Memory Anchor:** *'Fewer columns = smaller model & faster refresh'* — VertiPaq loves lean tables.",
        "options": ["increasing the refresh speed", "reducing the size of the data model", "enabling bidirectional RLS automatically", "forcing DirectQuery mode"],
        "answer": ["increasing the refresh speed", "reducing the size of the data model"],
        "explanation": "Dropping unused columns reduces memory footprint (VertiPaq footprint) and accelerates refresh times.",
        "video_url": "http://www.youtube.com/watch?v=Ul8J-rKe0sc"
    },
    {
        "id": 39,
        "type": "Multiple Choice",
        "domain": "Manage and Secure (15-20%)",
        "question": "What is the recommended initial action to take inside a PBIX file before evaluating visual rendering times with Performance Analyzer?",
        "keywords": ["Performance Analyzer", "Add a blank page"],
        "muscle_memory": "👆 **Muscle Memory Action:** Add blank page -> Switch to it before starting recording to ensure clean render slate.",
        "mnemonic": "🔑 **Memory Anchor:** *'Start on a blank page for clean analyzer runs'* — Prevents pre-rendered visual cache interference.",
        "options": ["Add a blank page to the PBIX file", "Export the model to XML", "Delete all DAX measures", "Turn off Windows firewall"],
        "answer": "Add a blank page to the PBIX file",
        "explanation": "Starting your test session on a blank page ensures that switching views triggers a fresh render evaluation for Performance Analyzer.",
        "video_url": "http://www.youtube.com/watch?v=GwKyxPMeiBg"
    },
    {
        "id": 40,
        "type": "Multiple Select",
        "domain": "Manage and Secure (15-20%)",
        "question": "Which cloud file locations support scheduled refresh in Power BI using Microsoft 365 organizational credentials without requiring an on-premises data gateway? (Choose two)",
        "keywords": ["cloud file locations", "OneDrive for Business", "SharePoint – Team Sites"],
        "muscle_memory": "👆 **Muscle Memory Action:** Save PBIX to OneDrive/SharePoint -> Power BI Service -> Dataset settings -> Cloud connection credentials.",
        "mnemonic": "🔑 **Memory Anchor:** *'OneDrive and SharePoint sync directly to cloud'* — No gateway needed for M365 cloud files.",
        "options": ["OneDrive for Business", "SharePoint – Team Sites", "Local corporate file server share", "Local developer laptop C: drive"],
        "answer": ["OneDrive for Business", "SharePoint – Team Sites"],
        "explanation": "Power BI connects natively to OneDrive for Business and SharePoint Online without needing an on-premises gateway.",
        "video_url": "http://www.youtube.com/watch?v=JgizPdne_0Y"
    },
    {
        "id": 41,
        "type": "Multiple Choice",
        "domain": "Prepare the Data (25-30%)",
        "question": "You have a Power BI data model containing an Orders table with many columns. You need to resolve an error when publishing and reduce model size while minimizing scheduled refresh queries and keeping the original Orders table unchanged. What should you do?",
        "keywords": ["Reference Orders", "disable load for Orders"],
        "muscle_memory": "👆 **Muscle Memory Action:** Power Query -> Right-click Orders -> **Reference** -> Keep only required columns -> Uncheck 'Enable load' on original Orders table.",
        "mnemonic": "🔑 **Memory Anchor:** *'Reference and disable load keeps staging clean'* — Keeps source query intact while loading only slimmed columns.",
        "options": ["Duplicate Orders, and then reference the duplicate.", "Move the four required columns to a new table and update visuals.", "Reference Orders, remove all columns from reference except the four used, and disable load for Orders.", "Split queries so each visual queries only required fields."],
        "answer": "Reference Orders, remove all columns from reference except the four used, and disable load for Orders.",
        "explanation": "Referencing the table allows Orders to act as an unloaded staging query while loading only the slimmed reference table, minimizing model size and refresh queries.",
        "video_url": "http://www.youtube.com/watch?v=uHAnAxwDrn4"
    },
    {
        "id": 42,
        "type": "Multiple Choice",
        "domain": "Prepare the Data (25-30%)",
        "question": "You need to combine multiple CSV files from a shared folder. What is the most efficient Power Query folder connector method?",
        "keywords": ["combine multiple CSV files", "Combine & Transform Data"],
        "muscle_memory": "👆 **Muscle Memory Action:** Get Data -> Folder -> Click dropdown next to Combine -> **Combine & Transform Data**.",
        "mnemonic": "🔑 **Memory Anchor:** *'Combine & Transform automates folder merging'* — Builds helper functions automatically.",
        "options": ["Query the folder and select Combine & Transform Data.", "Query the folder and select Transform Data.", "Merge each CSV file manually in DAX.", "Import each file into Excel first."],
        "answer": "Query the folder and select Combine & Transform Data.",
        "explanation": "Choosing 'Combine & Transform Data' automatically creates the sample file transformation pipeline and expands all files in the folder cleanly.",
        "video_url": "http://www.youtube.com/watch?v=a35rFVTsuh4"
    },
    {
        "id": 43,
        "type": "Multiple Choice",
        "domain": "Prepare the Data (25-30%)",
        "question": "When importing data from a folder containing multiple structured CSV files, what action should you take to consolidate them properly?",
        "keywords": ["consolidate them properly", "Combine & Transform Data"],
        "muscle_memory": "👆 **Muscle Memory Action:** Get Data -> Folder -> Combine & Transform.",
        "mnemonic": "🔑 **Memory Anchor:** *'Combine and Transform handles multi-file ingestion'* — Native folder merge pipeline.",
        "options": ["Combine & Transform Data", "Transform Data only", "Append queries manually one by one", "Disable table load"],
        "answer": "Combine & Transform Data",
        "explanation": "Selecting Combine & Transform Data invokes Power Query's automated multi-file combination mechanics.",
        "video_url": "http://www.youtube.com/watch?v=Ul8J-rKe0sc"
    },
    {
        "id": 44,
        "type": "Multiple Select",
        "domain": "Prepare the Data (25-30%)",
        "question": "You have a sales table where a numeric column contains null values and text corruptions. Which two Power Query actions should you perform to clean the column? (Choose two)",
        "keywords": ["numeric column contains null values and text corruptions", "filter out null values", "replace text with numbers"],
        "muscle_memory": "👆 **Muscle Memory Action:** Power Query -> Transform/Replace values -> Remove error rows.",
        "mnemonic": "🔑 **Memory Anchor:** *'Filter errors and replace nulls before typing'* — Cleans data prior to integer casting.",
        "options": ["Use Power Query to filter out null values or handle errors", "Use Power Query to replace text with numbers or remove corrupted rows", "Convert table to DirectQuery mode", "Write a DAX CALCULATE measure"],
        "answer": ["Use Power Query to filter out null values or handle errors", "Use Power Query to replace text with numbers or remove corrupted rows"],
        "explanation": "Handling errors and cleaning text anomalies in Power Query prevents type conversion failures during refresh.",
        "video_url": "http://www.youtube.com/watch?v=GwKyxPMeiBg"
    },
    {
        "id": 45,
        "type": "Multiple Choice",
        "domain": "Visualize and Analyze (25-30%)",
        "question": "You notice certain product categories disappear from matrix visuals when they have no sales during specific months. What option should you enable?",
        "keywords": ["categories disappear", "show items with no data"],
        "muscle_memory": "👆 **Muscle Memory Action:** Visualizations pane -> Field well -> Right-click category field -> Check **Show items with no data**.",
        "mnemonic": "🔑 **Memory Anchor:** *'Show items with no data keeps missing rows visible'* — Prevents matrix blank collapse.",
        "options": ["Enable the option to show items with no data", "Apply a Page-level filter", "Enable bidirectional cross-filtering", "Delete blank rows in Power Query"],
        "answer": "Enable the option to show items with no data",
        "explanation": "Enabling 'Show items with no data' forces matrix and table rows/columns to display even when underlying measures evaluate to blank.",
        "video_url": "http://www.youtube.com/watch?v=JgizPdne_0Y"
    },
    {
        "id": 46,
        "type": "Multiple Select",
        "domain": "Prepare the Data (25-30%)",
        "question": "A ProductID column contains a leading prefix string (e.g., 'PRD-1005'). You need to remove the 'PRD-' prefix. Which two Power Query transformations can you use? (Choose two)",
        "keywords": ["remove leading prefix", "Replace Values", "Trim"],
        "muscle_memory": "👆 **Muscle Memory Action:** Power Query -> Transform column -> Replace Values / Extract text after delimiter.",
        "mnemonic": "🔑 **Memory Anchor:** *'Replace or Extract strips prefixes'* — Standard text cleaning transformations.",
        "options": ["Replace Values", "Trim", "Merge Queries", "Unpivot Columns"],
        "answer": ["Replace Values", "Trim"],
        "explanation": "Replace Values substitutes specific text strings, and Trim removes extraneous whitespace, allowing clean prefix removal.",
        "video_url": "http://www.youtube.com/watch?v=uHAnAxwDrn4"
    },
    {
        "id": 47,
        "type": "Multiple Select",
        "domain": "Manage and Secure (15-20%)",
        "question": "You need to publish and update a Power BI app from a workspace. Which two workspace roles allow a user to publish or update an app? (Choose two)",
        "keywords": ["publish an app", "Admin", "Member"],
        "muscle_memory": "👆 **Muscle Memory Action:** Workspace -> **Update app** (top right) -> Configure Navigation & Audience -> Publish app.",
        "mnemonic": "🔑 **Memory Anchor:** *'Admins and Members manage Apps'* — Contributors can edit content, but only Admins and Members can publish apps.",
        "options": ["Admin", "Member", "Contributor", "Viewer"],
        "answer": ["Admin", "Member"],
        "explanation": "Only users assigned the Admin or Member workspace role have permissions to publish or update a Power BI app.",
        "video_url": "http://www.youtube.com/watch?v=JgizPdne_0Y"
    },
    {
        "id": 48,
        "type": "Multiple Choice",
        "domain": "Model the Data (25-30%)",
        "question": "You have a composite model with a massive DirectQuery fact table and small lookup dimension tables. Which storage mode should you configure on the dimension tables to optimize slicer and filter query performance?",
        "keywords": ["composite model", "lookup dimension tables", "Dual"],
        "muscle_memory": "👆 **Muscle Memory Action:** Model view -> Select dimension table -> Properties pane -> Advanced -> Storage mode -> **Dual**.",
        "mnemonic": "🔑 **Memory Anchor:** *'Dual serves both worlds'* — Dual tables act as Import for slicers and DirectQuery when joined to DirectQuery facts.",
        "options": ["Dual", "DirectQuery", "Live Connection", "Disconnected"],
        "answer": "Dual",
        "explanation": "Setting dimension tables to Dual storage mode allows Power BI to serve slicer queries from fast in-memory cache while pushing joins down to the DirectQuery source.",
        "video_url": "http://www.youtube.com/watch?v=uHAnAxwDrn4"
    },
    {
        "id": 49,
        "type": "Multiple Choice",
        "domain": "Visualize and Analyze (25-30%)",
        "question": "You want report users to right-click a specific product category on a summary bar chart and navigate directly to a detail page filtered to that product. What feature should you configure on the destination page?",
        "keywords": ["right-click", "navigate to detail page filtered", "Drillthrough"],
        "muscle_memory": "👆 **Muscle Memory Action:** Destination page -> Visualizations pane -> Drag Category field into **Drillthrough** well -> Auto-generates Back button.",
        "mnemonic": "🔑 **Memory Anchor:** *'Drillthrough jumps pages with context'* — Right-click a data point to drill into a dedicated detail page.",
        "options": ["Drillthrough", "Bookmarks", "Sync Slicers", "Q&A"],
        "answer": "Drillthrough",
        "explanation": "Adding a field to the Drillthrough well on a destination page enables users to right-click a data point on any source page and jump to that page filtered by the selected item.",
        "video_url": "http://www.youtube.com/watch?v=GwKyxPMeiBg"
    },
    {
        "id": 50,
        "type": "Multiple Choice",
        "domain": "Prepare the Data (25-30%)",
        "question": "During a scheduled refresh, a Power BI semantic model fails due to data type conversion errors in a specific column. You want to isolate and inspect the exact rows causing the failure in Power Query Editor. What should you do?",
        "keywords": ["isolate exact rows causing failure", "Keep Errors"],
        "muscle_memory": "👆 **Muscle Memory Action:** Power Query Editor -> Home tab -> Keep Rows -> **Keep Errors** -> Inspect failing values.",
        "mnemonic": "🔑 **Memory Anchor:** *'Keep Errors isolates the culprits'* — Filters the preview down to only rows throwing conversion errors.",
        "options": ["Select Keep Errors on the column", "Enable Auto Date/Time", "Switch the table to Dual mode", "Apply a Row-Level Security filter"],
        "answer": "Select Keep Errors on the column",
        "explanation": "Using 'Keep Errors' in Power Query Editor filters the table to show only rows containing errors, making it easy to diagnose data type conversion issues.",
        "video_url": "http://www.youtube.com/watch?v=a35rFVTsuh4"
    },
    {
        "id": 51,
        "type": "Multiple Choice",
        "domain": "Model the Data (25-30%)",
        "question": "When should you create a calculated column instead of a DAX measure?",
        "keywords": ["calculated column vs measure", "row context", "slicers and rows"],
        "muscle_memory": "👆 **Muscle Memory Action:** Data View -> Modeling tab -> New Column. Used when you need values evaluated per row for slicers or grouping.",
        "mnemonic": "🔑 **Memory Anchor:** *'Columns consume RAM for rows, Measures calculate on the fly'* — Use columns for slicing and measures for aggregating.",
        "options": ["When you need to slice and filter data by the calculated result", "When calculating total sales revenue across all filtered rows", "When using time intelligence functions like SAMEPERIODLASTYEAR", "When memory optimization is top priority"],
        "answer": "When you need to slice and filter data by the calculated result",
        "explanation": "Calculated columns compute values for every row during data refresh and store them in memory, making them ideal for slicers, rows, and columns in matrices.",
        "video_url": "http://www.youtube.com/watch?v=uHAnAxwDrn4"
    },
    {
        "id": 52,
        "type": "Multiple Choice",
        "domain": "Model the Data (25-30%)",
        "question": "What is the primary performance advantage of storing numeric transactional amounts as measures rather than calculated columns in Power BI?",
        "keywords": ["measures vs calculated columns", "VertiPaq storage", "on-the-fly calculation"],
        "muscle_memory": "👆 **Muscle Memory Action:** Report View -> Right-click table -> New Measure. Evaluated dynamically in filter context.",
        "mnemonic": "🔑 **Memory Anchor:** *'Measures compute on demand'* — They do not consume storage space per row in the VertiPaq database.",
        "options": ["Measures are computed on demand and do not consume row storage space", "Measures enable automatic query folding back to SQL databases", "Measures allow calculated tables to refresh faster", "Measures bypass row-level security filters"],
        "answer": "Measures are computed on demand and do not consume row storage space",
        "explanation": "Measures do not take up physical storage in the data model; they are calculated dynamically based on user interactions and filter context.",
        "video_url": "http://www.youtube.com/watch?v=a35rFVTsuh4"
    },
    {
        "id": 53,
        "type": "Multiple Select",
        "domain": "Prepare the Data (25-30%)",
        "question": "Which two data sources fully support Query Folding in Power Query? (Choose two)",
        "keywords": ["Query Folding", "SQL Server", "Oracle database"],
        "muscle_memory": "👆 **Muscle Memory Action:** Power Query Editor -> Right-click final step -> Check if 'View Native Query' is clickable.",
        "mnemonic": "🔑 **Memory Anchor:** *'Relational databases fold queries back'* — SQL Server and enterprise databases push transformations to the source server.",
        "options": ["SQL Server database", "Oracle database", "Local CSV text files", "Local JSON configuration files"],
        "answer": ["SQL Server database", "Oracle database"],
        "explanation": "Relational database sources like SQL Server and Oracle support query folding, pushing transformation steps back to the database engine for faster processing.",
        "video_url": "http://www.youtube.com/watch?v=Ul8J-rKe0sc"
    },
    {
        "id": 54,
        "type": "Multiple Choice",
        "domain": "Manage and Secure (15-20%)",
        "question": "You are managing deployment pipelines in Power BI. Which workspace stage is typically used by developers to build and test new report iterations before pushing to production?",
        "keywords": ["deployment pipelines", "Test stage", "Development stage"],
        "muscle_memory": "👆 **Muscle Memory Action:** Power BI Service -> Deployment Pipelines -> Compare workspaces -> Deploy to Test / Production.",
        "mnemonic": "🔑 **Memory Anchor:** *'Dev to Test to Prod'* — Standard ALM release pipeline progression in Power BI.",
        "options": ["Development workspace", "Production workspace", "Master admin portal", "Personal workspace"],
        "answer": "Development workspace",
        "explanation": "The Development workspace stage is where report creators build, edit, and perform initial validation before deploying to Test and Production.",
        "video_url": "http://www.youtube.com/watch?v=GwKyxPMeiBg"
    },
    {
        "id": 55,
        "type": "Multiple Choice",
        "domain": "Visualize and Analyze (25-30%)",
        "question": "You need to display a summary card that changes its conditional background color dynamically based on whether a KPI target is met. How should you configure this?",
        "keywords": ["conditional background color", "fx button", "Card visual"],
        "muscle_memory": "👆 **Muscle Memory Action:** Format pane -> Visual -> Background -> Click **fx** (conditional formatting) -> Select DAX measure rule.",
        "mnemonic": "🔑 **Memory Anchor:** *'fx button unlocks conditional formatting'* — Links visual formatting properties directly to DAX measures.",
        "options": ["Click the fx button next to the background property and select a DAX formatting measure", "Write a DAX measure that modifies the underlying database schema", "Install a custom visual from AppSource", "Use bookmarks to swap card colors"],
        "answer": "Click the fx button next to the background property and select a DAX formatting measure",
        "explanation": "The fx formatting button allows color properties to be driven dynamically by DAX rules or measure outputs.",
        "video_url": "http://www.youtube.com/watch?v=JgizPdne_0Y"
    },
    {
        "id": 56,
        "type": "Multiple Choice",
        "domain": "Model the Data (25-30%)",
        "question": "What happens when you establish a bidirectional cross-filter relationship between two tables in a star schema model?",
        "keywords": ["bidirectional cross-filter", "performance overhead", "ambiguity"],
        "muscle_memory": "👆 **Muscle Memory Action:** Edit Relationship -> Cross filter direction -> **Both**. Use sparingly to avoid performance hits.",
        "mnemonic": "🔑 **Memory Anchor:** *'Bidirectional flows both ways but risks ambiguity'* — Can slow down VertiPaq query engine performance.",
        "options": ["Filters propagate in both directions between the tables, increasing query processing overhead", "Query performance is automatically doubled across all relationships", "Row-level security is disabled on both tables", "All dimension tables convert into fact tables"],
        "answer": "Filters propagate in both directions between the tables, increasing query processing overhead",
        "explanation": "Bidirectional filtering allows filters to flow across lookup tables into other dimensions, but introduces performance overhead and potential relationship ambiguities.",
        "video_url": "http://www.youtube.com/watch?v=uHAnAxwDrn4"
    },
    {
        "id": 57,
        "type": "Multiple Choice",
        "domain": "Prepare the Data (25-30%)",
        "question": "You have a table containing columns for FirstName and LastName. You need to combine them into a single FullName column in Power Query without losing the original columns. What should you do?",
        "keywords": ["combine columns", "Merge Columns", "Power Query"],
        "muscle_memory": "👆 **Muscle Memory Action:** Power Query Editor -> Select both columns -> Add Column tab -> **Merge Columns** -> Choose space separator.",
        "mnemonic": "🔑 **Memory Anchor:** *'Add Column Merge keeps original data'* — Transform merges in-place, while Add Column preserves source fields.",
        "options": ["Use Add Column -> Merge Columns", "Use Transform -> Merge Columns", "Write a DAX calculated relationship", "Use Append Queries"],
        "answer": "Use Add Column -> Merge Columns",
        "explanation": "Using 'Add Column' for merging creates a new combined column while keeping the original source columns intact.",
        "video_url": "http://www.youtube.com/watch?v=a35rFVTsuh4"
    },
    {
        "id": 58,
        "type": "Multiple Choice",
        "domain": "Visualize and Analyze (25-30%)",
        "question": "You want to enable report consumers to dynamically switch between viewing Sales Amount, Profit Margin, and Quantity on a bar chart using a dropdown selection. What feature should you build?",
        "keywords": ["dynamically switch between metrics", "Fields parameter"],
        "muscle_memory": "👆 **Muscle Memory Action:** Modeling tab -> New Parameter -> **Fields** -> Drag multiple measures into list -> Drop parameter slicer onto canvas.",
        "mnemonic": "🔑 **Memory Anchor:** *'Fields parameters swap metrics instantly'* — Allows users to toggle measures inside visuals dynamically.",
        "options": ["A Fields parameter", "A bookmark navigator", "A Row-Level Security role", "A custom R script visual"],
        "answer": "A Fields parameter",
        "explanation": "Fields parameters allow users to dynamically change measures or columns displayed in a visual using a native slicer.",
        "video_url": "http://www.youtube.com/watch?v=Ul8J-rKe0sc"
    },
    {
        "id": 59,
        "type": "Multiple Choice",
        "domain": "Manage and Secure (15-20%)",
        "question": "Which administrative role in Power BI allows a user to manage tenant-wide settings, user licenses, and workspace audits without needing access to individual report content?",
        "keywords": ["tenant-wide settings", "Power BI Administrator"],
        "muscle_memory": "👆 **Muscle Memory Action:** Microsoft 365 Admin Center / Power BI Admin Portal -> Tenant settings -> Assign Power BI Administrator role.",
        "mnemonic": "🔑 **Memory Anchor:** *'Power BI Admin governs the entire tenant tenant-wide'* — Manages global capacity and policies.",
        "options": ["Power BI Administrator", "Workspace Contributor", "Report Publisher", "Dataset Certifier"],
        "answer": "Power BI Administrator",
        "explanation": "The Power BI Administrator role has global governance access over tenant settings, tenant capacity, and auditing logs.",
        "video_url": "http://www.youtube.com/watch?v=GwKyxPMeiBg"
    },
    {
        "id": 60,
        "type": "Multiple Choice",
        "domain": "Model the Data (25-30%)",
        "question": "What is the primary purpose of marking a table as a date table in Power BI Desktop?",
        "keywords": ["marking a table as a date table", "time intelligence functions"],
        "muscle_memory": "👆 **Muscle Memory Action:** Modeling tab -> **Mark as date table** -> Select unique date column.",
        "mnemonic": "🔑 **Memory Anchor:** *'Mark as Date Table activates time intelligence'* — Ensures DAX time functions operate seamlessly without date gaps.",
        "options": ["To enable seamless usage of DAX time intelligence functions like TOTALYTD and SAMEPERIODLASTYEAR", "To automatically enable Power Query query folding on calendar files", "To convert all text columns in the model into datetime formatting", "To force DirectQuery mode across calendar relationships"],
        "answer": "To enable seamless usage of DAX time intelligence functions like TOTALYTD and SAMEPERIODLASTYEAR",
        "explanation": "Marking a table as a date table tells the formula engine that the table contains valid, continuous dates required for advanced time intelligence calculations.",
        "video_url": "http://www.youtube.com/watch?v=JgizPdne_0Y"
    }
]

if tab == "Interactive Practice Hub (All 60 + Voice)":
    st.subheader("📝 PL-300 Real-Time Practice Hub (Full 60 Question Repository)")
    st.markdown("Examine the **Power BI scenario**, test your knowledge, review **Muscle Memory actions**, and use the **Voice Reader** to listen to questions!")
    st.write("---")

    answered_count = 0
    correct_count = 0

    for q in questions:
        st.markdown(f"### Q{q['id']} — [{q['domain']}] 🏷️ *({q['type']})*")
        st.markdown(q['question'])
        
        # Safe JSON-escaped Web Speech API Trigger
        safe_q_text = q['question'].replace("'", "\\'").replace('"', '\\"')
        speech_html = f"""
        <script>
        function speak_{q['id']}() {{
            window.speechSynthesis.cancel();
            let utterance = new SpeechSynthesisUtterance("{safe_q_text}");
            window.speechSynthesis.speak(utterance);
        }}
        </script>
        <button onclick="speak_{q['id']}()" style="background-color:#0078d4; color:white; border:none; padding:6px 12px; border-radius:4px; cursor:pointer; font-weight:bold; margin-bottom:10px;">
            🔊 Read Question Aloud
        </button>
        """
        st.components.v1.html(speech_html, height=45)

        user_choice = None

        if q['type'] == "Multiple Select":
            user_choice = []
            st.markdown("*(Select all correct options below)*:")
            for opt in q['options']:
                if st.checkbox(opt, key=f"cb_{q['id']}_{opt}"):
                    user_choice.append(opt)
            if not user_choice:
                user_choice = None
        else:
            user_choice = st.radio(
                "Choose your answer:", 
                q['options'], 
                index=None, 
                key=f"mc_{q['id']}"
            )

        if user_choice is not None:
            answered_count += 1
            
            if q['type'] == "Multiple Select":
                is_correct = set(user_choice) == set(q['answer'])
            else:
                is_correct = (user_choice == q['answer'])
            
            if is_correct:
                correct_count += 1
                st.success("✅ **Correct!**")
            else:
                st.error("❌ **Incorrect.**")
                if isinstance(q['answer'], list):
                    st.info(f"💡 **Correct Answer:** `{', '.join(q['answer'])}`")
                else:
                    st.info(f"💡 **Correct Answer:** `{q['answer']}`")

            with st.expander("🧠 Muscle Memory, Memory Anchor & Video Demo", expanded=True):
                st.markdown(q['muscle_memory'])
                st.markdown(q['mnemonic'])
                st.markdown(f"**Key Focus Words:** `{'`, `'.join(q['keywords'])}`")
                st.write(f"**Explanation:** {q['explanation']}")
                st.markdown(f"📺 **[Watch Concept Demo Video]({q['video_url']})**")
        else:
            with st.expander("🔑 Peek at Muscle Memory & Key Words"):
                st.markdown(q['muscle_memory'])
                st.markdown(f"**Key Focus Words:** `{'`, `'.join(q['keywords'])}`")

        st.write("---")

    if answered_count > 0:
        pct = (correct_count / answered_count) * 100
        st.sidebar.markdown("---")
        st.sidebar.markdown("### 📊 Live Performance")
        st.sidebar.metric("Attempted", f"{answered_count} / {len(questions)}")
        st.sidebar.metric("Accuracy", f"{pct:.1f}%", f"{correct_count} Correct")

elif tab == "🆓 Microsoft Free Practice Assessment Hub":
    st.subheader("🆓 Microsoft Official Free Practice Assessment & Study Guide")
    st.markdown("Access Microsoft's official free practice assessments and study materials directly on Microsoft Learn.")
    st.write("---")
    st.info("💡 **Recommended Study Strategy:** Take Microsoft's free assessment to benchmark your readiness before attempting timed simulations.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🔗 Official Microsoft Study Links")
        st.markdown("[🌐 Launch Microsoft Learn PL-300 Practice Assessment](https://learn.microsoft.com/en-us/credentials/certifications/data-analyst-associate/practice/assessment?assessment-type=practice&assessmentId=48&practice-assessment-type=certification)")
        st.markdown("[📖 Official PL-300 Study Guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-300)")
    with col2:
        st.markdown("### 🛡️ Exam Sandbox & Interface")
        st.markdown("[🧪 Try Microsoft Exam Sandbox](https://aka.ms/examsandbox)")

    st.write("---")
    st.markdown("### 📋 Practice Assessment Domain Breakdown")
    st.markdown("""
    * **Prepare the Data (25–30%)**
    * **Model the Data (25–30%)**
    * **Visualize and Analyze (25–30%)**
    * **Manage and Secure Assets (15–20%)**
    """)

elif tab == "⏱️ Official Timed Exam Simulator (100 Min)":
    st.subheader("⏱️ Official PL-300 Timed Certification Simulator")
    st.markdown("Simulating Pearson VUE testing conditions (100 minutes, 60 questions).")
    st.write("---")
    
    sim_answers = {}
    for i, q in enumerate(questions):
        st.markdown(f"**Question {i+1}** [{q['domain']}] — *{q['type']}*")
        st.markdown(q['question'])
        
        if q['type'] == "Multiple Select":
            sel_list = []
            st.markdown("*(Select all correct options)*:")
            for opt in q['options']:
                if st.checkbox(opt, key=f"sim_cb_{q['id']}_{opt}"):
                    sel_list.append(opt)
            sim_answers[q['id']] = sel_list
        else:
            sim_answers[q['id']] = st.radio("Select option:", q['options'], index=None, key=f"sim_mob_{q['id']}")
        st.write("---")

    if st.button("Submit Simulation Exam", type="primary"):
        sim_correct = 0
        st.markdown("---")
        st.subheader("📊 Exam Submission Breakdown & Review")
        
        for q in questions:
            user_ans = sim_answers.get(q['id'])
            correct_ans = q['answer']
            
            if q['type'] == "Multiple Select":
                is_q_correct = set(user_ans) == set(correct_ans)
            else:
                is_q_correct = (user_ans == correct_ans)
                
            if is_q_correct:
                sim_correct += 1
                st.markdown(f"**Q{q['id']} [{q['domain']}]: ✅ Correct**")
            else:
                st.markdown(f"**Q{q['id']} [{q['domain']}]: ❌ Incorrect**")
            
            # Show question text and choices
            st.markdown(f"> *{q['question']}*")
            if isinstance(correct_ans, list):
                st.markdown(f"   * **Your Answer:** `{user_ans}`")
                st.markdown(f"   * **Correct Answer:** `{', '.join(correct_ans)}`")
            else:
                st.markdown(f"   * **Your Answer:** `{user_ans}`")
                st.markdown(f"   * **Correct Answer:** `{correct_ans}`")
            
            # Show Memory Anchor and Explanation
            st.markdown(f"   * {q['mnemonic']}")
            st.markdown(f"   * 💡 *Explanation:* {q['explanation']}")
            st.write("---")

        sim_score = (sim_correct / len(questions)) * 100
        st.markdown(f"## Final Simulation Score: {sim_score:.1f}% ({sim_correct} / {len(questions)} Correct)")
        
        if sim_score >= 70:
            st.success("🎉 **PASS** — Met the 70% threshold! You are well-prepared for the real exam.")
        else:
            st.error("⚠️ **NOT PASSING** — Below the 70% Microsoft passing threshold.")
            
            st.markdown("---")
            st.subheader("🎯 Personalized Improvement Recommendations")
            st.markdown("""
            To boost your score above 70%, focus heavily on these high-yield study actions:
            1. **Master Power Query Transformations (Q41–Q46, Q53, Q57):** Review rules for *Referencing vs. Duplicating* tables, *Keep Errors*, *Query Folding*, and *Merge Columns*. These make up 25-30% of the exam.
            2. **Star Schema, Measures & Storage Modes (Q25–Q32, Q51, Q52, Q56, Q60):** Drill down into *Dual storage mode* for dimension tables, *Measures vs Calculated Columns*, and why *Mark as Date Table* unlocks time intelligence.
            3. **Security & Administration (Q9, Q33, Q54, Q59):** Memorize how `USERPRINCIPALNAME()` powers dynamic RLS and how Deployment Pipelines and Admin roles operate in Power BI Service.
            4. **Retake Practice Hub Mode:** Use the **Interactive Practice Hub** tab where you can click **Read Question Aloud**, review **Muscle Memory actions**, and watch the concept videos for every missed question!
            """)

elif tab == "DAX & Power Query Flashcards":
    st.subheader("⚡ High-Yield Microsoft Exam Flashcards")
    flashcards = {
        "CALCULATE()": "🧠 **Anchor:** Modifies filter context. Core workhorse of DAX.",
        "Mark as Date Table": "🧠 **Anchor:** Mandatory for time intelligence functions (SAMEPERIODLASTYEAR).",
        "Merge vs. Append": "🧠 **Anchor:** Merge = SQL Join (columns). Append = SQL Union (rows).",
        "UserPrincipalName()": "🧠 **Anchor:** Dynamic RLS function filtering data by logged-in user email.",
        "Query Folding": "🧠 **Anchor:** Pushing Power Query steps back to source database for speed."
    }
    term = st.selectbox("Select Concept:", list(flashcards.keys()))
    if st.button("Reveal Memory Anchor"):
        st.success(flashcards[term])

elif tab == "Exam Blueprint & Skill Weights":
    st.subheader("📌 Official Microsoft PL-300 Exam Domains")
    st.markdown("""
    * **Prepare the Data (25–30%)**
    * **Model the Data (25–30%)**
    * **Visualize and Analyze (25–30%)**
    * **Manage and Secure Assets (15–20%)**
    """)
