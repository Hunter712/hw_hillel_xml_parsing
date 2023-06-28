import json
import xml.etree.ElementTree as ET


tree = ET.parse('pages.xml')
root = tree.getroot()
resulted_dict = {}


for page in root:
    element_dict = {}

    for element in page:
        locator_dict = {}
        platform_list = []

        for locator in element:
            locator_dict[locator.attrib["platform"]] = [locator.attrib["locator_type"], locator.text]

        element_dict[element.attrib["name"]] = locator_dict

    resulted_dict[page.attrib["name"]] = element_dict

print(resulted_dict)

with open("data_file.json", "w") as write_file:
    json.dump(resulted_dict, write_file, indent='\t')
