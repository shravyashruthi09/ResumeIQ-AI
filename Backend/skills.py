"""
skills.py

Professional Skill Database for AI Resume Analyzer

Each skill contains:
- name     : Display name
- aliases  : Different ways the skill may appear in resumes or JDs
"""

SKILLS = {

    # ==========================================================
    # PROGRAMMING LANGUAGES
    # ==========================================================
    "Programming Languages": [

        {"name": "Python", "aliases": ["python", "python3"]},
        {"name": "Java", "aliases": ["java"]},
        {"name": "C", "aliases": ["c language", "c"]},
        {"name": "C++", "aliases": ["c++", "cpp"]},
        {"name": "C#", "aliases": ["c#", "csharp"]},
        {"name": "JavaScript", "aliases": ["javascript", "js"]},
        {"name": "TypeScript", "aliases": ["typescript", "ts"]},
        {"name": "Go", "aliases": ["go", "golang"]},
        {"name": "Rust", "aliases": ["rust"]},
        {"name": "Kotlin", "aliases": ["kotlin"]},
        {"name": "Swift", "aliases": ["swift"]},
        {"name": "PHP", "aliases": ["php"]},
        {"name": "Ruby", "aliases": ["ruby"]},
        {"name": "Scala", "aliases": ["scala"]},
        {"name": "R", "aliases": ["r language", "r programming"]},
        {"name": "MATLAB", "aliases": ["matlab"]},
        {"name": "Perl", "aliases": ["perl"]},
        {"name": "Dart", "aliases": ["dart"]},
        {"name": "Lua", "aliases": ["lua"]},
        {"name": "Julia", "aliases": ["julia"]},
        {"name": "Shell Scripting", "aliases": ["shell scripting", "bash scripting"]},
        {"name": "Bash", "aliases": ["bash"]},
        {"name": "PowerShell", "aliases": ["powershell"]}

    ],

    # ==========================================================
    # FRONTEND DEVELOPMENT
    # ==========================================================
    "Frontend": [

        {"name": "HTML", "aliases": ["html", "html5"]},
        {"name": "CSS", "aliases": ["css", "css3"]},
        {"name": "Bootstrap", "aliases": ["bootstrap"]},
        {"name": "Tailwind CSS", "aliases": ["tailwind", "tailwind css"]},
        {"name": "React", "aliases": ["react", "reactjs", "react.js"]},
        {"name": "Next.js", "aliases": ["nextjs", "next.js"]},
        {"name": "Angular", "aliases": ["angular"]},
        {"name": "Vue.js", "aliases": ["vue", "vuejs", "vue.js"]},
        {"name": "Redux", "aliases": ["redux"]},
        {"name": "Material UI", "aliases": ["material ui", "mui"]},
        {"name": "Chakra UI", "aliases": ["chakra ui"]},
        {"name": "jQuery", "aliases": ["jquery"]},
        {"name": "SASS", "aliases": ["sass", "scss"]},
        {"name": "Responsive Design", "aliases": [
            "responsive design",
            "responsive web design",
            "mobile first design"
        ]},
        {"name": "AJAX", "aliases": ["ajax"]},
        {"name": "Webpack", "aliases": ["webpack"]},
        {"name": "Vite", "aliases": ["vite"]},
        {"name": "Babel", "aliases": ["babel"]},
        {"name": "npm", "aliases": ["npm"]},
        {"name": "Yarn", "aliases": ["yarn"]}

    ],

    # ==========================================================
    # BACKEND DEVELOPMENT
    # ==========================================================
    "Backend": [

        {"name": "FastAPI", "aliases": ["fastapi"]},
        {"name": "Flask", "aliases": ["flask"]},
        {"name": "Django", "aliases": ["django"]},
        {"name": "Node.js", "aliases": ["node", "nodejs", "node.js"]},
        {"name": "Express.js", "aliases": ["express", "expressjs", "express.js"]},
        {"name": "Spring Boot", "aliases": ["spring boot"]},
        {"name": "ASP.NET", "aliases": ["asp.net", ".net"]},
        {"name": "Laravel", "aliases": ["laravel"]},
        {"name": "Ruby on Rails", "aliases": ["rails", "ruby on rails"]},
        {"name": "Hibernate", "aliases": ["hibernate"]},
        {"name": "Servlets", "aliases": ["servlets"]},
        {"name": "JSP", "aliases": ["jsp"]},
        {"name": "MVC Architecture", "aliases": [
            "mvc",
            "mvc architecture",
            "model view controller"
        ]},
        {"name": "Microservices", "aliases": [
            "microservice",
            "microservices"
        ]},
        {"name": "WebSockets", "aliases": [
            "websocket",
            "websockets"
        ]},
        {"name": "SOAP", "aliases": ["soap", "soap api"]},
        {"name": "GraphQL", "aliases": ["graphql"]}

    ],

    # ==========================================================
    # DATABASES
    # ==========================================================
    "Databases": [

        {"name": "SQL", "aliases": ["sql"]},
        {"name": "MySQL", "aliases": ["mysql"]},
        {"name": "PostgreSQL", "aliases": ["postgresql", "postgres"]},
        {"name": "SQLite", "aliases": ["sqlite"]},
        {"name": "MongoDB", "aliases": ["mongodb", "mongo"]},
        {"name": "Oracle Database", "aliases": ["oracle", "oracle database"]},
        {"name": "Redis", "aliases": ["redis"]},
        {"name": "Firebase", "aliases": ["firebase"]},
        {"name": "MariaDB", "aliases": ["mariadb"]},
        {"name": "Cassandra", "aliases": ["cassandra"]},
        {"name": "DynamoDB", "aliases": ["dynamodb"]},
        {"name": "SQL Server", "aliases": [
            "sql server",
            "microsoft sql server",
            "ms sql"
        ]},
        {"name": "Neo4j", "aliases": ["neo4j"]},
        {"name": "Elasticsearch", "aliases": [
            "elasticsearch",
            "elastic search"
        ]}

    ],

    # ==========================================================
    # APIs & AUTHENTICATION
    # ==========================================================
    "APIs & Authentication": [

        {
            "name": "REST API",
            "aliases": [
                "rest api",
                "rest apis",
                "restful api",
                "restful apis",
                "rest services",
                "restful services"
            ]
        },

        {
            "name": "JWT Authentication",
            "aliases": [
                "jwt",
                "jwt authentication",
                "json web token"
            ]
        },

        {
            "name": "OAuth",
            "aliases": [
                "oauth",
                "oauth2",
                "oauth 2.0"
            ]
        },

        {
            "name": "API Integration",
            "aliases": [
                "api integration",
                "third party api",
                "third-party api"
            ]
        },

        {
            "name": "OpenAPI",
            "aliases": [
                "openapi",
                "swagger"
            ]
        },

        {
            "name": "JSON",
            "aliases": [
                "json"
            ]
        },

        {
            "name": "XML",
            "aliases": [
                "xml"
            ]
        }

    ],
    # ==========================================================
    # CLOUD COMPUTING
    # ==========================================================
    "Cloud Computing": [

        {"name": "Amazon Web Services", "aliases": ["aws", "amazon web services"]},
        {"name": "AWS EC2", "aliases": ["ec2", "aws ec2"]},
        {"name": "AWS S3", "aliases": ["s3", "aws s3"]},
        {"name": "AWS Lambda", "aliases": ["lambda", "aws lambda"]},
        {"name": "AWS IAM", "aliases": ["iam", "aws iam"]},
        {"name": "AWS RDS", "aliases": ["rds", "aws rds"]},
        {"name": "AWS CloudFormation", "aliases": ["cloudformation"]},
        {"name": "AWS CloudWatch", "aliases": ["cloudwatch"]},

        {"name": "Microsoft Azure", "aliases": ["azure", "microsoft azure"]},
        {"name": "Azure Functions", "aliases": ["azure functions"]},
        {"name": "Azure DevOps", "aliases": ["azure devops"]},

        {"name": "Google Cloud Platform", "aliases": ["gcp", "google cloud"]},
        {"name": "Google Compute Engine", "aliases": ["gce"]},
        {"name": "Google Cloud Storage", "aliases": ["gcs"]},

        {"name": "Heroku", "aliases": ["heroku"]},
        {"name": "Netlify", "aliases": ["netlify"]},
        {"name": "Vercel", "aliases": ["vercel"]},
        {"name": "DigitalOcean", "aliases": ["digitalocean"]},
        {"name": "Render", "aliases": ["render"]}

    ],

    # ==========================================================
    # DEVOPS
    # ==========================================================
    "DevOps": [

        {"name": "Docker", "aliases": ["docker"]},
        {"name": "Docker Compose", "aliases": ["docker compose"]},
        {"name": "Kubernetes", "aliases": ["kubernetes", "k8s"]},
        {"name": "Helm", "aliases": ["helm"]},

        {"name": "Jenkins", "aliases": ["jenkins"]},
        {"name": "GitHub Actions", "aliases": ["github actions"]},
        {"name": "GitLab CI/CD", "aliases": ["gitlab ci", "gitlab ci/cd"]},
        {"name": "CircleCI", "aliases": ["circleci"]},
        {"name": "Travis CI", "aliases": ["travis ci"]},

        {"name": "Terraform", "aliases": ["terraform"]},
        {"name": "Ansible", "aliases": ["ansible"]},
        {"name": "Puppet", "aliases": ["puppet"]},
        {"name": "Chef", "aliases": ["chef"]},

        {"name": "Prometheus", "aliases": ["prometheus"]},
        {"name": "Grafana", "aliases": ["grafana"]},
        {"name": "ELK Stack", "aliases": ["elk", "elk stack"]},

        {"name": "Nginx", "aliases": ["nginx"]},
        {"name": "Apache HTTP Server", "aliases": ["apache", "apache server"]}

    ],

    # ==========================================================
    # VERSION CONTROL
    # ==========================================================
    "Version Control": [

        {"name": "Git", "aliases": ["git"]},
        {"name": "GitHub", "aliases": ["github"]},
        {"name": "GitLab", "aliases": ["gitlab"]},
        {"name": "Bitbucket", "aliases": ["bitbucket"]},
        {"name": "SVN", "aliases": ["svn", "subversion"]},
        {"name": "Mercurial", "aliases": ["mercurial", "hg"]}

    ],

    # ==========================================================
    # OPERATING SYSTEMS
    # ==========================================================
    "Operating Systems": [

        {"name": "Linux", "aliases": ["linux"]},
        {"name": "Ubuntu", "aliases": ["ubuntu"]},
        {"name": "CentOS", "aliases": ["centos"]},
        {"name": "Red Hat Enterprise Linux", "aliases": ["rhel", "red hat"]},
        {"name": "Debian", "aliases": ["debian"]},
        {"name": "Windows", "aliases": ["windows"]},
        {"name": "Windows Server", "aliases": ["windows server"]},
        {"name": "macOS", "aliases": ["macos", "mac os"]},
        {"name": "Unix", "aliases": ["unix"]}

    ],

    # ==========================================================
    # CONTAINERS & ORCHESTRATION
    # ==========================================================
    "Containers & Orchestration": [

        {"name": "Containerization", "aliases": ["containerization"]},
        {"name": "Docker Swarm", "aliases": ["docker swarm"]},
        {"name": "Kubernetes Cluster", "aliases": ["kubernetes cluster"]},
        {"name": "OpenShift", "aliases": ["openshift"]},
        {"name": "Helm Charts", "aliases": ["helm charts"]}

    ],

    # ==========================================================
    # WEB SERVERS & NETWORKING
    # ==========================================================
    "Web Servers & Networking": [

        {"name": "HTTP", "aliases": ["http"]},
        {"name": "HTTPS", "aliases": ["https"]},
        {"name": "TCP/IP", "aliases": ["tcp", "tcp/ip"]},
        {"name": "DNS", "aliases": ["dns"]},
        {"name": "Load Balancing", "aliases": ["load balancing"]},
        {"name": "Reverse Proxy", "aliases": ["reverse proxy"]},
        {"name": "CDN", "aliases": ["cdn", "content delivery network"]},
        {"name": "SSL/TLS", "aliases": ["ssl", "tls", "ssl/tls"]}

    ],

    # ==========================================================
    # MESSAGE BROKERS & STREAMING
    # ==========================================================
    "Messaging & Streaming": [

        {"name": "Apache Kafka", "aliases": ["kafka", "apache kafka"]},
        {"name": "RabbitMQ", "aliases": ["rabbitmq"]},
        {"name": "Apache ActiveMQ", "aliases": ["activemq"]},
        {"name": "Redis Streams", "aliases": ["redis streams"]}

    ],
    
    # ==========================================================
    # ARTIFICIAL INTELLIGENCE & MACHINE LEARNING
    # ==========================================================
    "Artificial Intelligence": [

        {"name": "Artificial Intelligence", "aliases": ["artificial intelligence", "ai"]},
        {"name": "Machine Learning", "aliases": ["machine learning", "ml"]},
        {"name": "Deep Learning", "aliases": ["deep learning", "dl"]},
        {"name": "Neural Networks", "aliases": ["neural networks", "ann"]},
        {"name": "CNN", "aliases": ["cnn", "convolutional neural network"]},
        {"name": "RNN", "aliases": ["rnn", "recurrent neural network"]},
        {"name": "LSTM", "aliases": ["lstm"]},
        {"name": "GAN", "aliases": ["gan", "generative adversarial network"]},
        {"name": "Transformer", "aliases": ["transformer"]},
        {"name": "Transfer Learning", "aliases": ["transfer learning"]},
        {"name": "Reinforcement Learning", "aliases": ["reinforcement learning"]},
        {"name": "Supervised Learning", "aliases": ["supervised learning"]},
        {"name": "Unsupervised Learning", "aliases": ["unsupervised learning"]},
        {"name": "Semi-Supervised Learning", "aliases": ["semi supervised learning"]}

    ],

    # ==========================================================
    # DATA SCIENCE
    # ==========================================================
    "Data Science": [

        {"name": "NumPy", "aliases": ["numpy"]},
        {"name": "Pandas", "aliases": ["pandas"]},
        {"name": "Matplotlib", "aliases": ["matplotlib"]},
        {"name": "Seaborn", "aliases": ["seaborn"]},
        {"name": "Plotly", "aliases": ["plotly"]},
        {"name": "SciPy", "aliases": ["scipy"]},
        {"name": "Statsmodels", "aliases": ["statsmodels"]},
        {"name": "Jupyter Notebook", "aliases": ["jupyter", "jupyter notebook"]},
        {"name": "Google Colab", "aliases": ["google colab", "colab"]},
        {"name": "Data Visualization", "aliases": ["data visualization"]},
        {"name": "Exploratory Data Analysis", "aliases": ["eda", "exploratory data analysis"]},
        {"name": "Feature Engineering", "aliases": ["feature engineering"]},
        {"name": "Feature Selection", "aliases": ["feature selection"]},
        {"name": "Data Cleaning", "aliases": ["data cleaning", "data preprocessing"]}

    ],

    # ==========================================================
    # MACHINE LEARNING LIBRARIES
    # ==========================================================
    "Machine Learning Libraries": [

        {"name": "Scikit-learn", "aliases": ["scikit learn", "scikit-learn", "sklearn"]},
        {"name": "TensorFlow", "aliases": ["tensorflow", "tf"]},
        {"name": "PyTorch", "aliases": ["pytorch"]},
        {"name": "Keras", "aliases": ["keras"]},
        {"name": "XGBoost", "aliases": ["xgboost"]},
        {"name": "LightGBM", "aliases": ["lightgbm"]},
        {"name": "CatBoost", "aliases": ["catboost"]},
        {"name": "OpenCV", "aliases": ["opencv"]},
        {"name": "NLTK", "aliases": ["nltk"]},
        {"name": "spaCy", "aliases": ["spacy"]},
        {"name": "Gensim", "aliases": ["gensim"]}

    ],

    # ==========================================================
    # NLP
    # ==========================================================
    "Natural Language Processing": [

        {"name": "Natural Language Processing", "aliases": ["nlp", "natural language processing"]},
        {"name": "Sentiment Analysis", "aliases": ["sentiment analysis"]},
        {"name": "Named Entity Recognition", "aliases": ["ner", "named entity recognition"]},
        {"name": "Text Classification", "aliases": ["text classification"]},
        {"name": "Topic Modeling", "aliases": ["topic modeling"]},
        {"name": "Tokenization", "aliases": ["tokenization"]},
        {"name": "Word Embeddings", "aliases": ["word embeddings", "word2vec", "glove"]},
        {"name": "BERT", "aliases": ["bert"]},
        {"name": "RoBERTa", "aliases": ["roberta"]},
        {"name": "T5", "aliases": ["t5"]}

    ],

    # ==========================================================
    # COMPUTER VISION
    # ==========================================================
    "Computer Vision": [

        {"name": "Computer Vision", "aliases": ["computer vision"]},
        {"name": "Image Processing", "aliases": ["image processing"]},
        {"name": "Object Detection", "aliases": ["object detection"]},
        {"name": "Image Classification", "aliases": ["image classification"]},
        {"name": "YOLO", "aliases": ["yolo"]},
        {"name": "OCR", "aliases": ["ocr", "optical character recognition"]},
        {"name": "Face Recognition", "aliases": ["face recognition"]},
        {"name": "Image Segmentation", "aliases": ["image segmentation"]}

    ],

    # ==========================================================
    # GENERATIVE AI & LLMs
    # ==========================================================
    "Generative AI": [

        {"name": "Generative AI", "aliases": ["generative ai", "gen ai"]},
        {"name": "Large Language Models", "aliases": ["llm", "large language models"]},
        {"name": "Prompt Engineering", "aliases": ["prompt engineering"]},
        {"name": "Retrieval Augmented Generation", "aliases": ["rag", "retrieval augmented generation"]},
        {"name": "Fine Tuning", "aliases": ["fine tuning", "finetuning"]},
        {"name": "Embeddings", "aliases": ["embeddings"]},
        {"name": "Vector Databases", "aliases": ["vector database", "vector databases"]},
        {"name": "OpenAI", "aliases": ["openai", "gpt", "chatgpt"]},
        {"name": "Google Gemini", "aliases": ["gemini", "google gemini"]},
        {"name": "Claude", "aliases": ["claude"]},
        {"name": "Llama", "aliases": ["llama", "llama2", "llama3"]},
        {"name": "Mistral", "aliases": ["mistral"]},
        {"name": "Ollama", "aliases": ["ollama"]},
        {"name": "Hugging Face", "aliases": ["huggingface", "hugging face"]},
        {"name": "Transformers", "aliases": ["transformers"]},
        {"name": "LangChain", "aliases": ["langchain"]},
        {"name": "LangGraph", "aliases": ["langgraph"]},
        {"name": "LlamaIndex", "aliases": ["llamaindex"]},
        {"name": "CrewAI", "aliases": ["crewai"]},
        {"name": "AutoGen", "aliases": ["autogen"]},
        {"name": "Semantic Kernel", "aliases": ["semantic kernel"]},
        {"name": "DSPy", "aliases": ["dspy"]}

    ],

    # ==========================================================
    # VECTOR DATABASES
    # ==========================================================
    "Vector Databases": [

        {"name": "FAISS", "aliases": ["faiss"]},
        {"name": "ChromaDB", "aliases": ["chromadb", "chroma"]},
        {"name": "Pinecone", "aliases": ["pinecone"]},
        {"name": "Weaviate", "aliases": ["weaviate"]},
        {"name": "Milvus", "aliases": ["milvus"]},
        {"name": "Qdrant", "aliases": ["qdrant"]}

    ],

    # ==========================================================
    # DATA ENGINEERING
    # ==========================================================
    "Data Engineering": [

        {"name": "Apache Spark", "aliases": ["spark", "apache spark"]},
        {"name": "PySpark", "aliases": ["pyspark"]},
        {"name": "Apache Hadoop", "aliases": ["hadoop", "apache hadoop"]},
        {"name": "Apache Airflow", "aliases": ["airflow", "apache airflow"]},
        {"name": "Apache Hive", "aliases": ["hive", "apache hive"]},
        {"name": "Apache Pig", "aliases": ["pig", "apache pig"]},
        {"name": "Databricks", "aliases": ["databricks"]},
        {"name": "ETL", "aliases": ["etl"]},
        {"name": "Data Warehouse", "aliases": ["data warehouse"]},
        {"name": "Data Lake", "aliases": ["data lake"]}

    ],
    
    # ==========================================================
    # MOBILE DEVELOPMENT
    # ==========================================================
    "Mobile Development": [

        {"name": "Android Development", "aliases": ["android development", "android"]},
        {"name": "iOS Development", "aliases": ["ios development", "ios"]},
        {"name": "Flutter", "aliases": ["flutter"]},
        {"name": "React Native", "aliases": ["react native"]},
        {"name": "Xamarin", "aliases": ["xamarin"]},
        {"name": "Jetpack Compose", "aliases": ["jetpack compose"]},
        {"name": "Android Studio", "aliases": ["android studio"]},
        {"name": "SwiftUI", "aliases": ["swiftui"]},
        {"name": "Expo", "aliases": ["expo"]},
        {"name": "Firebase Cloud Messaging", "aliases": ["fcm", "firebase cloud messaging"]}

    ],

    # ==========================================================
    # SOFTWARE ENGINEERING
    # ==========================================================
    "Software Engineering": [

        {"name": "Object Oriented Programming", "aliases": ["oop", "oops", "object oriented programming"]},
        {"name": "Data Structures", "aliases": ["data structures", "ds"]},
        {"name": "Algorithms", "aliases": ["algorithms", "algorithm"]},
        {"name": "Design Patterns", "aliases": ["design patterns"]},
        {"name": "SOLID Principles", "aliases": ["solid", "solid principles"]},
        {"name": "MVC Architecture", "aliases": ["mvc", "model view controller"]},
        {"name": "Clean Code", "aliases": ["clean code"]},
        {"name": "Refactoring", "aliases": ["refactoring"]},
        {"name": "Code Review", "aliases": ["code review"]},
        {"name": "Agile", "aliases": ["agile"]},
        {"name": "Scrum", "aliases": ["scrum"]},
        {"name": "Kanban", "aliases": ["kanban"]},
        {"name": "SDLC", "aliases": ["sdlc", "software development life cycle"]},
        {"name": "System Design", "aliases": ["system design"]},
        {"name": "Distributed Systems", "aliases": ["distributed systems"]},
        {"name": "Multithreading", "aliases": ["multithreading", "multi threading"]},
        {"name": "Concurrency", "aliases": ["concurrency"]},
        {"name": "Parallel Programming", "aliases": ["parallel programming"]},
        {"name": "Event Driven Architecture", "aliases": ["event driven architecture"]},
        {"name": "Scalable Applications", "aliases": ["scalable applications", "application scalability"]}

    ],

    # ==========================================================
    # TESTING & QA
    # ==========================================================
    "Testing & QA": [

        {"name": "Unit Testing", "aliases": ["unit testing"]},
        {"name": "Integration Testing", "aliases": ["integration testing"]},
        {"name": "System Testing", "aliases": ["system testing"]},
        {"name": "Regression Testing", "aliases": ["regression testing"]},
        {"name": "Manual Testing", "aliases": ["manual testing"]},
        {"name": "Automation Testing", "aliases": ["automation testing"]},
        {"name": "PyTest", "aliases": ["pytest"]},
        {"name": "JUnit", "aliases": ["junit"]},
        {"name": "Mockito", "aliases": ["mockito"]},
        {"name": "Selenium", "aliases": ["selenium"]},
        {"name": "Cypress", "aliases": ["cypress"]},
        {"name": "Playwright", "aliases": ["playwright"]},
        {"name": "Postman", "aliases": ["postman"]},
        {"name": "Swagger Testing", "aliases": ["swagger testing"]},
        {"name": "API Testing", "aliases": ["api testing"]},
        {"name": "Performance Testing", "aliases": ["performance testing"]},
        {"name": "Load Testing", "aliases": ["load testing"]},
        {"name": "Stress Testing", "aliases": ["stress testing"]}

    ],

    # ==========================================================
    # CYBER SECURITY
    # ==========================================================
    "Cyber Security": [

        {"name": "Cyber Security", "aliases": ["cyber security", "cybersecurity"]},
        {"name": "Network Security", "aliases": ["network security"]},
        {"name": "Application Security", "aliases": ["application security"]},
        {"name": "Penetration Testing", "aliases": ["penetration testing", "pentesting"]},
        {"name": "Ethical Hacking", "aliases": ["ethical hacking"]},
        {"name": "OWASP", "aliases": ["owasp"]},
        {"name": "Encryption", "aliases": ["encryption"]},
        {"name": "Cryptography", "aliases": ["cryptography"]},
        {"name": "Identity Management", "aliases": ["identity management"]},
        {"name": "Access Control", "aliases": ["access control"]},
        {"name": "Firewalls", "aliases": ["firewall", "firewalls"]},
        {"name": "VPN", "aliases": ["vpn"]},
        {"name": "SIEM", "aliases": ["siem"]},
        {"name": "Zero Trust", "aliases": ["zero trust"]},
        {"name": "Security Auditing", "aliases": ["security auditing"]}

    ],

    # ==========================================================
    # BUILD TOOLS
    # ==========================================================
    "Build Tools": [

        {"name": "Maven", "aliases": ["maven"]},
        {"name": "Gradle", "aliases": ["gradle"]},
        {"name": "Ant", "aliases": ["apache ant", "ant"]},
        {"name": "CMake", "aliases": ["cmake"]},
        {"name": "Make", "aliases": ["make", "gnu make"]},
        {"name": "Webpack", "aliases": ["webpack"]},
        {"name": "Vite", "aliases": ["vite"]},
        {"name": "Babel", "aliases": ["babel"]}

    ],
    
    # ==========================================================
    # SOFT SKILLS
    # ==========================================================
    "Soft Skills": [

        {"name": "Communication", "aliases": ["communication", "communication skills"]},
        {"name": "Verbal Communication", "aliases": ["verbal communication"]},
        {"name": "Written Communication", "aliases": ["written communication"]},
        {"name": "Presentation Skills", "aliases": ["presentation skills"]},
        {"name": "Leadership", "aliases": ["leadership"]},
        {"name": "Teamwork", "aliases": ["teamwork", "team player"]},
        {"name": "Collaboration", "aliases": ["collaboration"]},
        {"name": "Problem Solving", "aliases": ["problem solving", "problem-solving"]},
        {"name": "Critical Thinking", "aliases": ["critical thinking"]},
        {"name": "Analytical Thinking", "aliases": ["analytical thinking"]},
        {"name": "Decision Making", "aliases": ["decision making"]},
        {"name": "Time Management", "aliases": ["time management"]},
        {"name": "Project Management", "aliases": ["project management"]},
        {"name": "Adaptability", "aliases": ["adaptability"]},
        {"name": "Creativity", "aliases": ["creativity"]},
        {"name": "Innovation", "aliases": ["innovation"]},
        {"name": "Attention to Detail", "aliases": ["attention to detail"]},
        {"name": "Conflict Resolution", "aliases": ["conflict resolution"]},
        {"name": "Mentoring", "aliases": ["mentoring"]},
        {"name": "Negotiation", "aliases": ["negotiation"]},
        {"name": "Emotional Intelligence", "aliases": ["emotional intelligence"]},
        {"name": "Customer Focus", "aliases": ["customer focus"]},
        {"name": "Self Learning", "aliases": ["self learning", "self-learning"]},
        {"name": "Fast Learner", "aliases": ["fast learner"]}

    ],

    # ==========================================================
    # PROJECT MANAGEMENT
    # ==========================================================
    "Project Management": [

        {"name": "JIRA", "aliases": ["jira"]},
        {"name": "Confluence", "aliases": ["confluence"]},
        {"name": "Trello", "aliases": ["trello"]},
        {"name": "Asana", "aliases": ["asana"]},
        {"name": "Monday.com", "aliases": ["monday", "monday.com"]},
        {"name": "ClickUp", "aliases": ["clickup"]},
        {"name": "Notion", "aliases": ["notion"]},
        {"name": "Agile Methodology", "aliases": ["agile methodology"]},
        {"name": "Sprint Planning", "aliases": ["sprint planning"]},
        {"name": "Backlog Management", "aliases": ["backlog management"]}

    ],

    # ==========================================================
    # IDEs & EDITORS
    # ==========================================================
    "IDEs & Editors": [

        {"name": "Visual Studio Code", "aliases": ["vs code", "vscode", "visual studio code"]},
        {"name": "Visual Studio", "aliases": ["visual studio"]},
        {"name": "PyCharm", "aliases": ["pycharm"]},
        {"name": "IntelliJ IDEA", "aliases": ["intellij", "intellij idea"]},
        {"name": "Eclipse", "aliases": ["eclipse"]},
        {"name": "NetBeans", "aliases": ["netbeans"]},
        {"name": "Android Studio", "aliases": ["android studio"]},
        {"name": "Xcode", "aliases": ["xcode"]},
        {"name": "JupyterLab", "aliases": ["jupyterlab"]},
        {"name": "Sublime Text", "aliases": ["sublime text"]},
        {"name": "Notepad++", "aliases": ["notepad++"]}

    ],

    # ==========================================================
    # UI / UX TOOLS
    # ==========================================================
    "UI UX": [

        {"name": "Figma", "aliases": ["figma"]},
        {"name": "Adobe XD", "aliases": ["adobe xd"]},
        {"name": "Sketch", "aliases": ["sketch"]},
        {"name": "Canva", "aliases": ["canva"]},
        {"name": "Adobe Photoshop", "aliases": ["photoshop", "adobe photoshop"]},
        {"name": "Adobe Illustrator", "aliases": ["illustrator", "adobe illustrator"]}

    ],

    # ==========================================================
    # DOCUMENTATION
    # ==========================================================
    "Documentation": [

        {"name": "Markdown", "aliases": ["markdown", "md"]},
        {"name": "Swagger", "aliases": ["swagger"]},
        {"name": "OpenAPI Documentation", "aliases": ["openapi documentation"]},
        {"name": "ReadTheDocs", "aliases": ["readthedocs"]},
        {"name": "Technical Documentation", "aliases": ["technical documentation"]}

    ],

    # ==========================================================
    # CERTIFICATIONS
    # ==========================================================
    "Certifications": [

        {"name": "AWS Certified Solutions Architect", "aliases": ["aws certified solutions architect"]},
        {"name": "AWS Certified Developer", "aliases": ["aws developer"]},
        {"name": "Microsoft Azure Fundamentals", "aliases": ["azure fundamentals", "az-900"]},
        {"name": "Google Professional Cloud Architect", "aliases": ["google cloud architect"]},
        {"name": "Oracle Certified Java Programmer", "aliases": ["ocjp"]},
        {"name": "Cisco CCNA", "aliases": ["ccna"]},
        {"name": "CompTIA Security+", "aliases": ["security+"]},
        {"name": "Certified Kubernetes Administrator", "aliases": ["cka"]},
        {"name": "TensorFlow Developer Certificate", "aliases": ["tensorflow developer"]}

    ],

    # ==========================================================
    # BUSINESS INTELLIGENCE
    # ==========================================================
    "Business Intelligence": [

        {"name": "Power BI", "aliases": ["power bi"]},
        {"name": "Tableau", "aliases": ["tableau"]},
        {"name": "Looker", "aliases": ["looker"]},
        {"name": "Google Data Studio", "aliases": ["google data studio"]},
        {"name": "Excel", "aliases": ["excel", "microsoft excel"]}

    ],

    # ==========================================================
    # MISCELLANEOUS
    # ==========================================================
    "Miscellaneous": [

        {"name": "Blockchain", "aliases": ["blockchain"]},
        {"name": "Internet of Things", "aliases": ["iot", "internet of things"]},
        {"name": "Robotics", "aliases": ["robotics"]},
        {"name": "Embedded Systems", "aliases": ["embedded systems"]},
        {"name": "AR/VR", "aliases": ["augmented reality", "virtual reality", "ar", "vr"]},
        {"name": "Quantum Computing", "aliases": ["quantum computing"]},
        {"name": "Edge Computing", "aliases": ["edge computing"]},
        {"name": "5G", "aliases": ["5g"]},
        {"name": "ERP", "aliases": ["erp"]},
        {"name": "CRM", "aliases": ["crm"]}

    ]

}
