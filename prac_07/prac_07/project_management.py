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

def filter_projects(projects):
    """Ask user for a date and show projects that start after that date."""
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    filter_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()

    filtered = [p for p in projects if p.start_date >= filter_date]
    filtered.sort(key=lambda p: p.start_date)

    for project in filtered:
        print(project)

def add_new_project(projects):
    """Ask user for details and add a new project."""
    print("Let's add a new project")
    name = input("Name: ")
    date_string = input("Start date (dd/mm/yyyy): ")
    start_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))

    new_project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(new_project)
    print("Project added.\n")

def update_project(projects):
    """Select a project and update its percentage and/or priority."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    choice_text = input("Project choice: ")
    if not choice_text.isdigit():
        return
    choice = int(choice_text)
    project = projects[choice]
    print(project)
    percentage_text = input("New Percentage: ")
    priority_text = input("New Priority: ")

    if percentage_text != "":
        project.completion_percentage = int(percentage_text)
    if priority_text != "":
        project.priority = int(priority_text)
    print("Project updated.\n")

def main():
    """Main menu-driven program."""
    print("Welcome to Pythonic Project Management")

    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")

    menu = ("- (L)oad projects\n"
            "- (S)ave projects\n"
            "- (D)isplay projects\n"
            "- (F)ilter projects by date\n"
            "- (A)dd new project\n"
            "- (U)pdate project\n"
            "- (Q)uit")

    choice = ""
    while choice.lower() != "q":
        print(menu)
        choice = input(">>> ").lower()
        if choice == "l":
            filename = input("Filename to load from: ")
            projects = load_projects(filename)
        elif choice == "s":
            filename = input("Filename to save to: ")
            save_projects(filename, projects)
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            filter_projects(projects)
        elif choice == "a":
            add_new_project(projects)
        elif choice == "u":
            update_project(projects)
        elif choice == "q":
            answer = input(f"Would you like to save to {FILENAME}? ").lower()
            if answer.startswith("y"):
                save_projects(FILENAME, projects)
            print("Thank you for using custom-built project management software.")
        else:
            print("Invalid menu choice")


main()