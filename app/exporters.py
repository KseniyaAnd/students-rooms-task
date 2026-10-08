from abc import abstractmethod
from decimal import Decimal
import json 
import xml.etree.ElementTree as ET 

def rows_to_dicts(rows, columns):
    result = []

    for row in rows:
        item = {}

        for key, value in zip(columns, row):
            if isinstance(value, Decimal):
                value = float(value)

            item[key] = value

        result.append(item)

    return result

class Exporter:
    @abstractmethod
    def export(self, data, file_path):
        pass

class JSONExporter(Exporter):
    def export(self, data, file_path):
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

class XMLExporter(Exporter):
    def export(self, data, file_path):
        root = ET.Element("results") 
        
        for section_name, rows in data.items(): 
            section = ET.SubElement(root, section_name) 
            
            for row in rows: 
                item = ET.SubElement(section, "item") 
                for key, value in row.items(): 
                    element = ET.SubElement(item, key) 
                    element.text = str(value) 
        tree = ET.ElementTree(root) 
        tree.write(file_path, encoding="utf-8", xml_declaration=True) 