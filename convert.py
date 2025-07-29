import os
import re
import weasyprint
from htmldocx import HtmlToDocx
from pathlib import Path

# ==============================================================================
# ==                      📝 RESUME DATA (EDIT HERE)                          ==
# ==============================================================================
# Edit your personal details, experience, projects, etc., in this section.
# This separates the content of your resume from the code that generates it.

RESUME_DATA = {
    "name": "Khushal Sindhav",
    "role": "Full Stack Developer",
    "degree": "B.Tech | Artificial Intelligence & Data Science | IIT Jodhpur",
    "contact": {
        "phone": "+91-9328576258",
        "linkedin": "KhushalSindhav",
        "github": "MagnusCarlsen26",
    },
    "summary": "I am a passionate Engineer who likes to solve real life difficult problems. I am a fast learner, who can adapt to fast paced enviorments and slow paced enviorments. Linux is my daily driver.",
    "education": [
        {"institution": "IIT Jodhpur", "degree": "B.Tech in AI & Data Science", "date": "May 2025", "percentage": ""},
        {"institution": "JHASV, Surat", "degree": "Class 12", "date": "May 2021", "percentage": "93%"},
        {"institution": "JHASV, Surat", "degree": "Class 10", "date": "May 2019", "percentage": "91%"},
    ],
    "skills": [
        {"category": "Languages", "tags": ["C/C++", "JavaScript", "Python"]},
        {"category": "Full Stack", "tags": ["React", "NextJS", "Bootstrap", "Tailwind", "MongoDB", "NodeJS", "Flask"]},
        {"category": "DevOps", "tags": ["AWS", "Firebase", "Docker", "Kubernetes"]},
    ],
    "experience": [
        {
            "title": "Oasis of Ideas",
            "date": "Feb 2025 – May 2025",
            "skills": ["Python", "Asyncio", "OpenRouter", "AWS EC2", "tmux"],
            "description": [
                "Solely designed, implemented, and maintained an end-to-end system for scraping and processing startup ideas.",
                "Scraped data from multiple websites using asynchronous Python programming.",
                "Processed scraped content via multi-stage LLM pipelines powered by OpenAI, DeepSeek, and Gemini.",
            ],
        },
    ],
    "projects": [
        {
            "title": "SURVEY PORTAL",
            "date": "Dec 2024",
            "supervisor": "Dr. Dweepobotee Brahma",
            "skills": ["NextJS", "TailwindCSS", "NodeJS", "Firestore"],
            "description": [
                "Developed a custom survey website to conduct surveys at IIT Jodhpur, handling 270 users without errors.",
                "Designed a responsive UI and implemented security measures to ensure data integrity.",
            ],
        },
        {
            "title": "PRACTO SCRAPER",
            "date": "Dec 2024",
            "supervisor": "Dr. Dweepobotee Brahma",
            "skills": ["Javascript", "Docker", "Kubernetes", "AWS EKS"],
            "description": [
                "Scraped data of 6,600 doctors in 2 hours from Practo for research using a master-worker architecture.",
                "Deployed the system using Firebase Functions and Docker containers on AWS Elastic Kubernetes Service (EKS).",
            ],
        },
    ],
    "achievements": [
        "Discovered an authentication vulnerability in the college ERP system.",
        "Pupil at Codeforces with a peak rating of 1369.",
        "Achieved a global rank of 352 in CodeChef Starters 92 (Div. 2).",
        "Ranked in the top 0.8% in JEE Advanced 2021.",
    ]
}


# ==============================================================================
# ==                  🏗️ HTML BUILDER FUNCTIONS (MODULAR)                     ==
# ==============================================================================
# These functions build the HTML for each section of the resume by processing
# the data from the RESUME_DATA dictionary.

def _build_skill_tags(tags):
    return "".join(f'<span class="skill-tag">{tag}</span>' for tag in tags)

def _build_list_items(items):
    return "".join(f'<li>{item}</li>' for item in items)

def build_header_section(data):
    return f"""
    <div class="section">
        <div class="header-section">
            <div style="display: flex; align-items: center; gap: 20px;">
                <div class="profile-image"></div>
                <div class="header-info">
                    <h1>{data['name']}</h1>
                    <p class="role">{data['role']}</p>
                    <p class="education">{data['degree']}</p>
                </div>
            </div>
            <div class="contact-info">
                <div class="contact-item">📞 {data['contact']['phone']}</div>
                <div class="contact-item">
                    <a href="https://www.linkedin.com/in/{data['contact']['linkedin']}" target="_blank">...<span>{data['contact']['linkedin']}</span></a>
                </div>
                <div class="contact-item">
                    <a href="https://github.com/{data['contact']['github']}" target="_blank">...<span>{data['contact']['github']}</span></a>
                </div>
            </div>
        </div>
    </div>
    """

