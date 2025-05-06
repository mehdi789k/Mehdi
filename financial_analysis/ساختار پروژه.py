import os

# تعریف ساختار پروژه
project_structure = {
    "financial_analysis": {
        "main.py": "# Main application file\n",
        "config.py": "# General project settings\n",
        "modules": {
            "welcome.py": "# Display welcome message\n",
            "menu.py": "# Menu management and access to sections\n",
            "search.py": "# Search and initial symbol information\n",
            "analysis": {
                "crypto.py": "# Cryptocurrency market analysis\n",
                "forex.py": "# Forex market analysis\n",
                "stocks.py": "# Stock market analysis\n",
                "metals.py": "# Metals market analysis\n",
                "timeframe.py": "# Timeframe management\n"
            },
            "trading.py": "# Trading management\n",
            "notifications.py": "# Important market notifications\n",
            "utils": {
                "charts.py": "# Chart generation utilities\n",
                "backup.py": "# Backup management\n",
                "helpers.py": "# Helper functions\n"
            }
        },
        "assets": {
            "styles": {},
            "backups": {}
        },
        "requirements.txt": "# List of required libraries\n",
        "README.md": "# Financial Analysis Project\n\nThis project provides tools for analyzing financial markets.\n"
    }
}

def create_project_structure(base_path, structure):
    """
    ایجاد ساختار پروژه به صورت بازگشتی
    :param base_path: مسیر پایه برای ایجاد ساختار
    :param structure: دیکشنری حاوی ساختار پروژه
    """
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            # اگر محتوا یک دیکشنری باشد، پوشه ایجاد کنید
            os.makedirs(path, exist_ok=True)
            create_project_structure(path, content)
        else:
            # اگر محتوا یک رشته باشد، فایل ایجاد کنید
            with open(path, "w", encoding="utf-8") as file:
                file.write(content)

if __name__ == "__main__":
    # مسیر دسکتاپ کاربر
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    
    # ایجاد ساختار پروژه در دسکتاپ
    create_project_structure(desktop_path, project_structure)
    print("ساختار پروژه با موفقیت ایجاد شد!")