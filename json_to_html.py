import json

def generate_resume_html(json_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        resume_data = json.load(f)

    icon_size = 15

    linkedin_svg = f'''<svg fill="#000000" version="1.1" id="Capa_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 93.06 93.06" xml:space="preserve" width="{icon_size}" height="{icon_size}"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <g> <g> <path d="M11.185,0.08C5.004,0.08,0.001,5.092,0,11.259c0,6.173,5.003,11.184,11.186,11.184c6.166,0,11.176-5.011,11.176-11.184 C22.362,5.091,17.351,0.08,11.185,0.08z"></path> <rect x="1.538" y="30.926" width="19.287" height="62.054"></rect> <path d="M69.925,29.383c-9.382,0-15.673,5.144-18.248,10.022h-0.258v-8.479H32.921H32.92v62.053h19.27V62.281 c0-8.093,1.541-15.932,11.575-15.932c9.89,0,10.022,9.256,10.022,16.451v30.178H93.06V58.942 C93.06,42.235,89.455,29.383,69.925,29.383z"></path> </g> </g> </g></svg>'''

    gmail_svg = f'''<svg fill="#000000" viewBox="0 0 32 32" version="1.1" xmlns="http://www.w3.org/2000/svg" width="{icon_size}" height="{icon_size}"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <title>gmail</title> <path d="M30.996 7.824v17.381c0 0 0 0 0 0.001 0 1.129-0.915 2.044-2.044 2.044-0 0-0 0-0.001 0h-4.772v-11.587l-8.179 6.136-8.179-6.136v11.588h-4.772c0 0 0 0-0 0-1.129 0-2.044-0.915-2.044-2.044 0-0 0-0.001 0-0.001v0-17.381c0-0 0-0.001 0-0.001 0-1.694 1.373-3.067 3.067-3.067 0.694 0 1.334 0.231 1.848 0.619l-0.008-0.006 10.088 7.567 10.088-7.567c0.506-0.383 1.146-0.613 1.84-0.613 1.694 0 3.067 1.373 3.067 3.067v0z"></path> </g></svg>'''

    github_svg = f'''<svg viewBox="0 0 20 20" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" fill="#000000" width="{icon_size}" height="{icon_size}"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <title>github [#142]</title> <desc>Created with Sketch.</desc> <defs> </defs> <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd"> <g id="Dribbble-Light-Preview" transform="translate(-140.000000, -7559.000000)" fill="#000000"> <g id="icons" transform="translate(56.000000, 160.000000)"> <path d="M94,7399 C99.523,7399 104,7403.59 104,7409.253 C104,7413.782 101.138,7417.624 97.167,7418.981 C96.66,7419.082 96.48,7418.762 96.48,7418.489 C96.48,7418.151 96.492,7417.047 96.492,7415.675 C96.492,7414.719 96.172,7414.095 95.813,7413.777 C98.04,7413.523 100.38,7412.656 100.38,7408.718 C100.38,7407.598 99.992,7406.684 99.35,7405.966 C99.454,7405.707 99.797,7404.664 99.252,7403.252 C99.252,7403.252 98.414,7402.977 96.505,7404.303 C95.706,7404.076 94.85,7403.962 94,7403.958 C93.15,7403.962 92.295,7404.076 91.497,7404.303 C89.586,7402.977 88.746,7403.252 88.746,7403.252 C88.203,7404.664 88.546,7405.707 88.649,7405.966 C88.01,7406.684 87.619,7407.598 87.619,7408.718 C87.619,7412.646 89.954,7413.526 92.175,7413.785 C91.889,7414.041 91.63,7414.493 91.54,7415.156 C90.97,7415.418 89.522,7415.871 88.63,7414.304 C88.63,7414.304 88.101,7413.319 87.097,7413.247 C87.097,7413.247 86.122,7413.234 87.029,7413.87 C87.029,7413.87 87.684,7414.185 88.139,7415.37 C88.139,7415.37 88.726,7417.2 91.508,7416.58 C91.513,7417.437 91.522,7418.245 91.522,7418.489 C91.522,7418.76 91.338,7419.077 90.839,7418.982 C86.865,7417.627 84,7413.783 84,7409.253 C84,7403.59 88.478,7399 94,7399" id="github-[#142]"> </path> </g> </g> </g></svg>'''

    # Basic HTML structure, mimicking the original CSS classes
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{} - Resume</title>
    <style>
        :root {{
          --primary-color: #0c77f2;
          --secondary-color: #64748b;
          --background-color: #f8fafc;
          --text-primary: #1e293b;
          --text-secondary: #475569;
        }}
        
        * {{
          margin: 0;
          padding: 0;
          box-sizing: border-box;
        }}
        
        body {{
          font-family: "Arial", sans-serif;
          background-color: var(--background-color);
          line-height: 1.6;
          color: var(--text-primary);
          font-size: 14px;
        }}
        
        .container {{
          max-width: 100%;
          margin: 0;
          padding: 0;
          display: flex;
          flex-direction: column;
          gap: 0;
        }}
        
        .section {{
          background: white;
          box-shadow: 0 1px 3px rgba(0,0,0,0.1);
          padding: 8px;
          display: flex;
          gap: 20px;
          border-bottom: 1px solid #000000;
          border-top: 1px solid #000000;
          max-width: 100vh;
          overflow: auto;
        }}
        
        .section:last-child {{
          border-bottom: none;
        }}
        
        .section-title {{
          display: flex;
          align-items: center;
          justify-content: center;
          border-right: 1px solid black;
          font-size: 16px;
          font-weight: bold;
          color: var(--text-primary);
          width: 120px;
          text-align: center;
          flex-shrink: 0;
        }}
        
        .section-content {{
          flex: 1;
        }}
        
        .header-section {{
          display: flex;
          align-items: center;
          gap: 20px;
        }}
        
        .profile-image {{
          /* background-image: url('1694689775214.jpeg'); */
          /* background-size: cover; */
          /* background-position: center; */
          width: 80px;
          height: 80px;
          border-radius: 50%;
          /* background-color: #e2e8f0; */
          flex-shrink: 0;
          object-fit: cover;
        }}
        
        .header-content {{
          display: flex;
          flex-direction: row;
          justify-content: space-between;
          align-items: space-between;
          width: 100%;
          /* gap: 16px; */
        }}
        
        .header-info h1 {{
          font-size: 22px;
          font-weight: bold;
          color: var(--text-primary);
          margin-bottom: 3px;
        }}
        
        .header-info .role {{
          font-size: 14px;
          font-weight: 500;
          color: var(--primary-color);
          margin-bottom: 3px;
        }}
        
        .header-info .education {{
          font-size: 13px;
          color: var(--text-secondary);
        }}
        
        .contact-info {{
          display: flex;
          flex-direction: column;
          gap: 4px;
          font-size: 12px;
          color: var(--text-secondary);
        }}
        
        .contact-item {{
          display: flex;
          align-items: center;
          gap: 6px;
          text-decoration: none;
          color: var(--primary-color);
        }}
        
        .contact-item a {{
          color: var(--primary-color);
          text-decoration: none;
        }}
        
        .contact-item a:hover {{
          color: var(--primary-color);
        }}
        
        .summary-text {{
          font-size: 13px;
          color: var(--text-secondary);
          line-height: 1.5;
        }}
        
        .education-table {{
          width: 100%;
          border-collapse: collapse;
          font-size: 12px;
          margin: 0;
        }}
        
        .education-table th {{
          font-weight: 600;
          color: var(--text-secondary);
          padding: 4px 4px;
          text-align: left;
          border-bottom: 1px solid #e2e8f0;
        }}
        
        .education-table td {{
          padding: 4px 4px;
          color: var(--text-secondary);
          border-bottom: 1px solid #e2e8f0;
        }}
        
        .education-table th:last-child,
        .education-table td:last-child {{
          text-align: right;
        }}
        
        .skills-grid {{
          display: flex;
          flex-direction: column;
          gap: 8px;
          font-size: 12px;
        }}
        
        .skill-category {{
          display: flex;
          gap: 12px;
          align-items: flex-start;
        }}
        
        .skill-category h3 {{
          font-weight: 600;
          color: var(--text-primary);
          width: 80px;
          flex-shrink: 0;
          font-size: 12px;
        }}
        
        .skill-tags {{
          display: flex;
          flex-wrap: nowrap;
          gap: 4px;
          flex: 1;
          overflow: hidden;
        }}
        
        .skill-tag {{
          background: #f1f5f9;
          color: var(--text-secondary);
          font-size: 10px;
          font-weight: 500;
          padding: 3px 6px;
          border-radius: 12px;
          white-space: nowrap;
        }}
        
        .experience-item {{
          margin-bottom: 16px;
        }}
        
        .experience-header {{
          display: flex;
          justify-content: space-between;
          align-items: flex-start;
          margin-bottom: 3px;
        }}
        
        .experience-title {{
          font-weight: 600;
          color: var(--text-primary);
          font-size: 13px;
        }}
        
        .experience-date {{
          font-size: 11px;
          color: var(--text-secondary);
        }}
        
        .experience-company {{
          font-size: 11px;
          color: var(--text-secondary);
          margin-bottom: 6px;
        }}
        
        .experience-role {{
          font-size: 11px;
          color: var(--text-secondary);
          margin-bottom: 3px;
        }}
        
        .experience-skills {{
          display: flex;
          flex-wrap: wrap;
          gap: 3px;
          margin-bottom: 6px;
        }}
        
        .experience-list {{
          list-style: disc;
          padding-left: 16px;
          color: var(--text-secondary);
          font-size: 11px;
        }}
        
        .experience-list li {{
          margin-bottom: 3px;
          line-height: 1.3;
        }}
        
        .project-item {{
          margin-bottom: 16px;
        }}
        
        .project-header {{
          display: flex;
          justify-content: space-between;
          align-items: flex-start;
          margin-bottom: 3px;
        }}
        
        .project-title {{
          font-weight: 600;
          color: var(--text-primary);
          font-size: 13px;
        }}
        
        .project-meta {{
          display: flex;
          justify-content: space-between;
          align-items: center;
        }}

        .experience-meta {{
          display: flex;
          align-items: center;
          gap: 8px;
        }}
        
        .project-supervisor {{
          font-size: 11px;
          color: var(--text-secondary);
        }}
        
        .project-github {{
          font-size: 11px;
          color: var(--text-secondary);
          text-decoration: none;
        }}
        
        .project-skills {{
          display: flex;
          flex-wrap: wrap;
          gap: 3px;
          margin-bottom: 6px;
        }}
        
        .project-list {{
          list-style: disc;
          padding-left: 16px;
          color: var(--text-secondary);
          font-size: 11px;
        }}
        
        .project-list li {{
          margin-bottom: 3px;
          line-height: 1.3;
        }}
        
        .achievements-list {{
          list-style: disc;
          padding-left: 16px;
          color: var(--text-secondary);
          font-size: 12px;
        }}
        
        .achievements-list li {{
          margin-bottom: 4px;
          line-height: 1.3;
        }}
        
        @page {{
          size: A4;
          margin: 0;
        }}
    </style>
</head>
<body>
    <div class="container">
        <!-- Header Section -->
        <div class="section">
          <div style="display: flex; gap: 270px; align-items: center; width: 100%;">
            <div class="header-section">
                <img src="1694689775214.jpeg" alt="Profile Picture" class="profile-image">
                <div class="header-content">
                    <div class="header-info">
                        <h1>{header_name}</h1>
                        <p class="role">{header_role}</p>
                        <p class="education">{header_education_0}</p>
                        <p class="education">{header_education_1}</p>
                    </div>
                </div>
            </div>
            <div class="contact-info">
                <!-- Phone -->
              <span class="contact-item" style="display: flex; align-items: center; gap: 8px;">
                <img src="https://cdn-icons-png.flaticon.com/512/455/455705.png" alt="Phone" width="{icon_size}" height="{icon_size}" />
                {contact_phone}
              </span>

              <!-- Email -->
              <span class="contact-item" style="display: flex; align-items: center; gap: 8px;">
                {gmail_svg}
                {contact_email}
              </span>

              <!-- LinkedIn -->
              <a class="contact-item" href="{contact_linkedin_link}" target="_blank" rel="noopener noreferrer" style="display: flex; align-items: center; gap: 8px;">
                {linkedin_svg}
                {contact_linkedin}
              </a>

              <!-- GitHub -->
              <a class="contact-item" href="{contact_github_link}" target="_blank" rel="noopener noreferrer" style="display: flex; align-items: center; gap: 8px;">
                {github_svg}
                {contact_github}
              </a>

              <!-- Codeforces (no official icon, use logo SVG) -->
              <a class="contact-item" href="{contact_codeforces_link}" target="_blank" rel="noopener noreferrer" style="display: flex; align-items: center; gap: 8px;">
                <img src="https://sta.codeforces.com/s/12138/images/codeforces-logo-with-telegram.png" alt="Codeforces" width="{icon_size}" height="{icon_size}" />
                {contact_codeforces}
              </a>
            </div>
          </div>
        </div>
        
        <!-- Summary Section -->
        <div class="section">
            <h2 class="section-title">Summary</h2>
            <div class="section-content">
                <p class="summary-text">{summary}</p>
            </div>
        </div>
        
        <!-- Education Section -->
        <div class="section">
            <h2 class="section-title">Education</h2>
            <div class="section-content">
                <table class="education-table">
                    <thead>
                        <tr>
                            <th>Institution</th>
                            <th>Degree/Class</th>
                            <th>Date</th>
                            <th>Percentage</th>
                        </tr>
                    </thead>
                    <tbody>
                        {education_entries}
                    </tbody>
                </table>
            </div>
        </div>
        
        <!-- Skills Section -->
        <div class="section">
            <h2 class="section-title">Skills</h2>
            <div class="section-content">
                <div class="skills-grid">
                    {skill_categories}
                </div>
            </div>
        </div>
        
        <!-- Experience Section -->
        <div class="section">
            <h2 class="section-title">Experience</h2>
            <div class="section-content">
                {experience_items}
            </div>
        </div>
        
        <!-- Projects Section -->
        <div class="section">
            <h2 class="section-title">Projects</h2>
            <div class="section-content">
                {project_items}
            </div>
        </div>
        
        <!-- Achievements Section -->
        <div class="section">
            <h2 class="section-title">Achievements</h2>
            <div class="section-content">
                <ul class="achievements-list">
                    {achievement_items}
                </ul>
            </div>
        </div>
    </div>
</body>
</html>""".format(
        resume_data['header']['name'],
        header_name=resume_data['header']['name'],
        header_role=resume_data['header']['role'],
        header_education_0=resume_data['header']['education_header'][0],
        header_education_1=resume_data['header']['education_header'][1],
        contact_phone=resume_data['header']['contact']['phone'],
        contact_email=resume_data['header']['contact']['email'],
        contact_linkedin_link=resume_data['header']['contact']['linkedin'],
        contact_linkedin="Khushal Sindhav",
        contact_github_link=resume_data['header']['contact']['github'],
        contact_github="MagnusCarlsen26",
        contact_codeforces_link=resume_data['header']['contact']['codeforces'],
        contact_codeforces="_magnus_carlsen_",
        summary=resume_data['summary'],
        education_entries=''.join([
            f"""
                        <tr>
                            <td>{edu['institution']}</td>
                            <td>{edu['degree_class']}</td>
                            <td>{edu['date']}</td>
                            <td>{edu['percentage']}</td>
                        </tr>""" for edu in resume_data['education']
        ]),
        skill_categories=''.join([
            f"""
                    <div class="skill-category">
                        <h3>{category.capitalize()}</h3>
                        <div class="skill-tags">
                            {''.join([f'<span class="skill-tag">{skill}</span>' for skill in skills])}
                        </div>
                    </div>""" for category, skills in resume_data['skills'].items()
        ]),
        experience_items=''.join([
            f"""
                <div class="experience-item">
                    <div class="experience-header">
                        <div style="display: flex;">
                          <h3 class="experience-title">{exp['title']} &nbsp;</h3>
                          <div class="experience-meta">
                            <p class="experience-role">{exp.get('role', '')}</p>
                            {f'''<a href="{exp['linkedin']}" target="_blank" rel="noopener noreferrer">{linkedin_svg}</a>''' if 'linkedin' in exp else ''}
                            {f'''<a href="{exp['github']}" target="_blank" rel="noopener noreferrer">{github_svg}</a>''' if 'github' in exp else ''}
                          </div>
                        </div>
                        <p class="experience-date">{exp['date']}</p>
                    </div>
                      <div class="experience-skills">
                        {''.join([f'<span class="skill-tag">{skill}</span>' for skill in exp['skills']])}
                    </div>
                    <ul class="experience-list">
                        {''.join([f'<li>{duty}</li>' for duty in exp['duties']])}
                    </ul>
                </div>""" for exp in resume_data['experience']
        ]),
        project_items=''.join([
            f"""
                <div class="project-item">
                    <div class="project-header">
                        <div style="display: flex;">
                          <h3 class="project-title">{proj['title']} &nbsp;</h3>
                          <div class="project-meta">
                            <p class="project-supervisor">{proj.get('supervisor', '')} &nbsp;</p>
                            {f'''<a href="{proj['github']}" target="_blank" rel="noopener noreferrer">{github_svg}</a>''' if 'github' in proj else ''}
                          </div>
                        </div>
                        <p class="experience-date">{proj['date']}</p>
                    </div>

                    <div class="project-skills">
                        {''.join([f'<span class="skill-tag">{skill}</span>' for skill in proj['skills']])}
                    </div>
                    <ul class="project-list">
                        {''.join([f'<li>{desc}</li>' for desc in proj['description']])}
                    </ul>
                </div>""" for proj in resume_data['projects']
        ]),
        achievement_items=''.join([
            f"<li>{ach}</li>" for ach in resume_data['achievements']
        ]),
        icon_size=icon_size,
        gmail_svg=gmail_svg,
        linkedin_svg=linkedin_svg,
        github_svg=github_svg
    )

    return html_content

if __name__ == "__main__":
    json_file_path = "resume.json"
    output_html_path = "resume_from_json.html"
    
    html_output = generate_resume_html(json_file_path)
    
    with open(output_html_path, 'w', encoding='utf-8') as f:
        f.write(html_output)
    
    print(f"Successfully converted {json_file_path} to {output_html_path}") 