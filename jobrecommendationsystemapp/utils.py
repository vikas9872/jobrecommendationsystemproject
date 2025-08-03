import re
COMMON_SKILLS = [
    "python", "django", "sql", "machine learning", "data analysis", "java", "c++",
    "data structures", "algorithms", "software development", "marketing", "seo",
    "communication", "social media", "content creation", "javascript", "react",
    "html", "css", "aws", "git","access", "control", "controls", "acquisition", "adam", "administration", "management", 
    "adobe", "analytics", "advertising", "agile", "development", "methodology", "process", "al", "algorithms", 
    "alteryx", "analysis", "analytical", "skill", "skills", "method", "validation", "android", "application", 
    "engineering", "programming", "security", "support", "testing", "applications", "api", "microservices", 
    "apis", "integration", "apache", "camel", "assessment", "asset", "accounting", "servicing", "assistance", 
    "assurance", "aws", "cloud", "lambda", "sagemaker", "stack", "or", "azure", "aws/azure/gcp", "banking", 
    "domain", "product", "products", "backend", "operations", "back", "office", "processing", "bagging", "balance", 
    "basic", "benefits", "benefit", "bidding", "big", "data", "engineer", "bigdata", "technologies", "billing", 
    "bioinformatics", "biostatistics", "bi", "bi", "platforms", "tools", "bpo", "brand", "awareness", "building", 
    "brd", "bricks", "business", "analysis", "analyst", "applications", "banking", "case", "central", "consulting", 
    "excellence", "objects", "improvement", "modeling", "mapping", "reporting", "rule", "solutions", "strategy", 
    "transformation", "c", "c++", "cakephp", "campaign", "campaigns", "canva", "canvas", "capacity", "planning", 
    "catalog", "change", "chatbot", "chemistry", "chaid", "cleaning", "cleanse", "cleansing", "clinical", "operations", 
    "research", "trials", "data", "architecture", "computing", "platform", "infrastructure", "services", "clustering", 
    "coaching", "coding", "coffee", "collections", "collaboration", "collaborative", "communication", "compliance", 
    "computation", "computer", "languages", "operator", "proficiency", "science", "vision", "application", "conceptualization", 
    "configuration", "conflict", "resolution", "confluence", "consumption", "content", "writing", "control", "system", "systems", 
    "corporate", "actions", "lending", "relation", "recruitment", "training", "cost", "sheet", "costing", "counseling", "cmmi", "crm", 
    "css", "csv", "cvo", "cvs", "customer", "acquisition", "care", "engagement", "experience", "interaction", "satisfaction", "service", 
    "delivery", "dashboarding", "dashboards", "analyics", "bricks", "cleansing", "collection", "conversion", "crunching", "engineering", 
    "entry", "extraction", "governance", "integrity", "maintenance", "manipulation", "merge", "migration", "mining", "pipeline", "preparation", 
    "profiler", "profiling", "quality", "scientist", "science", "services", "structures", "validation", "warehousing", "warehouse", "concepts", 
    "database", "administration", "design", "dax", "queries", "debugging", "deep", "learning", "frameworks", "algorithms", "delivery", "demand", 
    "forecasting", "design", "patterns", "segmentation", "life", "cycle", "methodologies", "devops", "digital", "marketing", "media", "dimension", 
    "modelling/dimensional", "modelling", "documentation", "documents", "document", "review", "knowledge", "dotcom", "draft", "drafting", "driving", 
    "drug", "due", "diligence", "e-commerce", "e-governance", "edge", "education", "efficiency", "email", "emr", "employee", "engagement", "end", "user", "enterprise", "integration", "risk", 
    "entry", "operator", "environment", "environmental", "erp", "erwin", "etl", "pipelines", "tool", "excellence", "execution", "extraction", "figma", "fpa", 
    "fsd", "factory", "factor", "facility", "feeding", "feasibility", "studies", "finance", "module", "financial", "modelling", "and", "restructuring", "risk", 
    "statement", "statements", "fixed", "project", "assets", "income", "flow", "charts", "focus", "framework", "frd", "front", "end", "gap", "gathering", "general", "generation", "german", "github", "gl", 
    "git", "good", "goods", "graphics", "grc", "gurobi", "gui", "hbase", "hdfs", "health", "healthcare", "helpdesk", "hive", "hl7", "hoovers", "hr", "manager", "hrsd", "html", "http", "hypothesis", 
    "ich", "image", "improvement", "incident", "information", "retrieval", "informatica", "initiative", "innovation", "insights", 
    "intelligence", "intellectual", "property", "internal", "audit", "interpreter", "interpretation", "internet", "searching", "internship", "international", "clients", "inventory", 
    "valuation", "investment", "invoicing", "prepayments", "iso", "it", "projects", "java", "javascript", "jira", "json", "jupyter", "notebook", "kanban", "keras", "key", "accounts", "kinesis", "kpo", "kpi", "kra", "kyc", "laboratory", 
    "lab", "labour", "laravel", "large", "account", "language", "languages", "leadership", "lean", "manufacturing", "six", "sigma", "legal", "licensing", "linux", "lis", "loan", "logic", "logistic", "regression", "logistics", "logs", "loop", 
    "lstm", "lucene", "machine", "macros", "advance", "excel", "advanced", "system", "technology", "manufacturing", "market", "intelligence", "sizing", "marketing", "campaigns", "collaterals", "mathematics", "maverick", "maven", "mba", "finance", 
    "media", "medical", "billing", "imaging", "insurance", "records", "mentoring", "metadata", "methods", "microsoft", "dynamics", "365", "navision", "outlook", "power", "sql", "server", "windows", "mis", "preparation", "mobile", "monitoring", "new", 
    "neural", "networks", "networking", "nlp", "nlpadvanced", "no", "nosql", "nodejs", "note", "notebooks", "online", "bidding", "oops", "open", "source", "operating", "operation", "omc", "optimization", "oracle", "adf", "database", "order", "organization", 
    "structure", "orchestration", "otc", "automation", "oil", "&", "gas", "markets", "sales", "retail", "opencv", "ot", "outcome", "outsourcing", "packaging", "paint", "palantir", "paas", "pandas", "partner", "pattern", "recognition", "pc", "pdf", "people", "peoplesoft", 
    "performance", "appraisal", "monitoring", "optimization", "tuning", "perl", "pharmaceutical", "phd", "php", "physical", "plsql", "planning", "policies", "portfolio", "powerapps", "desktop", "reports", "point", "presentation", "query", "powerpoint", "preventive", "pricing", "innovation", "program", "execution", "handling", 
    "implementation", "prometheus", "procurement", "problem", "solving", "production", "productivity", "professional", "profitability", "pronunciation", "owner", "prototype", "prototyping", "psm", "publishing", "public", "python", "qa", "assurance", "standards", "quantitative", 
    "techniques", "quickbooks", "r", "r&d", "random", "forest", "rational", "rbac", "rdbms", "reactive", "readiness", "react", "time", "operating", "pcr", "reconciliation", "recruitment", "recruiter", "redhat", "relationship", "release", "relational", "databases", "remediation", "generation", "writing", "repo", "requirements", 
    "research", "researching", "paper", "resource", "allocation", "resourcing", "retail", "revenue", "enhancement", "review", "assessment", "rnn", "root", "cause", "rpa", "rfi", "rfp", "rules", "rup", "s3", "saas", "salesforce", "admin", "sales", "safety", "tables", "scheduling", 
    "sdlc", "scripting", "scrum", "search", "secure", "securities", "security", "selection", "self-motivation", "semantic", "web", "seo", "semiconductor", "senior", "serv", "level", "service-based", "sheet", "shell", "simulation", "sizing", "sm", "smm", "snl", "social", "networking", "software", "methodologies", 
    "solution", "spss", "sqa", "knowledge", "querying", "tuning", "ssas", "ssis", "ssrs", "standard", "procedures", "statistics", "statistical", "analyses", "strategy", "strategic", "stress", "structured", "subject", "matter", "expertise", "submission", "supervision", "supervisory", 
    "supply", "chain", "support", "survey", "swot", "symbolic", "configuration", "maintenance", "talent", "taxation", "team", "leading", "technical", "specifications", "telecommunication", "terraform", "test", "cases", "scenarios", "scripts", "text", "textblob", "tlf", "time", 
    "managements", "series", "tqm", "training", "transition", "trend", "troubleshooting", "t-sql", "turbine", "typing", "uml", "diagrams", "unix", "unit", "usage", "user", "acceptance", "stories", "usability", "valuation", "vba", "vendor", "version", "video", 
    "conferencing", "visualization", "vlookup", "vpn", "wan", "designing", "technologies", "well-being", "wellness", "word", "workflow", "written", "xml"
]

def extract_skills_from_resume(resume_text):
    resume_text_lower = resume_text.lower()
    skills_found = set()
    for skill in COMMON_SKILLS:
        pattern = r'\b' + re.escape(skill.lower()) + r'\b'
        if re.search(pattern, resume_text_lower):
            skills_found.add(skill)
    return ', '.join(skills_found)