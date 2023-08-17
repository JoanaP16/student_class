# o clasa care sa scrie in fisier si sa scrie si sa citeasca, folosind clase, nu functii.
from docx import Document


class CVWriter:
    "This class write experience in a specific filename(cv)"

    def __init__(self, filename, experience):
        self.filename = filename
        self.experience = experience
        # self.path = input('Enter a path:')
        document = Document()
        document.add_heading('Experience')
        with open(self.filename, 'a') as cv_write:
            cv_write.write('Experience:\n')
            for i in experience:
                filename.write(i + "\n")


class CVReader:
    "This class read experience from a specific filename(cv)"

    def __init__(self, filename, experience, tehnical_skills):
        self.filename = filename
        self.experience = experience
        self.tehnical_skills = tehnical_skills

        with open(self.filename, 'r') as file:
            centralizare_experience = []
            lines = file.readlines()
            for line in lines:
                if line == "Experience":
                    is_experience = True
                    centralizare_experience.append(line)
        return centralizare_experience


if __name__ == "__main__":
    updatecv = CVWriter('CV Ioana Perciun.docx', 'Tester Junior')
