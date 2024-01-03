class Programmer:
    
    def __init__(self, name, language, skills):
        self.name = name
        self.language = language
        self.skills = skills
        
    def watch_course(self, course, language, skills):
        if language == self.language: 
            self.skills += skills
            return f"{self.name} watched {course}"
        return f"{self.name} does not know {language}"

    def change_language(self, new_language, skills_needed):
        curr_lang = self.language
        if self.language != new_language and self.skills >= skills_needed:
            self.language = new_language
            return f"{self.name} switched from {curr_lang} to {new_language}"
        elif self.skills >= skills_needed:
            return f"{self.name} already knows {new_language}"
        
        return f"{self.name} needs {skills_needed - self.skills} more skills"
    
# Test Cases

programmer1 = Programmer("Alice", "Python", 50)

print(programmer1.watch_course("Python Basics", "Python", 10))  

print(programmer1.watch_course("JavaScript Advanced", "JavaScript", 15)) 

print(programmer1.change_language("JavaScript", 30))  

print(programmer1.change_language("JavaScript", 10)) 

print(programmer1.change_language("JavaScript", 70)) 