def build_summary_section(summary):
    return f"""
    <div class="section">
        <h2 class="section-title">Summary</h2>
        <div class="section-content"><p class="summary-text">{summary}</p></div>
    </div>
    """

def build_education_section(education_data):
    rows = "".join(f"""
    <tr>
        <td>{edu['institution']}</td>
        <td>{edu['degree']}</td>
        <td>{edu['date']}</td>
        <td>{edu['percentage']}</td>
    </tr>""" for edu in education_data)
    
    return f"""
    <div class="section">
        <h2 class="section-title">Education</h2>
        <div class="section-content">
            <table class="education-table">
                <thead><tr><th>Institution</th><th>Degree/Class</th><th>Date</th><th>Percentage</th></tr></thead>
                <tbody>{rows}</tbody>
            </table>
        </div>
    </div>
    """

def build_skills_section(skills_data):
    categories = "".join(f"""
    <div class="skill-category">
        <h3>{cat['category']}</h3>
        <div class="skill-tags">{_build_skill_tags(cat['tags'])}</div>
    </div>""" for cat in skills_data)
    
    return f"""
    <div class="section">
        <h2 class="section-title">Skills</h2>
        <div class="section-content"><div class="skills-grid">{categories}</div></div>
    </div>
    """
    
def _build_experience_item(job):
    return f"""
    <div class="experience-item">
        <div class="experience-header">
            <h3 class="experience-title">{job['title']}</h3>
            <p class="experience-date">{job['date']}</p>
        </div>
        <div class="experience-skills">{_build_skill_tags(job['skills'])}</div>
        <ul class="experience-list">{_build_list_items(job['description'])}</ul>
    </div>
    """

def build_experience_section(experience_data):
    items = "".join(_build_experience_item(job) for job in experience_data)
    return f"""
    <div class="section">
        <h2 class="section-title">Experience</h2>
        <div class="section-content">{items}</div>
    </div>
    """
    
def _build_project_item(project):
    return f"""
    <div class="project-item">
        <div class="project-header">
            <h3 class="project-title">{project['title']}</h3>
            <p class="experience-date">{project['date']}</p>
        </div>
        <p class="project-supervisor">Supervisor: {project['supervisor']}</p>
        <div class="project-skills">{_build_skill_tags(project['skills'])}</div>
        <ul class="project-list">{_build_list_items(project['description'])}</ul>
    </div>
    """

def build_projects_section(projects_data):
    items = "".join(_build_project_item(proj) for proj in projects_data)
    return f"""
    <div class="section">
        <h2 class="section-title">Projects</h2>
        <div class="section-content">{items}</div>
    </div>
    """
    
def build_achievements_section(achievements_data):
    return f"""
    <div class="section">
        <h2 class="section-title">Achievements</h2>
        <div class="section-content">
            <ul class="achievements-list">{_build_list_items(achievements_data)}</ul>
        </div>
    </div>
    """

