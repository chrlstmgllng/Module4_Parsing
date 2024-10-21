import xml.etree.cElementTree as et 

tree = et.parse("sample.xml")

root = tree.getroot()

Job_Title = []
Company_Name = []

for title in root.iter('job_title'):
    Job_Title.append(title.text)

for company in root.iter('company_name'):
    Company_Name.append(company.text)

print(Job_Title)
print(Company_Name)