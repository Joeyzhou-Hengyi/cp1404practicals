import datetime
from project import Project


FILENAME = "projects.txt"


def load_projects(filename):
    """Load projects from a tab-delimited text file."""
    projects = []
    in_file = open(filename, "r", encoding="utf-8")
    in_file.readline()  # skip header
    for line in in_file:
        parts = line.strip().split('\t')
        if len(parts) < 5:
            continue
        name = parts[0]
        start_date = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
        priority = int(parts[2])
        cost_estimate = float(parts[3])
        completion_percentage = int(parts[4])
        project = Project(name, start_date, priority, cost_estimate, completion_percentage)
        projects.append(project)
    in_file.close()
    return projects

def save_projects(filename, projects):
    """Save all projects to a tab-delimited text file."""
    out_file = open(filename, "w", encoding="utf-8")
    print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
    for project in projects:
        date_string = project.start_date.strftime("%d/%m/%Y")
        print(f"{project.name}\t{date_string}\t{project.priority}\t"
              f"{project.cost_estimate:.2f}\t{project.completion_percentage}", file=out_file)
    out_file.close()

def display_projects(projects):
    """Show incomplete and completed projects sorted by priority."""
    incomplete = [p for p in projects if not p.is_complete()]
    complete = [p for p in projects if p.is_complete()]

    incomplete.sort()
    complete.sort()

    print("Incomplete projects:")
    for project in incomplete:
        print(f"  {project}")
    print("Completed projects:")
    for project in complete:
        print(f"  {project}")