def build_full_html(data):
    """Assembles the full HTML document from modular components."""
    content = (
        build_header_section(data) +
        build_summary_section(data['summary']) +
        build_education_section(data['education']) +
        build_skills_section(data['skills']) +
        build_experience_section(data['experience']) +
        build_projects_section(data['projects']) +
        build_achievements_section(data['achievements'])
    )
    
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>{data['name']} - Resume</title>
    </head>
    <body>
        <div class="container">{content}</div>
    </body>
    </html>
    """

# ==============================================================================
# ==                        🎨 CSS STYLES                                     ==
# ==============================================================================

CSS_STYLE = """
@import url('https://fonts.googleapis.com/icon?family=Material+Icons');
:root {
  --primary-color: #0c77f2;
  --secondary-color: #64748b;
  --text-primary: #1e293b;
}
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: "Arial", sans-serif; background-color: #fff; line-height: 1.6; color: var(--text-primary); font-size: 14px; }
.container { max-width: 100%; margin: 0; padding: 0; display: flex; flex-direction: column; }
.section { background: white; padding: 16px; display: flex; gap: 20px; border-bottom: 2px solid #e2e8f0; }
.section:last-child { border-bottom: none; }
.section-title { font-size: 16px; font-weight: bold; width: 100px; flex-shrink: 0; }
.section-content { flex: 1; }
.header-section { display: flex; justify-content: space-between; align-items: flex-start; width: 100%; }
.profile-image { width: 80px; height: 80px; border-radius: 50%; background: #e2e8f0; margin-right: 20px; }
.header-info h1 { font-size: 22px; font-weight: bold; margin-bottom: 3px; }
.header-info .role { font-size: 14px; font-weight: 500; color: var(--primary-color); margin-bottom: 3px; }
.header-info .education { font-size: 13px; color: var(--secondary-color); }
.contact-info { display: flex; flex-direction: column; gap: 4px; font-size: 12px; color: var(--secondary-color); }
.contact-item { display: flex; align-items: center; gap: 6px; }
.contact-item a { color: var(--secondary-color); text-decoration: none; }
.summary-text { font-size: 13px; color: var(--secondary-color); line-height: 1.5; }
.education-table { width: 100%; border-collapse: collapse; font-size: 12px; }
.education-table th, .education-table td { padding: 4px; text-align: left; border-bottom: 1px solid #e2e8f0; color: var(--secondary-color); }
.education-table th { font-weight: 600; color: var(--text-primary); }
.education-table th:last-child, .education-table td:last-child { text-align: right; }
.skills-grid { display: flex; flex-direction: column; gap: 8px; font-size: 12px; }
.skill-category { display: flex; gap: 12px; align-items: flex-start; }
.skill-category h3 { font-weight: 600; width: 80px; flex-shrink: 0; font-size: 12px; }
.skill-tags { display: flex; flex-wrap: wrap; gap: 4px; flex: 1; }
.skill-tag { background: #f1f5f9; color: var(--secondary-color); font-size: 10px; padding: 3px 6px; border-radius: 12px; white-space: nowrap; }
.experience-item, .project-item { margin-bottom: 16px; }
.experience-item:last-child, .project-item:last-child { margin-bottom: 0; }
.experience-header, .project-header { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 3px; }
.experience-title, .project-title { font-weight: 600; font-size: 13px; }
.experience-date { font-size: 11px; color: var(--secondary-color); flex-shrink: 0; }
.project-supervisor { font-size: 11px; color: var(--secondary-color); margin-bottom: 6px; }
.experience-skills, .project-skills { display: flex; flex-wrap: wrap; gap: 3px; margin-bottom: 6px; }
.experience-list, .project-list, .achievements-list { list-style: disc; padding-left: 16px; color: var(--secondary-color); font-size: 11px; }
.experience-list li, .project-list li, .achievements-list li { margin-bottom: 3px; line-height: 1.3; }
.achievements-list { font-size: 12px; }
@page { size: A4; margin: 0; }
"""

# ==============================================================================
# ==                      ⚙️ CORE ENGINE (MAIN SCRIPT)                        ==
# ==============================================================================

def setup_environment():
    """Defines file paths and ensures the output directory exists."""
    print("INFO: Setting up environment...")
    base_dir = Path(__file__).parent
    output_dir = base_dir / "output"
    output_dir.mkdir(exist_ok=True)
    
    config = {
        "pdf_output": output_dir / "resume.pdf",
        "docx_output": output_dir / "resume.docx",
        "base_url": base_dir.as_uri()
    }
    print(f"SUCCESS: Output will be saved to '{output_dir}'.")
    return config

def create_pdf(config: dict, html_content: str):
    """Generates a PDF from the provided HTML content."""
    print("\nINFO: Starting PDF conversion...")
    
    final_html = html_content.replace('</head>', f'<style>{CSS_STYLE}</style></head>')
    
    try:
        html_to_render = weasyprint.HTML(string=final_html, base_url=config["base_url"])
        html_to_render.write_pdf(config["pdf_output"])
        print(f"✅ SUCCESS: PDF saved to '{config['pdf_output']}'.")
    except Exception as e:
        print(f"❌ ERROR: PDF conversion failed: {e}")

def create_docx(config: dict, html_content: str):
    """Generates a DOCX from the provided HTML content."""
    print("\nINFO: Starting DOCX conversion...")
    
    html_for_docx = re.sub(r'style="[^"]*"', '', html_content)
    parser = HtmlToDocx()
    
    try:
        parser.parse_html_string(html_for_docx)
        parser.save(config["docx_output"])
        print(f"✅ SUCCESS: DOCX saved to '{config['docx_output']}'.")
    except Exception as e:
        print(f"❌ ERROR: DOCX conversion failed: {e}")

def main():
    """Main function to orchestrate the resume conversion process."""
    config = setup_environment()
    
    print("\nINFO: Building HTML from data...")
    final_html_content = build_full_html(RESUME_DATA)
    print("SUCCESS: HTML built.")
    
    create_pdf(config, final_html_content)
    create_docx(config, final_html_content)
    
    print(f"\n✨ All files are ready in the 'output' directory.")

if __name__ == "__main__":
    main()