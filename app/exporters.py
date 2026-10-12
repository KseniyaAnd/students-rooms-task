import json
import xml.etree.ElementTree as ET
from abc import abstractmethod
from decimal import Decimal
from typing import Any


def rows_to_dicts(
        rows: list, 
        columns: list
    ) -> list[dict[str, Any]]:
    """Convert database rows into dictionaries.

    Decimal values are converted to floats to support JSON serialization.

    :param rows: Rows returned by a database query.
    :param columns: Column names corresponding to the row values.
    :return: A list of dictionaries containing the query results.
    :rtype: list[dict[str, Any]]
    """

    result: list[dict[str, object]] = []

    for row in rows:
        item: dict[str, object] = {}

        for key, value in zip(columns, row):
            if isinstance(value, Decimal):
                value: float = float(value)

            item[key] = value

        result.append(item)

    return result


class Exporter:
    """Define the interface for exporting query results."""

    @abstractmethod
    def export(
        self, 
        data: dict, 
        file_path: str
    ) -> None:
        """Export data to a file.

        :param data: Data to export.
        :param file_path: Destination file path.
        :return: None.
        """



class JSONExporter(Exporter):
    """Export query results as a JSON file."""

    def export(
            self, 
            data: dict, 
            file_path: str
        ) -> None:
        """Write query results to a JSON file.

        :param data: Data to export.
        :param file_path: Destination file path.
        :return: None.
        """

        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)


class XMLExporter(Exporter):
    """Export query results as an XML file."""

    def export(
            self, 
            data: dict, 
            file_path: str
        ) -> None:
        """Write query results to an XML file.

        :param data: Data to export.
        :param file_path: Destination file path.
        :return: None.
        """

        root: ET.Element = ET.Element("results")

        for section_name, rows in data.items():
            section: ET.Element = ET.SubElement(root, section_name)

            for row in rows:
                item: ET.Element = ET.SubElement(section, "item")
                for key, value in row.items():
                    element: ET.Element = ET.SubElement(item, key)
                    element.text = str(value)
        tree: ET.ElementTree = ET.ElementTree(root)
        tree.write(file_path, encoding="utf-8", xml_declaration=True)
